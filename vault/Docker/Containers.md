**Backlinks**
[[Docker]] [[Images]] [[Network]] [[Attach]]
___
# Run
Docker run allows you to run a docker image.
- `--network host` bind the docker container to use the host network stack/interface instead of its own. You can now access localhost from within docker
- `--mount type=bind,src=.,dst=/app` mounts the host top level directory `.` to container's `/app` (work) directory. Allow for copied files to sync between host and container.

```bash
docker run \
	-it \ # Interactive, TTY
	--rm \ # Remove once ended
	--network host \ # Use newtwork of host
	--mount type=bind,src=.,dst=/app \ # Mount
	--name my-running-app python-app # Name of container
```

## Volume
Mounts `cwd` to `/lambda` folder in the container
- Can access files from `cwd` from `lambda folder`
- creates container `prov-run` using image `prov:latest`
```bash
docker container run -v $(pwd):/lambda --name prov-run prov:latest
```
## Network
You can setup isolated networks for your docker containers or use the host machines network for communication.

**Host**
Removes docker network isolation and uses the host machines network interface for communication.
# Attach
Attach allows you to attach to the docker's TTY instance for STDOUT, allowing you to view STDOUT logs in real time.

```bash
docker attach <container-name>
```

Exec allows you to execute a command on the image's TTY.
```bash
docker exec -it <container-name> bash
```
## Logs
This prints `stdout` of the docker container, can be used on a stopped container.

```bash
docker logs <container-id>
```

# Stop

# Links
Docker Networking
- https://docs.docker.com/engine/network/
- https://docs.docker.com/reference/compose-file/build/#network
Docker Container Stop
- https://docs.docker.com/reference/cli/docker/container/stop/