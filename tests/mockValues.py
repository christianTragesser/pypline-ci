import sys

networksList = [   
    {   
        u'Attachable': False,
        u'ConfigFrom': {   u'Network': u''},
        u'ConfigOnly': False,
        u'Containers': {   },
        u'Created': u'2018-08-11T17:39:18.101651486Z',
        u'Driver': u'bridge',
        u'EnableIPv6': False,
        u'IPAM': {   u'Config': [   {   u'Gateway': u'172.17.0.1',
                                        u'Subnet': u'172.17.0.0/16'}],
                     u'Driver': u'default',
                     u'Options': None},
        u'Id': u'777ebde16b8eba8355cae9759b87ab47360e4c14090a9bb54a3ab9daa0eb42ec',
        u'Ingress': False,
        u'Internal': False,
        u'Labels': {   },
        u'Name': u'bridge',
        u'Options': {   u'com.docker.network.bridge.default_bridge': u'true',
                        u'com.docker.network.bridge.enable_icc': u'true',
                        u'com.docker.network.bridge.enable_ip_masquerade': u'true',
                        u'com.docker.network.bridge.host_binding_ipv4': u'0.0.0.0',
                        u'com.docker.network.bridge.name': u'docker0',
                        u'com.docker.network.driver.mtu': u'1500'},
        u'Scope': u'local'
    },
    {   u'Attachable': False,
        u'ConfigFrom': {   u'Network': u''},
        u'ConfigOnly': False,
        u'Containers': {   },
        u'Created': u'2018-04-22T18:01:29.651211257Z',
        u'Driver': u'null',
        u'EnableIPv6': False,
        u'IPAM': {   u'Config': [], u'Driver': u'default', u'Options': None},
        u'Id': u'bbb549cc23711468544e6fddea2d166d5f55f9ef81704afb363e721176a9ed08',
        u'Ingress': False,
        u'Internal': False,
        u'Labels': {   },
        u'Name': u'none',
        u'Options': {   },
        u'Scope': u'local'
    },
    {   u'Attachable': False,
        u'ConfigFrom': {   u'Network': u''},
        u'ConfigOnly': False,
        u'Containers': {   },
        u'Created': u'2018-04-22T18:01:29.680576532Z',
        u'Driver': u'host',
        u'EnableIPv6': False,
        u'IPAM': {   u'Config': [], u'Driver': u'default', u'Options': None},
        u'Id': u'df416915cc2b0ab78301f5f1c99b9fdba3c7794f1dce600a7bf505a5d3b85af6',
        u'Ingress': False,
        u'Internal': False,
        u'Labels': {   },
        u'Name': u'host',
        u'Options': {   },
        u'Scope': u'local'
     },
     {   
        u'Attachable': False,
        u'ConfigFrom': {   u'Network': u''},
        u'ConfigOnly': False,
        u'Containers': {   },
        u'Created': u'2018-08-11T17:39:18.101651486Z',
        u'Driver': u'bridge',
        u'EnableIPv6': False,
        u'IPAM': {   u'Config': [   {   u'Gateway': u'172.17.2.1',
                                        u'Subnet': u'172.17.2.0/16'}],
                     u'Driver': u'default',
                     u'Options': None},
        u'Id': u'83c8e3546cdbf5d639ff4a740df23ae019e9c235231a2226e0208b59bd19a82f',
        u'Ingress': False,
        u'Internal': False,
        u'Labels': {   },
        u'Name': u'test1',
        u'Options': {   u'com.docker.network.bridge.default_bridge': u'true',
                        u'com.docker.network.bridge.enable_icc': u'true',
                        u'com.docker.network.bridge.enable_ip_masquerade': u'true',
                        u'com.docker.network.bridge.host_binding_ipv4': u'0.0.0.0',
                        u'com.docker.network.bridge.name': u'docker0',
                        u'com.docker.network.driver.mtu': u'1500'},
        u'Scope': u'local'
    }
]

createdNetwork = {
    u'Warning': u'',
    u'Id': u'83c8e3546cdbf5d639ff4a740df23ae019e9c235231a2226e0208b59bd19a82f'
}

createdContainer = {
    u'Warning': u'',
    u'Id': u'f8ff8c989760534ac5d491682a3f1995d2b80c6df4d33b36268bc6492e570822'
}

pull_image = ''' 
    {"status":"Pulling from test/dind","id":"latest"}
    {"status":"Digest: sha256:7043076348bf5040220df6ad703798fd8593a0918d06d3ce30c6c93be117e430"}
    {"status":"Status: Image is up to date for test/dind:latest"}
'''

inspectContainer = {
    u'AppArmorProfile': u'',
    u'Args': [u'3600'],
    u'Config': {   u'AttachStderr': True,
                   u'AttachStdin': False,
                   u'AttachStdout': True,
                   u'Cmd': [u'sleep', u'3600'],
                   u'Domainname': u'',
                   u'Entrypoint': None,
                   u'Env': [   u'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
                   u'Hostname': u'24c15e6cb0c8',
                   u'Image': u'alpine:latest',
                   u'Labels': {   },
                   u'OnBuild': None,
                   u'OpenStdin': False,
                   u'StdinOnce': False,
                   u'Tty': False,
                   u'User': u'',
                   u'Volumes': None,
                   u'WorkingDir': u''},
    u'Created': u'2018-08-21T01:10:13.6048143Z',
    u'Driver': u'overlay2',
    u'ExecIDs': None,
    u'GraphDriver': {   u'Data': {   u'LowerDir': u'/var/lib/docker/overlay2/2e0ede8ec92db1730ddd52d02d6cb8d6f617e8c24b7504760975f5b0c0bf796e-init/diff:/var/lib/docker/overlay2/bc8a4676370619b28f77121f7e37d17f1501b34f1aa1945a58076d1fa721c608/diff',
                                     u'MergedDir': u'/var/lib/docker/overlay2/2e0ede8ec92db1730ddd52d02d6cb8d6f617e8c24b7504760975f5b0c0bf796e/merged',
                                     u'UpperDir': u'/var/lib/docker/overlay2/2e0ede8ec92db1730ddd52d02d6cb8d6f617e8c24b7504760975f5b0c0bf796e/diff',
                                     u'WorkDir': u'/var/lib/docker/overlay2/2e0ede8ec92db1730ddd52d02d6cb8d6f617e8c24b7504760975f5b0c0bf796e/work'},
                        u'Name': u'overlay2'},
    u'HostConfig': {   u'AutoRemove': False,
                       u'Binds': None,
                       u'BlkioDeviceReadBps': None,
                       u'BlkioDeviceReadIOps': None,
                       u'BlkioDeviceWriteBps': None,
                       u'BlkioDeviceWriteIOps': None,
                       u'BlkioWeight': 0,
                       u'BlkioWeightDevice': None,
                       u'CapAdd': None,
                       u'CapDrop': None,
                       u'Cgroup': u'',
                       u'CgroupParent': u'',
                       u'ConsoleSize': [0, 0],
                       u'ContainerIDFile': u'',
                       u'CpuCount': 0,
                       u'CpuPercent': 0,
                       u'CpuPeriod': 0,
                       u'CpuQuota': 0,
                       u'CpuRealtimePeriod': 0,
                       u'CpuRealtimeRuntime': 0,
                       u'CpuShares': 0,
                       u'CpusetCpus': u'',
                       u'CpusetMems': u'',
                       u'DeviceCgroupRules': None,
                       u'Devices': None,
                       u'DiskQuota': 0,
                       u'Dns': None,
                       u'DnsOptions': None,
                       u'DnsSearch': None,
                       u'ExtraHosts': None,
                       u'GroupAdd': None,
                       u'IOMaximumBandwidth': 0,
                       u'IOMaximumIOps': 0,
                       u'IpcMode': u'shareable',
                       u'Isolation': u'',
                       u'KernelMemory': 0,
                       u'Links': None,
                       u'LogConfig': {   u'Config': {   }, u'Type': u'json-file'},
                       u'MaskedPaths': [   u'/proc/acpi',
                                           u'/proc/kcore',
                                           u'/proc/keys',
                                           u'/proc/latency_stats',
                                           u'/proc/timer_list',
                                           u'/proc/timer_stats',
                                           u'/proc/sched_debug',
                                           u'/proc/scsi',
                                           u'/sys/firmware'],
                       u'Memory': 0,
                       u'MemoryReservation': 0,
                       u'MemorySwap': 0,
                       u'MemorySwappiness': None,
                       u'NanoCpus': 0,
                       u'NetworkMode': u'default',
                       u'OomKillDisable': False,
                       u'OomScoreAdj': 0,
                       u'PidMode': u'',
                       u'PidsLimit': 0,
                       u'PortBindings': None,
                       u'Privileged': False,
                       u'PublishAllPorts': False,
                       u'ReadonlyPaths': [   u'/proc/asound',
                                             u'/proc/bus',
                                             u'/proc/fs',
                                             u'/proc/irq',
                                             u'/proc/sys',
                                             u'/proc/sysrq-trigger'],
                       u'ReadonlyRootfs': False,
                       u'RestartPolicy': {   u'MaximumRetryCount': 0,
                                             u'Name': u''},
                       u'Runtime': u'runc',
                       u'SecurityOpt': None,
                       u'ShmSize': 67108864,
                       u'UTSMode': u'',
                       u'Ulimits': None,
                       u'UsernsMode': u'',
                       u'VolumeDriver': u'',
                       u'VolumesFrom': None},
    u'HostnamePath': u'/var/lib/docker/containers/24c15e6cb0c8473e0d186a2198d92d95898601ddadf10cc3f70495baadc17860/hostname',
    u'HostsPath': u'/var/lib/docker/containers/24c15e6cb0c8473e0d186a2198d92d95898601ddadf10cc3f70495baadc17860/hosts',
    u'Id': u'f8ff8c989760534ac5d491682a3f1995d2b80c6df4d33b36268bc6492e570822',
    u'Image': u'sha256:11cd0b38bc3ceb958ffb2f9bd70be3fb317ce7d255c8a4c3f4af30e298aa1aab',
    u'LogPath': u'/var/lib/docker/containers/24c15e6cb0c8473e0d186a2198d92d95898601ddadf10cc3f70495baadc17860/24c15e6cb0c8473e0d186a2198d92d95898601ddadf10cc3f70495baadc17860-json.log',
    u'MountLabel': u'',
    u'Mounts': [],
    u'Name': u'/test1',
    u'NetworkSettings': {   u'Bridge': u'',
                            u'EndpointID': u'3a1e2173c10f24d1ce50cee6b24b6d786b07895a4dd0619cd4986b937aed781f',
                            u'Gateway': u'172.17.0.1',
                            u'GlobalIPv6Address': u'',
                            u'GlobalIPv6PrefixLen': 0,
                            u'HairpinMode': False,
                            u'IPAddress': u'172.17.0.5',
                            u'IPPrefixLen': 16,
                            u'IPv6Gateway': u'',
                            u'LinkLocalIPv6Address': u'',
                            u'LinkLocalIPv6PrefixLen': 0,
                            u'MacAddress': u'02:42:ac:11:00:05',
                            u'Networks': {   u'bridge': {   u'Aliases': None,
                                                            u'DriverOpts': None,
                                                            u'EndpointID': u'3a1e2173c10f24d1ce50cee6b24b6d786b07895a4dd0619cd4986b937aed781f',
                                                            u'Gateway': u'172.17.0.1',
                                                            u'GlobalIPv6Address': u'',
                                                            u'GlobalIPv6PrefixLen': 0,
                                                            u'IPAMConfig': None,
                                                            u'IPAddress': u'172.17.0.5',
                                                            u'IPPrefixLen': 16,
                                                            u'IPv6Gateway': u'',
                                                            u'Links': None,
                                                            u'MacAddress': u'02:42:ac:11:00:05',
                                                            u'NetworkID': u'777ebde16b8eba8355cae9759b87ab47360e4c14090a9bb54a3ab9daa0eb42ec'}},
                            u'Ports': {   },
                            u'SandboxID': u'cdcbcae5dac33a9774338902e25450b91f29847afd0ba8cb374319372afc283a',
                            u'SandboxKey': u'/var/run/docker/netns/cdcbcae5dac3',
                            u'SecondaryIPAddresses': None,
                            u'SecondaryIPv6Addresses': None},
    u'Path': u'sleep',
    u'Platform': u'linux',
    u'ProcessLabel': u'',
    u'ResolvConfPath': u'/var/lib/docker/containers/24c15e6cb0c8473e0d186a2198d92d95898601ddadf10cc3f70495baadc17860/resolv.conf',
    u'RestartCount': 0,
    u'State': {   u'Dead': False,
                  u'Error': u'',
                  u'ExitCode': 0,
                  u'FinishedAt': u'0001-01-01T00:00:00Z',
                  u'OOMKilled': False,
                  u'Paused': False,
                  u'Pid': 49334,
                  u'Restarting': False,
                  u'Running': True,
                  u'StartedAt': u'2018-08-21T01:10:14.1127812Z',
                  u'Status': u'running'}
}

execCreate = {u'Id': u'cc89adf84ea67ac0de20fc36596a632ee61ad10a62a3a63a90ab22bbd8ff77f9'}

execInspect = {
    u'CanRemove': False,
    u'ContainerID': u'b42143950ec9eee57ad3dac93ddd2b96348b8798107704f5878969e5f55eab64',
    u'DetachKeys': u'',
    u'ExitCode': 0,
    u'ID': u'cc89adf84ea67ac0de20fc36596a632ee61ad10a62a3a63a90ab22bbd8ff77f9',
    u'OpenStderr': True,
    u'OpenStdin': False,
    u'OpenStdout': True,
    u'Pid': 0,
    u'ProcessConfig': {   u'arguments': [u'hello'],
                          u'entrypoint': u'echo',
                          u'privileged': False,
                          u'tty': False},
    u'Running': False
}

# use to test error exit code
errorInspect = {
    u'CanRemove': False,
    u'ContainerID': u'b42143950ec9eee57ad3dac93ddd2b96348b8798107704f5878969e5f55eab64',
    u'DetachKeys': u'',
    u'ExitCode': 22,
    u'ID': u'cc89adf84ea67ac0de20fc36596a632ee61ad10a62a3a63a90ab22bbd8ff77f9',
    u'OpenStderr': True,
    u'OpenStdin': False,
    u'OpenStdout': True,
    u'Pid': 0,
    u'ProcessConfig': {   u'arguments': [u'hello'],
                          u'entrypoint': u'echo',
                          u'privileged': False,
                          u'tty': False},
    u'Running': False
}

#encoded string which is decoded by library
if sys.version_info[0] < 3:
    checkmark = u'\u2713' #unicode checkmark
else:
    checkmark = bytes(u'\u2713', 'utf-8') #unicode checkmark
execResult = checkmark+' hello\n'.encode()

pruneResult = {
    u'ContainersDeleted': 
    [   
        u'139e5d9d5c513ff7eef7d5844a202ce697d86f477a83c49acb629f8a8b1f68de',
        u'c86f7e4376396e0a660e40e507fbbbc707b92be31661caebeedaeb005e5ad2f7',
        u'6fcc6d4c3514ab2dd6695f193a252fc4f01379fb704add88417b0c0b5a236c78'
    ],
    u'SpaceReclaimed': 0
}
