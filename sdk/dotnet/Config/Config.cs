// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Immutable;

namespace Pulumi.Lxd
{
    public static class Config
    {
        [global::System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Design", "IDE1006", Justification = 
        "Double underscore prefix used to avoid conflicts with variable names.")]
        private sealed class __Value<T>
        {
            private readonly Func<T> _getter;
            private T _value = default!;
            private bool _set;

            public __Value(Func<T> getter)
            {
                _getter = getter;
            }

            public T Get() => _set ? _value : _getter();

            public void Set(T value)
            {
                _value = value;
                _set = true;
            }
        }

        private static readonly global::Pulumi.Config __config = new global::Pulumi.Config("lxd");

        private static readonly __Value<bool?> _acceptRemoteCertificate = new __Value<bool?>(() => __config.GetBoolean("acceptRemoteCertificate"));
        /// <summary>
        /// Accept the server certificate
        /// </summary>
        public static bool? AcceptRemoteCertificate
        {
            get => _acceptRemoteCertificate.Get();
            set => _acceptRemoteCertificate.Set(value);
        }

        private static readonly __Value<string?> _address = new __Value<string?>(() => __config.Get("address"));
        public static string? Address
        {
            get => _address.Get();
            set => _address.Set(value);
        }

        private static readonly __Value<string?> _configDir = new __Value<string?>(() => __config.Get("configDir"));
        /// <summary>
        /// The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
        /// </summary>
        public static string? ConfigDir
        {
            get => _configDir.Get();
            set => _configDir.Set(value);
        }

        private static readonly __Value<bool?> _generateClientCertificates = new __Value<bool?>(() => __config.GetBoolean("generateClientCertificates"));
        public static bool? GenerateClientCertificates
        {
            get => _generateClientCertificates.Get();
            set => _generateClientCertificates.Set(value);
        }

        private static readonly __Value<ImmutableArray<Pulumi.Lxd.Config.Types.LxdRemotes>> _lxdRemotes = new __Value<ImmutableArray<Pulumi.Lxd.Config.Types.LxdRemotes>>(() => __config.GetObject<ImmutableArray<Pulumi.Lxd.Config.Types.LxdRemotes>>("lxdRemotes"));
        public static ImmutableArray<Pulumi.Lxd.Config.Types.LxdRemotes> LxdRemotes
        {
            get => _lxdRemotes.Get();
            set => _lxdRemotes.Set(value);
        }

        private static readonly __Value<string?> _port = new __Value<string?>(() => __config.Get("port"));
        public static string? Port
        {
            get => _port.Get();
            set => _port.Set(value);
        }

        private static readonly __Value<string?> _project = new __Value<string?>(() => __config.Get("project"));
        /// <summary>
        /// The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
        /// </summary>
        public static string? Project
        {
            get => _project.Get();
            set => _project.Set(value);
        }

        private static readonly __Value<string?> _refreshInterval = new __Value<string?>(() => __config.Get("refreshInterval"));
        /// <summary>
        /// How often to poll during state changes (default 10s)
        /// </summary>
        public static string? RefreshInterval
        {
            get => _refreshInterval.Get();
            set => _refreshInterval.Set(value);
        }

        private static readonly __Value<string?> _remote = new __Value<string?>(() => __config.Get("remote"));
        public static string? Remote
        {
            get => _remote.Get();
            set => _remote.Set(value);
        }

        private static readonly __Value<string?> _remotePassword = new __Value<string?>(() => __config.Get("remotePassword"));
        public static string? RemotePassword
        {
            get => _remotePassword.Get();
            set => _remotePassword.Set(value);
        }

        private static readonly __Value<string?> _scheme = new __Value<string?>(() => __config.Get("scheme"));
        public static string? Scheme
        {
            get => _scheme.Get();
            set => _scheme.Set(value);
        }

        public static class Types
        {

             public class LxdRemotes
             {
                public string? Address { get; set; } = null!;
                public bool? Default { get; set; }
                public string Name { get; set; }
                public string? Password { get; set; } = null!;
                public string? Port { get; set; } = null!;
                public string? Scheme { get; set; } = null!;
            }
        }
    }
}
