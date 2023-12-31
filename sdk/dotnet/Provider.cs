// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Lxd
{
    /// <summary>
    /// The provider type for the lxd package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [LxdResourceType("pulumi:providers:lxd")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        [Output("address")]
        public Output<string?> Address { get; private set; } = null!;

        /// <summary>
        /// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
        /// </summary>
        [Output("configDir")]
        public Output<string?> ConfigDir { get; private set; } = null!;

        [Output("port")]
        public Output<string?> Port { get; private set; } = null!;

        /// <summary>
        /// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
        /// </summary>
        [Output("project")]
        public Output<string?> Project { get; private set; } = null!;

        /// <summary>
        /// How often to poll during state changes (default 10s)
        /// </summary>
        [Output("refreshInterval")]
        public Output<string?> RefreshInterval { get; private set; } = null!;

        [Output("remote")]
        public Output<string?> Remote { get; private set; } = null!;

        [Output("remotePassword")]
        public Output<string?> RemotePassword { get; private set; } = null!;

        [Output("scheme")]
        public Output<string?> Scheme { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("lxd", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/aleshkashell/pulumi-lxd",
                AdditionalSecretOutputs =
                {
                    "remotePassword",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Accept the server certificate
        /// </summary>
        [Input("acceptRemoteCertificate", json: true)]
        public Input<bool>? AcceptRemoteCertificate { get; set; }

        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
        /// </summary>
        [Input("configDir")]
        public Input<string>? ConfigDir { get; set; }

        [Input("generateClientCertificates", json: true)]
        public Input<bool>? GenerateClientCertificates { get; set; }

        [Input("lxdRemotes", json: true)]
        private InputList<Inputs.ProviderLxdRemoteArgs>? _lxdRemotes;
        public InputList<Inputs.ProviderLxdRemoteArgs> LxdRemotes
        {
            get => _lxdRemotes ?? (_lxdRemotes = new InputList<Inputs.ProviderLxdRemoteArgs>());
            set => _lxdRemotes = value;
        }

        [Input("port")]
        public Input<string>? Port { get; set; }

        /// <summary>
        /// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// How often to poll during state changes (default 10s)
        /// </summary>
        [Input("refreshInterval")]
        public Input<string>? RefreshInterval { get; set; }

        [Input("remote")]
        public Input<string>? Remote { get; set; }

        [Input("remotePassword")]
        private Input<string>? _remotePassword;
        [Obsolete(@"Use `lxd_remote.password` instead.")]
        public Input<string>? RemotePassword
        {
            get => _remotePassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _remotePassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("scheme")]
        public Input<string>? Scheme { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
