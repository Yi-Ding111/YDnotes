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

import tracemalloc
tracemalloc.start()

import warnings
warnings.filterwarnings("ignore",category=ResourceWarning)

from cash_rate_crawler_AU import lambda_handler

# global environment variables
# cash_rates_envir={
#     'bucket_name':os.environ.get('bucket_name','neo-external-data'),
#     'prefix':os.environ.get('prefix','AU/national_external_data/cash_rates/'),
#     'url':os.environ.get('url','https://www.rba.gov.au/statistics/cash-rate/')
# }

@mock_s3
@mock_logs
@mock_events
@mock_lambda
@mock_iam
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






        # print(event_client.describe_rule(Name='cash_rate_rule')['Arn'])

        self.lambda_client=boto3.client('lambda',region_name='us-west-1')
        self.lambda_client.create_function(
            FunctionName='cash_rate_crawler_AU',
            Runtime='python3.9',
            Timeout=300,
            Role=role_arn,
            Handler='cash_rate_crawler_AU.lambda_handler',
            Code={
                'ZipFile':"""
            def lambda_handler(event,context):
                print('hello world!')

                return{
                    'status':200
                }
            """
            },
            Description='mock lambda function',
            Publish=True
        )

        # create mocked lambda

        # # Join the directory with the filename
        # # temp store current working directory
        # original_cwd=os.getcwd()
        # # change to abs directory
        # os.chdir(os.path.join(os.getcwd(),'external_data_scraper','unit_test','AU','tests','src'))

        # # prepare a testing lambda fucntion file as a zip 
        # zip_code=BytesIO()

        # with zipfile.ZipFile(zip_code,'w') as zf:
        #     zf.write('cash_rate_crawler_AU.py')
        
        # zip_code.seek(0)

        # # rechange to current working directory
        # os.chdir(original_cwd)

        # # mock lambda service with existing function file
        # self.lambda_client=boto3.client('lambda',region_name='us-west-1')

        # current_datetime = datetime.now()
        # formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")

        # self.lambda_client.create_function(
        #     FunctionName=self.lambda_name,
        #     Runtime='python3.9',
        #     Role=role_arn,
        #     Handler=self.lambda_name+'.lambda_handler',
        #     Code={
        #         'ZipFile':zip_code.read()
        #     },
        #     Description='mock lambda function',
        #     Publish=True,
        #     Environment={
        #         'Variables': {
        #             'AWS_LAMBDA_LOG_GROUP_NAME': self.log_group_name,
        #             'AWS_LAMBDA_LOG_STREAM_NAME':str(formatted_datetime)
        #         }
        #     }
        # )

        print('bbb')
        # connect event rule as a trigger for the lambda function
        self.lambda_client.add_permission(
            Action='lambda:InvokeFunction',
            StatementId='123412341234',
            Principal='events.amazonaws.com',
            FunctionName=self.lambda_name,
            # give event rule connection to lambda function
            SourceArn=self.event_client.describe_rule(
                Name=self.rule_name
            )['Arn']
        )
        print('ccc')

        # # print the lambda arn
        # response=lambda_client.get_function(FunctionName='cash_rate_crawler_AU')
        # arn=response['Configuration']['FunctionArn']
        # print(arn)


    def test_lambda_invoked(self):
        # time=datetime(2020, 4, 15, 10, 0)
        # print(time)
        # event_client=boto3.client('events',region_name='us-west-1')
        # response=event_client.list_rules()
        # print(response['Rules'])

        # print the lambda arn
        # lambda_client=boto3.client('lambda',region_name='us-west-1')
        # response=self.lambda_client.get_function(FunctionName=self.lambda_name)
        # lambda_arn=response['Configuration']['FunctionArn']

        response=self.event_client.put_targets(
            Rule=self.rule_name,
            EventBusName='default',
            # the resurces that are invoked when a rule is triggered
            Targets=[{
                'Id':'target',
                'Arn':self.lambda_client.get_function(FunctionName=self.lambda_name)['Configuration']['FunctionArn']
                # 'Arn':lambda_arn
            }]
        )
        # print(response)

        # event=event_client.describe_event_bus()
        original_cwd=os.getcwd()

        os.chdir(os.path.join(os.getcwd(),'external_data_scraper','unit_test','AU','tests','events'))

        with open('cash_rate_test_event.json','r') as file:
            event_data=json.load(file)
        
        os.chdir(original_cwd)

        # event=self.event_client.put_events(Entries=[event_data])

        # print(event)

        # response=self.event_client.enable_rule(Name=self.rule_name)
        # print(response)

        # response=self.lambda_client.invoke(
        #     FunctionName=self.lambda_name,
        #     InvocationType='RequestResponse',
        #     Payload=json.dumps(event_data)
        # )
        # print('-----')
        # print(response)
        # print('-----')

        # response=lambda_handler(event=event_data,context=None)
        # print(response)

        lambda_funcs=self.lambda_client.list_functions()
        print(lambda_funcs)

        # self.assertEqual(len(lambda_funcs['Functions']),1)

        # self.assertEqual(lambda_funcs['Functions'][0]['FunctionName'],self.lambda_name)
        

        # print('dddd')

        # self.assertTrue(True)








    # def load_event_from_file():
    #     '''
    #     load and validate test events from the file
    #     '''
    #     event_file_name="./events/cash_rate_test_event.json"
    #     with open(event_file_name,"r",encoding='UTF-8') as file_handle:
    #         event=json.load(file_handle)

        





    def test_log_written(self):
        '''
        test if the lambda write logs into log group
        '''
        pass



    # def test_s3_store(self):
    #     '''
    #     test if the the lambda can push files into s3 bucket
    #     '''
    #     s3_client=boto3.client('s3',region_name='us-west-1')

    #     response_s3 = s3_client.list_objects_v2(
    #         Bucket=self.bucket_name,
    #         Prefix=self.prefix
    #     )

    #     print(response_s3)

    #     # the s3 bucket is writtrn
    #     if response_s3['KeyCount']>1:
    #         self.assertTrue(True)
    #     # the s3 bucket is empty
    #     else:
    #         self.fail('lambda function can not push data into bucket')








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

        sockets=[x for x in tracemalloc.take_snapshot().statistics('filename')
                    if 'moto/core/models.py' in x.traceback.format()]
        
        for s in sockets:
            try:
                s.close()
            except:
                pass

        




if __name__ == "__main__":





    load_dotenv()

    # Get the directory of the current script
    # current_directory = os.path.dirname(os.path.abspath(__file__))
    # print(current_directory)
    # # Join the directory with the filename
    # file_path = os.path.join(current_directory, 'cash_rate_crawler_AU.py')

    # print(file_path)

    # original_cwd=os.getcwd()
    # os.chdir(os.path.join(os.getcwd(),'external_data_scraper','unit_test','AU','tests','events'))

    # file_path = "/Users/yiding/bitbucket/neoml/external_data_scraper/unit_test/AU/tests/events/cash_rate_test_event.json"
    # file_path="external_data_scraper/unit_test/AU/tests/events/cash_rate_test_event.json"
    # file_path='../events/cash_rate_test_event.json'

    # with open('cash_rate_test_event.json',"r",encoding='UTF-8') as file_handle:
    #     event=json.load(file_handle)
    # print(event)

    # zip_code=BytesIO()

    # with zipfile.ZipFile(zip_code,'w') as zf:
    #     zf.write(file_path)
    # print(os.environ.get('bucket_name'))
    # set_up()
    unittest.main()

    # 


    # tear_down()
