# Container Spinup
- ==Spin up container per invocation==
	- We can use STDOUT for our communication
	- Have standard format
- Warm containers
	- Use a lightweight HTTP or RPC communication method

# Image Building
- Generalise Lambda Base Image
	- Include runtime
	- Include invoker function
		- read input, load user code, run user code, return output
	- User dependencies get more complicated
- Mount Volume to user code onto container
- https://docs.docker.com/engine/storage/volumes/
```bash
docker run --rm \
  -v /path/to/user_function:/var/task \
  my-lambda-base \
  python handler.py

```
