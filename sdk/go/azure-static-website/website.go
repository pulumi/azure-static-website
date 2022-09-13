// Code generated by Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package azurestaticwebsite

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type Website struct {
	pulumi.ResourceState

	// The CDN hostname of the website.
	CdnHostname pulumi.StringPtrOutput `pulumi:"cdnHostname"`
	// The CDN URL of the website.
	CdnURL pulumi.StringPtrOutput `pulumi:"cdnURL"`
	// The custom-domain URL of the website.
	DomainURL pulumi.StringPtrOutput `pulumi:"domainURL"`
	// The hostname of the origin.
	OriginHostname pulumi.StringOutput `pulumi:"originHostname"`
	// The direct URL of the website.
	OriginURL pulumi.StringOutput `pulumi:"originURL"`
	// The name of the created resource group.
	ResourceGroupName pulumi.StringOutput `pulumi:"resourceGroupName"`
}

// NewWebsite registers a new resource with the given unique name, arguments, and options.
func NewWebsite(ctx *pulumi.Context,
	name string, args *WebsiteArgs, opts ...pulumi.ResourceOption) (*Website, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SitePath == nil {
		return nil, errors.New("invalid value for required argument 'SitePath'")
	}
	var resource Website
	err := ctx.RegisterRemoteComponentResource("azure-static-website:index:Website", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type websiteArgs struct {
	Cdn interface{} `pulumi:"cdn"`
	// The domain configuration of the website.
	Domain *WebsiteDomainConfig `pulumi:"domain"`
	// The default error page for the website. Defaults to error.html.
	ErrorDoc *string `pulumi:"errorDoc"`
	// The default document for the site. Defaults to index.html.
	IndexDoc *string `pulumi:"indexDoc"`
	// The root directory containing contents of the built website contents.
	SitePath string `pulumi:"sitePath"`
	// The storage configuration of the website.
	Storage *WebsiteStorageConfig `pulumi:"storage"`
}

// The set of arguments for constructing a Website resource.
type WebsiteArgs struct {
	Cdn pulumi.Input
	// The domain configuration of the website.
	Domain WebsiteDomainConfigPtrInput
	// The default error page for the website. Defaults to error.html.
	ErrorDoc pulumi.StringPtrInput
	// The default document for the site. Defaults to index.html.
	IndexDoc pulumi.StringPtrInput
	// The root directory containing contents of the built website contents.
	SitePath pulumi.StringInput
	// The storage configuration of the website.
	Storage WebsiteStorageConfigPtrInput
}

func (WebsiteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*websiteArgs)(nil)).Elem()
}

type WebsiteInput interface {
	pulumi.Input

	ToWebsiteOutput() WebsiteOutput
	ToWebsiteOutputWithContext(ctx context.Context) WebsiteOutput
}

func (*Website) ElementType() reflect.Type {
	return reflect.TypeOf((**Website)(nil)).Elem()
}

func (i *Website) ToWebsiteOutput() WebsiteOutput {
	return i.ToWebsiteOutputWithContext(context.Background())
}

func (i *Website) ToWebsiteOutputWithContext(ctx context.Context) WebsiteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteOutput)
}

// WebsiteArrayInput is an input type that accepts WebsiteArray and WebsiteArrayOutput values.
// You can construct a concrete instance of `WebsiteArrayInput` via:
//
//          WebsiteArray{ WebsiteArgs{...} }
type WebsiteArrayInput interface {
	pulumi.Input

	ToWebsiteArrayOutput() WebsiteArrayOutput
	ToWebsiteArrayOutputWithContext(context.Context) WebsiteArrayOutput
}

type WebsiteArray []WebsiteInput

func (WebsiteArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Website)(nil)).Elem()
}

func (i WebsiteArray) ToWebsiteArrayOutput() WebsiteArrayOutput {
	return i.ToWebsiteArrayOutputWithContext(context.Background())
}

func (i WebsiteArray) ToWebsiteArrayOutputWithContext(ctx context.Context) WebsiteArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteArrayOutput)
}

// WebsiteMapInput is an input type that accepts WebsiteMap and WebsiteMapOutput values.
// You can construct a concrete instance of `WebsiteMapInput` via:
//
//          WebsiteMap{ "key": WebsiteArgs{...} }
type WebsiteMapInput interface {
	pulumi.Input

	ToWebsiteMapOutput() WebsiteMapOutput
	ToWebsiteMapOutputWithContext(context.Context) WebsiteMapOutput
}

type WebsiteMap map[string]WebsiteInput

func (WebsiteMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Website)(nil)).Elem()
}

func (i WebsiteMap) ToWebsiteMapOutput() WebsiteMapOutput {
	return i.ToWebsiteMapOutputWithContext(context.Background())
}

func (i WebsiteMap) ToWebsiteMapOutputWithContext(ctx context.Context) WebsiteMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebsiteMapOutput)
}

type WebsiteOutput struct{ *pulumi.OutputState }

func (WebsiteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Website)(nil)).Elem()
}

func (o WebsiteOutput) ToWebsiteOutput() WebsiteOutput {
	return o
}

func (o WebsiteOutput) ToWebsiteOutputWithContext(ctx context.Context) WebsiteOutput {
	return o
}

type WebsiteArrayOutput struct{ *pulumi.OutputState }

func (WebsiteArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Website)(nil)).Elem()
}

func (o WebsiteArrayOutput) ToWebsiteArrayOutput() WebsiteArrayOutput {
	return o
}

func (o WebsiteArrayOutput) ToWebsiteArrayOutputWithContext(ctx context.Context) WebsiteArrayOutput {
	return o
}

func (o WebsiteArrayOutput) Index(i pulumi.IntInput) WebsiteOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Website {
		return vs[0].([]*Website)[vs[1].(int)]
	}).(WebsiteOutput)
}

type WebsiteMapOutput struct{ *pulumi.OutputState }

func (WebsiteMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Website)(nil)).Elem()
}

func (o WebsiteMapOutput) ToWebsiteMapOutput() WebsiteMapOutput {
	return o
}

func (o WebsiteMapOutput) ToWebsiteMapOutputWithContext(ctx context.Context) WebsiteMapOutput {
	return o
}

func (o WebsiteMapOutput) MapIndex(k pulumi.StringInput) WebsiteOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Website {
		return vs[0].(map[string]*Website)[vs[1].(string)]
	}).(WebsiteOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteInput)(nil)).Elem(), &Website{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteArrayInput)(nil)).Elem(), WebsiteArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WebsiteMapInput)(nil)).Elem(), WebsiteMap{})
	pulumi.RegisterOutputType(WebsiteOutput{})
	pulumi.RegisterOutputType(WebsiteArrayOutput{})
	pulumi.RegisterOutputType(WebsiteMapOutput{})
}
