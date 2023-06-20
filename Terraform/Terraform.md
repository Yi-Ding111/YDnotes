# Terraform

### run Teraform project
	terraform init
	
	terraform plan
		terraform plan -out config.terraform
	
	terraform apply (--auto-approve)
		* give variable name with apply command
		e.g. terraform apply -var "s3_given_name=test-yiding"
		e.g. terraform apply -var-file aws_dev.tfvars


​	
​	
### destory remote objects 
	terraform apply -destory
		alias-- terraform destory (destory all objects)
	
	terraform plan -destory

### state
	terraform state list
	
	terraform state show (one from list)


### print terraform output information
	terraform output

### target resource
	terrafrom destory -target (...)
	
	terraform apply -target (...)





## for_each

`for_each`: <https://www.terraform.io/language/meta-arguments/for_each>

Example:

```terraform
variable "test" {
  type = map(object({
    bucket     = string
    object_key = string
  }))
  
  default = {
    sample_name = {
      bucket     = "your-s3-bucket-name"
      object_key = ""
    }
    // ... other Lambda configurations
  }
}
```

Define a variable `test` , 





## BLOCK: data

*Data sources* allow Terraform to use information defined outside of Terraform, defined by another separate Terraform configuration, or modified by functions.

`data`块用于从外部源（例如云提供商或其他API）获取数据并将其用于配置。它允许您在配置期间检索和使用静态数据，这些数据对于正确设置资源非常重要。

https://developer.hashicorp.com/terraform/language/data-sources



`data` block creates a data instance of the given ***type*** (first block label) and ***name*** (second block label). The combination of the type and name must be **unique**.

```terraform
data "provider_type" "local_name"{
  # configurations
  }
```

1. `provider_type`: a given data source. 

是指定数据源的提供程序类型。例如，如果您要从AWS获取数据，则可以使用`aws`作为提供程序类型。

e.g. the aws privider type is listed: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ami?product_intent=terraform

2. `local_name`: The name is used to refer to this resource from elsewhere in the ***<u>same</u>*** Terraform module, but has no significance outside of the scope of a module.

是数据块的名称，用于在Terraform配置中引用数据。

3. `configurations`: query constraints defined by the data source. 

可以使用提供程序的特定配置选项来指定要检索的数据。这些选项根据提供程序类型的不同而有所不同。例如，在AWS提供程序中，您可以指定`region`、`access_key`、`secret_key`等选项。





## AWS



### Use s3 as a trigger for lambda????

TF: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_notification#add-notification-configuration-to-lambda-function

AWS: https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html







### Use resource in S3 bucket ????

aws_s3_object: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_object















### upload files into s3
ref these terraform functions

`fileset`: <https://www.terraform.io/language/functions/fileset>

`for_each`: <https://www.terraform.io/language/meta-arguments/for_each>


tree
	
	print terraform files in tree structure
	 
	 terraform graph

fmt

	format terraform files
	
		terraform fmt


### AWS IAM user with MFA using through terraform 

1. Because dev aws account is 2fa, including password and MFA. It is complex using terraform command directly. 

2. Instead using aws-vault to manage account passwords. 

[aws-valut](https://github.com/99designs/aws-vault)


    aws-vault add neo --> neo is aws credentials in .aws/
    
    aws-vault exec neoyi -- terraform init
    
    aws-vault exec neoyi -- terraform plan
    
    aws-vault exec neoyi -- terraform apply
    
    aws-vault exec neoyi -- terraform destroy





## What is terraform provider

Terraform relies on plugins called providers to interact with cloud providers, SaaS providers, and other APIs.

Terraform configurations must declare which providers they require so that Terraform can install and use them. Additionally, some providers require configuration (like endpoint URLs or cloud regions) before they can be used.



Provider是一种插件系统，用于与各种基础设施和服务进行交互。它允许Terraform与云提供商、虚拟化平台、网络设备等各种资源进行集成。

每个Provider都用于管理一组资源，例如Amazon Web Services (AWS)、Microsoft Azure、Google Cloud Platform (GCP)等。Terraform通过Provider与这些服务进行通信，创建、更新或删除资源。

Provider为Terraform提供了资源的定义和操作方法，它知道如何与具体的服务进行交互，以便将资源配置为所需的状态。例如，AWS Provider知道如何与AWS API进行通信，以创建和管理云资源，而Azure Provider知道如何与Azure API进行交互。





## Different blocks: data & resource ????

```terraform
data "aws_s3_object" "test" {}
```

```terraform
resourece "aws_s3_object" "test" {}
```

`resource`: is known as a ***managed resource***. Cause Terraform to create, update, and delete infrastructure objects.

`data`: Cause Terraform only to *read* objects.







1. Purpose: 

​	The `data` block is used to retrieve information or perform lookups on **existing** resources. It allows you 	to fetch metadata or attributes of the resource without creating or modifying it. 

​	The `resource` block is used to manage and create **new** resources within your infrastructure.

