**Backlinks**
[[RabbitMQ]] 
________________
# Running RabbitMQ Container
`-d` to run detached

```bash
docker run \
	-itd \ # Interactive, Terminal, Detached
	--rm \ # Remove when finished running
	--name rabbitmq \ # name of container
	-p 5672:5672 -p 15672:15672 \ # port for accessing rabbitmq & dashboard
	rabbitmq:4-management # RabbitMQ Management image
```

# RabbitMQ Management Dashboard
Using management image we can visited a management dashboard to allows us to quickly monitor queues, exchanges and connections.
Located at `http://127.0.0.1:15672/`

**Default User**
user: `guest`
pass: `guest`
# Exchanges: Topics & Routing
- https://seventhstate.io/rabbitmqs-anatomy-understanding-topic-exchanges/
- https://spring.io/blog/2011/04/01/routing-topologies-for-performance-and-scalability-with-rabbitmq