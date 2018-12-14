# Python docker delivery pipeline library
[![pipeline status](https://gitlab.com/christianTragesser/pypline-ci/badges/master/pipeline.svg)](https://gitlab.com/christianTragesser/pypline-ci/commits/master)

### Why?
I'm currently experimenting with docker-in-docker delivery pipelines written in a *high-level language* hoping to capitalize on object-oriented concepts native to Python.  While bash does provide the simple ability to script docker-in-docker pipelines; at a certain scale, creating and maintaining independent scripts across multiple repositories or projects becomes cumbersome and inefficient.

##### Why Python 2.7 by default?
For most Docker development workstations(popular Linux distros or MacOS) Python 2.7 is as natively available as bash. A major focus of this tooling is minimal dependencies however, this library should be compatible with Python 3 as well.

#### Examples
* Build image and run container
```python
import os
from pyplineCI import Pipeline

dirPath = os.path.dirname(os.path.realpath(__file__))
buildPath = dirPath+'/docker/'
localTag = 'local/foo:latest'

pipeline = Pipeline()
pipeline.buildImage(buildPath, localTag)
pipeline.runContainerDetached(localTag)
```

* Run testing framework from a dedicated testing image
```python
import os
from pyplineCI import Pipeline

dirPath = os.path.dirname(os.path.realpath(__file__))
volumes = { dirPath: { 'bind': '/tmp', 'mode': 'rw' } }
testDir = '/tmp/tests'

pipeline = Pipeline(dockerRegistry='registry.gitlab.com/christiantragesser/')
pipeline.runContainerInteractive(
    image=pipeline.dockerRegistry+'pyplineCI:latest',
    name='foo-test', working_dir=testDir,
    volumes=volumes, command='pytest')
```

* Orchestrate application stack for UAT testing then remove all containers if tests are successful
```python
import os
from pyplineCI import Pipeline

dirPath = os.path.dirname(os.path.realpath(__file__))
cleanUp = []

uat_volume = { dirPath: { 'bind': '/tmp', 'mode': 'rw' } }
testDir = '/tmp/tests'
db_env_vars = {
            'MYSQL_ROOT_PASSWORD': 'root',
            'MYSQL_DATABASE': 'foo-db',
            'MYSQL_ROOT_HOST': '%'
}
app_env_vars = {
            'DB_HOST': 'mysql-test',
            'DB_USER': 'root',
            'DB_PASSWORD': 'root',
            'DATABASE': 'foo-db'
}

pl = Pipeline()
cleanUp.append(pl.runContainerDetached(image='mysql:5.7', name='mysql-test', environment=db_env_vars))
cleanUp.append(pl.runContainerDetached(image='local/foo_app', name='foo-app-test', environment=app_env_vars))
pl.runContaineInteractive(image='tutum/curl:latest', name='foo-uat',
                      working_dir=testDir, volumes=uat_volume,
                      command='./uat.sh foo-app-test:5000')
pl.purgeContainers(cleanUp)
``` 
* Perform CVE scan on a docker image
```python
from pyplineCI import Pipeline

pl = Pipeline()
pl.cveScan('nginx:latest')
```
#### API reference
* **Pipeline**(_network='ci_net', dockerRegistry='library/'_)

  ```class pypline-ci.pyplineCI.Pipeline```
  - **createNetwork(** _network_ **)** | Create docker pipeline network.  
  parameters:
    + network(_str_) - Name of pipeline network, default `ci_net`
  - **buildImage(** _path, tag_ **)** | Build docker image.  
  parameters:
    + path(_str_) - Path to the directory containing the Dockerfile.
    + tag(_str_) - Tag applied to newly built image.
  - **pullImage(** _image_ **)** | Pull an image of the given name, similar to the `docker pull` command. If no tag is specified, all tags from that repository will be pulled.  
  parameters:
    + image(_str_) - Image name to pull.
  - **runContainerDetached(** _image, stderr=None, ports=None, volumes=None, name=None, environment=None, network=_<obj network\>_, command=None, detach=True, remove=False_ **)** |
  Performs pull action on provided image, runs a daemonized container, then returns the container ID.  
  parameters:
    + environment(_dict or list_) - Environment variables to set inside the container.
    + image(_str_) - The image to update and run.
    + name(_str_) - The name for this container.
    + ports(_dict_) - Port bindings to the container. The keys of the dictionary are the ports to bind inside the container, either as an integer or a string in the form port/protocol, where the protocol is either tcp or udp. The values of the dictionary are the corresponding ports to open on the host.
    + volumes(_dict_) - Configure volumes mounted inside the container.
  - **runContainerInteractive(** _image, command, name=None, volumes=None, working_dir='/root', tty=True, environment=None, stdin_open=True, network=_<obj network\>_, auto_remove=False_ **)** | Performs pull action on provided image, runs an interactive container implementing provided command, then returns container stdout logs and command exit status(zero or non-zero).  
  parameters:
    + command(_str_) - The command to run in the container.
    + environment(_dict or list_) - Environment variables to set inside the container.
    + image(_str_) - The image to update and run.
    + name(_str_) - The name for this container.
    + ports(_dict_) - Port bindings to the container. The keys of the dictionary are the ports to bind inside the container, either as an integer or a string in the form port/protocol, where the protocol is either tcp or udp. The values of the dictionary are the corresponding ports to open on the host.
    + volumes(_dict_) - Configure volumes mounted inside the container.
    + working_dir(_str_) - Path to the working directory.
  - **purgeContainers(** _ids_ **)** | Force deletion of container by container ID.  
  parameters:
    + ids(_list_) - List of container IDs to delete.
  - **cveScan(** _scanImage_ **)** | Perform CVE scan of docker image using [CoreOS Clair](https://coreos.com/clair/docs/latest/).  
  parameters:
    + scanImage(_str_) - The image to scan.

#### Install
Install on docker host:
* From [PyPi](https://pypi.org/project/pypline-ci/)
```sh
$ pip install pypline-ci
```

or

* Via docker:

```sh
$ docker run --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $PWD:/tmp \
    -w /tmp \
    registry.gitlab.com/christiantragesser/pypline-ci:latest /bin/sh
```

* For Python 3:

```sh
$ docker run --rm -it \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v $PWD:/tmp \
    -w /tmp \
    registry.gitlab.com/christiantragesser/pypline-ci:3 /bin/sh
```