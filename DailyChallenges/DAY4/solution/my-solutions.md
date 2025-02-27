### AWS Networking
- App server created in public subnet
- Database created in private subnet

### App and web server setup 
- launch ec2 servers for app and database
- to start the app copy the code to the server and start the app
- on db server install the mysql server
    - Install 
        - wget https://dev.mysql.com/get/mysql84-community-release-el9-1.noarch.rpm
        - sudo yum localinstall mysql84-community-release-el9-1.noarch.rpm
        - yum repolist enabled | grep mysql.*-community
        - sudo yum-config-manager --disable mysql-8.4-lts-community
        - sudo yum-config-manager --enable  mysql80-community
        - sudo yum install mysql-community-server
        - systemctl status mysqld
        - sudo systemctl start mysqld
        - 

    - Login as root, create new custom user(same username and password should be mentioned in the app code)
        - get root password
        ```
            - sudo grep 'temporary password' /var/log/mysqld.log
            - mysql -u root -p
        ```
        -   
        ```
            CREATE USER 'pratik'@'localhost' IDENTIFIED BY 'Admin@123';
            GRANT ALL PRIVILEGES ON *.* TO 'pratik'@'localhost' WITH GRANT OPTION;
            FLUSH PRIVILEGES;
        ```
           
        - create database and table
        ```
            CREATE DATABASE todo_app;
            USE todo_app;
            CREATE TABLE todos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task VARCHAR(255) NOT NULL
            );
        ```
        -


    

- install nginx on app server
- configure the nginx for http with attached default.conf
- to configure https redirect
    - generate tls sertificates
    - update the nginx config



