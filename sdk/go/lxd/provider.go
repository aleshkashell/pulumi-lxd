// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lxd

import (
	"context"
	"reflect"

	"github.com/aleshkashell/pulumi-lxd/sdk/go/lxd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The provider type for the lxd package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// Deprecated: Use `lxd_remote.address` instead.
	Address pulumi.StringPtrOutput `pulumi:"address"`
	// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
	ConfigDir pulumi.StringPtrOutput `pulumi:"configDir"`
	// Deprecated: Use `lxd_remote.port` instead.
	Port pulumi.StringPtrOutput `pulumi:"port"`
	// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
	Project pulumi.StringPtrOutput `pulumi:"project"`
	// How often to poll during state changes (default 10s)
	RefreshInterval pulumi.StringPtrOutput `pulumi:"refreshInterval"`
	// Deprecated: Use `lxd_remote.name` instead.
	Remote pulumi.StringPtrOutput `pulumi:"remote"`
	// Deprecated: Use `lxd_remote.password` instead.
	RemotePassword pulumi.StringPtrOutput `pulumi:"remotePassword"`
	// Deprecated: Use `lxd_remote.scheme` instead.
	Scheme pulumi.StringPtrOutput `pulumi:"scheme"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	if args.RemotePassword != nil {
		args.RemotePassword = pulumi.ToSecret(args.RemotePassword).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"remotePassword",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:lxd", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// Accept the server certificate
	AcceptRemoteCertificate *bool `pulumi:"acceptRemoteCertificate"`
	// Deprecated: Use `lxd_remote.address` instead.
	Address *string `pulumi:"address"`
	// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
	ConfigDir                  *string             `pulumi:"configDir"`
	GenerateClientCertificates *bool               `pulumi:"generateClientCertificates"`
	LxdRemotes                 []ProviderLxdRemote `pulumi:"lxdRemotes"`
	// Deprecated: Use `lxd_remote.port` instead.
	Port *string `pulumi:"port"`
	// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
	Project *string `pulumi:"project"`
	// How often to poll during state changes (default 10s)
	RefreshInterval *string `pulumi:"refreshInterval"`
	// Deprecated: Use `lxd_remote.name` instead.
	Remote *string `pulumi:"remote"`
	// Deprecated: Use `lxd_remote.password` instead.
	RemotePassword *string `pulumi:"remotePassword"`
	// Deprecated: Use `lxd_remote.scheme` instead.
	Scheme *string `pulumi:"scheme"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// Accept the server certificate
	AcceptRemoteCertificate pulumi.BoolPtrInput
	// Deprecated: Use `lxd_remote.address` instead.
	Address pulumi.StringPtrInput
	// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
	ConfigDir                  pulumi.StringPtrInput
	GenerateClientCertificates pulumi.BoolPtrInput
	LxdRemotes                 ProviderLxdRemoteArrayInput
	// Deprecated: Use `lxd_remote.port` instead.
	Port pulumi.StringPtrInput
	// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
	Project pulumi.StringPtrInput
	// How often to poll during state changes (default 10s)
	RefreshInterval pulumi.StringPtrInput
	// Deprecated: Use `lxd_remote.name` instead.
	Remote pulumi.StringPtrInput
	// Deprecated: Use `lxd_remote.password` instead.
	RemotePassword pulumi.StringPtrInput
	// Deprecated: Use `lxd_remote.scheme` instead.
	Scheme pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

func (i *Provider) ToOutput(ctx context.Context) pulumix.Output[*Provider] {
	return pulumix.Output[*Provider]{
		OutputState: i.ToProviderOutputWithContext(ctx).OutputState,
	}
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

func (o ProviderOutput) ToOutput(ctx context.Context) pulumix.Output[*Provider] {
	return pulumix.Output[*Provider]{
		OutputState: o.OutputState,
	}
}

// Deprecated: Use `lxd_remote.address` instead.
func (o ProviderOutput) Address() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Address }).(pulumi.StringPtrOutput)
}

// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
func (o ProviderOutput) ConfigDir() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ConfigDir }).(pulumi.StringPtrOutput)
}

// Deprecated: Use `lxd_remote.port` instead.
func (o ProviderOutput) Port() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Port }).(pulumi.StringPtrOutput)
}

// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
func (o ProviderOutput) Project() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Project }).(pulumi.StringPtrOutput)
}

// How often to poll during state changes (default 10s)
func (o ProviderOutput) RefreshInterval() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.RefreshInterval }).(pulumi.StringPtrOutput)
}

// Deprecated: Use `lxd_remote.name` instead.
func (o ProviderOutput) Remote() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Remote }).(pulumi.StringPtrOutput)
}

// Deprecated: Use `lxd_remote.password` instead.
func (o ProviderOutput) RemotePassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.RemotePassword }).(pulumi.StringPtrOutput)
}

// Deprecated: Use `lxd_remote.scheme` instead.
func (o ProviderOutput) Scheme() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Scheme }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
