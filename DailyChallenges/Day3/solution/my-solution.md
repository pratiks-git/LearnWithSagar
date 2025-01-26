-- 
Considering that we are configuring the nginx on differnet server and the other services are configured on seperate servers
e.g server1 nginx
    server2 jenkins
    server3 grafana

1. Launched EC2 instance with the terraform setup
2. Installed pre-requisite softwares
    - sudo yum update
    - sudo yum install nginx
        sudo systemctl start nginx
        sudo systemctl enable nginx (to start service when system bootup)
    - sudo yum install docker
        sudo usermod -aG docker ec2-user
        sudo systemctl restart docker
        sudo sytemctl enable docker (to start service when system bootup)
3. Installed jenkins and grafana with dokcer image
    - docker run -d -p 3000:3000 --name=grafana grafana/grafana-enterprise
    - docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --name=jenkins jenkins/jenkins:lts-jdk11

4. Now the services can be accessed on respective ports on localhost
    - http://localhost:8080
    - http://localhost:3000

5. Created a file in folder conf.d - /etc/nginx/conf.d/default.conf
6. Now we configure our own local machine (i.e, client) to access these services with the domains grafana.local, jenkins.local
    - Update the /etc/hosts file on local machine
    ```
    <NGINX SERVER PUBLIC IP ADDRESS> grafana.local
    <NGINX SERVER PUBLIC IP ADDRESS> jenkins.local

7. Now when we access the above domains, these are passed as server_name parameter/header to the nginx. Based on these values nginx routes the traffic to respective backend server
8. Configure SSL redirect
    1. Generate self-signed SSL certificate 
        ```
        sudo mkdir /etc/nginx/ssl
        sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/server.key -out /etc/nginx/ssl/server.crt
        ```
    2. Update the /etc/nginx/conf.d/default.conf to redirect all(to server_names grafana.local, jenkins.local) http traffic to https
    3. Update resepective server blocks for both domains
9. To configure basic http authentication
    1. Install htpassd utility
        For al2023 based instances - sudo yum install httpd-tools
    2. Generate the username and password with htpassd command
        ```
        htpasswd -c /etc/nginx/.htpasswd <username>
        ```
    3. Add the auth related directives to nginx.conf
    ###### Note:   Jenkins uses http auth headers, so in order to use http_auth with jenkins match the http username and password with Jenkins credentials

