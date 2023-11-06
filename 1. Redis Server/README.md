## Start Redis server

- For start the cluster and configuration cluster node use:
```console
docker exec -it redis-cluster-config redis-cli --cluster create --cluster-replicas 1 <ip_redis-1>:6379 <ip_redis-2>:6380 
```
- For start service use:
```console
redis-server
```
