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
        /// Blah.
        /// </summary>
        [Output("cdnURL")]
        public Output<string?> CdnURL { get; private set; } = null!;

        /// <summary>
        /// Fixme.
        /// </summary>
        [Output("customDomainURL")]
        public Output<string?> CustomDomainURL { get; private set; } = null!;

        /// <summary>
        /// Blah
        /// </summary>
        [Output("originURL")]
        public Output<string> OriginURL { get; private set; } = null!;

        /// <summary>
        /// Blah
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
        /// default 404 page
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
        /// Provision CloudFront CDN to serve content.
        /// </summary>
        [Input("withCDN")]
        public Input<bool>? WithCDN { get; set; }

        public WebsiteArgs()
        {
        }
    }
}