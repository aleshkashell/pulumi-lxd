# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Project resource.
        """
        ProjectArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            config=config,
            description=description,
            name=name,
            target=target,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             target: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if config is not None:
            _setter("config", config)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if target is not None:
            _setter("target", target)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        """
        _ProjectState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            config=config,
            description=description,
            name=name,
            target=target,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             description: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             target: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        if config is not None:
            _setter("config", config)
        if description is not None:
            _setter("description", description)
        if name is not None:
            _setter("name", name)
        if target is not None:
            _setter("target", target)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Project resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProjectArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Project resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProjectArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["config"] = config
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["target"] = target
        super(Project, __self__).__init__(
            'lxd:index/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["config"] = config
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["target"] = target
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "target")

