

* Running simple docker containers for testing

e.g ```docker run -d --name my-nginx -p 8080:80 nginx```
Inspecting and exploring metadata - ```docker ps```,  ``` docker logs my-nginx ```, ``` docker inspect my-nginx ```

![Running simple docker containers](<Screenshot 2025-04-08 at 11.42.50 PM.png>)

* Accessing the nginx container from browser (http://localhost:8080)

![alt text](<Screenshot 2025-04-08 at 11.43.35 PM.png>)

* Accessing the container ran with custom docker image from brower (http://localhost:8081)

![alt text](<Screenshot 2025-04-08 at 11.43.26 PM.png>)