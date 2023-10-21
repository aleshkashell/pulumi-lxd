// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class InstanceFile extends pulumi.CustomResource {
    /**
     * Get an existing InstanceFile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceFileState, opts?: pulumi.CustomResourceOptions): InstanceFile {
        return new InstanceFile(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'lxd:index/instanceFile:InstanceFile';

    /**
     * Returns true if the given object is an instance of InstanceFile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is InstanceFile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === InstanceFile.__pulumiType;
    }

    public readonly append!: pulumi.Output<boolean | undefined>;
    public readonly content!: pulumi.Output<string | undefined>;
    public readonly createDirectories!: pulumi.Output<boolean | undefined>;
    public readonly gid!: pulumi.Output<number | undefined>;
    public readonly instanceName!: pulumi.Output<string>;
    public readonly mode!: pulumi.Output<string | undefined>;
    public readonly project!: pulumi.Output<string | undefined>;
    public readonly remote!: pulumi.Output<string | undefined>;
    public readonly source!: pulumi.Output<string | undefined>;
    public readonly targetFile!: pulumi.Output<string>;
    public readonly uid!: pulumi.Output<number | undefined>;

    /**
     * Create a InstanceFile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceFileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceFileArgs | InstanceFileState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as InstanceFileState | undefined;
            resourceInputs["append"] = state ? state.append : undefined;
            resourceInputs["content"] = state ? state.content : undefined;
            resourceInputs["createDirectories"] = state ? state.createDirectories : undefined;
            resourceInputs["gid"] = state ? state.gid : undefined;
            resourceInputs["instanceName"] = state ? state.instanceName : undefined;
            resourceInputs["mode"] = state ? state.mode : undefined;
            resourceInputs["project"] = state ? state.project : undefined;
            resourceInputs["remote"] = state ? state.remote : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["targetFile"] = state ? state.targetFile : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as InstanceFileArgs | undefined;
            if ((!args || args.instanceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceName'");
            }
            if ((!args || args.targetFile === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targetFile'");
            }
            resourceInputs["append"] = args ? args.append : undefined;
            resourceInputs["content"] = args ? args.content : undefined;
            resourceInputs["createDirectories"] = args ? args.createDirectories : undefined;
            resourceInputs["gid"] = args ? args.gid : undefined;
            resourceInputs["instanceName"] = args ? args.instanceName : undefined;
            resourceInputs["mode"] = args ? args.mode : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["remote"] = args ? args.remote : undefined;
            resourceInputs["source"] = args ? args.source : undefined;
            resourceInputs["targetFile"] = args ? args.targetFile : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(InstanceFile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering InstanceFile resources.
 */
export interface InstanceFileState {
    append?: pulumi.Input<boolean>;
    content?: pulumi.Input<string>;
    createDirectories?: pulumi.Input<boolean>;
    gid?: pulumi.Input<number>;
    instanceName?: pulumi.Input<string>;
    mode?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    targetFile?: pulumi.Input<string>;
    uid?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a InstanceFile resource.
 */
export interface InstanceFileArgs {
    append?: pulumi.Input<boolean>;
    content?: pulumi.Input<string>;
    createDirectories?: pulumi.Input<boolean>;
    gid?: pulumi.Input<number>;
    instanceName: pulumi.Input<string>;
    mode?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    targetFile: pulumi.Input<string>;
    uid?: pulumi.Input<number>;
}