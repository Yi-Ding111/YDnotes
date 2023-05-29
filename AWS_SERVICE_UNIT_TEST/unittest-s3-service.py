import requests
from bs4 import BeautifulSoup
import datetime
from io import BytesIO
import json
import os
import boto3
import pandas as pd

from datetime import datetime
import zipfile
from dotenv import load_dotenv
import sys
import unittest
from moto import mock_s3,mock_logs,mock_events,mock_lambda,mock_iam


from cash_rate_crawler_AU import lambda_handler

# global environment variables
# cash_rates_envir={
#     'bucket_name':os.environ.get('bucket_name','neo-external-data'),
#     'prefix':os.environ.get('prefix','AU/national_external_data/cash_rates/'),
#     'url':os.environ.get('url','https://www.rba.gov.au/statistics/cash-rate/')
# }

@mock_s3
class TestLambdaEvents(unittest.TestCase):

    # # mock s3 service
    # @mock_s3
    # @mock_logs
    # @mock_events
    # @mock_lambda
    def setUp(self):
        '''
        create a bucket and destination virtual AWS account for s3 bucekt and sub folders
        '''

        self.bucket_name='neo-external-data'
        self.prefix='AU/national_external_data/cash_rates/'
        self.log_group_name='/aws/lambda/cash_rate_crawler_AU'
        self.lambda_name='cash_rate_crawler_AU'
        self.rule_name='cash_rate_rule'

        # mock s3 service
        self.s3_client=boto3.client('s3',region_name='us-west-1')

        # create a bucket
        self.s3_client.create_bucket(Bucket=self.bucket_name,
            CreateBucketConfiguration={
            'LocationConstraint':'us-west-1'
        })

        # enable versioning
        self.s3_client.put_bucket_versioning(Bucket=self.bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )

        # create folder
        self.s3_client.put_object(Bucket=self.bucket_name,
            Key=self.prefix
        ) 




    def test_s3_store(self):
        '''
        test if the the lambda can push files into s3 bucket
        '''
        # run lambda 

        test_event={
            'test':1
        }
        
        lambda_handler(event=test_event,context=None)

        response_s3 = self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=self.prefix
        )

        print(response_s3)

        # the s3 bucket is writtrn
        if response_s3['KeyCount']>1:
            self.assertTrue(True)
        # the s3 bucket is empty
        else:
            self.fail('lambda function can not push data into bucket')








    # @mock_s3
    def tearDown(self) -> None:
        '''
        delete s3 bucket and objects in mocked AWS account
        '''
        # remove S3 objects and buckets
        s3_client=boto3.client('s3',region_name='us-west-1')

        # grab objects in bucket
        response=s3_client.list_objects(Bucket=self.bucket_name)

        # response=s3_client.list_objects(Bucket='neo-external-data')
        # print(response)

        if 'Contents' in response:
            objects = response['Contents']
            # delete objects
            for obj in objects:
                s3_client.delete_object(Bucket=self.bucket_name,Key=obj['Key'])

        
        # response=s3_client.list_objects(Bucket='neo-external-data')
        # print(response)
        
        # delete bucket
        # response=s3_client.delete_bucket(Bucket='neo-external-data')


        




if __name__ == "__main__":





    load_dotenv()

    unittest.main()
