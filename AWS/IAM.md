# IAM



## Policy in json

Policy为实体(如用户、角色)赋予权限,控制其可以访问的资源和 API 操作。

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowReadWriteS3Bucket",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::YD/wingwing/*"
        },
        {
            "Sid": "AllowWriteCloudwatchLogs",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

Here above is one example of Policy in json. Each `Statement` in the policy includes some keys:

* `Sid`: the Statement's id, it could be any string.

* `Effect`: the Statement to allow or deny permissions. Can be `Allow` or `Deny`.

* `Action`: The action to allow or deny, such as "s3:GetObject".

  https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html

* `Resource`: The resource to allow or deny the operation. 

  1. ```json
     "Resource": "arn:aws:s3:::my-bucket/*"
     ```

​		This means allow|deny operations on all objects in the /my-bucket.

2. ```json
   "Resource": "arn:aws:sqs:us-east-1:*:*" 
   ```

   This means allow|deny operations on all SQS queues of the current account in the us-east-1 region.

3. ```json
   "Resource": "*" 
   ```

   This means allow the operation on <u>all resources</u>. **It is not recommended in practice.**

4. ```json
   "Resource": "arn:aws:s3:::my-bucket/YD/"
   ```

​		This will only allow operations on the `YD/` folder itself in the `nu_bucket/`, excluding any objects or subfolders within it.

5. ```json
   "Resource": "arn:aws:s3:::my-bucket/YD/*"
   ```

   This will allow operations on all objects (including subfolders and files) under the `YD/` folder in the `my-bucket/`.

6. 如果需要对文件夹下所有TXT文件有读权限

   ```json
   "Resource": "arn:aws:s3:::my-bucket/YD/*.txt"
   ```



## Trust relationship

Trust Policy定义允许哪些实体代入一个角色,用于控制角色的使用范围。

1. ```json
   {
     "Version": "2012-10-17",
     "Statement": {
       "Effect": "Allow",
       "Principal": {"Service": "lambda.amazonaws.com"},
       "Action": "sts:AssumeRole"
     }
   }
   ```

   This means that the <u>lambda service</u> is allowed to assume this role.

2. ```json
   {
     "Version": "2012-10-17",
     "Statement": {
       "Effect": "Allow",
       "Principal": {"AWS": "arn:aws:iam::111122223333:root"}, 
       "Action": "sts:AssumeRole" 
     }
   }
   ```

   Then only entities with that principal are allowed to assume the role.

## Role

Roles are used to grant specific privileges to specific actors. 

A role needs two things: 

* **permission policies** (what resources can be accessed and what actions can be taken)
* **trust relationships** (what entities can assume the role).

### S3

#### read only access to all buckets

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid":"AllowReadS3Bucket",
      "Effect": "Allow",
      "Action": "s3:GetObject"
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

Or access permission into all buckets

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid":"AllowReadS3Bucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "*"
    }
  ]
}
```



#### write objects from s3 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid":"AllowWriteS3Bucket",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```



#### list S3 objects

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid":"AllowListS3Bucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::bucket-name-1/*",
        "arn:aws:s3:::bucket-name-2/*"
      ]
    }
  ]
}
```



### Cloudwatch log group

#### write logs

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid":"AllowWriteCloudwatchLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutlogEvents"
      ],
      "Resource": [
        "arn:aws:logs:us-west-1:1111222233334444:log-group:aws/lambda/lambda_name1:*",
        "arn:aws:logs:us-west-1:1111222233334444:log-group:aws/lambda/lambda_name2:*"
      ]
    }
  ]
}
```

