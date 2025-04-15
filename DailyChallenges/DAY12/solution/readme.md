### Steps followed to Complete the Challenge
---
1. Created a Docker Network:
  - Started by creating a user-defined bridge network for container communication.
    ``` docker network create yelb-network ```
2. Run the Redis Server
  - Deployed Redis, which acts as a caching layer to store page views.
```
docker run --name redis-server \
  --network=yelb-network \
  -p 6379:6379 \
  -d redis:4.0.2
```
3. Run the PostgreSQL Database:
  - Started PostgreSQL to store persistent vote data.
```
docker run --name yelb-db \
  --network=yelb-network \
  -p 5432:5432 \
  -d mreferre/yelb-db:0.6
```
4. Run the Yelb Appserver:
  - Launched the application server, ensuring it connects to Redis and PostgreSQL.

```
docker run --name yelb-appserver \
  --network=yelb-network \
  -d -p 4567:4567 \
  -e RACK_ENV=test \
  mreferre/yelb-appserver:0.7
```
5. Run the Yelb UI:
  - Deployed the front-end, connecting it to the app server, and exposing it for user access.
```
docker run --name yelb-ui \
  --network=yelb-network \
  -d -p 8080:80 \
  -e UI_ENV=test \
  mreferre/yelb-ui:0.10
```
6. Test the Application:
    - Validating the existing docker networks and the containers using it and 
    - ![alt text](<Screenshot 2025-04-08 at 11.58.25 PM.png>)

    - ![alt text](<Screenshot 2025-04-09 at 12.02.25 AM.png>)

    - Accessing web UI of the application from browser (http://localhost:8080) and  Interact with the Yelb UI to confirm all services are working correctly.

    - ![alt text](<Screenshot 2025-04-08 at 11.53.51 PM.png>)