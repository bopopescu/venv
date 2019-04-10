#!/usr/bin/python3.6
import yaml
import sys
import boto3
from botocore.exceptions import ClientError

ecinstance_id = sys.argv[1]

ec2 = boto3.client('ec2')


response = ec2.describe_instances()
#rint(response)
#for i in response:
    #print(i)


response2 = ec2.describe_instance_status()
#print(response2)

#for i in response2:


ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    if (instance.id == ecinstance_id):
            print (instance.id , instance.state['Name'])
