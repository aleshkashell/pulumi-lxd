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

type CachedImage struct {
	pulumi.CustomResourceState

	Aliases       pulumi.StringArrayOutput `pulumi:"aliases"`
	Architecture  pulumi.StringOutput      `pulumi:"architecture"`
	CopiedAliases pulumi.StringArrayOutput `pulumi:"copiedAliases"`
	CopyAliases   pulumi.BoolPtrOutput     `pulumi:"copyAliases"`
	CreatedAt     pulumi.IntOutput         `pulumi:"createdAt"`
	Fingerprint   pulumi.StringOutput      `pulumi:"fingerprint"`
	Project       pulumi.StringPtrOutput   `pulumi:"project"`
	Remote        pulumi.StringPtrOutput   `pulumi:"remote"`
	SourceImage   pulumi.StringOutput      `pulumi:"sourceImage"`
	SourceRemote  pulumi.StringOutput      `pulumi:"sourceRemote"`
	Type          pulumi.StringPtrOutput   `pulumi:"type"`
}

// NewCachedImage registers a new resource with the given unique name, arguments, and options.
func NewCachedImage(ctx *pulumi.Context,
	name string, args *CachedImageArgs, opts ...pulumi.ResourceOption) (*CachedImage, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SourceImage == nil {
		return nil, errors.New("invalid value for required argument 'SourceImage'")
	}
	if args.SourceRemote == nil {
		return nil, errors.New("invalid value for required argument 'SourceRemote'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CachedImage
	err := ctx.RegisterResource("lxd:index/cachedImage:CachedImage", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCachedImage gets an existing CachedImage resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCachedImage(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CachedImageState, opts ...pulumi.ResourceOption) (*CachedImage, error) {
	var resource CachedImage
	err := ctx.ReadResource("lxd:index/cachedImage:CachedImage", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CachedImage resources.
type cachedImageState struct {
	Aliases       []string `pulumi:"aliases"`
	Architecture  *string  `pulumi:"architecture"`
	CopiedAliases []string `pulumi:"copiedAliases"`
	CopyAliases   *bool    `pulumi:"copyAliases"`
	CreatedAt     *int     `pulumi:"createdAt"`
	Fingerprint   *string  `pulumi:"fingerprint"`
	Project       *string  `pulumi:"project"`
	Remote        *string  `pulumi:"remote"`
	SourceImage   *string  `pulumi:"sourceImage"`
	SourceRemote  *string  `pulumi:"sourceRemote"`
	Type          *string  `pulumi:"type"`
}

type CachedImageState struct {
	Aliases       pulumi.StringArrayInput
	Architecture  pulumi.StringPtrInput
	CopiedAliases pulumi.StringArrayInput
	CopyAliases   pulumi.BoolPtrInput
	CreatedAt     pulumi.IntPtrInput
	Fingerprint   pulumi.StringPtrInput
	Project       pulumi.StringPtrInput
	Remote        pulumi.StringPtrInput
	SourceImage   pulumi.StringPtrInput
	SourceRemote  pulumi.StringPtrInput
	Type          pulumi.StringPtrInput
}

func (CachedImageState) ElementType() reflect.Type {
	return reflect.TypeOf((*cachedImageState)(nil)).Elem()
}

type cachedImageArgs struct {
	Aliases      []string `pulumi:"aliases"`
	CopyAliases  *bool    `pulumi:"copyAliases"`
	Project      *string  `pulumi:"project"`
	Remote       *string  `pulumi:"remote"`
	SourceImage  string   `pulumi:"sourceImage"`
	SourceRemote string   `pulumi:"sourceRemote"`
	Type         *string  `pulumi:"type"`
}

// The set of arguments for constructing a CachedImage resource.
type CachedImageArgs struct {
	Aliases      pulumi.StringArrayInput
	CopyAliases  pulumi.BoolPtrInput
	Project      pulumi.StringPtrInput
	Remote       pulumi.StringPtrInput
	SourceImage  pulumi.StringInput
	SourceRemote pulumi.StringInput
	Type         pulumi.StringPtrInput
}

func (CachedImageArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cachedImageArgs)(nil)).Elem()
}

type CachedImageInput interface {
	pulumi.Input

	ToCachedImageOutput() CachedImageOutput
	ToCachedImageOutputWithContext(ctx context.Context) CachedImageOutput
}

func (*CachedImage) ElementType() reflect.Type {
	return reflect.TypeOf((**CachedImage)(nil)).Elem()
}

func (i *CachedImage) ToCachedImageOutput() CachedImageOutput {
	return i.ToCachedImageOutputWithContext(context.Background())
}

func (i *CachedImage) ToCachedImageOutputWithContext(ctx context.Context) CachedImageOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CachedImageOutput)
}

func (i *CachedImage) ToOutput(ctx context.Context) pulumix.Output[*CachedImage] {
	return pulumix.Output[*CachedImage]{
		OutputState: i.ToCachedImageOutputWithContext(ctx).OutputState,
	}
}

// CachedImageArrayInput is an input type that accepts CachedImageArray and CachedImageArrayOutput values.
// You can construct a concrete instance of `CachedImageArrayInput` via:
//
//	CachedImageArray{ CachedImageArgs{...} }
type CachedImageArrayInput interface {
	pulumi.Input

	ToCachedImageArrayOutput() CachedImageArrayOutput
	ToCachedImageArrayOutputWithContext(context.Context) CachedImageArrayOutput
}

type CachedImageArray []CachedImageInput

func (CachedImageArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CachedImage)(nil)).Elem()
}

func (i CachedImageArray) ToCachedImageArrayOutput() CachedImageArrayOutput {
	return i.ToCachedImageArrayOutputWithContext(context.Background())
}

func (i CachedImageArray) ToCachedImageArrayOutputWithContext(ctx context.Context) CachedImageArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CachedImageArrayOutput)
}

func (i CachedImageArray) ToOutput(ctx context.Context) pulumix.Output[[]*CachedImage] {
	return pulumix.Output[[]*CachedImage]{
		OutputState: i.ToCachedImageArrayOutputWithContext(ctx).OutputState,
	}
}

// CachedImageMapInput is an input type that accepts CachedImageMap and CachedImageMapOutput values.
// You can construct a concrete instance of `CachedImageMapInput` via:
//
//	CachedImageMap{ "key": CachedImageArgs{...} }
type CachedImageMapInput interface {
	pulumi.Input

	ToCachedImageMapOutput() CachedImageMapOutput
	ToCachedImageMapOutputWithContext(context.Context) CachedImageMapOutput
}

type CachedImageMap map[string]CachedImageInput

func (CachedImageMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CachedImage)(nil)).Elem()
}

func (i CachedImageMap) ToCachedImageMapOutput() CachedImageMapOutput {
	return i.ToCachedImageMapOutputWithContext(context.Background())
}

func (i CachedImageMap) ToCachedImageMapOutputWithContext(ctx context.Context) CachedImageMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CachedImageMapOutput)
}

func (i CachedImageMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*CachedImage] {
	return pulumix.Output[map[string]*CachedImage]{
		OutputState: i.ToCachedImageMapOutputWithContext(ctx).OutputState,
	}
}

type CachedImageOutput struct{ *pulumi.OutputState }

func (CachedImageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CachedImage)(nil)).Elem()
}

func (o CachedImageOutput) ToCachedImageOutput() CachedImageOutput {
	return o
}

func (o CachedImageOutput) ToCachedImageOutputWithContext(ctx context.Context) CachedImageOutput {
	return o
}

func (o CachedImageOutput) ToOutput(ctx context.Context) pulumix.Output[*CachedImage] {
	return pulumix.Output[*CachedImage]{
		OutputState: o.OutputState,
	}
}

func (o CachedImageOutput) Aliases() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringArrayOutput { return v.Aliases }).(pulumi.StringArrayOutput)
}

func (o CachedImageOutput) Architecture() pulumi.StringOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringOutput { return v.Architecture }).(pulumi.StringOutput)
}

func (o CachedImageOutput) CopiedAliases() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringArrayOutput { return v.CopiedAliases }).(pulumi.StringArrayOutput)
}

func (o CachedImageOutput) CopyAliases() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.BoolPtrOutput { return v.CopyAliases }).(pulumi.BoolPtrOutput)
}

func (o CachedImageOutput) CreatedAt() pulumi.IntOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.IntOutput { return v.CreatedAt }).(pulumi.IntOutput)
}

func (o CachedImageOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringOutput { return v.Fingerprint }).(pulumi.StringOutput)
}

func (o CachedImageOutput) Project() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringPtrOutput { return v.Project }).(pulumi.StringPtrOutput)
}

func (o CachedImageOutput) Remote() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringPtrOutput { return v.Remote }).(pulumi.StringPtrOutput)
}

func (o CachedImageOutput) SourceImage() pulumi.StringOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringOutput { return v.SourceImage }).(pulumi.StringOutput)
}

func (o CachedImageOutput) SourceRemote() pulumi.StringOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringOutput { return v.SourceRemote }).(pulumi.StringOutput)
}

func (o CachedImageOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CachedImage) pulumi.StringPtrOutput { return v.Type }).(pulumi.StringPtrOutput)
}

type CachedImageArrayOutput struct{ *pulumi.OutputState }

func (CachedImageArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CachedImage)(nil)).Elem()
}

func (o CachedImageArrayOutput) ToCachedImageArrayOutput() CachedImageArrayOutput {
	return o
}

func (o CachedImageArrayOutput) ToCachedImageArrayOutputWithContext(ctx context.Context) CachedImageArrayOutput {
	return o
}

func (o CachedImageArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*CachedImage] {
	return pulumix.Output[[]*CachedImage]{
		OutputState: o.OutputState,
	}
}

func (o CachedImageArrayOutput) Index(i pulumi.IntInput) CachedImageOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CachedImage {
		return vs[0].([]*CachedImage)[vs[1].(int)]
	}).(CachedImageOutput)
}

type CachedImageMapOutput struct{ *pulumi.OutputState }

func (CachedImageMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CachedImage)(nil)).Elem()
}

func (o CachedImageMapOutput) ToCachedImageMapOutput() CachedImageMapOutput {
	return o
}

func (o CachedImageMapOutput) ToCachedImageMapOutputWithContext(ctx context.Context) CachedImageMapOutput {
	return o
}

func (o CachedImageMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*CachedImage] {
	return pulumix.Output[map[string]*CachedImage]{
		OutputState: o.OutputState,
	}
}

func (o CachedImageMapOutput) MapIndex(k pulumi.StringInput) CachedImageOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CachedImage {
		return vs[0].(map[string]*CachedImage)[vs[1].(string)]
	}).(CachedImageOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CachedImageInput)(nil)).Elem(), &CachedImage{})
	pulumi.RegisterInputType(reflect.TypeOf((*CachedImageArrayInput)(nil)).Elem(), CachedImageArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CachedImageMapInput)(nil)).Elem(), CachedImageMap{})
	pulumi.RegisterOutputType(CachedImageOutput{})
	pulumi.RegisterOutputType(CachedImageArrayOutput{})
	pulumi.RegisterOutputType(CachedImageMapOutput{})
}
