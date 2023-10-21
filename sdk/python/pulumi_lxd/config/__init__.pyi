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

acceptRemoteCertificate: Optional[bool]
"""
Accept the server certificate
"""

address: Optional[str]

configDir: Optional[str]
"""
The directory to look for existing LXD configuration. default = $HOME/snap/lxd/common/config:$HOME/.config/lxc
"""

generateClientCertificates: Optional[bool]

lxdRemotes: Optional[str]

port: Optional[str]

project: Optional[str]
"""
The project where project-scoped resources will be created. Can be overridden in individual resources. default = default
"""

refreshInterval: Optional[str]
"""
How often to poll during state changes (default 10s)
"""

remote: Optional[str]

remotePassword: Optional[str]

scheme: Optional[str]

