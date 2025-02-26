
Usage:
- This bash script should be stored on the server for which we are going to generate health reports
- Necessary execute permissions should be provided to the default user or the user which will be using the script
(chmod u+x server-health.sh)

Configuring ssmtp server:
- To automate the server-health report via email, I have used ssmtp(Simple smtp)
- I have used below config to configure the ssmtp 
```
sudo yum install -y ssmtp
sudo vim /etc/ssmtp/ssmtp.conf
```

Update the ssmtp.conf file with below config
```
root=postmaster
mailhub=smtp.gmail.com:587
AuthUser=my-email@gmail.com
AuthPass=App_password
UseTLS=YES
UseSTARTTLS=YES
```
Note that app password needs to be created from respective google account.

