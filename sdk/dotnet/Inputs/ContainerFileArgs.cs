// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd.Inputs
{

    public sealed class ContainerFileArgs : global::Pulumi.ResourceArgs
    {
        [Input("content")]
        public Input<string>? Content { get; set; }

        [Input("createDirectories")]
        public Input<bool>? CreateDirectories { get; set; }

        [Input("gid")]
        public Input<int>? Gid { get; set; }

        [Input("mode")]
        public Input<string>? Mode { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("targetFile", required: true)]
        public Input<string> TargetFile { get; set; } = null!;

        [Input("uid")]
        public Input<int>? Uid { get; set; }

        public ContainerFileArgs()
        {
        }
        public static new ContainerFileArgs Empty => new ContainerFileArgs();
    }
}