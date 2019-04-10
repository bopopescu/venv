import boto3

myS3 = boto3.client('s3')

try:
    S3result = myS3.list_buckets()


    output = ""
    for bucket in S3result['Buckets']:
   #     output = output + bucket['Name']
        print(bucket['Name'])

    print(output)
except:
    print("S3 absent")

