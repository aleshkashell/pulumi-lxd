// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd
{
    [LxdResourceType("lxd:index/storagePool:StoragePool")]
    public partial class StoragePool : global::Pulumi.CustomResource
    {
        [Output("config")]
        public Output<ImmutableDictionary<string, object>?> Config { get; private set; } = null!;

        [Output("driver")]
        public Output<string> Driver { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("project")]
        public Output<string?> Project { get; private set; } = null!;

        [Output("remote")]
        public Output<string?> Remote { get; private set; } = null!;

        [Output("target")]
        public Output<string?> Target { get; private set; } = null!;


        /// <summary>
        /// Create a StoragePool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StoragePool(string name, StoragePoolArgs args, CustomResourceOptions? options = null)
            : base("lxd:index/storagePool:StoragePool", name, args ?? new StoragePoolArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StoragePool(string name, Input<string> id, StoragePoolState? state = null, CustomResourceOptions? options = null)
            : base("lxd:index/storagePool:StoragePool", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/aleshkashell/pulumi-lxd",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing StoragePool resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StoragePool Get(string name, Input<string> id, StoragePoolState? state = null, CustomResourceOptions? options = null)
        {
            return new StoragePool(name, id, state, options);
        }
    }

    public sealed class StoragePoolArgs : global::Pulumi.ResourceArgs
    {
        [Input("config")]
        private InputMap<object>? _config;
        public InputMap<object> Config
        {
            get => _config ?? (_config = new InputMap<object>());
            set => _config = value;
        }

        [Input("driver", required: true)]
        public Input<string> Driver { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("target")]
        public Input<string>? Target { get; set; }

        public StoragePoolArgs()
        {
        }
        public static new StoragePoolArgs Empty => new StoragePoolArgs();
    }

    public sealed class StoragePoolState : global::Pulumi.ResourceArgs
    {
        [Input("config")]
        private InputMap<object>? _config;
        public InputMap<object> Config
        {
            get => _config ?? (_config = new InputMap<object>());
            set => _config = value;
        }

        [Input("driver")]
        public Input<string>? Driver { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("target")]
        public Input<string>? Target { get; set; }

        public StoragePoolState()
        {
        }
        public static new StoragePoolState Empty => new StoragePoolState();
    }
}
