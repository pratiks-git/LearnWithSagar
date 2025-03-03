## Custom Images, Snapshots, and Cross-Region Magic!

- Used terraform to create initial instance from base ami-image, project for maintaing aws-infra can be reffered here - https://github.com/pratiks-git/my-cloud-infra
terraform apply --auto-approve


## Used below commands to install required packages on EC2 for hardening 
```
#Update the system packages
sudo yum update -y


#Install SSM manager 
sudo yum install amazon-ssm-agent -y
sudo systemctl enable amazon-ssm-agent


###Install other application related softwares


#Install docker and configure user
sudo yum install docker
systemctl status docker
sudo usermod -aG docker ec2-user
sudo systemctl restart docker


#Install nginx
sudo yum install nginx
sudo systemctl start nginx
sudo systemctl enable nginx


#Copy Application related files from source control or scp or S3

```
----------------------

### Create image and copy to target region
```
aws ec2 create-image --instance-id i-0acebdbd0938fc265 --name "Hardened-AMI-v1"
aws ec2 copy-image --name ami-copy --source-image-id ami-0cad7bf098d4d5836 --source-region us-east-1 --region eu-west-1 
```
### Create snapshotand copy to target region
```
aws ec2 create-snapshot --volume-id vol-0f4ca227d3a69aa40 --description source-snapshot
aws ec2 copy-snapshot --description copy-snapshot --destination-region eu-west-1 --source-region us-east-1 --source-snapshot-id snap-092a5b94cfb9a3aa9
```

### Create a new volume from the snapshot and attach to an ec2 instance 
```
aws ec2 create-volume --availability-zone eu-west-1c --snapshot-id snap-0e7ab8e1de3fdf5bd --region eu-west-1
aws ec2 attach-volume --volume-id vol-06485d2cc09394b98 --instance-id i-0664ee64ad133413d --device /dev/xvdf --region eu-west-1
```