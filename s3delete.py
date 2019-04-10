import boto3, os

myS3 = boto3.client('s3')




try:
    S3result = myS3.list_buckets()

    output = ""
    for bucket in S3result['Buckets']:
        #     output = output + bucket['Name']

        if "lambda" in bucket['Name']:
            S3ToRemove = bucket['Name']
            print("Next bucket will be removed: " + S3ToRemove)
            try:
                response = myS3.delete_bucket(
                Bucket= S3ToRemove
                )
            except:
                print("Cant delete bucket")
            print("bucket removed")
        else:
            print(bucket['Name'])



 #   print(output)
except:
    print("S3 absent")