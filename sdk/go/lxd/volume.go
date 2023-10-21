// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lxd

import (
	"context"
	"reflect"

	"errors"
	"github.com/aleshkashell/pulumi-lxd//sdk/go/lxd/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

type Volume struct {
	pulumi.CustomResourceState

	Config         pulumi.MapOutput       `pulumi:"config"`
	ContentType    pulumi.StringPtrOutput `pulumi:"contentType"`
	ExpandedConfig pulumi.MapOutput       `pulumi:"expandedConfig"`
	Location       pulumi.StringOutput    `pulumi:"location"`
	Name           pulumi.StringOutput    `pulumi:"name"`
	Pool           pulumi.StringOutput    `pulumi:"pool"`
	Project        pulumi.StringPtrOutput `pulumi:"project"`
	Remote         pulumi.StringPtrOutput `pulumi:"remote"`
	Target         pulumi.StringPtrOutput `pulumi:"target"`
	Type           pulumi.StringPtrOutput `pulumi:"type"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Pool == nil {
		return nil, errors.New("invalid value for required argument 'Pool'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Volume
	err := ctx.RegisterResource("lxd:index/volume:Volume", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeState, opts ...pulumi.ResourceOption) (*Volume, error) {
	var resource Volume
	err := ctx.ReadResource("lxd:index/volume:Volume", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Volume resources.
type volumeState struct {
	Config         map[string]interface{} `pulumi:"config"`
	ContentType    *string                `pulumi:"contentType"`
	ExpandedConfig map[string]interface{} `pulumi:"expandedConfig"`
	Location       *string                `pulumi:"location"`
	Name           *string                `pulumi:"name"`
	Pool           *string                `pulumi:"pool"`
	Project        *string                `pulumi:"project"`
	Remote         *string                `pulumi:"remote"`
	Target         *string                `pulumi:"target"`
	Type           *string                `pulumi:"type"`
}

type VolumeState struct {
	Config         pulumi.MapInput
	ContentType    pulumi.StringPtrInput
	ExpandedConfig pulumi.MapInput
	Location       pulumi.StringPtrInput
	Name           pulumi.StringPtrInput
	Pool           pulumi.StringPtrInput
	Project        pulumi.StringPtrInput
	Remote         pulumi.StringPtrInput
	Target         pulumi.StringPtrInput
	Type           pulumi.StringPtrInput
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	Config      map[string]interface{} `pulumi:"config"`
	ContentType *string                `pulumi:"contentType"`
	Name        *string                `pulumi:"name"`
	Pool        string                 `pulumi:"pool"`
	Project     *string                `pulumi:"project"`
	Remote      *string                `pulumi:"remote"`
	Target      *string                `pulumi:"target"`
	Type        *string                `pulumi:"type"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	Config      pulumi.MapInput
	ContentType pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	Pool        pulumi.StringInput
	Project     pulumi.StringPtrInput
	Remote      pulumi.StringPtrInput
	Target      pulumi.StringPtrInput
	Type        pulumi.StringPtrInput
}

func (VolumeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeArgs)(nil)).Elem()
}

type VolumeInput interface {
	pulumi.Input

	ToVolumeOutput() VolumeOutput
	ToVolumeOutputWithContext(ctx context.Context) VolumeOutput
}

func (*Volume) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (i *Volume) ToVolumeOutput() VolumeOutput {
	return i.ToVolumeOutputWithContext(context.Background())
}

func (i *Volume) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeOutput)
}

func (i *Volume) ToOutput(ctx context.Context) pulumix.Output[*Volume] {
	return pulumix.Output[*Volume]{
		OutputState: i.ToVolumeOutputWithContext(ctx).OutputState,
	}
}

// VolumeArrayInput is an input type that accepts VolumeArray and VolumeArrayOutput values.
// You can construct a concrete instance of `VolumeArrayInput` via:
//
//	VolumeArray{ VolumeArgs{...} }
type VolumeArrayInput interface {
	pulumi.Input

	ToVolumeArrayOutput() VolumeArrayOutput
	ToVolumeArrayOutputWithContext(context.Context) VolumeArrayOutput
}

type VolumeArray []VolumeInput

func (VolumeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Volume)(nil)).Elem()
}

func (i VolumeArray) ToVolumeArrayOutput() VolumeArrayOutput {
	return i.ToVolumeArrayOutputWithContext(context.Background())
}

func (i VolumeArray) ToVolumeArrayOutputWithContext(ctx context.Context) VolumeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeArrayOutput)
}

func (i VolumeArray) ToOutput(ctx context.Context) pulumix.Output[[]*Volume] {
	return pulumix.Output[[]*Volume]{
		OutputState: i.ToVolumeArrayOutputWithContext(ctx).OutputState,
	}
}

// VolumeMapInput is an input type that accepts VolumeMap and VolumeMapOutput values.
// You can construct a concrete instance of `VolumeMapInput` via:
//
//	VolumeMap{ "key": VolumeArgs{...} }
type VolumeMapInput interface {
	pulumi.Input

	ToVolumeMapOutput() VolumeMapOutput
	ToVolumeMapOutputWithContext(context.Context) VolumeMapOutput
}

type VolumeMap map[string]VolumeInput

func (VolumeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Volume)(nil)).Elem()
}

func (i VolumeMap) ToVolumeMapOutput() VolumeMapOutput {
	return i.ToVolumeMapOutputWithContext(context.Background())
}

func (i VolumeMap) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeMapOutput)
}

func (i VolumeMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Volume] {
	return pulumix.Output[map[string]*Volume]{
		OutputState: i.ToVolumeMapOutputWithContext(ctx).OutputState,
	}
}

type VolumeOutput struct{ *pulumi.OutputState }

func (VolumeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (o VolumeOutput) ToVolumeOutput() VolumeOutput {
	return o
}

func (o VolumeOutput) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return o
}

func (o VolumeOutput) ToOutput(ctx context.Context) pulumix.Output[*Volume] {
	return pulumix.Output[*Volume]{
		OutputState: o.OutputState,
	}
}

func (o VolumeOutput) Config() pulumi.MapOutput {
	return o.ApplyT(func(v *Volume) pulumi.MapOutput { return v.Config }).(pulumi.MapOutput)
}

func (o VolumeOutput) ContentType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.ContentType }).(pulumi.StringPtrOutput)
}

func (o VolumeOutput) ExpandedConfig() pulumi.MapOutput {
	return o.ApplyT(func(v *Volume) pulumi.MapOutput { return v.ExpandedConfig }).(pulumi.MapOutput)
}

func (o VolumeOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

func (o VolumeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o VolumeOutput) Pool() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Pool }).(pulumi.StringOutput)
}

func (o VolumeOutput) Project() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.Project }).(pulumi.StringPtrOutput)
}

func (o VolumeOutput) Remote() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.Remote }).(pulumi.StringPtrOutput)
}

func (o VolumeOutput) Target() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.Target }).(pulumi.StringPtrOutput)
}

func (o VolumeOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.Type }).(pulumi.StringPtrOutput)
}

type VolumeArrayOutput struct{ *pulumi.OutputState }

func (VolumeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Volume)(nil)).Elem()
}

func (o VolumeArrayOutput) ToVolumeArrayOutput() VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) ToVolumeArrayOutputWithContext(ctx context.Context) VolumeArrayOutput {
	return o
}

func (o VolumeArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Volume] {
	return pulumix.Output[[]*Volume]{
		OutputState: o.OutputState,
	}
}

func (o VolumeArrayOutput) Index(i pulumi.IntInput) VolumeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Volume {
		return vs[0].([]*Volume)[vs[1].(int)]
	}).(VolumeOutput)
}

type VolumeMapOutput struct{ *pulumi.OutputState }

func (VolumeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Volume)(nil)).Elem()
}

func (o VolumeMapOutput) ToVolumeMapOutput() VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) ToVolumeMapOutputWithContext(ctx context.Context) VolumeMapOutput {
	return o
}

func (o VolumeMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Volume] {
	return pulumix.Output[map[string]*Volume]{
		OutputState: o.OutputState,
	}
}

func (o VolumeMapOutput) MapIndex(k pulumi.StringInput) VolumeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Volume {
		return vs[0].(map[string]*Volume)[vs[1].(string)]
	}).(VolumeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeInput)(nil)).Elem(), &Volume{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeArrayInput)(nil)).Elem(), VolumeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeMapInput)(nil)).Elem(), VolumeMap{})
	pulumi.RegisterOutputType(VolumeOutput{})
	pulumi.RegisterOutputType(VolumeArrayOutput{})
	pulumi.RegisterOutputType(VolumeMapOutput{})
}
