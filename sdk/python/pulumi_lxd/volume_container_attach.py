# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VolumeContainerAttachArgs', 'VolumeContainerAttach']

@pulumi.input_type
class VolumeContainerAttachArgs:
    def __init__(__self__, *,
                 container_name: pulumi.Input[str],
                 path: pulumi.Input[str],
                 pool: pulumi.Input[str],
                 volume_name: pulumi.Input[str],
                 device_name: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeContainerAttach resource.
        """
        VolumeContainerAttachArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            container_name=container_name,
            path=path,
            pool=pool,
            volume_name=volume_name,
            device_name=device_name,
            remote=remote,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             container_name: pulumi.Input[str],
             path: pulumi.Input[str],
             pool: pulumi.Input[str],
             volume_name: pulumi.Input[str],
             device_name: Optional[pulumi.Input[str]] = None,
             remote: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'containerName' in kwargs:
            container_name = kwargs['containerName']
        if 'volumeName' in kwargs:
            volume_name = kwargs['volumeName']
        if 'deviceName' in kwargs:
            device_name = kwargs['deviceName']

        if container_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""container_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        _setter("container_name", container_name)
        if path is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""path is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        _setter("path", path)
        if pool is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""pool is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        _setter("pool", pool)
        if volume_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""volume_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        _setter("volume_name", volume_name)
        if device_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""device_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if device_name is not None:
            _setter("device_name", device_name)
        if remote is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""remote is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if remote is not None:
            _setter("remote", remote)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""container_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""path is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Input[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""pool is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""volume_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_name", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""device_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def remote(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""remote is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "remote")

    @remote.setter
    def remote(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote", value)


@pulumi.input_type
class _VolumeContainerAttachState:
    def __init__(__self__, *,
                 container_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VolumeContainerAttach resources.
        """
        _VolumeContainerAttachState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            container_name=container_name,
            device_name=device_name,
            path=path,
            pool=pool,
            remote=remote,
            volume_name=volume_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             container_name: Optional[pulumi.Input[str]] = None,
             device_name: Optional[pulumi.Input[str]] = None,
             path: Optional[pulumi.Input[str]] = None,
             pool: Optional[pulumi.Input[str]] = None,
             remote: Optional[pulumi.Input[str]] = None,
             volume_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'containerName' in kwargs:
            container_name = kwargs['containerName']
        if 'deviceName' in kwargs:
            device_name = kwargs['deviceName']
        if 'volumeName' in kwargs:
            volume_name = kwargs['volumeName']

        if container_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""container_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if container_name is not None:
            _setter("container_name", container_name)
        if device_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""device_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if device_name is not None:
            _setter("device_name", device_name)
        if path is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""path is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if path is not None:
            _setter("path", path)
        if pool is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""pool is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if pool is not None:
            _setter("pool", pool)
        if remote is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""remote is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if remote is not None:
            _setter("remote", remote)
        if volume_name is not None:
            warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
            pulumi.log.warn("""volume_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")
        if volume_name is not None:
            _setter("volume_name", volume_name)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""container_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""device_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""path is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""pool is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def remote(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""remote is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "remote")

    @remote.setter
    def remote(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""volume_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class VolumeContainerAttach(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a VolumeContainerAttach resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeContainerAttachArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a VolumeContainerAttach resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param VolumeContainerAttachArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeContainerAttachArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            VolumeContainerAttachArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeContainerAttachArgs.__new__(VolumeContainerAttachArgs)

            if container_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_name'")
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["device_name"] = device_name
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            if pool is None and not opts.urn:
                raise TypeError("Missing required property 'pool'")
            __props__.__dict__["pool"] = pool
            __props__.__dict__["remote"] = remote
            if volume_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_name'")
            __props__.__dict__["volume_name"] = volume_name
        super(VolumeContainerAttach, __self__).__init__(
            'lxd:index/volumeContainerAttach:VolumeContainerAttach',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_name: Optional[pulumi.Input[str]] = None,
            device_name: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            remote: Optional[pulumi.Input[str]] = None,
            volume_name: Optional[pulumi.Input[str]] = None) -> 'VolumeContainerAttach':
        """
        Get an existing VolumeContainerAttach resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VolumeContainerAttachState.__new__(_VolumeContainerAttachState)

        __props__.__dict__["container_name"] = container_name
        __props__.__dict__["device_name"] = device_name
        __props__.__dict__["path"] = path
        __props__.__dict__["pool"] = pool
        __props__.__dict__["remote"] = remote
        __props__.__dict__["volume_name"] = volume_name
        return VolumeContainerAttach(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""container_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Output[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""device_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""path is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""pool is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "pool")

    @property
    @pulumi.getter
    def remote(self) -> pulumi.Output[Optional[str]]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""remote is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "remote")

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Output[str]:
        warnings.warn("""lxd_volume_container_attach has been deprecated and will be removed""", DeprecationWarning)
        pulumi.log.warn("""volume_name is deprecated: lxd_volume_container_attach has been deprecated and will be removed""")

        return pulumi.get(self, "volume_name")

