**Source**
- [Article](https://medium.com/@joudwawad/aws-lambda-architecture-deep-dive-bef856b9b2c4)
# Runtime
- Provides a language specific runtime
- Runtime runs on in execution environment on a virtual machine
![[Pasted image 20250909204428.png]]

# Worker Hosts & Micro Services
- Operates on worker hosts (EC2 Instance / Machine)
- That manages multiple micro VMs
	- Holds execution environment
- Each micro environment is dedicated to a single function invocation
	- Secure & Isolated environment
- Designed so multiple worker hosts can concurrently handle invocations of the same lambda function
	- High availability, load balancing
- Workers lease time of 14 hours before terminating and no further invocations being routed to it
	- Lambda monitors lifecycle activities of its fleet's lifetime
![[Pasted image 20250909204614.png]]
# Firecracker
- Engine powering Lambda functions
- Virtualization technology
	- Developed at AWS, written in Rust
- Enables creation of lightweight, secure Micro VMs for each function invocation
- Lambda service managed overall workers while firecracker managed Micro VMs inside worker Machine
![[Pasted image 20250909205246.png]]

# Lambda Invocations
- [**More Info:**](https://medium.com/@joudwawad/understanding-aws-lambda-invocation-types-893513a9609f)
- Synchronous
	- Wait for response
	- Interactive workloads like APIs
- Asynchronous 
	- Where immediate response is not required for processing
- Event Source Mapping
	- Polls sources and invokes functions on it
	- Batch processing
# General Architecture
- Process varies based on whether or not sync or async call
	- Queue is used or directly invoked
- Frontend service entry point for lambda service
	- When lambda function is invoked it manages request and directs it to appropriate data plane
	- Initiating the execution process
![[Pasted image 20250909214847.png]]

## Execution : Synchronous
- The invoke API can be called via 2 modes
	- **_Event_** mode queues the payload for an _asynchronous invocation_.
	- **_Request-response_** mode _synchronously_ invokes the function with the provided payload and returns a response immediately.
- Response Request
	- it is passed to service directly
	- If invoke service is unavailable
		- the callers may queue request client side to try invocation a set number of times
	- If invoked service receives payload
		- attempt to find available execution environment
		- dynamically crafted if non exist
		- While in transit invoke payload secured via TSL
	- Traffic within Lambda Service passes through VPC
		- Virtual Private Cloud
			- Owned by Lambda service within region request was sent
- Step 1 : Worker manager communicates with placement service responsible for placing a workload on a location for the given host.
		- Its provisioning sandbox and returns it to worker manager
> Lambda functions run within a sandbox, which provides a minimal Linux userland, some common libraries and utilities. It creates the Execution environment (worker) on EC2 instances.

- Step 2 : Worker manager can then call `init` to initialize the function for execution by downloading the lambda package from S3/ECR image and setting up lambda runtime
- Step 3 : The frontend worker is now able to call `invoke`
![[Pasted image 20250909220341.png]]