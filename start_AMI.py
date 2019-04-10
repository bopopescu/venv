#!/usr/bin/python3.6
import boto3


ami_id = 'ami-0ef838dd7d1e336ef'


conn_args = {
    'aws_access_key_id': 'AKIAIOOEIHOTO2OAIZMA',
    'aws_secret_access_key': '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',
    'region_name': 'us-east-2'
}

ec2_res = boto3.resource('ec2', **conn_args)

new_instance = ec2_res.create_instances(
    ImageId=ami_id,
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my_aws_key2019')
 #   Tags = [{'Key': 'Name', 'Value': 'TES'}])


print("NEW instance started with ID:", )