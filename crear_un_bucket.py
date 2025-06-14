import json
import boto3
def lambda_handler(event, context):
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event['body']
    bucket_name = body['bucket']
    
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'bucket_creado': bucket_name
        })
    }
