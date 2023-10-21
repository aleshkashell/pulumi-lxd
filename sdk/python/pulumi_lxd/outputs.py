# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ContainerDevice',
    'ContainerFile',
    'InstanceDevice',
    'InstanceFile',
    'ProfileDevice',
]

@pulumi.output_type
class ContainerDevice(dict):
    def __init__(__self__, *,
                 name: str,
                 properties: Mapping[str, Any],
                 type: str):
        ContainerDevice._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            properties=properties,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             properties: Mapping[str, Any],
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("name", name)
        _setter("properties", properties)
        _setter("type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Mapping[str, Any]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class ContainerFile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetFile":
            suggest = "target_file"
        elif key == "createDirectories":
            suggest = "create_directories"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerFile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerFile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerFile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_file: str,
                 content: Optional[str] = None,
                 create_directories: Optional[bool] = None,
                 gid: Optional[int] = None,
                 mode: Optional[str] = None,
                 source: Optional[str] = None,
                 uid: Optional[int] = None):
        ContainerFile._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            target_file=target_file,
            content=content,
            create_directories=create_directories,
            gid=gid,
            mode=mode,
            source=source,
            uid=uid,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             target_file: str,
             content: Optional[str] = None,
             create_directories: Optional[bool] = None,
             gid: Optional[int] = None,
             mode: Optional[str] = None,
             source: Optional[str] = None,
             uid: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'targetFile' in kwargs:
            target_file = kwargs['targetFile']
        if 'createDirectories' in kwargs:
            create_directories = kwargs['createDirectories']

        _setter("target_file", target_file)
        if content is not None:
            _setter("content", content)
        if create_directories is not None:
            _setter("create_directories", create_directories)
        if gid is not None:
            _setter("gid", gid)
        if mode is not None:
            _setter("mode", mode)
        if source is not None:
            _setter("source", source)
        if uid is not None:
            _setter("uid", uid)

    @property
    @pulumi.getter(name="targetFile")
    def target_file(self) -> str:
        return pulumi.get(self, "target_file")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> Optional[bool]:
        return pulumi.get(self, "create_directories")

    @property
    @pulumi.getter
    def gid(self) -> Optional[int]:
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def uid(self) -> Optional[int]:
        return pulumi.get(self, "uid")


@pulumi.output_type
class InstanceDevice(dict):
    def __init__(__self__, *,
                 name: str,
                 properties: Mapping[str, Any],
                 type: str):
        InstanceDevice._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            properties=properties,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             properties: Mapping[str, Any],
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("name", name)
        _setter("properties", properties)
        _setter("type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Mapping[str, Any]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class InstanceFile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetFile":
            suggest = "target_file"
        elif key == "createDirectories":
            suggest = "create_directories"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in InstanceFile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        InstanceFile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        InstanceFile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 target_file: str,
                 content: Optional[str] = None,
                 create_directories: Optional[bool] = None,
                 gid: Optional[int] = None,
                 mode: Optional[str] = None,
                 source: Optional[str] = None,
                 uid: Optional[int] = None):
        InstanceFile._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            target_file=target_file,
            content=content,
            create_directories=create_directories,
            gid=gid,
            mode=mode,
            source=source,
            uid=uid,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             target_file: str,
             content: Optional[str] = None,
             create_directories: Optional[bool] = None,
             gid: Optional[int] = None,
             mode: Optional[str] = None,
             source: Optional[str] = None,
             uid: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if 'targetFile' in kwargs:
            target_file = kwargs['targetFile']
        if 'createDirectories' in kwargs:
            create_directories = kwargs['createDirectories']

        _setter("target_file", target_file)
        if content is not None:
            _setter("content", content)
        if create_directories is not None:
            _setter("create_directories", create_directories)
        if gid is not None:
            _setter("gid", gid)
        if mode is not None:
            _setter("mode", mode)
        if source is not None:
            _setter("source", source)
        if uid is not None:
            _setter("uid", uid)

    @property
    @pulumi.getter(name="targetFile")
    def target_file(self) -> str:
        return pulumi.get(self, "target_file")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> Optional[bool]:
        return pulumi.get(self, "create_directories")

    @property
    @pulumi.getter
    def gid(self) -> Optional[int]:
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def uid(self) -> Optional[int]:
        return pulumi.get(self, "uid")


@pulumi.output_type
class ProfileDevice(dict):
    def __init__(__self__, *,
                 name: str,
                 properties: Mapping[str, Any],
                 type: str):
        ProfileDevice._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            properties=properties,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: str,
             properties: Mapping[str, Any],
             type: str,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):

        _setter("name", name)
        _setter("properties", properties)
        _setter("type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Mapping[str, Any]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


