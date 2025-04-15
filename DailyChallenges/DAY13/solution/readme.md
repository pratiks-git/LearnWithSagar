## Challenge Steps followed
1. Persist Data for Yelb Components:
   - Use Docker volumes to persist data for Redis and PostgreSQL.
   - Run PostgreSQL with a Volume
   - Create a volume for PostgreSQL data:
     ``` docker volume create pg-data ```
2. Start the PostgreSQL container with the volume:
  ```
  docker run --name yelb-db \
  --network=yelb-network \
  -v pg-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  -d mreferre/yelb-db:0.6
  ```

3. Run Redis with a Volume:
  - Create a volume for Redis data:
    ``` docker volume create redis-data ```
4. Start the Redis container with the volume:
     ``` 
    docker run --name redis-server \
    --network=yelb-network \
    -v redis-data:/data \
    -p 6379:6379 \
    -d redis:4.0.2
    ```

5. Verify Data Persistence:
  - Stop and remove the Redis and PostgreSQL containers:
    ```
      docker stop redis-server yelb-db
      docker rm redis-server yelb-db
    ```
  - Restart the containers and verify that data is retained:
    ```
    docker run --name yelb-db \
    --network=yelb-network \
    -v pg-data:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d mreferre/yelb-db:0.6
    ```
    
    ```
    docker run --name redis-server \
    --network=yelb-network \
    -v redis-data:/data \
    -p 6379:6379 \
    -d redis:4.0.2
    
6. Inspect Volume Usage
  - Inspect the volumes to confirm they are in use:
    ```
      docker volume inspect pg-data
      docker volume inspect redis-data
    ```


* Validating the existing docker volumes and the containers using it

![alt text](<Screenshot 2025-04-09 at 12.33.38 AM.png>)


* Validating the data consistency from Web UI after restarting new db and caching servers (redis-server, postgres-db) - http://localhost:8080

![alt text](<Screenshot 2025-04-08 at 11.53.51 PM.png>)