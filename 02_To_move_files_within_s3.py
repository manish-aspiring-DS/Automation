# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:30:13 2023

@author: Pandas Analytics Hub   ||   p.analyticshub@gmail.com   || +91-9774083186

"""

# =============================================================================
#                          Code to move files within S3
# =============================================================================


# Importing the Pacakages
import boto3

# Defining the variables
# A good practice to define keys or variables.
# Easier to manage  & easier to update.

AWS_ACCESS_KEY_ID = 'Place the aws access key id here within quotes'
AWS_SECRET_ACCESS_KEY = 'Place the aws secret access key here within quotes '

# Keep in mind to only place the name of bucket (The top level)
SOURCE_BUCKET_NAME='Name of the s3 bucket from which we want to move file '
ARCHIVE_BUCKET='Name of the s3 bucket in which we want to move file'

# Keep the path of folder from file need to be moved
# For e.g folder/subfolder/file_name(with extension)

# =============================================================================
# s3://Bucket Name on S3/ Folder name /Sub folder /file name.csv
# =============================================================================

SOURCE_TARGET='s3 path from which file needs to be moved excluding the bucket name'
ARCHIVE_TARGET='s3 path of to which file needs to be moved excluding the bucket name'


# A dictionary with bucket & File path mapping
# Make sure we are using forward slash "/" in the path
S3_SOURCE_LOCATION={'Bucket':SOURCE_BUCKET_NAME,
           'Key': SOURCE_TARGET}




# Creating a user defined function for moving file within S3.
# Functions help break down complex logic into smaller,
# more manageable pieces, making the code easier to read
# and understand, which is a good coding practice.

# Function to copy files from one S3 location to other and then delete it from source S3 location  
  
def move_file_on_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,S3_SOURCE_LOCATION,
                    ARCHIVE_BUCKET,SOURCE_BUCKET_NAME,SOURCE_TARGET,ARCHIVE_TARGET):
    #logging in the aws
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY 
    )
    # Creatin s3 object
    s3 = session.resource('s3')
    
    # Copy files from one location to other by calling copy method.
    s3.meta.client.copy(S3_SOURCE_LOCATION,ARCHIVE_BUCKET,ARCHIVE_TARGET)
    # Deleting the file which has been moved by calling delete method
    s3.Object(SOURCE_BUCKET_NAME,SOURCE_TARGET).delete()

if __name__ == '__main__':
    try :
        move_file_on_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,S3_SOURCE_LOCATION,ARCHIVE_BUCKET,SOURCE_BUCKET_NAME,SOURCE_TARGET,ARCHIVE_TARGET)
        print("File has been moved Sucessfully")
    except Exception as e:
        print(f"Failed to complete move because :\n{e}")

