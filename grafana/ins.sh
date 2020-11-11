#!/bin/sh
#kubectl create configmap kapi --from-file=dashboards/Kubernetes_API_server.json
# kubectl create secret generic datasource-secret --from-file=datasource-secret.yaml
helm install --debug grafana . --set admin.password=ey123

#"Password: $(kubectl get secret grafana-admin --namespace default -o jsonpath="{.data.GF_SECURITY_ADMIN_PASSWORD}" | base64 --decode)"