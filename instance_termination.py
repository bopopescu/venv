#!/usr/bin/python3.6
import sys
import boto3


instance_id = sys.argv[1]
print("instance_id:", instance_id)

ec2 = boto3.client('ec2')



response = ec2.terminate_instances(InstanceIds=[instance_id], DryRun=False)
print(response)

