import docker
import os
import sys


# this class is from stack overflow; greatful.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Pipeline(object):
    def __init__(self, network='ci_net', dockerRegistry='library/'):
        self.client = docker.from_env()
        self.network = network
        self.dockerRegistry = dockerRegistry
        self.create_network(self.network)

    def create_network(self, network):
        self.ciNet = network
        self.existingNets = self.client.networks.list()
        self.netNames = []
        for net in self.existingNets:
            self.netNames.append(net.name)

        if self.ciNet in self.netNames:
            return 'existing'
        else:
            try:
                self.client.networks.create(self.ciNet, check_duplicate=True, driver='bridge')
                return 'created'
            except docker.errors.APIError as e:
                print(e)

    def build_image(self, path, tag):
        self.path = path
        self.tag = tag
        print(bcolors.BOLD+'  + Building image {0:s}, please wait'.format(self.tag)+bcolors.ENDC)
        try:
            self.client.images.build(path=self.path, tag=self.tag, rm=True, pull=True)
            print('    + {0:s} image ready'.format(self.tag))
        except docker.errors.BuildError as e:
            print(bcolors.FAIL+'Error attempting to build image {0:s}:'.format(self.tag)+bcolors.ENDC)
            print(e)

    def pull_image(self, image):
        self.image = image
        if image.startswith('local/'):
            print(bcolors.OKGREEN+'    . local image {0:s}'.format(self.image)+bcolors.ENDC)
        else:
            print(bcolors.OKGREEN+'    . Pulling image {0:s}'.format(self.image)+bcolors.ENDC)
            try:
                self.client.images.pull(self.image)
                print('      {0:s} image ready'.format(self.image))
            except Exception as e:
                print(bcolors.FAIL+'Error attempting to pull image {0:s}:'.format(self.image)+bcolors.ENDC)
                print(e)

    def rund(self, image, stderr=None, ports=None, volumes=None, name=None, env_vars=None, network=None, command=None,
             detach=None, remove=None):
        if network is None:
            network = self.network
        if detach is None:
            detach = True
        if detach is False:
            remove = True

        print(bcolors.BOLD+'  + Starting container {0:s}'.format(str(name))+bcolors.ENDC)

        self.pull_image(image)

        try:
            self.instance = self.client.containers.run(image=image, ports=ports, volumes=volumes, name=name, environment=env_vars,
                                                       command=command, network=network, detach=detach, remove=remove)
        except docker.errors.ContainerError as err:
            print(err)
            return err

        if detach is True:
            print('     '+self.instance.id)
            return self.instance.id

    def runi(self, image, command, name=None, volumes=None, working_dir=None,
             tty=True, env_vars=None, stdin_open=True, network=None, auto_remove=False):
        self.name = str(name)
        self.command = command
        self.working_dir = working_dir
        if network is None:
            network = self.network
        if working_dir is None:
            self.working_dir = '/root'

        print(bcolors.BOLD+'  + Starting container {0:s}'.format(image)+bcolors.ENDC)

        self.pull_image(image)

        container = self.client.containers.create(image=image, command='sleep 600', environment=env_vars, volumes=volumes,
                                                  tty=tty, stdin_open=stdin_open, network=network, auto_remove=auto_remove)
        container.start()
        print('    '+container.id)
        exec_log = container.exec_run(self.command, workdir=self.working_dir, stdout=True, stderr=True, stream=False)
        print(bcolors.UNDERLINE +
              '\n  {0:s} attached output  \n'.format(self.name) +
              bcolors.ENDC +
              exec_log.output.decode() +
              '---{0:s} output detached---\n'.format(self.name))
        container.remove(force=True)
        if exec_log.exit_code != 0:
            print(bcolors.FAIL + '  * Attached container returned non-zero value, exiting...' + bcolors.ENDC)
            sys.tracebacklimit = 0
            raise Exception(bcolors.FAIL + 'Pipeline error' + bcolors.ENDC)
        return exec_log.exit_code

    def purge_containers(self, ids):
        self.ids = ids
        for container in self.ids:
            self.client.api.remove_container(container, force=True)
        self.client.containers.prune()

    def cve_scan(self, scanImage):
        self.scanImg = scanImage
        self.scanVolumes = {
            '/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}
        }
        self.command = '/bin/sh -c "/opt/clair-scan.sh {0:s}"'.format(self.scanImg)
        self.cleanMe = []

        print(bcolors.HEADER+'  * Scanning image {0:s} for known CVEs, please wait'.format(self.scanImg)+bcolors.ENDC)

        self.pull_image(scanImage)
        self.cleanMe.append(self.rund(image='arminc/clair-db:latest', name='postgres'))
        self.rund(image='christiantragesser/clair-scanner', name='db-wait',
                  command='/bin/sh -c "while ! timeout -t 1 sh -c \'nc -zv postgres 5432\' &>/dev/null; do :; done"',
                  detach=False)
        self.cleanMe.append(self.rund(image='arminc/clair-local-scan:latest', name='clair'))
        try:
            self.runi(image='christiantragesser/clair-scanner', command=self.command, name='clair-scanner', volumes=self.scanVolumes)
            print('  - CVE scan cleanup')
            self.purge_containers(self.cleanMe)
        except Exception:
            self.purge_containers(self.cleanMe)
