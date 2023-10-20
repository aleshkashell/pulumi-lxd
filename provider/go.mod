module github.com/aleshkashell/pulumi-lxd/provider

go 1.20

replace github.com/hashicorp/terraform-plugin-sdk/v2 => github.com/pulumi/terraform-plugin-sdk/v2 v2.0.0-20230912190043-e6d96b3b8f7e

require (
	github.com/pulumi/pulumi-terraform-bridge/v3 v3.47.2
	github.com/pulumi/pulumi/sdk/v3 v3.67.1
)
