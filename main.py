import json
import boto3
import base64
client = boto3.client('lambda')

with open('example.txt', 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

payload = {
    'file_name':'uploaded_file.txt',
    'file_content': file_content
}
response = client.invoke(
    FunctionName='s3bucket-dump',
    Payload=json.dumps(payload),
)

print(response['Payload'].read())