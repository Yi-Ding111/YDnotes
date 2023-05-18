# Lambda



## def lambda_handler(event,context):

1. The method in the AWS Lambda function code processes events.
2. When the handler exits or returns a response, it becomes available to process another event.





## Lambda Unit Testing

https://aws.amazon.com/cn/blogs/devops/unit-testing-aws-lambda-with-python-and-mock-aws-services/?nc1=h_ls (AWS Blog Reference)

We will mock the service integrations to s3 isolate and focus our test on the lambda function code, and not on the behaviour of AWS services.

1. **Define the AWS Service resources in the Lambda Function**







2. **Define global environment variables if lambda needs**

```python
import os

lambda_environ={
    'bucket_name':os.environ.get('bucket_name','wingwing'),
    'prefix':os.environ.get('prefix','Ding/YD/')
}
```







### moto Library

[A library that allows you to easily mock out tests based on AWS infrasturctures.](https://docs.getmoto.org/en/latest/)











## .zip file deployment (code with dependencies)

https://docs.aws.amazon.com/zh_cn/lambda/latest/dg/python-package.html (AWS official document)

https://www.youtube.com/watch?v=Jtlxf_kn5zY&t=629s (Youtube Video)

```sh
mkdir code-with-dependency

cd code-with-dependency

touch lambda_function.py

zip my-deployment.zip lambda_function.py

mkdir dependencies

pip3 install --target=dependencies requests

cd ..

rm my-deployment.zip

cd dependencies

## zip -r <zip_file> <file> <file> ...
zip -r ../my-deployment.zip .

cd ..

zip my-deployment.zip lambda_function.py
```



```sh
cd <current_folder_path>

mkdir cash-rate-deployment-package

cd cash-rate-deployment-package

## copy the python file into current path
cp ../src/cash_rate_crawler_AU.py .

## rename the current file to lambda_function.py
mv ./cash_rate_crawler_AU.py ./lambda_function.py

mkdir python

## pip3 install -r ../src/requirements.txt --target=./dependencies
pip3 install -r ../src/requirements.txt -t ./python

cd python

zip -r ../python.zip .

cd ..

zip python.zip lambda_function.py
```



 use virtual environment

```sh
cd <current_folder_path>

mkdir cash-rate-deployment-package

cd cash-rate-deployment-package

virtualenv myvenv

source myvenv/bin/activate

pip3 install -r ../src/requirements.txt

cd myvenv/lib/python3.8/site-packages/

zip -r ../../../../cash-rates-deployment.zip .

cd ../../../../

zip cash-rates-deployment.zip lambda_function.py

## deactive the venv
deactivate

## delete the venv
rm -rf myvenv
```









