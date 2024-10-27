from dotenv import load_dotenv
import os

from S3Credential import S3Credential
from s3transfer_aws import transfer_objects

if __name__ == "__main__":
    load_dotenv()

    s3_credential = S3Credential()
    s3_credential.set_source_bucket_name(os.getenv("SOURCE_ACCOUNT_BUCKET_NAME"))
    s3_credential.set_dest_bucket_name(os.getenv("DEST_ACCOUNT_BUCKET_NAME"))
    s3_credential.set_source_access_key_id(os.getenv('SOURCE_ACCESS_KEY_ID'))
    s3_credential.set_source_secret_access_key(os.getenv('SOURCE_SECRET_ACCESS_KEY'))
    s3_credential.set_dest_access_key_id(os.getenv('DEST_ACCESS_KEY_ID'))
    s3_credential.set_dest_secret_access_key(os.getenv('DEST_SECRET_ACCESS_KEY'))

    transfer_objects(s3_credential)