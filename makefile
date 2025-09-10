
rm_prov:
	docker container stop prov &&  docker container rm prov

prune_none:
	docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi
