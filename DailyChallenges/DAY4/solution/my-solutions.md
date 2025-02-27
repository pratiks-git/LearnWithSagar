### AWS Networking and security 

#### Networking 
- Created a Nat-gateway
- Created a route-table for the private subnet and add the route to NAT gateway

#### Security
- Security group for the EC2 instances
    - With usual practice, SG of database instance should allow inboud traffic from the SG of the app instance
    - Here I just created one SG and added a self-referencing rule for simplicity

#### EC2 instances
- App server created in public subnet
- Database created in private subnet


### App and DB server setup 

#### DB configuration

- On DB server install the mysql server with the script created at install-mysql.sh
    
    - ##### Configure DB user (IMP)

    - Login as root, create new custom user(same username and password should be mentioned in the app code)
        - get root password
        ```
            - sudo grep 'temporary password' /var/log/mysqld.log
            - mysql -u root -p
        ```
        -   Change/update root user password (required)
        ```
        ALTER USER 'root'@'localhost' IDENTIFIED BY 'Admin@123';
        ```
        - Create new app user for the flask app
        ```
            CREATE USER 'pratik'@'localhost' IDENTIFIED BY 'Admin@123';
            GRANT ALL PRIVILEGES ON *.* TO 'pratik'@'localhost' WITH GRANT OPTION;
            FLUSH PRIVILEGES;
        ```
        -
        ```
        CREATE USER 'flask_user'@'<PRIVATE_IP_OF_APP_INSTANCE>' IDENTIFIED BY 'Admin@123';
        GRANT ALL PRIVILEGES ON todo_app.* TO 'flask_user'@'<PRIVATE_IP_OF_APP_INSTANCE>';
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


#### App instance configuration
- To start the app copy the code to the app instance(git/scp) 
- Update the db_config(db connection) in the app.py with correct host, user, password

    ```
    - sudo yum install python3 python3-pip
    - pip -r requirements.txt
    - python3 app.py
    ```     

- Install nginx on app server
- Configure the nginx with attached default.conf (path should be /etc/nginx/conf.d/default.conf)
- To configure https redirect (as performed for Day3 challenge)
    - generate tls sertificates
    - update the nginx config



