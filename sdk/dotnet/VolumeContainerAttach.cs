// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd
{
    [LxdResourceType("lxd:index/volumeContainerAttach:VolumeContainerAttach")]
    public partial class VolumeContainerAttach : global::Pulumi.CustomResource
    {
        [Output("containerName")]
        public Output<string> ContainerName { get; private set; } = null!;

        [Output("deviceName")]
        public Output<string> DeviceName { get; private set; } = null!;

        [Output("path")]
        public Output<string> Path { get; private set; } = null!;

        [Output("pool")]
        public Output<string> Pool { get; private set; } = null!;

        [Output("remote")]
        public Output<string?> Remote { get; private set; } = null!;

        [Output("volumeName")]
        public Output<string> VolumeName { get; private set; } = null!;


        /// <summary>
        /// Create a VolumeContainerAttach resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VolumeContainerAttach(string name, VolumeContainerAttachArgs args, CustomResourceOptions? options = null)
            : base("lxd:index/volumeContainerAttach:VolumeContainerAttach", name, args ?? new VolumeContainerAttachArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VolumeContainerAttach(string name, Input<string> id, VolumeContainerAttachState? state = null, CustomResourceOptions? options = null)
            : base("lxd:index/volumeContainerAttach:VolumeContainerAttach", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing VolumeContainerAttach resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VolumeContainerAttach Get(string name, Input<string> id, VolumeContainerAttachState? state = null, CustomResourceOptions? options = null)
        {
            return new VolumeContainerAttach(name, id, state, options);
        }
    }

    public sealed class VolumeContainerAttachArgs : global::Pulumi.ResourceArgs
    {
        [Input("containerName", required: true)]
        public Input<string> ContainerName { get; set; } = null!;

        [Input("deviceName")]
        public Input<string>? DeviceName { get; set; }

        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        [Input("pool", required: true)]
        public Input<string> Pool { get; set; } = null!;

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("volumeName", required: true)]
        public Input<string> VolumeName { get; set; } = null!;

        public VolumeContainerAttachArgs()
        {
        }
        public static new VolumeContainerAttachArgs Empty => new VolumeContainerAttachArgs();
    }

    public sealed class VolumeContainerAttachState : global::Pulumi.ResourceArgs
    {
        [Input("containerName")]
        public Input<string>? ContainerName { get; set; }

        [Input("deviceName")]
        public Input<string>? DeviceName { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("pool")]
        public Input<string>? Pool { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("volumeName")]
        public Input<string>? VolumeName { get; set; }

        public VolumeContainerAttachState()
        {
        }
        public static new VolumeContainerAttachState Empty => new VolumeContainerAttachState();
    }
}