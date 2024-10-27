class S3Credential:
    def __init__(self):
        self.source_bucket_name = None
        self.dest_bucket_name = None
        self.source_access_key_id = None
        self.source_access_key_id = None
        self.dest_access_key_id = None
        self.dest_secret_access_key = None

    def set_source_bucket_name(self, bucket_name):
        self.source_bucket_name = bucket_name if bucket_name else None
    def get_source_bucket_name(self):
        return self.source_bucket_name
    
    def set_dest_bucket_name(self, bucket_name):
        self.dest_bucket_name = bucket_name if bucket_name else None
    def get_dest_bucket_name(self):
        return self.dest_bucket_name
    
    def set_source_access_key_id(self, access_key_id):
        self.source_access_key_id = access_key_id if access_key_id else None
    def get_source_access_key_id(self):
        return self.source_access_key_id
    
    def set_source_secret_access_key(self, secret_access_key):
        self.source_secret_access_key = secret_access_key if secret_access_key else None
    def get_source_secret_access_key(self):
        return self.source_secret_access_key
    
    def set_dest_access_key_id(self, access_key_id):
        self.dest_access_key_id = access_key_id if access_key_id else None
    def get_dest_access_key_id(self):
        return self.dest_access_key_id
    
    def set_dest_secret_access_key(self, secret_access_key):
        self.dest_secret_access_key = secret_access_key if secret_access_key else None
    def get_dest_secret_access_key(self):
        return self.dest_secret_access_key