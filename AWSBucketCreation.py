#Importing sys to file
import sys
sys.path.insert(0, r'C:\Users\a.sannazzaro')

#Importing boto3 and creating resource and creating a bucket
import boto3
s3 = boto3.resource('s3')

#Get user bucket name
bucket_name = input("Enter name for bucket: ")

s3.create_bucket(Bucket=bucket_name)

#Creating folder
s3 = boto3.resource('s3')
folder = input("Enter folder name: ")
my_bucket = s3.Bucket(bucket_name)
my_bucket.put_object(Key= folder+'/')

#Setting bucket access to public
import boto3
import json

s3client = boto3.client('s3')
#bucket_name = 'fdutest22'
s3client.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': False,
                    'IgnorePublicAcls': False,
                    'BlockPublicPolicy': False,
                    'RestrictPublicBuckets': False
                }
            )


s3client.put_bucket_ownership_controls( 
    Bucket=bucket_name,    
    OwnershipControls={
        'Rules': [{'ObjectOwnership' : 'BucketOwnerPreferred'}]
    }
)
s3client.put_bucket_acl(Bucket=bucket_name, ACL='public-read')

s3 = boto3.resource('s3')
#bucket_name = 'fdutest22'

my_bucket = s3.Bucket(bucket_name)
my_bucket.Acl().put(ACL='public-read')

#Enabling bucket policy
policy_payload = {
   
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MakeItPublic",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::%s/*" % bucket_name
        }
    ]
}
   
s3client.put_bucket_policy(Bucket=bucket_name, 
	Policy=json.dumps(policy_payload))

#Enable static web hosting
s3 = boto3.resource('s3')
#bucket_name = 'fdutest22'

website_payload = {
    'ErrorDocument': {
        'Key': 'error.html'
    },
    'IndexDocument': {
        'Suffix': 'index.html'
    }
}


bucket_website = s3.BucketWebsite(bucket_name)
bucket_website.put(WebsiteConfiguration=website_payload)

#Get user directory to upload
userDir = input("Enter the directory to upload all files from: ")

#Uploading a directory
import os
directory = userDir
filelist = os.listdir(directory)
for file in filelist:
    my_bucket.upload_file(Filename=directory+'\\'+file, Key=folder+'/'+file) 
    print(file+" is uploaded")




