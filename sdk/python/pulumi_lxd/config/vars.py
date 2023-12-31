# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

import types

__config__ = pulumi.Config('lxd')


class _ExportableConfig(types.ModuleType):
    @property
    def accept_remote_certificate(self) -> Optional[bool]:
        """
        Accept the server certificate
        """
        return __config__.get_bool('acceptRemoteCertificate')

    @property
    def address(self) -> Optional[str]:
        return __config__.get('address')

    @property
    def config_dir(self) -> Optional[str]:
        """
        The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
        """
        return __config__.get('configDir')

    @property
    def generate_client_certificates(self) -> Optional[bool]:
        return __config__.get_bool('generateClientCertificates')

    @property
    def lxd_remotes(self) -> Optional[str]:
        return __config__.get('lxdRemotes')

    @property
    def port(self) -> Optional[str]:
        return __config__.get('port')

    @property
    def project(self) -> Optional[str]:
        """
        The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
        """
        return __config__.get('project')

    @property
    def refresh_interval(self) -> Optional[str]:
        """
        How often to poll during state changes (default 10s)
        """
        return __config__.get('refreshInterval')

    @property
    def remote(self) -> Optional[str]:
        return __config__.get('remote')

    @property
    def remote_password(self) -> Optional[str]:
        return __config__.get('remotePassword')

    @property
    def scheme(self) -> Optional[str]:
        return __config__.get('scheme')

