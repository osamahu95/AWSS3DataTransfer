import boto3
from S3Credential import S3Credential
from file_write import write_to_file

def get_source_objects(bucket_name, s3_boto):
    objects = []
    paginator = s3_boto.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name)
    for page in pages:
        for obj in page['Contents']:
            objects.append(obj['Key'])
    return objects

def transfer_objects(credential: S3Credential):
    source_s3 = boto3.client(
        's3',
        aws_access_key_id = credential.get_source_access_key_id(),
        aws_secret_access_key = credential.get_source_secret_access_key(),
    )

    dest_s3 = boto3.client(
        's3',
        aws_access_key_id = credential.get_dest_access_key_id(),
        aws_secret_access_key = credential.get_dest_secret_access_key()
    )

    source_bucket_name = credential.get_source_bucket_name()
    dest_bucket_name = credential.get_dest_bucket_name()

    print("Started....")

    source_objects = get_source_objects(source_bucket_name, source_s3)
    dest_objects = get_source_objects(dest_bucket_name, dest_s3)

    missing_objects = list(set(source_objects) - set(dest_objects))

    print("Difference: {0} and length {1}".format(missing_objects, len(missing_objects)))

    if missing_objects:
        for obj in missing_objects:  
            try:
                print("------------------------------------------------------")
                print(f"Start for {obj}")
                dest_s3.copy_object(CopySource = {
                    'Bucket': credential.get_source_bucket_name(),
                    'Key': obj
                }, Bucket = dest_bucket_name, Key=obj)
                print(f"End for {obj}")
                print("------------------------------------------------------")
            except Exception as e:
                print(f"Error while creating the object in Bucket {dest_bucket_name} for {obj}")
                write_to_file(f"Error while creating the object in Bucket {dest_bucket_name} for {obj}")