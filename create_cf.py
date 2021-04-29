import sys
import json
import boto3
from botocore.exceptions import ClientError

def main(aws_profile_name, stack_name, template_URL, key_name):
    session = boto3.Session(profile_name=aws_profile_name)
    cf = session.client('cloudformation') 
    params = {
        'StackName': stack_name,
        'TemplateURL': template_URL,
        'Parameters': [{
            'ParameterKey': 'KeyName',
            'ParameterValue': key_name
        }],
    }
    
    try:
        print('Creating stack ...')
        cf_result = cf.create_stack(**params)
        waiter = cf.get_waiter('stack_create_complete')
        print("Waiting for stack creation ... ")
        waiter.wait(StackName=stack_name)
    except ClientError as ex:
        error_message = ex.response['Error']['Message']
        print(error_message)
    else:
        print(json.dumps(
            cf.describe_stacks(StackName=cf_result['StackId']),
            default=str
        ))

if __name__ == '__main__':
    main(*sys.argv[1:])