import boto3, os, time

AWS_DEFAULT_REGION = "us-east-2"
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucket_name = "lambda.created.me.on-" + str(time.time())



myS3 = boto3.resource('s3')
try:
    response = myS3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
    'LocationConstraint': AWS_DEFAULT_REGION}
    )
    print("bucket created succesfully" + str(response))
except:
      print("bucket not created")

