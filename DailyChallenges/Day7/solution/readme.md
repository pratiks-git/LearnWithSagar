## Jenkins Magic: Build, Test, Deploy a Flask App!


### Steps followed to solve the challenge  

- Setup kubernetes cluster with Rancher Desktop
- Install and setup jenkins on kubernetes cluster using helm and configure it (Steps mentioned in the attached jenkins-setup.md)
- Create a Jenkins pipeline with the attached Jenkinsfile

- Setup a new repo/use the example repo for the flask app - 

Source repo - https://github.com/pallets/flask/tree/main/examples/tutorial

Cloned project repo for flask-app - https://github.com/pratiks-git/my-jenkins/tree/main

- Add a Docker file to the root path of the repo to build the image.





