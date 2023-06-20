# Terraform: Data Block

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



## 