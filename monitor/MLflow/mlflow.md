# MLflow

Challenges of machine learning in production:

1. It is difficult to keep track of experiments.
2. It is difficult to reproduce code
3. There is no standard way to package and deploy models
4. There is no central store to manage models



What is MLflow:

1. Open-source ML lifecycle management tool.
2. single solution for all of the above challenges.
3. Library agnostic and language-agnostic.



## Four components:



### MLFlow tracking

The MLflow Tracking component is an API and UI for logging parameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results.






### MLFlow projects

Package data science code in a format to **reproduce** runs on any platform.

MLflow Projects are just **a convention for organizing and describing your code** to let other data scientists (or automated tools) run it.

Each project is simply a directory of files, or a Git repository containing code.



### MLFlow models

An MLflow Model is a standard format for packaging machine learning models that can be used in a variety of downstream tools.



### Model registry

The MLflow Model Registry component is a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. 

## Open MLFlow UI

open MLFlow UI:

```shell
mlflow ui
```



1. we must change the directory into the one we are working on.



If getting error on `mlflow ui` command like:

```she
[2022-04-19 10:48:02 -0400] [89933] [INFO] Starting gunicorn 20.1.0
[2022-04-19 10:48:02 -0400] [89933] [ERROR] Connection in use: ('127.0.0.1', 5000)
[2022-04-19 10:48:02 -0400] [89933] [ERROR] Retrying in 1 second.
[2022-04-19 10:48:03 -0400] [89933] [ERROR] Connection in use: ('127.0.0.1', 5000)
[2022-04-19 10:48:03 -0400] [89933] [ERROR] Retrying in 1 second.
[2022-04-19 10:48:04 -0400] [89933] [ERROR] Connection in use: ('127.0.0.1', 5000)
[2022-04-19 10:48:04 -0400] [89933] [ERROR] Retrying in 1 second.
[2022-04-19 10:48:05 -0400] [89933] [ERROR] Connection in use: ('127.0.0.1', 5000)
[2022-04-19 10:48:05 -0400] [89933] [ERROR] Retrying in 1 second.
[2022-04-19 10:48:06 -0400] [89933] [ERROR] Connection in use: ('127.0.0.1', 5000)
[2022-04-19 10:48:06 -0400] [89933] [ERROR] Retrying in 1 second.
[2022-04-19 10:48:07 -0400] [89933] [ERROR] Can't connect to ('127.0.0.1', 5000)
```

Step 1: Get the process id:

```shell
ps -A | grep gunicorn
```

```shell
20734 ?? 0:39.17 /usr/local/Cellar/python@3.9/3.9.10/Frameworks/Python.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python /Users/XXX/env/bin/gunicorn -b 127.0.0.1:5000 -w 1 mlflow.server:app
```

Take the **PID** from last output and kill the process with that PID that is using the port

```shell
kill 20734
```









## Reference

[MLflow 的搭建使用](https://blog.csdn.net/monkeyboy_tech/article/details/109381668)

[MLflow model registry](https://blog.csdn.net/monkeyboy_tech/article/details/109674668)

[MLOps with MLFlow and Amazon SageMaker Pipelines](https://towardsdatascience.com/mlops-with-mlflow-and-amazon-sagemaker-pipelines-33e13d43f238)