<template>
    <b-container class="my-5">
        <b-row>
            <notification :error="error" v-if="error"></notification>
        </b-row>
        <b-row class="text-right my-3">
            <b-col>
                <nuxt-link is="b-button" to="/wiki/mobs" variant="danger">Cancel</nuxt-link>
            </b-col>
        </b-row>
        <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
            <b-container>
                <b-form-row>
                    <b-col cols="4">
                        <h1>{{ mob.name }}</h1>
                    </b-col>
                    <b-col cols="8"></b-col>
                </b-form-row>
                <hr/>
                <b-form-row>
                    <b-col class="text-center" cols="4">
                        <template v-if="preview">
                            <b-img fluid rounded :src="preview" alt=""></b-img>
                        </template>
                        <template v-else-if="mob.image">
                            <b-img fluid rounded :src="mob.image" alt=""></b-img>
                        </template>
                        <template v-else>
                            <b-img fluid rounded src="https://img.icons8.com/color/480/000000/image.png" alt=""></b-img>
                        </template>
                    </b-col>
                    <b-col cols="8">
                        <table class="table table-hover">
                            <tbody>
                            <tr>
                                <th scope="row">
                                    Name
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="name-input"
                                                v-model="mob.name"
                                                placeholder="Name of the mob"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Image</th>
                                <td>
                                    <b-form-group>
                                        <b-form-file
                                                id="image-file"
                                                v-model="newImage"
                                                accept="image/jpeg, image/png, image/gif"
                                                @change="onFileChange"
                                                placeholder="Choose a file or drop it here"
                                                drop-placeholder="Drop file here"
                                        ></b-form-file>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Health Points
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="health-input"
                                                v-model="mob.health_points"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Height
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="height-input"
                                                v-model="mob.height"
                                                type="number"
                                                placeholder="eg. 10.0"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Width
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="width-input"
                                                v-model="mob.width"
                                                type="number"
                                                placeholder="eg. 10.0"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Behavior</th>
                                <td>
                                    <b-form-row>
                                        <b-col>
                                            <b-form-group>
                                                <b-form-select v-model="mob.behavior" :options="options"
                                                               v-if="!newBehavior"></b-form-select>
                                                <b-form-input
                                                        id="behavior-input"
                                                        v-model="mob.behavior"
                                                        placeholder="Enter new behavior name"
                                                        v-else
                                                ></b-form-input>
                                            </b-form-group>
                                        </b-col>
                                        <b-col cols="2">
                                            <b-button variant="primary" @click="addBehavior">
                                                <b-icon icon="plus" variant="white"></b-icon>
                                            </b-button>
                                        </b-col>
                                    </b-form-row>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Attack Strength</th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="attack-input"
                                                v-model="mob.attack_strength"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Spawn
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-textarea
                                                id="spawn-input"
                                                v-model="mob.spawn"
                                                placeholder="Text about mob spawning"
                                                rows="3"
                                                max-rows="5"
                                        ></b-form-textarea>
                                    </b-form-group>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </b-col>
                </b-form-row>
                <b-form-row class="text-right">
                    <b-col>
                        <b-button type="submit" variant="success">Submit</b-button>
                        <b-button type="reset" variant="secondary">Reset</b-button>
                    </b-col>
                </b-form-row>
            </b-container>
        </b-form>
    </b-container>
</template>

<script>
    import notification from "@/components/common/notification";
    import {BIcon, BIconPlus, BIconAsterisk} from 'bootstrap-vue';

    export default {
        name: "mobEdit",
        head() {
            return {
                title: "Wiki | Mob Edition"
            }
        },
        layout: 'wiki',
        middleware: 'auth',
        components: {
            notification,
            BIcon,
            BIconPlus,
            BIconAsterisk
        },
        async asyncData({$axios, params}) {
            try {
                // Get mob behaviors and setup options
                let behaviors = await $axios.$get(`/mobBehaviors/`);
                let options = [{value: null, text: 'Please select a behavior'}];
                for (let b of behaviors.results) {
                    options.push({value: b.id, text: b.name});
                }

                let mob = await $axios.$get(`/mobs/${params.id}/`);

                return {
                    mob: mob,
                    originalMob: Object.assign({}, mob),
                    preview: false,
                    error: null,
                    show: true,
                    options: options,
                    newBehavior: false,
                    newImage: null
                }
            } catch (e) {
                return {
                    mob: {
                        name: "",
                        image: null,
                        health_points: null,
                        height: null,
                        width: null,
                        behavior: null,
                        attack_strength: null,
                        spawn: ""
                    },
                    originalMob: {
                        name: "",
                        image: null,
                        health_points: null,
                        height: null,
                        width: null,
                        behavior: null,
                        attack_strength: null,
                        spawn: ""
                    },
                    preview: false,
                    error: null,
                    show: true,
                    options: [{value: null, text: 'Please select a behavior'}],
                    newBehavior: false,
                    newImage: null
                }
            }
        },
        data() {
            return {
                mob: {
                    name: "",
                    image: null,
                    health_points: null,
                    height: null,
                    width: null,
                    behavior: null,
                    attack_strength: null,
                    spawn: ""
                },
                originalMob: {
                    name: "",
                    image: null,
                    health_points: null,
                    height: null,
                    width: null,
                    behavior: null,
                    attack_strength: null,
                    spawn: ""
                },
                preview: false,
                error: null,
                show: true,
                options: [{value: null, text: 'Please select a behavior'}],
                newBehavior: false,
                newImage: null
            };
        },
        methods: {
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length)
                    return;
                this.newImage = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                let reader = new FileReader();
                reader.onload = e => {
                    this.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },
            addBehavior(event) {
                this.newBehavior = this.newBehavior ? false : true;
                this.mob.behavior = null;
            },
            async onSubmit(event) {
                try {
                    // Create new behavior if newBehavior is true
                    if (this.newBehavior) {
                        let res = await this.$axios.$post(`/mobBehaviors/`, {name: this.mob.behavior});
                        this.mob.behavior = res.id;
                    }

                    // Delete image from mob object if image wasn't changed
                    if (this.mob.image.indexOf("http://") != -1 && !this.newImage)
                        delete this.mob["image"];
                    else
                        this.mob.image = this.preview;

                    // Create new mob
                    await this.$axios.$patch(`/mobs/${this.mob.id}/`, this.mob);
                    await this.$router.replace(`/wiki/mobs`);
                } catch (e) {
                    this.error = e.response.data;
                }
            },
            onReset(event) {
                for (let key in this.mob)
                    this.mob[key] = this.originalMob[key];
                this.preview = false;
                this.error = null;
                this.newImage = null;
                this.show = false;
                this.$nextTick(() => {
                    this.show = true;
                });
            }
        }
    }
</script>

<style scoped>

</style>
