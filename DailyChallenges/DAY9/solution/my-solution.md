Done with Day8,9 challenge - Build a Distributed Logging System

#### The focus of this task was on to understand the essentials of log management, message queues, and monitoring, all critical to modern DevOps practices. 

### Taks performed: ( On EC2 test server)
- Install and Configure Message Queue
  - Install RabbitMq from official page (https://www.rabbitmq.com/docs/install-rpm)
  - Enable Management plugin
  - Set up user and queue
  - Configure network access

- Install required python libraries
  - Create producer and consumer scripts
  - Test consumer scripts

- Test Work queues with multiple workers(consumers)



### Install RabbitMq from official page
<details>
<summary>Read more about this topic</summary>

- Import signing keys 
    ```
    ## primary RabbitMQ signing key
    rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0 rabbitmq-release-signing-key.asc'
    ## modern Erlang repository
    rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key'
    ## RabbitMQ server repository
    rpm --import 'https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key'
    ```

- Add Yum Repositories for RabbitMQ and Modern Erlang
    - In order to use the Yum repository, a .repo file (e.g. rabbitmq.repo) has to be added under the /etc/yum.repos.d/ directory.
    ```
    # In /etc/yum.repos.d/rabbitmq.repo

    ##
    ## Zero dependency Erlang RPM
    ##

    [modern-erlang]
    name=modern-erlang-el9
    # Use a set of mirrors maintained by the RabbitMQ core team.
    # The mirrors have significantly higher bandwidth quotas.
    baseurl=https://yum1.rabbitmq.com/erlang/el/9/$basearch
            https://yum2.rabbitmq.com/erlang/el/9/$basearch
    repo_gpgcheck=1
    enabled=1
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key
    gpgcheck=1
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1
    type=rpm-md

    [modern-erlang-noarch]
    name=modern-erlang-el9-noarch
    # Use a set of mirrors maintained by the RabbitMQ core team.
    # The mirrors have significantly higher bandwidth quotas.
    baseurl=https://yum1.rabbitmq.com/erlang/el/9/noarch
            https://yum2.rabbitmq.com/erlang/el/9/noarch
    repo_gpgcheck=1
    enabled=1
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key
        https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
    gpgcheck=1
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1
    type=rpm-md

    [modern-erlang-source]
    name=modern-erlang-el9-source
    # Use a set of mirrors maintained by the RabbitMQ core team.
    # The mirrors have significantly higher bandwidth quotas.
    baseurl=https://yum1.rabbitmq.com/erlang/el/9/SRPMS
            https://yum2.rabbitmq.com/erlang/el/9/SRPMS
    repo_gpgcheck=1
    enabled=1
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-erlang.E495BB49CC4BBE5B.key
        https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
    gpgcheck=1
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1


    ##
    ## RabbitMQ Server
    ##

    [rabbitmq-el9]
    name=rabbitmq-el9
    baseurl=https://yum2.rabbitmq.com/rabbitmq/el/9/$basearch
            https://yum1.rabbitmq.com/rabbitmq/el/9/$basearch
    repo_gpgcheck=1
    enabled=1
    # Cloudsmith's repository key and RabbitMQ package signing key
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key
        https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
    gpgcheck=1
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1
    type=rpm-md

    [rabbitmq-el9-noarch]
    name=rabbitmq-el9-noarch
    baseurl=https://yum2.rabbitmq.com/rabbitmq/el/9/noarch
            https://yum1.rabbitmq.com/rabbitmq/el/9/noarch
    repo_gpgcheck=1
    enabled=1
    # Cloudsmith's repository key and RabbitMQ package signing key
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key
        https://github.com/rabbitmq/signing-keys/releases/download/3.0/rabbitmq-release-signing-key.asc
    gpgcheck=1
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1
    type=rpm-md

    [rabbitmq-el9-source]
    name=rabbitmq-el9-source
    baseurl=https://yum2.rabbitmq.com/rabbitmq/el/9/SRPMS
            https://yum1.rabbitmq.com/rabbitmq/el/9/SRPMS
    repo_gpgcheck=1
    enabled=1
    gpgkey=https://github.com/rabbitmq/signing-keys/releases/download/3.0/cloudsmith.rabbitmq-server.9F4587F226208342.key
    gpgcheck=0
    sslverify=1
    sslcacert=/etc/pki/tls/certs/ca-bundle.crt
    metadata_expire=300
    pkg_gpgcheck=1
    autorefresh=1
    type=rpm-md

    ```

- Install Packages with Yum 
    ```
    yum update -y
    yum install -y logrotate
    yum install -y erlang rabbitmq-server ## install RabbitMQ and zero dependency Erlang

    ```

- Start the Rabbit MQ server 
    ```
    systemctl enable rabbitmq-server

    systemctl start rabbitmq-server

    systemctl status  rabbitmq-server

    systemctl stop rabbitmq-server
    ```
</details>


### Configure RabbitMQ 

-  Enable Management Plugin:
    ```
    sudo rabbitmq-plugins enable rabbitmq_management
    sudo systemctl restart rabbitmq-server
    ```

- Configure Network Acces
    Edit /etc/rabbitmq/rabbitmq.conf to allow external access:
    ```
    loopback_users = none
    listeners.tcp.default = 5672
    ```
- Restart RabbitMQ


### Install required python libraries

-   ``` 
    sudo yum install pip
    pip install pika 
    ```

- Create the Producer, Consumer scripts (log_producer.py. log_aggregator.py)
- Run consumer scripts from multiple shells to replicate multiple workers/consumers
  
  ref - https://www.rabbitmq.com/tutorials/tutorial-two-python
