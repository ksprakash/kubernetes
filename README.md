ALB Controller arn: arn:aws:iam::841451480360:policy/ALBIngressControllerIAMPolicy1


eksctl create iamserviceaccount \
    --region us-east-1 \
    --name alb-ingress-controller \
    --namespace kube-system \
    --cluster sg-sai-cluster \
    --attach-policy-arn arn:aws:iam::841451480360:policy/ALBIngressControllerIAMPolicy1 \
    --override-existing-serviceaccounts \
    --approve

AWS-LOAD-BALANCER-CONTROLLER
helm repo add eks https://aws.github.io/eks-charts
# If using IAM Roles for service account install as follows -  NOTE: you need to specify both of the chart values `serviceAccount.create=false` and `serviceAccount.name=aws-load-balancer-controller`
helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName=sg-sai-cluster -n kube-system --set serviceAccount.create=false --set serviceAccount.name=alb-ingress-controller
# If not using IAM Roles for service account
helm install aws-load-balancer-controller eks/aws-load-balancer-controller --set clusterName= -n kube-system

Public Subnets has some tags
kubernetes.io/role/elb	1
kubernetes.io/cluster/sg-sai-cluster	shared