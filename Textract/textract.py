import boto3
from trp import Document

#S3 Bucket Data
s3bucketname = "corleone-interlude"
Documentname = "sample.jpg"

#Amazon Textract Client
textractmodule = boto3.client('textract')

#Plaintext detection from document
response = textractmodule.detect_document_text(
    Document = {
        'S3Object':{
            'Bucket': s3bucketname,
            'Name': Documentname,
            
        }
    }
)
print('-------------------Print Plaintext detected text---------------')
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print('\033[92m' +item["Text"] + '\033[92m')
