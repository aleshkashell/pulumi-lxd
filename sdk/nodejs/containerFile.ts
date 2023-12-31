// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class ContainerFile extends pulumi.CustomResource {
    /**
     * Get an existing ContainerFile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ContainerFileState, opts?: pulumi.CustomResourceOptions): ContainerFile {
        return new ContainerFile(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'lxd:index/containerFile:ContainerFile';

    /**
     * Returns true if the given object is an instance of ContainerFile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContainerFile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContainerFile.__pulumiType;
    }

    public readonly append!: pulumi.Output<boolean | undefined>;
    public readonly containerName!: pulumi.Output<string>;
    public readonly content!: pulumi.Output<string | undefined>;
    public readonly createDirectories!: pulumi.Output<boolean | undefined>;
    public readonly gid!: pulumi.Output<number | undefined>;
    public readonly mode!: pulumi.Output<string | undefined>;
    public readonly project!: pulumi.Output<string | undefined>;
    public readonly remote!: pulumi.Output<string | undefined>;
    public readonly source!: pulumi.Output<string | undefined>;
    public readonly targetFile!: pulumi.Output<string>;
    public readonly uid!: pulumi.Output<number | undefined>;

    /**
     * Create a ContainerFile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContainerFileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ContainerFileArgs | ContainerFileState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ContainerFileState | undefined;
            resourceInputs["append"] = state ? state.append : undefined;
            resourceInputs["containerName"] = state ? state.containerName : undefined;
            resourceInputs["content"] = state ? state.content : undefined;
            resourceInputs["createDirectories"] = state ? state.createDirectories : undefined;
            resourceInputs["gid"] = state ? state.gid : undefined;
            resourceInputs["mode"] = state ? state.mode : undefined;
            resourceInputs["project"] = state ? state.project : undefined;
            resourceInputs["remote"] = state ? state.remote : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["targetFile"] = state ? state.targetFile : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as ContainerFileArgs | undefined;
            if ((!args || args.containerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'containerName'");
            }
            if ((!args || args.targetFile === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetFile'");
            }
            resourceInputs["append"] = args ? args.append : undefined;
            resourceInputs["containerName"] = args ? args.containerName : undefined;
            resourceInputs["content"] = args ? args.content : undefined;
            resourceInputs["createDirectories"] = args ? args.createDirectories : undefined;
            resourceInputs["gid"] = args ? args.gid : undefined;
            resourceInputs["mode"] = args ? args.mode : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["remote"] = args ? args.remote : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["targetFile"] = args ? args.targetFile : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ContainerFile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ContainerFile resources.
 */
export interface ContainerFileState {
    append?: pulumi.Input<boolean>;
    containerName?: pulumi.Input<string>;
    content?: pulumi.Input<string>;
    createDirectories?: pulumi.Input<boolean>;
    gid?: pulumi.Input<number>;
    mode?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    targetFile?: pulumi.Input<string>;
    uid?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a ContainerFile resource.
 */
export interface ContainerFileArgs {
    append?: pulumi.Input<boolean>;
    containerName: pulumi.Input<string>;
    content?: pulumi.Input<string>;
    createDirectories?: pulumi.Input<boolean>;
    gid?: pulumi.Input<number>;
    mode?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    targetFile: pulumi.Input<string>;
    uid?: pulumi.Input<number>;
}
