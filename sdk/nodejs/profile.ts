// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Profile extends pulumi.CustomResource {
    /**
     * Get an existing Profile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProfileState, opts?: pulumi.CustomResourceOptions): Profile {
        return new Profile(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'lxd:index/profile:Profile';

    /**
     * Returns true if the given object is an instance of Profile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Profile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Profile.__pulumiType;
    }

    public readonly config!: pulumi.Output<{[key: string]: any} | undefined>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly devices!: pulumi.Output<outputs.ProfileDevice[] | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string | undefined>;
    public readonly remote!: pulumi.Output<string | undefined>;

    /**
     * Create a Profile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProfileArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProfileArgs | ProfileState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProfileState | undefined;
            resourceInputs["config"] = state ? state.config : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["devices"] = state ? state.devices : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["project"] = state ? state.project : undefined;
            resourceInputs["remote"] = state ? state.remote : undefined;
        } else {
            const args = argsOrState as ProfileArgs | undefined;
            resourceInputs["config"] = args ? args.config : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["devices"] = args ? args.devices : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["remote"] = args ? args.remote : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Profile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Profile resources.
 */
export interface ProfileState {
    config?: pulumi.Input<{[key: string]: any}>;
    description?: pulumi.Input<string>;
    devices?: pulumi.Input<pulumi.Input<inputs.ProfileDevice>[]>;
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Profile resource.
 */
export interface ProfileArgs {
    config?: pulumi.Input<{[key: string]: any}>;
    description?: pulumi.Input<string>;
    devices?: pulumi.Input<pulumi.Input<inputs.ProfileDevice>[]>;
    name?: pulumi.Input<string>;
    project?: pulumi.Input<string>;
    remote?: pulumi.Input<string>;
}
