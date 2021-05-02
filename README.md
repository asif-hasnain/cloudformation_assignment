Deploys a Linux AWS EC2 instance with two volumes and two users.

Cloudformation file : cf.yml
<br />Script to create cloudformation stack : create_cf.py

## Pre-requisite: 
- AWS account
- AWS Credentials - https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
- Permission to S3 read file from S3 bucket, cloudformation, EC2 - https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/id_users_change-permissions.html
- python 3 in local computer - https://www.python.org/downloads/
- boto3 in local computer - https://pypi.org/project/boto3/

## Steps:
- Create key pair for Ec2 , user1 and user2 from EC2 -> Network & Security -> Key pairs
- upload cf.yml to s3 bucket and copy object url.
- Run create.py script with following command
- python3 create_cf.py 'AWS profile name' 'Stack Name' 's3 url of cf.yml' 'EC2 key pair name'
- Example : python3 create_cf.py default cf_ec2_stack https://cf-ec2-stack-bucket.s3.amazonaws.com/cf.yml instancekey
