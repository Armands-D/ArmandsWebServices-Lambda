# Permission Denied
Create docker group, add user to group or give root acces, to allow permission to run docker client in python programme.
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
su -s ${USER}
```
- https://docs.docker.com/reference/cli/dockerd/#examples
- https://stackoverflow.com/questions/61698133/docker-py-permissionerror13