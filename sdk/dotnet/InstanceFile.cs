// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd
{
    [LxdResourceType("lxd:index/instanceFile:InstanceFile")]
    public partial class InstanceFile : global::Pulumi.CustomResource
    {
        [Output("append")]
        public Output<bool?> Append { get; private set; } = null!;

        [Output("content")]
        public Output<string?> Content { get; private set; } = null!;

        [Output("createDirectories")]
        public Output<bool?> CreateDirectories { get; private set; } = null!;

        [Output("gid")]
        public Output<int?> Gid { get; private set; } = null!;

        [Output("instanceName")]
        public Output<string> InstanceName { get; private set; } = null!;

        [Output("mode")]
        public Output<string?> Mode { get; private set; } = null!;

        [Output("project")]
        public Output<string?> Project { get; private set; } = null!;

        [Output("remote")]
        public Output<string?> Remote { get; private set; } = null!;

        [Output("source")]
        public Output<string?> Source { get; private set; } = null!;

        [Output("targetFile")]
        public Output<string> TargetFile { get; private set; } = null!;

        [Output("uid")]
        public Output<int?> Uid { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceFile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceFile(string name, InstanceFileArgs args, CustomResourceOptions? options = null)
            : base("lxd:index/instanceFile:InstanceFile", name, args ?? new InstanceFileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceFile(string name, Input<string> id, InstanceFileState? state = null, CustomResourceOptions? options = null)
            : base("lxd:index/instanceFile:InstanceFile", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/aleshkashell/pulumi-lxd/releases/download/v0.0.1/pulumi-resource-lxd",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InstanceFile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceFile Get(string name, Input<string> id, InstanceFileState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceFile(name, id, state, options);
        }
    }

    public sealed class InstanceFileArgs : global::Pulumi.ResourceArgs
    {
        [Input("append")]
        public Input<bool>? Append { get; set; }

        [Input("content")]
        public Input<string>? Content { get; set; }

        [Input("createDirectories")]
        public Input<bool>? CreateDirectories { get; set; }

        [Input("gid")]
        public Input<int>? Gid { get; set; }

        [Input("instanceName", required: true)]
        public Input<string> InstanceName { get; set; } = null!;

        [Input("mode")]
        public Input<string>? Mode { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("targetFile", required: true)]
        public Input<string> TargetFile { get; set; } = null!;

        [Input("uid")]
        public Input<int>? Uid { get; set; }

        public InstanceFileArgs()
        {
        }
        public static new InstanceFileArgs Empty => new InstanceFileArgs();
    }

    public sealed class InstanceFileState : global::Pulumi.ResourceArgs
    {
        [Input("append")]
        public Input<bool>? Append { get; set; }

        [Input("content")]
        public Input<string>? Content { get; set; }

        [Input("createDirectories")]
        public Input<bool>? CreateDirectories { get; set; }

        [Input("gid")]
        public Input<int>? Gid { get; set; }

        [Input("instanceName")]
        public Input<string>? InstanceName { get; set; }

        [Input("mode")]
        public Input<string>? Mode { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("targetFile")]
        public Input<string>? TargetFile { get; set; }

        [Input("uid")]
        public Input<int>? Uid { get; set; }

        public InstanceFileState()
        {
        }
        public static new InstanceFileState Empty => new InstanceFileState();
    }
}
