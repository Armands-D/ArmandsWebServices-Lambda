**Backlinks**
[[Docker]] [[Containers]]
___
# Images
## Build
```bash
docker build -t python-app .
docker build -t python-app -f lambda.dockerfile .
```
### Common Flags
- `--no-cache`  don't cache when building image
- `-t` tag  = `repo:version`
- The `.` is the path to the context directory
	- The directory with the files your build can access
	  [Docker Build Context Docs](https://docs.docker.com/build/concepts/context/)
- `-f` flag if providing a custom `Dockerfile` name
### Tags
Tags follow this format `repo:tag` , where a tag is split into a repo and and tag component for images
```sh
# docker image ls
REPOSITORY, TAG, IMAGE ID, CREATED, SIZE  
<none>, <none>, 5bc35a571cf6, 12 minutes ago, 1.12GB  
provisioned, latest, eef1b81d611d, 5 days ago, 1.12GB
```

## Image IDs
A Docker image’s ID is a digest, which contains an SHA256 hash of the image’s JSON configuration object

## Removing Images

### Remove Image
We can remove images using the image id, or if an image id has multiple tags or repos we need to specify the `<repo:tag>` to delete it.

```bash
docker rmi <image-id>
docker rmi <repo:tag>
```

List all docker images, find lines with none, pipe list into xargs for deletion.
Depending on the structure or image ids, repos and tags this command might not work due to dependencies.
```bash
docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi
```
# Links
Docker Image IDs Explained
- https://windsock.io/explaining-docker-image-ids/
Docker Removing Images With Duplicate Tags
- https://stackoverflow.com/questions/38118791/can-t-delete-docker-image-with-dependent-child-images