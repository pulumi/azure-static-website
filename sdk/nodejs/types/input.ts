// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface WebsiteCDNConfigArgs {
    /**
     * Whether to restrict traffic to HTTPS only. Defaults to false.
     */
    contentTypesToCompress?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The custom domain to use for CNAME records. For example, `www.example.com`.
     */
    isCompressionEnabled?: pulumi.Input<boolean>;
}

export interface WebsiteDomainConfigArgs {
    /**
     * The domain name of the website -- e.g., `example.com` in `www.example.com`
     */
    name: pulumi.Input<string>;
    /**
     * The name of the Azure resource group containing the DNS zone
     */
    resourceGroupName?: pulumi.Input<string>;
    /**
     * The subdomain name of the website -- e.g., `www` in `www.example.com`
     */
    subdomain: pulumi.Input<string>;
}

export interface WebsiteStorageConfigArgs {
    /**
     * The custom domain to use for CNAME records. For example, `www.example.com`.
     */
    customDomain?: pulumi.Input<string>;
    /**
     * Whether to restrict traffic to HTTPS only. Defaults to false.
     */
    enableHttpsTrafficOnly?: pulumi.Input<boolean>;
}
