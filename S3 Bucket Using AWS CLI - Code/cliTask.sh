 truncate -s 2GB task.txt
for i in {11..20}
do
  name="syed${i}"
  aws s3 mb s3://$name
 aws s3 cp  task.txt s3://$name
  aws s3api put-public-access-block \
  --bucket $name \
  --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
 done

 echo "Enter name of bucket to make public "

 read bucname

  aws s3api put-public-access-block \
  --bucket $bucname \
  --public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" 


echo "checking the $bucname is public enabaled or not "

aws s3api get-public-access-block  --bucket $bucname

aws s3api put-bucket-policy --bucket syed12 --policy file://publicpolicy.json
 
echo "enter name of bucket to enable versioning"

read bucket_name


aws s3api put-bucket-versioning --bucket $bucket_name --versioning-configuration Status=Enabled  

echo "checking $bucket_name bucket versioning status"

aws s3api get-bucket-versioning --bucket $bucket_name

echo "Bucket name for enable log access:"
read buc

aws s3api put-bucket-policy --bucket syed14 --policy file://policy.json

aws s3api put-bucket-logging --bucket $buc --bucket-logging-status file://logging.json




aws s3 ls --summarize --human-readable --recursive s3://syed17









			