import json
import boto3
def lambda_handler(event, context):
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event['body']
    bucket_name = body['bucket']
    directorio = body['directorio'].rstrip('/') + '/'
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key=directorio)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "bucket": bucket_name,
            "directorio_creado": directorio
        })
    }
