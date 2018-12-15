import pytest
import mock
import docker
import sys
import os
import mockValues
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pyplineCI

pipeline = pyplineCI.Pipeline()

@mock.patch('docker.APIClient.inspect_network', return_value=mockValues.networksList[3])
@mock.patch('docker.APIClient.create_network', return_value=mockValues.createdNetwork)
@mock.patch('docker.APIClient.networks', return_value=mockValues.networksList)
def test_network_create(mock_list_networks, mock_create_network, mock_inspect_network):
    #takes in network name
    #checks for provided network,
    #return 'created' 
    responseCreated = pipeline.createNetwork('test')
    #return 'exists'
    responseExisting = pipeline.createNetwork('test1')

    assert responseCreated == 'created'
    assert responseExisting == 'existing'

@mock.patch('docker.APIClient.build')
def test_build_image(mock_build_image):
    #takes in path and image tag
    #runs docker SDK build
    pipeline.buildImage('/tmp/', 'test/pyplineCI:latest')

    assert mock_build_image.called

@mock.patch('docker.APIClient.pull')
def test_pull_image(mock_pull_image):
    #takes in image tag
    #runs docker SDK pull method 
    pipeline.pullImage('test/pyplineCI:latest')

    assert mock_pull_image.called

@mock.patch('docker.APIClient.inspect_container', return_value=mockValues.inspectContainer)
@mock.patch('docker.APIClient.start', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.create_container', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.pull', return_value=mockValues.pullImage)
def test_run_container_detached(mock_pull_image, mock_create_container,
                                   mock_run_container, mock_inspect_container):
    #takes in image and tag
    #runs docker SDK pull method
    #creates container
    #returns container ID 
    response = pipeline.runD('test/pyplineCI:latest')
    
    assert mock_pull_image.called
    assert response == mockValues.createdContainer['Id']

@mock.patch('docker.APIClient.inspect_container', return_value=mockValues.inspectContainer)
@mock.patch('docker.APIClient.start', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.create_container', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.pull')
def test_run_local_image(mock_pull_image, mock_create_container,
                         mock_run_container, mock_inspect_container):
    #takes in image and tag
    #runs docker SDK pull method
    #creates container
    #returns container ID 
    response = pipeline.runD('local/test:latest')
    
    assert not mock_pull_image.called
    assert response == mockValues.createdContainer['Id']

@mock.patch('docker.APIClient.remove_container')
@mock.patch('docker.APIClient.inspect_container', return_value=mockValues.inspectContainer)
@mock.patch('docker.APIClient.exec_inspect', return_value=mockValues.execInspect)
@mock.patch('docker.APIClient.exec_start', return_value=mockValues.execResult)
@mock.patch('docker.APIClient.exec_create', return_value=mockValues.execCreate)
@mock.patch('docker.APIClient.start', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.create_container', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.pull', return_value=mockValues.pullImage)
def test_run_container_interactive(mock_pull_image, mock_create_container,
                                   mock_run_container, mock_exec_create,
                                   mock_exec_start, mock_exec_inspect,
                                   mock_inspect_container, mock_remove_container):
    #takes in image and command
    #runs docker SDK pull method
    #creates starts container
    #executes command on container
    #returns output of interactive session
    response = pipeline.runI('test/pyplineCI:latest', 'echo hello')
    
    assert mock_pull_image.called
    assert response == 0

@mock.patch('docker.APIClient.remove_container')
@mock.patch('docker.APIClient.inspect_container', return_value=mockValues.inspectContainer)
@mock.patch('docker.APIClient.exec_inspect', return_value=mockValues.errorInspect)
@mock.patch('docker.APIClient.exec_start', return_value=mockValues.execResult)
@mock.patch('docker.APIClient.exec_create', return_value=mockValues.execCreate)
@mock.patch('docker.APIClient.start', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.create_container', return_value=mockValues.createdContainer)
@mock.patch('docker.APIClient.pull', return_value=mockValues.pullImage)
def test_error_container_interactive(mock_pull_image, mock_create_container,
                                   mock_run_container, mock_exec_create,
                                   mock_exec_start, mock_error_inspect,
                                   mock_inspect_container, mock_remove_container):
    #takes in image and command
    #runs docker SDK pull method
    #creates starts container
    #executes command on container
    #returns error
    with pytest.raises(Exception) as excinfo:
        pipeline.runI('test/pyplineCI:latest', 'echo hello')
    assert 'Pipeline error' in str(excinfo.value)

@mock.patch('docker.APIClient.prune_containers')
@mock.patch('docker.APIClient.remove_container')
@mock.patch('docker.APIClient.inspect_container', return_value=mockValues.inspectContainer)
def test_purge_containers(mock_inpect_container, mock_rm_container, mock_prune_containers):
    #takes in list of container IDs
    #removes(docker rm -f) list of container IDs
    #removes all stopped containers
    containerId = 'f8ff8c989760534ac5d491682a3f1995d2b80c6df4d33b36268bc6492e570822'
    removeMe = [ containerId ]

    pipeline.purgeContainers(removeMe)
    assert mock_rm_container.called
    assert mock_prune_containers.called
