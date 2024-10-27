import boto3
from S3Credential import S3Credential
from file_write import write_to_file

def get_source_bucket_object_count(bucket_name, s3_bucket) -> int:
    try:
        count = 0
        paginator = s3_bucket.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name)
        for page in pages:
            count += len(page['Contents'])
        return count
    except Exception as e:
        print(f"Error getting object count: {e}")
        return 0
    
def is_object_exists(s3_bucket, bucket_name, key) -> bool:
    try:
        s3_bucket.head_object(Bucket=bucket_name, Key=key)
        print(f"{key} -> Object Exists in {bucket_name}")
        return True
    except Exception as e:
        print(f"Error Head Object no found: {e}")
        write_to_file(f"{key} -> Object not found")
        return False

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

    # get all objects count from source account
    total_objects = get_source_bucket_object_count(source_bucket_name, source_s3)
    print(f"Total Objects in the Source Account: {total_objects}")

    if total_objects > 0:
        paginator = source_s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=source_bucket_name)

        # iterate over each page
        for page in pages:
            for obj in page['Contents']:
                key = obj['Key']
                print(f"Copying Object: {key} Started")

                print("----------------------------------------------------------------")
                is_bucket_object_exists = is_object_exists(dest_s3, dest_bucket_name, key)
                if not is_bucket_object_exists:
                    try:
                        dest_s3.copy_object(CopySource = {
                            'Bucket': credential.get_source_bucket_name(),
                            'Key': key
                        }, Bucket = dest_bucket_name, Key=key)
                        print(f"Created Object with Key {key} in {dest_bucket_name}")
                    except Exception as e:
                        print(f"{key} Object Failed to Copied to {dest_bucket_name}")
                        write_to_file(f"{key} Object Failed to Copied to {dest_bucket_name}")
                else:
                    print(f"Object Key {key} already copied to {dest_bucket_name}")
                print("----------------------------------------------------------------")
                print(f"Copying Object: {key} End")
    print(f"No Objects Found in your Source {source_bucket_name} S3 Bucket")
