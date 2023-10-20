module github.com/aleshkashell/pulumi-lxd/provider

go 1.18

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20220824175045-450992f2f5b9

require (
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.47.2
	github.com/pulumi/pulumi/sdk/v3 v3.67.1
)
