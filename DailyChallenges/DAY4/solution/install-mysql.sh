#!/bin/bash

wget https://dev.mysql.com/get/mysql84-community-release-el9-1.noarch.rpm 
sudo yum localinstall mysql84-community-release-el9-1.noarch.rpm -y 
yum repolist enabled | grep mysql.*-community
sudo yum-config-manager --disable mysql-8.4-lts-community
sudo yum-config-manager --enable  mysql80-community
sudo yum install mysql-community-server -y
systemctl status mysqld
sudo systemctl start mysqld