# Frontend and Backend Integration Test Project

This project demonstrates the integration between a frontend and backend service deployed on a local Kubernetes cluster using Kind. The goal is to verify that the frontend service can successfully communicate with the backend service and display the greeting message fetched from the backend.

## GitHub Repository Structure:

```
qa-test/
├── backend/
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── Deployment/
│   ├── backend-deployment.yaml
│   └── frontend-deployment.yaml
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── app.js
├── src/
│   └── test/
│       └── FrontendBackendIntegrationTest.java
└── README1.md
```



## Step-by-Step Setup Instructions

### Step 1: Install Kind on Windows using Chocolatey

1. **Open Command Prompt as Administrator:**
    - Right-click on the Start menu and select "Command Prompt (Admin)" to open Command Prompt with administrative privileges.

2. **Install Chocolatey (if not already installed):**
    - Chocolatey is a package manager for Windows. To install Chocolatey, run the following command in your Command Prompt:
      ```shell
      @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
      ```

3. **Install Kind using Chocolatey:**
    - After installing Chocolatey, you can install Kind by running the following command:
      ```shell
      choco install kind
      ```

4. **Verify Installation:**
    - Once installed, verify that Kind is set up correctly by running:
      ```shell
      kind version
      ```
    - This command should display the version of Kind installed on your system.

5. **Create a Kubernetes Cluster with Kind:**
    - To create a local Kubernetes cluster using Kind, run:
      ```shell
      kind create cluster
      ```

6. **Manage Clusters with Kind:**
    - You can now manage your clusters, deploy applications, and perform testing as needed using Kind.

### Step 2: Clone the Project Repository

1. **Clone the Repository:**
    - Clone the repository containing the services to your local machine:
      ```shell
      git clone https://github.com/Vengatesh-m/qa-test
      cd qa-test
      ```

### Step 3: Deploy Services to the Kubernetes Cluster

1. **Apply Kubernetes Deployment Files:**
    - Deploy the backend and frontend services using the provided YAML files:
      ```shell
      kubectl apply -f Deployment/backend-deployment.yaml
      kubectl apply -f Deployment/frontend-deployment.yaml
      ```

2. **Check Services and Pods:**
    - Verify that the services and pods are running:
      ```shell
      kubectl get services
      kubectl get pods
      ```

### Step 4: Verify Backend Service

1. **Test Backend Service Communication:**
    - Use a temporary pod to test communication with the backend service:
      ```shell
      kubectl run curl-pod --image=radial/busyboxplus:curl -i --tty --rm
      curl http://backend-service:3000/greet
      ```
    - Expected output:
      ```json
      {"message":"Hello from the Backend!"}
      ```

2. **Port Forward to Access Backend Service Locally:**
    - Alternatively, you can port forward to access the backend service from your local machine:
      ```shell
      kubectl port-forward svc/backend-service 8080:3000
      ```
    - Then, test the endpoint:
      ```shell
      curl http://localhost:8080/greet
      ```

### Step 5: Verify Frontend Service

1. **Port Forward to Access Frontend Service Locally:**
    - Port forward to access the frontend service from your local machine:
      ```shell
      kubectl port-forward svc/frontend-service 30997:80
      ```

2. **Test Frontend Service:**
    - Open a browser and navigate to `http://localhost:30997` to verify that the frontend service correctly displays the greeting message fetched from the backend.
    - You can also run the Maven test to check the integration:
      ```shell
      mvn clean test
      ```

## Summary

By following these steps, you will set up and run the automated integration tests for the frontend and backend services deployed on a local Kubernetes cluster.

## Note

Ensure that you have Docker installed and running on your machine since Kind uses Docker to create the Kubernetes clusters.
