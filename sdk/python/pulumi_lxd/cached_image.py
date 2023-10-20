# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CachedImageArgs', 'CachedImage']

@pulumi.input_type
class CachedImageArgs:
    def __init__(__self__, *,
                 source_image: pulumi.Input[str],
                 source_remote: pulumi.Input[str],
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 copy_aliases: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CachedImage resource.
        """
        CachedImageArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            source_image=source_image,
            source_remote=source_remote,
            aliases=aliases,
            copy_aliases=copy_aliases,
            project=project,
            remote=remote,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             source_image: pulumi.Input[str],
             source_remote: pulumi.Input[str],
             aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             copy_aliases: Optional[pulumi.Input[bool]] = None,
             project: Optional[pulumi.Input[str]] = None,
             remote: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'sourceImage' in kwargs:
            source_image = kwargs['sourceImage']
        if 'sourceRemote' in kwargs:
            source_remote = kwargs['sourceRemote']
        if 'copyAliases' in kwargs:
            copy_aliases = kwargs['copyAliases']

        _setter("source_image", source_image)
        _setter("source_remote", source_remote)
        if aliases is not None:
            _setter("aliases", aliases)
        if copy_aliases is not None:
            _setter("copy_aliases", copy_aliases)
        if project is not None:
            _setter("project", project)
        if remote is not None:
            _setter("remote", remote)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_image")

    @source_image.setter
    def source_image(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_image", value)

    @property
    @pulumi.getter(name="sourceRemote")
    def source_remote(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_remote")

    @source_remote.setter
    def source_remote(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_remote", value)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "aliases")

    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aliases", value)

    @property
    @pulumi.getter(name="copyAliases")
    def copy_aliases(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "copy_aliases")

    @copy_aliases.setter
    def copy_aliases(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_aliases", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def remote(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "remote")

    @remote.setter
    def remote(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _CachedImageState:
    def __init__(__self__, *,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 copied_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 copy_aliases: Optional[pulumi.Input[bool]] = None,
                 created_at: Optional[pulumi.Input[int]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 source_image: Optional[pulumi.Input[str]] = None,
                 source_remote: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CachedImage resources.
        """
        _CachedImageState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            aliases=aliases,
            architecture=architecture,
            copied_aliases=copied_aliases,
            copy_aliases=copy_aliases,
            created_at=created_at,
            fingerprint=fingerprint,
            project=project,
            remote=remote,
            source_image=source_image,
            source_remote=source_remote,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             architecture: Optional[pulumi.Input[str]] = None,
             copied_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             copy_aliases: Optional[pulumi.Input[bool]] = None,
             created_at: Optional[pulumi.Input[int]] = None,
             fingerprint: Optional[pulumi.Input[str]] = None,
             project: Optional[pulumi.Input[str]] = None,
             remote: Optional[pulumi.Input[str]] = None,
             source_image: Optional[pulumi.Input[str]] = None,
             source_remote: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'copiedAliases' in kwargs:
            copied_aliases = kwargs['copiedAliases']
        if 'copyAliases' in kwargs:
            copy_aliases = kwargs['copyAliases']
        if 'createdAt' in kwargs:
            created_at = kwargs['createdAt']
        if 'sourceImage' in kwargs:
            source_image = kwargs['sourceImage']
        if 'sourceRemote' in kwargs:
            source_remote = kwargs['sourceRemote']

        if aliases is not None:
            _setter("aliases", aliases)
        if architecture is not None:
            _setter("architecture", architecture)
        if copied_aliases is not None:
            _setter("copied_aliases", copied_aliases)
        if copy_aliases is not None:
            _setter("copy_aliases", copy_aliases)
        if created_at is not None:
            _setter("created_at", created_at)
        if fingerprint is not None:
            _setter("fingerprint", fingerprint)
        if project is not None:
            _setter("project", project)
        if remote is not None:
            _setter("remote", remote)
        if source_image is not None:
            _setter("source_image", source_image)
        if source_remote is not None:
            _setter("source_remote", source_remote)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "aliases")

    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aliases", value)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "architecture")

    @architecture.setter
    def architecture(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "architecture", value)

    @property
    @pulumi.getter(name="copiedAliases")
    def copied_aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "copied_aliases")

    @copied_aliases.setter
    def copied_aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "copied_aliases", value)

    @property
    @pulumi.getter(name="copyAliases")
    def copy_aliases(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "copy_aliases")

    @copy_aliases.setter
    def copy_aliases(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "copy_aliases", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def remote(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "remote")

    @remote.setter
    def remote(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remote", value)

    @property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_image")

    @source_image.setter
    def source_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image", value)

    @property
    @pulumi.getter(name="sourceRemote")
    def source_remote(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source_remote")

    @source_remote.setter
    def source_remote(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_remote", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class CachedImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 copy_aliases: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 source_image: Optional[pulumi.Input[str]] = None,
                 source_remote: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a CachedImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CachedImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CachedImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CachedImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CachedImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CachedImageArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 copy_aliases: Optional[pulumi.Input[bool]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 remote: Optional[pulumi.Input[str]] = None,
                 source_image: Optional[pulumi.Input[str]] = None,
                 source_remote: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CachedImageArgs.__new__(CachedImageArgs)

            __props__.__dict__["aliases"] = aliases
            __props__.__dict__["copy_aliases"] = copy_aliases
            __props__.__dict__["project"] = project
            __props__.__dict__["remote"] = remote
            if source_image is None and not opts.urn:
                raise TypeError("Missing required property 'source_image'")
            __props__.__dict__["source_image"] = source_image
            if source_remote is None and not opts.urn:
                raise TypeError("Missing required property 'source_remote'")
            __props__.__dict__["source_remote"] = source_remote
            __props__.__dict__["type"] = type
            __props__.__dict__["architecture"] = None
            __props__.__dict__["copied_aliases"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["fingerprint"] = None
        super(CachedImage, __self__).__init__(
            'lxd:index/cachedImage:CachedImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            copied_aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            copy_aliases: Optional[pulumi.Input[bool]] = None,
            created_at: Optional[pulumi.Input[int]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            remote: Optional[pulumi.Input[str]] = None,
            source_image: Optional[pulumi.Input[str]] = None,
            source_remote: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'CachedImage':
        """
        Get an existing CachedImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CachedImageState.__new__(_CachedImageState)

        __props__.__dict__["aliases"] = aliases
        __props__.__dict__["architecture"] = architecture
        __props__.__dict__["copied_aliases"] = copied_aliases
        __props__.__dict__["copy_aliases"] = copy_aliases
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["project"] = project
        __props__.__dict__["remote"] = remote
        __props__.__dict__["source_image"] = source_image
        __props__.__dict__["source_remote"] = source_remote
        __props__.__dict__["type"] = type
        return CachedImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[str]:
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter(name="copiedAliases")
    def copied_aliases(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "copied_aliases")

    @property
    @pulumi.getter(name="copyAliases")
    def copy_aliases(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "copy_aliases")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[int]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def remote(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "remote")

    @property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_image")

    @property
    @pulumi.getter(name="sourceRemote")
    def source_remote(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source_remote")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "type")

