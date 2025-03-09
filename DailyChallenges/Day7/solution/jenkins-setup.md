## Setting Up Jenkins on Rancher Desktop

### Prerequisites
- **Rancher Desktop installed**
- **kubectl installed and configured** (`kubectl get nodes` should show nodes running)
- **Helm installed** (`brew install helm` if not installed)

---

### Steps to Set Up Jenkins

#### 1️ Verify Kubernetes Cluster
Ensure Kubernetes is running:
```sh
kubectl get nodes
```

#### 2️ Add Helm Repository
```sh
helm repo add jenkins https://charts.jenkins.io
helm repo update
```

#### 3 Install Jenkins with admin username and password
```sh
helm repo add jenkins https://charts.jenkins.io
helm repo update
helm install jenkins jenkins/jenkins \\n  --set controller.serviceType=ClusterIP \\n  --set controller.admin.username=admin \\n  --set controller.admin.password=admin123\n
```


#### 4 Access Jenkins UI
```sh
kubectl port-forward svc/jenkins 8080:8080 -n jenkins
```
Then open [http://localhost:8080](http://localhost:8080) and log in using the retrieved password.

#### 5 Install Kubernetes Plugin
*Note - This should be installed by deafault with above helm installation, but if not installed below steps can be followed.*

Inside Jenkins:
1. Go to **Manage Jenkins > Manage Plugins**.
2. Install **Kubernetes Plugin**.
3. Restart Jenkins.

#### 6 Configure Kubernetes Cloud in Jenkins
1. **Go to** `Manage Jenkins > Configure System`.
2. **Add a new cloud** > Kubernetes.
3. **Kubernetes URL**: Use `kubectl cluster-info` to get API URL. (https://kubernetes.default)
4. **Jenkins URL**: Set `http://jenkins.jenkins.svc.cluster.local:8080`
5. **Namespace**: `default` OR `jenkins`
6. **Test Connection**.

#### 7 Configure Pod Template for Executors
1. **Add Pod Template** > Set label (e.g., `k8s-agent`).
2. **Container Template:**
 - Can be configured here or it can be passed in the jenkins pipeline script

#### 8 Run a Test Job
1. **Create a new job**.
