// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd.Outputs
{

    [OutputType]
    public sealed class InstanceFile
    {
        public readonly string? Content;
        public readonly bool? CreateDirectories;
        public readonly int? Gid;
        public readonly string? Mode;
        public readonly string? Source;
        public readonly string TargetFile;
        public readonly int? Uid;

        [OutputConstructor]
        private InstanceFile(
            string? content,

            bool? createDirectories,

            int? gid,

            string? mode,

            string? source,

            string targetFile,

            int? uid)
        {
            Content = content;
            CreateDirectories = createDirectories;
            Gid = gid;
            Mode = mode;
            Source = source;
            TargetFile = targetFile;
            Uid = uid;
        }
    }
}
