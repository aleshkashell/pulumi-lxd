// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class VolumeCopy extends pulumi.CustomResource {
    /**
     * Get an existing VolumeCopy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeCopyState, opts?: pulumi.CustomResourceOptions): VolumeCopy {
        return new VolumeCopy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'lxd:index/volumeCopy:VolumeCopy';

    /**
     * Returns true if the given object is an instance of VolumeCopy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VolumeCopy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VolumeCopy.__pulumiType;
    }

    public /*out*/ readonly config!: pulumi.Output<{[key: string]: any}>;
    public /*out*/ readonly contentType!: pulumi.Output<string>;
    public /*out*/ readonly expandedConfig!: pulumi.Output<{[key: string]: any}>;
    public /*out*/ readonly location!: pulumi.Output<string>;
    /**
     * The name of the destination volume.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The destination pool.
     */
    public readonly pool!: pulumi.Output<string>;
    /**
     * The destination remote.
     */
    public readonly remote!: pulumi.Output<string | undefined>;
    /**
     * The name of the source volume.
     */
    public readonly sourceName!: pulumi.Output<string>;
    /**
     * The source pool.
     */
    public readonly sourcePool!: pulumi.Output<string>;
    /**
     * The remote from which the source volume is copied.
     */
    public readonly sourceRemote!: pulumi.Output<string | undefined>;
    public readonly target!: pulumi.Output<string | undefined>;

    /**
     * Create a VolumeCopy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeCopyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeCopyArgs | VolumeCopyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VolumeCopyState | undefined;
            resourceInputs["config"] = state ? state.config : undefined;
            resourceInputs["contentType"] = state ? state.contentType : undefined;
            resourceInputs["expandedConfig"] = state ? state.expandedConfig : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["pool"] = state ? state.pool : undefined;
            resourceInputs["remote"] = state ? state.remote : undefined;
            resourceInputs["sourceName"] = state ? state.sourceName : undefined;
            resourceInputs["sourcePool"] = state ? state.sourcePool : undefined;
            resourceInputs["sourceRemote"] = state ? state.sourceRemote : undefined;
            resourceInputs["target"] = state ? state.target : undefined;
        } else {
            const args = argsOrState as VolumeCopyArgs | undefined;
            if ((!args || args.pool === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pool'");
            }
            if ((!args || args.sourceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceName'");
            }
            if ((!args || args.sourcePool === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourcePool'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pool"] = args ? args.pool : undefined;
            resourceInputs["remote"] = args ? args.remote : undefined;
            resourceInputs["sourceName"] = args ? args.sourceName : undefined;
            resourceInputs["sourcePool"] = args ? args.sourcePool : undefined;
            resourceInputs["sourceRemote"] = args ? args.sourceRemote : undefined;
            resourceInputs["target"] = args ? args.target : undefined;
            resourceInputs["config"] = undefined /*out*/;
            resourceInputs["contentType"] = undefined /*out*/;
            resourceInputs["expandedConfig"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(VolumeCopy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VolumeCopy resources.
 */
export interface VolumeCopyState {
    config?: pulumi.Input<{[key: string]: any}>;
    contentType?: pulumi.Input<string>;
    expandedConfig?: pulumi.Input<{[key: string]: any}>;
    location?: pulumi.Input<string>;
    /**
     * The name of the destination volume.
     */
    name?: pulumi.Input<string>;
    /**
     * The destination pool.
     */
    pool?: pulumi.Input<string>;
    /**
     * The destination remote.
     */
    remote?: pulumi.Input<string>;
    /**
     * The name of the source volume.
     */
    sourceName?: pulumi.Input<string>;
    /**
     * The source pool.
     */
    sourcePool?: pulumi.Input<string>;
    /**
     * The remote from which the source volume is copied.
     */
    sourceRemote?: pulumi.Input<string>;
    target?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VolumeCopy resource.
 */
export interface VolumeCopyArgs {
    /**
     * The name of the destination volume.
     */
    name?: pulumi.Input<string>;
    /**
     * The destination pool.
     */
    pool: pulumi.Input<string>;
    /**
     * The destination remote.
     */
    remote?: pulumi.Input<string>;
    /**
     * The name of the source volume.
     */
    sourceName: pulumi.Input<string>;
    /**
     * The source pool.
     */
    sourcePool: pulumi.Input<string>;
    /**
     * The remote from which the source volume is copied.
     */
    sourceRemote?: pulumi.Input<string>;
    target?: pulumi.Input<string>;
}
