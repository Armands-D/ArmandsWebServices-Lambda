# Table Of Contents
```dataview
List file.inlinks
From "Docker/Docker"
```
# Compose
Run build stage of docker compose
- `-d` should not be included, as we want a tty attached for our program
```bash
docker compose -f 'compose.yaml' up  --build 'lambda'
```

```bash
docker compose ps --all
```


# Attach
```
docker attach <container-name>
docker exec -it <container-name> bash
```
# Links
Docker Attach
- https://stackoverflow.com/questions/47753047/docker-detached-and-interactive/54174712
Docker Logs
- https://stackoverflow.com/questions/36666246/docker-look-at-the-log-of-an-exited-container
Docker Container Run Mounts
- https://dev.to/nasrulhazim/how-to-access-your-localhost-api-from-docker-containers-7ai
- https://docs.docker.com/engine/storage/bind-mounts/