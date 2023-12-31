// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { CachedImageArgs, CachedImageState } from "./cachedImage";
export type CachedImage = import("./cachedImage").CachedImage;
export const CachedImage: typeof import("./cachedImage").CachedImage = null as any;
utilities.lazyLoad(exports, ["CachedImage"], () => require("./cachedImage"));

export { ContainerArgs, ContainerState } from "./container";
export type Container = import("./container").Container;
export const Container: typeof import("./container").Container = null as any;
utilities.lazyLoad(exports, ["Container"], () => require("./container"));

export { ContainerFileArgs, ContainerFileState } from "./containerFile";
export type ContainerFile = import("./containerFile").ContainerFile;
export const ContainerFile: typeof import("./containerFile").ContainerFile = null as any;
utilities.lazyLoad(exports, ["ContainerFile"], () => require("./containerFile"));

export { InstanceArgs, InstanceState } from "./instance";
export type Instance = import("./instance").Instance;
export const Instance: typeof import("./instance").Instance = null as any;
utilities.lazyLoad(exports, ["Instance"], () => require("./instance"));

export { InstanceFileArgs, InstanceFileState } from "./instanceFile";
export type InstanceFile = import("./instanceFile").InstanceFile;
export const InstanceFile: typeof import("./instanceFile").InstanceFile = null as any;
utilities.lazyLoad(exports, ["InstanceFile"], () => require("./instanceFile"));

export { NetworkArgs, NetworkState } from "./network";
export type Network = import("./network").Network;
export const Network: typeof import("./network").Network = null as any;
utilities.lazyLoad(exports, ["Network"], () => require("./network"));

export { ProfileArgs, ProfileState } from "./profile";
export type Profile = import("./profile").Profile;
export const Profile: typeof import("./profile").Profile = null as any;
utilities.lazyLoad(exports, ["Profile"], () => require("./profile"));

export { ProjectArgs, ProjectState } from "./project";
export type Project = import("./project").Project;
export const Project: typeof import("./project").Project = null as any;
utilities.lazyLoad(exports, ["Project"], () => require("./project"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { PublishImageArgs, PublishImageState } from "./publishImage";
export type PublishImage = import("./publishImage").PublishImage;
export const PublishImage: typeof import("./publishImage").PublishImage = null as any;
utilities.lazyLoad(exports, ["PublishImage"], () => require("./publishImage"));

export { SnapshotArgs, SnapshotState } from "./snapshot";
export type Snapshot = import("./snapshot").Snapshot;
export const Snapshot: typeof import("./snapshot").Snapshot = null as any;
utilities.lazyLoad(exports, ["Snapshot"], () => require("./snapshot"));

export { StoragePoolArgs, StoragePoolState } from "./storagePool";
export type StoragePool = import("./storagePool").StoragePool;
export const StoragePool: typeof import("./storagePool").StoragePool = null as any;
utilities.lazyLoad(exports, ["StoragePool"], () => require("./storagePool"));

export { VolumeArgs, VolumeState } from "./volume";
export type Volume = import("./volume").Volume;
export const Volume: typeof import("./volume").Volume = null as any;
utilities.lazyLoad(exports, ["Volume"], () => require("./volume"));

export { VolumeContainerAttachArgs, VolumeContainerAttachState } from "./volumeContainerAttach";
export type VolumeContainerAttach = import("./volumeContainerAttach").VolumeContainerAttach;
export const VolumeContainerAttach: typeof import("./volumeContainerAttach").VolumeContainerAttach = null as any;
utilities.lazyLoad(exports, ["VolumeContainerAttach"], () => require("./volumeContainerAttach"));

export { VolumeCopyArgs, VolumeCopyState } from "./volumeCopy";
export type VolumeCopy = import("./volumeCopy").VolumeCopy;
export const VolumeCopy: typeof import("./volumeCopy").VolumeCopy = null as any;
utilities.lazyLoad(exports, ["VolumeCopy"], () => require("./volumeCopy"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "lxd:index/cachedImage:CachedImage":
                return new CachedImage(name, <any>undefined, { urn })
            case "lxd:index/container:Container":
                return new Container(name, <any>undefined, { urn })
            case "lxd:index/containerFile:ContainerFile":
                return new ContainerFile(name, <any>undefined, { urn })
            case "lxd:index/instance:Instance":
                return new Instance(name, <any>undefined, { urn })
            case "lxd:index/instanceFile:InstanceFile":
                return new InstanceFile(name, <any>undefined, { urn })
            case "lxd:index/network:Network":
                return new Network(name, <any>undefined, { urn })
            case "lxd:index/profile:Profile":
                return new Profile(name, <any>undefined, { urn })
            case "lxd:index/project:Project":
                return new Project(name, <any>undefined, { urn })
            case "lxd:index/publishImage:PublishImage":
                return new PublishImage(name, <any>undefined, { urn })
            case "lxd:index/snapshot:Snapshot":
                return new Snapshot(name, <any>undefined, { urn })
            case "lxd:index/storagePool:StoragePool":
                return new StoragePool(name, <any>undefined, { urn })
            case "lxd:index/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            case "lxd:index/volumeContainerAttach:VolumeContainerAttach":
                return new VolumeContainerAttach(name, <any>undefined, { urn })
            case "lxd:index/volumeCopy:VolumeCopy":
                return new VolumeCopy(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("lxd", "index/cachedImage", _module)
pulumi.runtime.registerResourceModule("lxd", "index/container", _module)
pulumi.runtime.registerResourceModule("lxd", "index/containerFile", _module)
pulumi.runtime.registerResourceModule("lxd", "index/instance", _module)
pulumi.runtime.registerResourceModule("lxd", "index/instanceFile", _module)
pulumi.runtime.registerResourceModule("lxd", "index/network", _module)
pulumi.runtime.registerResourceModule("lxd", "index/profile", _module)
pulumi.runtime.registerResourceModule("lxd", "index/project", _module)
pulumi.runtime.registerResourceModule("lxd", "index/publishImage", _module)
pulumi.runtime.registerResourceModule("lxd", "index/snapshot", _module)
pulumi.runtime.registerResourceModule("lxd", "index/storagePool", _module)
pulumi.runtime.registerResourceModule("lxd", "index/volume", _module)
pulumi.runtime.registerResourceModule("lxd", "index/volumeContainerAttach", _module)
pulumi.runtime.registerResourceModule("lxd", "index/volumeCopy", _module)
pulumi.runtime.registerResourcePackage("lxd", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:lxd") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
