## End to End ML-modular project with deployment

AWS deployment:

##Docker setup in EC2
1. sudo apt-get update -y
2. sudo apt-get upgrade
3. curl -fsSL https://get.docker.com -o get-docker.sh
4. sudo sh get-docker.sh
5. sudo usermod -aG docker ubuntu
6. newgrp docker
7. ##configure ec2 as self hosted runner
8. ##setup github secrets
9. AWS_ACCESS_KEY_ID
10. AWS_SECRET_ACCESS_KEY
11. AWS_REGION = ap-south-1
12. AWS_ECR_LOGIN_URI = 275234131660.dkr.ecr.ap-south-1.amazonaws.com
13. ECR_REPOSITORY_NAME = student_performance
