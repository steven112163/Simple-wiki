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
                        <template v-else>
                            <b-img fluid rounded src="https://img.icons8.com/color/480/000000/image.png" alt=""></b-img>
                        </template>
                    </b-col>
                    <b-col cols="8">
                        <table class="table table-hover">
                            <tbody>
                            <tr>
                                <th scope="row">Name</th>
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
                                                v-model="mob.image"
                                                accept="image/*"
                                                @change="onFileChange"
                                                placeholder="Choose a file or drop it here"
                                                drop-placeholder="Drop file here"
                                        ></b-form-file>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Health Points</th>
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
                                <th scope="row">Height</th>
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
                                <th scope="row">Width</th>
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
                                                        placeholder="Enter new behavior"
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
                                <th scope="row">Spawn</th>
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
    import {BIcon, BIconPlus} from 'bootstrap-vue';

    export default {
        name: "mobAdd",
        head() {
            return {
                title: "Wiki | Mob Addition"
            }
        },
        layout: 'wiki',
        middleware: 'auth',
        components: {
            notification,
            BIcon,
            BIconPlus
        },
        async asyncData({$axios, params}) {
            try {
                let behaviors = await $axios.$get(`/mobBehaviors/`);
                let options = [{value: null, text: 'Please select a behavior'}];
                for (let b of behaviors.results) {
                    options.push({value: b.id, text: b.name});
                }

                return {
                    mob: {
                        name: "",
                        image: null,
                        health_points: "",
                        height: "",
                        width: "",
                        behavior: null,
                        attack_strength: "",
                        spawn: ""
                    },
                    preview: false,
                    error: null,
                    show: true,
                    options: options,
                    newBehavior: false
                }
            } catch (e) {
                return {
                    mob: {
                        name: "",
                        image: null,
                        health_points: "",
                        height: "",
                        width: "",
                        behavior: null,
                        attack_strength: "",
                        spawn: ""
                    },
                    preview: false,
                    error: null,
                    show: true,
                    options: [],
                    newBehavior: false
                }
            }
        },
        data() {
            return {
                mob: {
                    name: "",
                    image: null,
                    health_points: "",
                    height: "",
                    width: "",
                    behavior: null,
                    attack_strength: "",
                    spawn: ""
                },
                preview: false,
                error: null,
                show: true,
                options: [],
                newBehavior: false
            };
        },
        methods: {
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length) {
                    return;
                }
                this.mob.image = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                let reader = new FileReader();
                let vm = this;
                reader.onload = e => {
                    vm.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },
            addBehavior(event) {
                this.newBehavior = this.newBehavior ? false : true;
            },
            async onSubmit(event) {
                // TODO
            },
            onReset(event) {
                this.mob.name = "";
                this.mob.image = "";
                this.mob.health_points = "";
                this.mob.height = "";
                this.mob.width = "";
                this.mob.behavior = null;
                this.mob.attack_strength = "";
                this.mob.spawn = "";
                this.preview = false;
                this.error = null;
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
