// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureStaticWebsite.Inputs
{

    public sealed class WebsiteCDNConfigArgs : Pulumi.ResourceArgs
    {
        [Input("contentTypesToCompress")]
        private InputList<string>? _contentTypesToCompress;

        /// <summary>
        /// Whether to restrict traffic to HTTPS only. Defaults to false.
        /// </summary>
        public InputList<string> ContentTypesToCompress
        {
            get => _contentTypesToCompress ?? (_contentTypesToCompress = new InputList<string>());
            set => _contentTypesToCompress = value;
        }

        /// <summary>
        /// The custom domain to use for CNAME records. For example, `www.example.com`.
        /// </summary>
        [Input("isCompressionEnabled")]
        public Input<bool>? IsCompressionEnabled { get; set; }

        public WebsiteCDNConfigArgs()
        {
        }
    }
}
