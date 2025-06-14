import json
import boto3
import base64
def lambda_handler(event, context):
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event['body']
    bucket_name = body['bucket']
    directorio = body['directorio'].rstrip('/')
    file_name = body['file_name']
    file_content_b64 = body['file_content_base64']
    
    file_bytes = base64.b64decode(file_content_b64)
    key = f"{directorio}/{file_name}"
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=key, Body=file_bytes)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'bucket': bucket_name,
            'key_subido': key
        })
    }
