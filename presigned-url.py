import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = event ["queryStringParameters"]["bucket"]
    file_name = event ["queryStringParameters"]["key"]

    response = s3.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': file_name},
                                                    ExpiresIn=900)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": f"<img src={response} />"
    }
