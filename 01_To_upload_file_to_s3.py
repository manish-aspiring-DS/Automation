# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:47:24 2023

@author: Pandas Analytics Hub   ||   p.analyticshub@gmail.com   || +91-9774083186



#----------------Code to upload files from local to S3----------------#

"""

# Importing the Pacakages
import boto3

# Defining the variables
# A good practice to define keys or variables.
# Easier to manage  & easier to update.

AWS_ACCESS_KEY_ID = 'Place the aws access key id here within quotes'
AWS_SECRET_ACCESS_KEY = 'Place the aws secret access key here within quotes '

# Keep in mind to only place the name of bucket (The top level)
BUCKET_NAME='Name of the s3 bucket in which you want to upload file '

# Keep the path of folder in which file need to be uploaded
# For e.g folder/subfolder/file_name(with extension)
UPLOAD_TARGET='Place the folder subfolder & file name here'

# Keep the path of local file 
# Make sure we are using forward slash "/" in the path
LOCAL_SOURCE_FILE='Place the path of local file to be uploaded'

# Creating a user defined function for uploading file to S3.
# Functions help break down complex logic into smaller,
# more manageable pieces, making the code easier to read
# and understand, which is a good coding practice.

def upload_local_to_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
                       ,BUCKET_NAME,LOCAL_SOURCE_FILE,UPLOAD_TARGET):
    # Creating session for logging in the AWS
    # Session would use AWS Access Key ID & AWS Secret access key to lgin
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY 
    )
    # creating an S3 object to access the resources of AWS S3
    s3 = session.resource('s3')
        
    # Filename - File to upload
    # Bucket - Bucket to upload to (the top level directory under AWS S3)
    # Key - S3 object name (can contain subdirectories).
    s3.meta.client.upload_file(Filename=LOCAL_SOURCE_FILE, Bucket=BUCKET_NAME, Key=UPLOAD_TARGET)


if __name__ == '__main__':
    try :
        upload_local_to_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY
                               ,BUCKET_NAME,LOCAL_SOURCE_FILE,UPLOAD_TARGET)
        print("File Uploaded Sucessfully")
    except Exception as e:
        print(f"Failed to upload because :\n{e}")

