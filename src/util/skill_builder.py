import os
import boto3
from ask_sdk_s3.adapter import S3Adapter
from ask_sdk_core.skill_builder import CustomSkillBuilder

bucket_region = os.environ.get('BUCKET_REGION')
bucket_name = os.environ.get('BUCKET_NAME')

s3_client = boto3.client('s3', region_name=bucket_region)
s3_adapter = S3Adapter(bucket_name,
                       path_prefix='gods_oracle/persistent_attributes',
                       s3_client=s3_client)

sb = CustomSkillBuilder(persistence_adapter=s3_adapter)
