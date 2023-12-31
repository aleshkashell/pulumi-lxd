// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lxd

import (
	"context"
	"reflect"

	"errors"
	"github.com/aleshkashell/pulumi-lxd/sdk/go/lxd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type Container struct {
	pulumi.CustomResourceState

	Config      pulumi.MapOutput             `pulumi:"config"`
	Devices     ContainerDeviceArrayOutput   `pulumi:"devices"`
	Ephemeral   pulumi.BoolPtrOutput         `pulumi:"ephemeral"`
	Files       ContainerFileTypeArrayOutput `pulumi:"files"`
	Image       pulumi.StringOutput          `pulumi:"image"`
	IpAddress   pulumi.StringOutput          `pulumi:"ipAddress"`
	Ipv4Address pulumi.StringOutput          `pulumi:"ipv4Address"`
	Ipv6Address pulumi.StringOutput          `pulumi:"ipv6Address"`
	Limits      pulumi.MapOutput             `pulumi:"limits"`
	MacAddress  pulumi.StringOutput          `pulumi:"macAddress"`
	Name        pulumi.StringOutput          `pulumi:"name"`
	// Deprecated: Use a config setting of security.privileged=1 instead
	Privileged     pulumi.BoolPtrOutput     `pulumi:"privileged"`
	Profiles       pulumi.StringArrayOutput `pulumi:"profiles"`
	Project        pulumi.StringPtrOutput   `pulumi:"project"`
	Remote         pulumi.StringPtrOutput   `pulumi:"remote"`
	StartContainer pulumi.BoolPtrOutput     `pulumi:"startContainer"`
	Status         pulumi.StringOutput      `pulumi:"status"`
	Target         pulumi.StringOutput      `pulumi:"target"`
	Type           pulumi.StringOutput      `pulumi:"type"`
	WaitForNetwork pulumi.BoolPtrOutput     `pulumi:"waitForNetwork"`
}

// NewContainer registers a new resource with the given unique name, arguments, and options.
func NewContainer(ctx *pulumi.Context,
	name string, args *ContainerArgs, opts ...pulumi.ResourceOption) (*Container, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Image == nil {
		return nil, errors.New("invalid value for required argument 'Image'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Container
	err := ctx.RegisterResource("lxd:index/container:Container", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContainer gets an existing Container resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContainer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContainerState, opts ...pulumi.ResourceOption) (*Container, error) {
	var resource Container
	err := ctx.ReadResource("lxd:index/container:Container", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Container resources.
type containerState struct {
	Config      map[string]interface{} `pulumi:"config"`
	Devices     []ContainerDevice      `pulumi:"devices"`
	Ephemeral   *bool                  `pulumi:"ephemeral"`
	Files       []ContainerFileType    `pulumi:"files"`
	Image       *string                `pulumi:"image"`
	IpAddress   *string                `pulumi:"ipAddress"`
	Ipv4Address *string                `pulumi:"ipv4Address"`
	Ipv6Address *string                `pulumi:"ipv6Address"`
	Limits      map[string]interface{} `pulumi:"limits"`
	MacAddress  *string                `pulumi:"macAddress"`
	Name        *string                `pulumi:"name"`
	// Deprecated: Use a config setting of security.privileged=1 instead
	Privileged     *bool    `pulumi:"privileged"`
	Profiles       []string `pulumi:"profiles"`
	Project        *string  `pulumi:"project"`
	Remote         *string  `pulumi:"remote"`
	StartContainer *bool    `pulumi:"startContainer"`
	Status         *string  `pulumi:"status"`
	Target         *string  `pulumi:"target"`
	Type           *string  `pulumi:"type"`
	WaitForNetwork *bool    `pulumi:"waitForNetwork"`
}

type ContainerState struct {
	Config      pulumi.MapInput
	Devices     ContainerDeviceArrayInput
	Ephemeral   pulumi.BoolPtrInput
	Files       ContainerFileTypeArrayInput
	Image       pulumi.StringPtrInput
	IpAddress   pulumi.StringPtrInput
	Ipv4Address pulumi.StringPtrInput
	Ipv6Address pulumi.StringPtrInput
	Limits      pulumi.MapInput
	MacAddress  pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	// Deprecated: Use a config setting of security.privileged=1 instead
	Privileged     pulumi.BoolPtrInput
	Profiles       pulumi.StringArrayInput
	Project        pulumi.StringPtrInput
	Remote         pulumi.StringPtrInput
	StartContainer pulumi.BoolPtrInput
	Status         pulumi.StringPtrInput
	Target         pulumi.StringPtrInput
	Type           pulumi.StringPtrInput
	WaitForNetwork pulumi.BoolPtrInput
}

func (ContainerState) ElementType() reflect.Type {
	return reflect.TypeOf((*containerState)(nil)).Elem()
}

type containerArgs struct {
	Config    map[string]interface{} `pulumi:"config"`
	Devices   []ContainerDevice      `pulumi:"devices"`
	Ephemeral *bool                  `pulumi:"ephemeral"`
	Files     []ContainerFileType    `pulumi:"files"`
	Image     string                 `pulumi:"image"`
	Limits    map[string]interface{} `pulumi:"limits"`
	Name      *string                `pulumi:"name"`
	// Deprecated: Use a config setting of security.privileged=1 instead
	Privileged     *bool    `pulumi:"privileged"`
	Profiles       []string `pulumi:"profiles"`
	Project        *string  `pulumi:"project"`
	Remote         *string  `pulumi:"remote"`
	StartContainer *bool    `pulumi:"startContainer"`
	Target         *string  `pulumi:"target"`
	Type           *string  `pulumi:"type"`
	WaitForNetwork *bool    `pulumi:"waitForNetwork"`
}

// The set of arguments for constructing a Container resource.
type ContainerArgs struct {
	Config    pulumi.MapInput
	Devices   ContainerDeviceArrayInput
	Ephemeral pulumi.BoolPtrInput
	Files     ContainerFileTypeArrayInput
	Image     pulumi.StringInput
	Limits    pulumi.MapInput
	Name      pulumi.StringPtrInput
	// Deprecated: Use a config setting of security.privileged=1 instead
	Privileged     pulumi.BoolPtrInput
	Profiles       pulumi.StringArrayInput
	Project        pulumi.StringPtrInput
	Remote         pulumi.StringPtrInput
	StartContainer pulumi.BoolPtrInput
	Target         pulumi.StringPtrInput
	Type           pulumi.StringPtrInput
	WaitForNetwork pulumi.BoolPtrInput
}

func (ContainerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*containerArgs)(nil)).Elem()
}

type ContainerInput interface {
	pulumi.Input

	ToContainerOutput() ContainerOutput
	ToContainerOutputWithContext(ctx context.Context) ContainerOutput
}

func (*Container) ElementType() reflect.Type {
	return reflect.TypeOf((**Container)(nil)).Elem()
}

func (i *Container) ToContainerOutput() ContainerOutput {
	return i.ToContainerOutputWithContext(context.Background())
}

func (i *Container) ToContainerOutputWithContext(ctx context.Context) ContainerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerOutput)
}

func (i *Container) ToOutput(ctx context.Context) pulumix.Output[*Container] {
	return pulumix.Output[*Container]{
		OutputState: i.ToContainerOutputWithContext(ctx).OutputState,
	}
}

// ContainerArrayInput is an input type that accepts ContainerArray and ContainerArrayOutput values.
// You can construct a concrete instance of `ContainerArrayInput` via:
//
//	ContainerArray{ ContainerArgs{...} }
type ContainerArrayInput interface {
	pulumi.Input

	ToContainerArrayOutput() ContainerArrayOutput
	ToContainerArrayOutputWithContext(context.Context) ContainerArrayOutput
}

type ContainerArray []ContainerInput

func (ContainerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Container)(nil)).Elem()
}

func (i ContainerArray) ToContainerArrayOutput() ContainerArrayOutput {
	return i.ToContainerArrayOutputWithContext(context.Background())
}

func (i ContainerArray) ToContainerArrayOutputWithContext(ctx context.Context) ContainerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerArrayOutput)
}

func (i ContainerArray) ToOutput(ctx context.Context) pulumix.Output[[]*Container] {
	return pulumix.Output[[]*Container]{
		OutputState: i.ToContainerArrayOutputWithContext(ctx).OutputState,
	}
}

// ContainerMapInput is an input type that accepts ContainerMap and ContainerMapOutput values.
// You can construct a concrete instance of `ContainerMapInput` via:
//
//	ContainerMap{ "key": ContainerArgs{...} }
type ContainerMapInput interface {
	pulumi.Input

	ToContainerMapOutput() ContainerMapOutput
	ToContainerMapOutputWithContext(context.Context) ContainerMapOutput
}

type ContainerMap map[string]ContainerInput

func (ContainerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Container)(nil)).Elem()
}

func (i ContainerMap) ToContainerMapOutput() ContainerMapOutput {
	return i.ToContainerMapOutputWithContext(context.Background())
}

func (i ContainerMap) ToContainerMapOutputWithContext(ctx context.Context) ContainerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerMapOutput)
}

func (i ContainerMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Container] {
	return pulumix.Output[map[string]*Container]{
		OutputState: i.ToContainerMapOutputWithContext(ctx).OutputState,
	}
}

type ContainerOutput struct{ *pulumi.OutputState }

func (ContainerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Container)(nil)).Elem()
}

func (o ContainerOutput) ToContainerOutput() ContainerOutput {
	return o
}

func (o ContainerOutput) ToContainerOutputWithContext(ctx context.Context) ContainerOutput {
	return o
}

func (o ContainerOutput) ToOutput(ctx context.Context) pulumix.Output[*Container] {
	return pulumix.Output[*Container]{
		OutputState: o.OutputState,
	}
}

func (o ContainerOutput) Config() pulumi.MapOutput {
	return o.ApplyT(func(v *Container) pulumi.MapOutput { return v.Config }).(pulumi.MapOutput)
}

func (o ContainerOutput) Devices() ContainerDeviceArrayOutput {
	return o.ApplyT(func(v *Container) ContainerDeviceArrayOutput { return v.Devices }).(ContainerDeviceArrayOutput)
}

func (o ContainerOutput) Ephemeral() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.BoolPtrOutput { return v.Ephemeral }).(pulumi.BoolPtrOutput)
}

func (o ContainerOutput) Files() ContainerFileTypeArrayOutput {
	return o.ApplyT(func(v *Container) ContainerFileTypeArrayOutput { return v.Files }).(ContainerFileTypeArrayOutput)
}

func (o ContainerOutput) Image() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Image }).(pulumi.StringOutput)
}

func (o ContainerOutput) IpAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.IpAddress }).(pulumi.StringOutput)
}

func (o ContainerOutput) Ipv4Address() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Ipv4Address }).(pulumi.StringOutput)
}

func (o ContainerOutput) Ipv6Address() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Ipv6Address }).(pulumi.StringOutput)
}

func (o ContainerOutput) Limits() pulumi.MapOutput {
	return o.ApplyT(func(v *Container) pulumi.MapOutput { return v.Limits }).(pulumi.MapOutput)
}

func (o ContainerOutput) MacAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.MacAddress }).(pulumi.StringOutput)
}

func (o ContainerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Deprecated: Use a config setting of security.privileged=1 instead
func (o ContainerOutput) Privileged() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.BoolPtrOutput { return v.Privileged }).(pulumi.BoolPtrOutput)
}

func (o ContainerOutput) Profiles() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Container) pulumi.StringArrayOutput { return v.Profiles }).(pulumi.StringArrayOutput)
}

func (o ContainerOutput) Project() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.StringPtrOutput { return v.Project }).(pulumi.StringPtrOutput)
}

func (o ContainerOutput) Remote() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.StringPtrOutput { return v.Remote }).(pulumi.StringPtrOutput)
}

func (o ContainerOutput) StartContainer() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.BoolPtrOutput { return v.StartContainer }).(pulumi.BoolPtrOutput)
}

func (o ContainerOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

func (o ContainerOutput) Target() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Target }).(pulumi.StringOutput)
}

func (o ContainerOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *Container) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

func (o ContainerOutput) WaitForNetwork() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Container) pulumi.BoolPtrOutput { return v.WaitForNetwork }).(pulumi.BoolPtrOutput)
}

type ContainerArrayOutput struct{ *pulumi.OutputState }

func (ContainerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Container)(nil)).Elem()
}

func (o ContainerArrayOutput) ToContainerArrayOutput() ContainerArrayOutput {
	return o
}

func (o ContainerArrayOutput) ToContainerArrayOutputWithContext(ctx context.Context) ContainerArrayOutput {
	return o
}

func (o ContainerArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Container] {
	return pulumix.Output[[]*Container]{
		OutputState: o.OutputState,
	}
}

func (o ContainerArrayOutput) Index(i pulumi.IntInput) ContainerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Container {
		return vs[0].([]*Container)[vs[1].(int)]
	}).(ContainerOutput)
}

type ContainerMapOutput struct{ *pulumi.OutputState }

func (ContainerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Container)(nil)).Elem()
}

func (o ContainerMapOutput) ToContainerMapOutput() ContainerMapOutput {
	return o
}

func (o ContainerMapOutput) ToContainerMapOutputWithContext(ctx context.Context) ContainerMapOutput {
	return o
}

func (o ContainerMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Container] {
	return pulumix.Output[map[string]*Container]{
		OutputState: o.OutputState,
	}
}

func (o ContainerMapOutput) MapIndex(k pulumi.StringInput) ContainerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Container {
		return vs[0].(map[string]*Container)[vs[1].(string)]
	}).(ContainerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerInput)(nil)).Elem(), &Container{})
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerArrayInput)(nil)).Elem(), ContainerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ContainerMapInput)(nil)).Elem(), ContainerMap{})
	pulumi.RegisterOutputType(ContainerOutput{})
	pulumi.RegisterOutputType(ContainerArrayOutput{})
	pulumi.RegisterOutputType(ContainerMapOutput{})
}
