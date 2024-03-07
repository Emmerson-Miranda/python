# Introduction
This python code waits until all replicas in of all deployments in a namespace are satisfied.

The ``run-test.sh`` script:
- Create a KinD cluster.
- Deploy two nginx:
- - The first will be deployed successfully.
- - The second deployment will never finish because it use a nodeSelector to a node that not exists.
- Run the python application.
- After 30 seconds patch the second deployment to fix it.
- Python app detect the change and finish.
- Destroy KinD cluster.

The execution log:

```
 % ./run-test.sh
Creating cluster "test-cluster" ...
 ✓ Ensuring node image (kindest/node:v1.29.1) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-test-cluster"
You can now use your cluster with:

kubectl cluster-info --context kind-test-cluster

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂
deployment.apps/nginx-success created
deployment.apps/nginx-pending created
Pending deployments: loop 1 ['nginx-pending', 'nginx-success']
Pending deployments: loop 2 ['nginx-pending']
Pending deployments: loop 3 ['nginx-pending']
deployment.apps/nginx-pending configured
Finished after 30 seconds
Shell Script Finished!
Deleting cluster "test-cluster" ...
Deleted nodes: ["test-cluster-control-plane"]

```
