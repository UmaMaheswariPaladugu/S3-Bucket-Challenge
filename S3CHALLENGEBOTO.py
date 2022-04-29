import boto3
import uuid


s3=boto3.client("s3",aws_access_key_id='AKIAYIEPAEP7IMPYULUX',aws_secret_access_key='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',region_name='us-east-1')
print(s3)
y=s3.create_bucket(Bucket='marvelaccesslog')
def create_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(uuid.uuid4())])
for i in range(1,11):
    s=create_bucket_name('marvel')
    response=s3.create_bucket(Bucket=s)
    print(response)
    if(i!=5):
        s3.upload_file(Filename=r'C:\Users\MAHESWARI\Downloads\mixkit-going-down-a-curved-highway-down-a-mountain-41576.mp4',Bucket=s, Key='captain.mp4')
    else:
        #s3.upload_file(Filename=r'C:\Users\MAHESWARI\Downloads\firstpage.html',Bucket=s, Key='public.html',ExtraArgs={'ACL': 'public-read'})
        s3.upload_file(Filename=r'C:\Users\MAHESWARI\Downloads\mixkit-going-down-a-curved-highway-down-a-mountain-41576.mp4',Bucket=s, Key='public.mp4',ExtraArgs={'ACL': 'public-read'})
        print(s)
        response2 = s3.put_bucket_versioning(Bucket=s,VersioningConfiguration={'MFADelete': 'Disabled','Status': 'Enabled',},)
        response3 = s3.get_bucket_versioning(Bucket=s)
        print(response3)
        response4 = s3.put_bucket_logging(Bucket=s,BucketLoggingStatus={'LoggingEnabled': {'TargetBucket':'marvelaccesslog' ,'TargetPrefix': 'marvel'} })
        response5 = s3.get_bucket_logging(Bucket=s)
        print(response5)
        
        

