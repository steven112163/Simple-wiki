<template>
    <b-container class="my-5">
        <b-row>
            <notification :error="error" v-if="error"></notification>
        </b-row>
        <b-row class="text-right my-3">
            <b-col>
                <nuxt-link is="b-button" to="/wiki/blocks" variant="danger">Cancel</nuxt-link>
            </b-col>
        </b-row>
        <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show" enctype="multipart/form-data">
            <b-container>
                <b-form-row>
                    <b-col cols="4">
                        <h1>{{ block.name }}</h1>
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
                                <th scope="row">
                                    Name
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="name-input"
                                                v-model="block.name"
                                                placeholder="Name of the block"
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
                                                v-model="block.image"
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
                                    Stackable
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-checkbox
                                                id="stackable-input"
                                                v-model="block.stackable">
                                            <span v-if="block.stackable" style="color: #28a745">is stackable</span>
                                            <span v-else style="color: #dc3545">not stackable</span>
                                        </b-form-checkbox>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Flammable
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-checkbox
                                                id="flammable-input"
                                                v-model="block.flammable">
                                            <span v-if="block.flammable" style="color: #28a745">is flammable</span>
                                            <span v-else style="color: #dc3545">not flammable</span>
                                        </b-form-checkbox>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Transparent
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-checkbox
                                                id="transparent-input"
                                                v-model="block.transparent">
                                            <span v-if="block.transparent" style="color: #28a745">is transparent</span>
                                            <span v-else style="color: #dc3545">not transparent</span>
                                        </b-form-checkbox>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Texture</th>
                                <td>
                                    <b-form-row>
                                        <b-col>
                                            <b-form-group>
                                                <b-form-select v-model="block.texture" :options="textureOptions"
                                                               v-if="!newTexture"></b-form-select>
                                                <b-form-input
                                                        id="texture-input"
                                                        v-model="block.texture"
                                                        placeholder="Enter new texture name"
                                                        v-else
                                                ></b-form-input>
                                            </b-form-group>
                                        </b-col>
                                        <b-col cols="2">
                                            <b-button variant="primary" @click="addTexture">
                                                <b-icon icon="plus" variant="white"></b-icon>
                                            </b-button>
                                        </b-col>
                                    </b-form-row>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Luminant
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="luminant-input"
                                                v-model="block.luminant"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Tools</th>
                                <td>
                                    <b-form-row>
                                        <b-col>
                                            <b-form-group>
                                                <b-form-select v-model="block.tool" :options="toolOptions"
                                                               multiple></b-form-select>
                                                <b-form-text>You can select multiple tools</b-form-text>
                                            </b-form-group>
                                        </b-col>
                                    </b-form-row>
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
        name: "blockAdd",
        head() {
            return {
                title: "Wiki | Block Addition"
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
                let tools = await $axios.$get(`/items/`);
                let toolOptions = [];
                for (let t of tools.results)
                    toolOptions.push({value: t.id, text: t.name});

                let textures = await $axios.$get(`/blockTextures/`);
                let textureOptions = [{value: null, text: 'Please select a texture'}];
                for (let t of textures.results)
                    textureOptions.push({value: t.id, text: t.name});

                return {
                    block: {
                        name: "",
                        image: null,
                        stackable: false,
                        flammable: false,
                        transparent: false,
                        luminant: null,
                        tool: [],
                        texture: null
                    },
                    preview: false,
                    error: null,
                    show: true,
                    toolOptions: toolOptions,
                    textureOptions: textureOptions,
                    newTexture: false
                }
            } catch (e) {
                return {
                    block: {
                        name: "",
                        image: null,
                        stackable: false,
                        flammable: false,
                        transparent: false,
                        luminant: null,
                        tool: [],
                        texture: null
                    },
                    preview: false,
                    error: null,
                    show: true,
                    toolOptions: [],
                    textureOptions: [{value: null, text: 'Please select a texture'}],
                    newTexture: false
                }
            }
        },
        data() {
            return {
                block: {
                    name: "",
                    image: null,
                    stackable: false,
                    flammable: false,
                    transparent: false,
                    luminant: null,
                    tool: [],
                    texture: null
                },
                preview: false,
                error: null,
                show: true,
                toolOptions: [],
                textureOptions: [{value: null, text: 'Please select a texture'}],
                newTexture: false
            };
        },
        methods: {
            onFileChange(e) {
                let files = e.target.files || e.dataTransfer.files;
                if (!files.length)
                    return;
                this.block.image = files[0];
                this.createImage(files[0]);
            },
            createImage(file) {
                let reader = new FileReader();
                reader.onload = e => {
                    this.preview = e.target.result;
                };
                reader.readAsDataURL(file);
            },
            addTexture(event) {
                this.newTexture = this.newTexture ? false : true;
                this.block.texture = null;
            },
            async onSubmit(event) {
                try {
                    // Create new texture if newTexture is true
                    if (this.newTexture) {
                        let res = await this.$axios.$post(`/blockTextures/`, {name: this.block.texture});
                        this.block.texture = res.id;
                    }

                    // Create new mob
                    this.block.image = this.preview;
                    await this.$axios.$post(`/blocks/`, this.block);
                    await this.$router.replace('/wiki/blocks');
                } catch (e) {
                    this.error = e.response.data;
                }
            },
            onReset(event) {
                this.block.name = "";
                this.block.image = null;
                this.block.stackable = false;
                this.block.flammable = false;
                this.block.transparent = false;
                this.block.luminant = null;
                this.block.tool = [];
                this.block.texture = null;
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
