from google.cloud import storage
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

key_path = 'iam_automation_storage.json'
project_id = 'iti-poc-372910'

credentials = service_account.Credentials.from_service_account_file(key_path)

storage_client = storage.Client(credentials=credentials, project=project_id)

bucket_name = 'amy_practice'

bucket = storage_client.get_bucket(bucket_name)

local_file_path = '/Users/chenruoting/Desktop/test/GoogleCloud/index.html'
gcs_object_name = 'index.html'

blob = bucket.blob(gcs_object_name)
blob.upload_from_filename(local_file_path)

print(f'檔案 {local_file_path} 已成功上傳到 Google Cloud Storage 中的 {gcs_object_name}')

"""
buckets = storage_client.list_buckets()
for bucket in buckets:
    print(bucket.name)
"""