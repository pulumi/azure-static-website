// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureStaticWebsite
{
    [AzureStaticWebsiteResourceType("azure-static-website:index:Website")]
    public partial class Website : Pulumi.ComponentResource
    {
        /// <summary>
        /// the CDN URL for the site
        /// </summary>
        [Output("cdnURL")]
        public Output<string?> CdnURL { get; private set; } = null!;

        /// <summary>
        /// the custom domain URL where the static website can be accessed
        /// </summary>
        [Output("customDomainURL")]
        public Output<string?> CustomDomainURL { get; private set; } = null!;

        /// <summary>
        /// the Storage URL for the site
        /// </summary>
        [Output("originURL")]
        public Output<string> OriginURL { get; private set; } = null!;

        /// <summary>
        /// the name of the resource group that was provisioned to contain the needed static website resources
        /// </summary>
        [Output("resourceGroupName")]
        public Output<string> ResourceGroupName { get; private set; } = null!;


        /// <summary>
        /// Create a Website resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Website(string name, WebsiteArgs args, ComponentResourceOptions? options = null)
            : base("azure-static-website:index:Website", name, args ?? new WebsiteArgs(), MakeResourceOptions(options, ""), remote: true)
        {
        }

        private static ComponentResourceOptions MakeResourceOptions(ComponentResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ComponentResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ComponentResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class WebsiteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the DNS zone.
        /// </summary>
        [Input("dnsZoneName")]
        public Input<string>? DnsZoneName { get; set; }

        /// <summary>
        /// The name of the resource group your domain is attached to
        /// </summary>
        [Input("domainResourceGroup")]
        public Input<string>? DomainResourceGroup { get; set; }

        /// <summary>
        /// The default 404 error page
        /// </summary>
        [Input("errorDocument")]
        public Input<string>? ErrorDocument { get; set; }

        /// <summary>
        /// The default document for the site. Defaults to index.html
        /// </summary>
        [Input("indexDocument")]
        public Input<string>? IndexDocument { get; set; }

        /// <summary>
        /// The root directory containing the website's contents.
        /// </summary>
        [Input("sitePath", required: true)]
        public Input<string> SitePath { get; set; } = null!;

        /// <summary>
        /// The subdomain used to access the static website. If not specified will configure with apex/root domain of the DNS zone specified.
        /// </summary>
        [Input("subdomain")]
        public Input<string>? Subdomain { get; set; }

        /// <summary>
        /// Provision CDN to serve content.
        /// </summary>
        [Input("withCDN")]
        public Input<bool>? WithCDN { get; set; }

        /// <summary>
        /// Provision a custom domain to serve the site from. This will require a you to set the domainResourceGroup property to the name of the resource group your domain is attached to, as well as the dnsZoneName property for the name of the DNS zone, configured in Azure
        /// </summary>
        [Input("withCustomDomain")]
        public Input<bool>? WithCustomDomain { get; set; }

        public WebsiteArgs()
        {
        }
    }
}
