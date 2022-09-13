# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from ._inputs import *

__all__ = ['WebsiteArgs', 'Website']

@pulumi.input_type
class WebsiteArgs:
    def __init__(__self__, *,
                 site_path: pulumi.Input[str],
                 cdn: Optional[pulumi.Input[Union[bool, 'WebsiteCDNConfigArgs']]] = None,
                 domain: Optional[pulumi.Input['WebsiteDomainConfigArgs']] = None,
                 error_doc: Optional[pulumi.Input[str]] = None,
                 index_doc: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input['WebsiteStorageConfigArgs']] = None):
        """
        The set of arguments for constructing a Website resource.
        :param pulumi.Input[str] site_path: The root directory containing contents of the built website contents.
        :param pulumi.Input['WebsiteDomainConfigArgs'] domain: The domain configuration of the website.
        :param pulumi.Input[str] error_doc: The default error page for the website. Defaults to error.html.
        :param pulumi.Input[str] index_doc: The default document for the site. Defaults to index.html.
        :param pulumi.Input['WebsiteStorageConfigArgs'] storage: The storage configuration of the website.
        """
        pulumi.set(__self__, "site_path", site_path)
        if cdn is not None:
            pulumi.set(__self__, "cdn", cdn)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if error_doc is not None:
            pulumi.set(__self__, "error_doc", error_doc)
        if index_doc is not None:
            pulumi.set(__self__, "index_doc", index_doc)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter(name="sitePath")
    def site_path(self) -> pulumi.Input[str]:
        """
        The root directory containing contents of the built website contents.
        """
        return pulumi.get(self, "site_path")

    @site_path.setter
    def site_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_path", value)

    @property
    @pulumi.getter
    def cdn(self) -> Optional[pulumi.Input[Union[bool, 'WebsiteCDNConfigArgs']]]:
        return pulumi.get(self, "cdn")

    @cdn.setter
    def cdn(self, value: Optional[pulumi.Input[Union[bool, 'WebsiteCDNConfigArgs']]]):
        pulumi.set(self, "cdn", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input['WebsiteDomainConfigArgs']]:
        """
        The domain configuration of the website.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input['WebsiteDomainConfigArgs']]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="errorDoc")
    def error_doc(self) -> Optional[pulumi.Input[str]]:
        """
        The default error page for the website. Defaults to error.html.
        """
        return pulumi.get(self, "error_doc")

    @error_doc.setter
    def error_doc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_doc", value)

    @property
    @pulumi.getter(name="indexDoc")
    def index_doc(self) -> Optional[pulumi.Input[str]]:
        """
        The default document for the site. Defaults to index.html.
        """
        return pulumi.get(self, "index_doc")

    @index_doc.setter
    def index_doc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index_doc", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input['WebsiteStorageConfigArgs']]:
        """
        The storage configuration of the website.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input['WebsiteStorageConfigArgs']]):
        pulumi.set(self, "storage", value)


class Website(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cdn: Optional[pulumi.Input[Union[bool, pulumi.InputType['WebsiteCDNConfigArgs']]]] = None,
                 domain: Optional[pulumi.Input[pulumi.InputType['WebsiteDomainConfigArgs']]] = None,
                 error_doc: Optional[pulumi.Input[str]] = None,
                 index_doc: Optional[pulumi.Input[str]] = None,
                 site_path: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[pulumi.InputType['WebsiteStorageConfigArgs']]] = None,
                 __props__=None):
        """
        Create a Website resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['WebsiteDomainConfigArgs']] domain: The domain configuration of the website.
        :param pulumi.Input[str] error_doc: The default error page for the website. Defaults to error.html.
        :param pulumi.Input[str] index_doc: The default document for the site. Defaults to index.html.
        :param pulumi.Input[str] site_path: The root directory containing contents of the built website contents.
        :param pulumi.Input[pulumi.InputType['WebsiteStorageConfigArgs']] storage: The storage configuration of the website.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebsiteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Website resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WebsiteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebsiteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cdn: Optional[pulumi.Input[Union[bool, pulumi.InputType['WebsiteCDNConfigArgs']]]] = None,
                 domain: Optional[pulumi.Input[pulumi.InputType['WebsiteDomainConfigArgs']]] = None,
                 error_doc: Optional[pulumi.Input[str]] = None,
                 index_doc: Optional[pulumi.Input[str]] = None,
                 site_path: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[pulumi.InputType['WebsiteStorageConfigArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebsiteArgs.__new__(WebsiteArgs)

            __props__.__dict__["cdn"] = cdn
            __props__.__dict__["domain"] = domain
            __props__.__dict__["error_doc"] = error_doc
            __props__.__dict__["index_doc"] = index_doc
            if site_path is None and not opts.urn:
                raise TypeError("Missing required property 'site_path'")
            __props__.__dict__["site_path"] = site_path
            __props__.__dict__["storage"] = storage
            __props__.__dict__["cdn_hostname"] = None
            __props__.__dict__["cdn_url"] = None
            __props__.__dict__["domain_url"] = None
            __props__.__dict__["origin_hostname"] = None
            __props__.__dict__["origin_url"] = None
            __props__.__dict__["resource_group_name"] = None
        super(Website, __self__).__init__(
            'azure-static-website:index:Website',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="cdnHostname")
    def cdn_hostname(self) -> pulumi.Output[Optional[str]]:
        """
        The CDN hostname of the website.
        """
        return pulumi.get(self, "cdn_hostname")

    @property
    @pulumi.getter(name="cdnURL")
    def cdn_url(self) -> pulumi.Output[Optional[str]]:
        """
        The CDN URL of the website.
        """
        return pulumi.get(self, "cdn_url")

    @property
    @pulumi.getter(name="domainURL")
    def domain_url(self) -> pulumi.Output[Optional[str]]:
        """
        The custom-domain URL of the website.
        """
        return pulumi.get(self, "domain_url")

    @property
    @pulumi.getter(name="originHostname")
    def origin_hostname(self) -> pulumi.Output[str]:
        """
        The hostname of the origin.
        """
        return pulumi.get(self, "origin_hostname")

    @property
    @pulumi.getter(name="originURL")
    def origin_url(self) -> pulumi.Output[str]:
        """
        The direct URL of the website.
        """
        return pulumi.get(self, "origin_url")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        The name of the created resource group.
        """
        return pulumi.get(self, "resource_group_name")

