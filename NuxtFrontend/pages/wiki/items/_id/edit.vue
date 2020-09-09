<template>
    <b-container class="my-5">
        <b-row>
            <notification :error="error" v-if="error"></notification>
        </b-row>
        <b-row class="text-right my-3">
            <b-col>
                <nuxt-link is="b-button" to="/wiki/items" variant="danger">Cancel</nuxt-link>
            </b-col>
        </b-row>
        <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
            <b-container>
                <b-form-row>
                    <b-col cols="4">
                        <h1>{{ item.name }}</h1>
                    </b-col>
                    <b-col cols="8"></b-col>
                </b-form-row>
                <hr/>
                <b-form-row>
                    <b-col class="text-center" cols="4">
                        <template v-if="preview">
                            <b-img fluid rounded :src="preview" alt=""></b-img>
                        </template>
                        <template v-else-if="item.image">
                            <b-img fluid rounded :src="item.image" alt=""></b-img>
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
                                                v-model="item.name"
                                                placeholder="Name of the item"
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
                                <th scope="row">Material</th>
                                <td>
                                    <b-form-row>
                                        <b-col>
                                            <b-form-group>
                                                <b-form-select v-model="item.material" :options="materialOptions"
                                                               v-if="!newMaterial"></b-form-select>
                                                <b-form-input
                                                        id="material-input"
                                                        v-model="item.material"
                                                        placeholder="Enter new material name"
                                                        v-else
                                                ></b-form-input>
                                            </b-form-group>
                                        </b-col>
                                        <b-col cols="2">
                                            <b-button variant="primary" @click="addMaterial">
                                                <b-icon icon="plus" variant="white"></b-icon>
                                            </b-button>
                                        </b-col>
                                    </b-form-row>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Type</th>
                                <td>
                                    <b-form-row>
                                        <b-col>
                                            <b-form-group>
                                                <b-form-select v-model="item.type" :options="typeOptions"
                                                               v-if="!newType"></b-form-select>
                                                <b-form-input
                                                        id="type-input"
                                                        v-model="item.type"
                                                        placeholder="Enter new type name"
                                                        v-else
                                                ></b-form-input>
                                            </b-form-group>
                                        </b-col>
                                        <b-col cols="2">
                                            <b-button variant="primary" @click="addType">
                                                <b-icon icon="plus" variant="white"></b-icon>
                                            </b-button>
                                        </b-col>
                                    </b-form-row>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Durability
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="durability-input"
                                                v-model="item.durability"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
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
                                                v-model="item.stackable">
                                            <span v-if="item.stackable" style="color: #28a745">is stackable</span>
                                            <span v-else style="color: #dc3545">not stackable</span>
                                        </b-form-checkbox>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">
                                    Renewable
                                    <b-icon icon="asterisk" variant="danger" font-scale="0.5" shift-v="16"></b-icon>
                                </th>
                                <td>
                                    <b-form-group>
                                        <b-form-checkbox
                                                id="renewable-input"
                                                v-model="item.renewable">
                                            <span v-if="item.renewable" style="color: #28a745">is renewable</span>
                                            <span v-else style="color: #dc3545">not renewable</span>
                                        </b-form-checkbox>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Attack Damage</th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="attack-damage-input"
                                                v-model="item.attack_damage"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Attack Speed</th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="attack-speed-input"
                                                v-model="item.attack_speed"
                                                type="number"
                                                placeholder="eg. 10.0"
                                        ></b-form-input>
                                    </b-form-group>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Defense Points</th>
                                <td>
                                    <b-form-group>
                                        <b-form-input
                                                id="defense-points-input"
                                                v-model="item.defense_points"
                                                type="number"
                                                placeholder="eg. 10"
                                        ></b-form-input>
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
        name: "itemEdit",
        head() {
            return {
                title: "Wiki | Item Edition"
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
                // Get item materials and types, then setup options for them
                let materials = await $axios.$get(`/itemMaterials/`);
                let types = await $axios.$get(`/itemTypes/`);
                let materialOptions = [{value: null, text: 'Please select a material'}];
                let typeOptions = [{value: null, text: 'Please select a type'}];
                for (let m of materials.results) {
                    materialOptions.push({value: m.id, text: m.name});
                }
                for (let t of types.results) {
                    typeOptions.push({value: t.id, text: t.name});
                }

                let item = await $axios.$get(`/items/${params.id}/`);

                return {
                    item: item,
                    originalItem: Object.assign({}, item),
                    preview: false,
                    error: null,
                    show: true,
                    materialOptions: materialOptions,
                    typeOptions: typeOptions,
                    newMaterial: false,
                    newType: false,
                    newImage: null
                }
            } catch (e) {
                return {
                    item: {
                        name: "",
                        image: null,
                        material: null,
                        type: null,
                        durability: null,
                        stackable: false,
                        renewable: false,
                        attack_damage: null,
                        attack_speed: null,
                        defense_points: null
                    },
                    originalItem: {
                        name: "",
                        image: null,
                        material: null,
                        type: null,
                        durability: null,
                        stackable: false,
                        renewable: false,
                        attack_damage: null,
                        attack_speed: null,
                        defense_points: null
                    },
                    preview: false,
                    error: null,
                    show: true,
                    materialOptions: [{value: null, text: 'Please select a material'}],
                    typeOptions: [{value: null, text: 'Please select a type'}],
                    newMaterial: false,
                    newType: false,
                    newImage: null
                }
            }
        },
        data() {
            return {
                item: {
                    name: "",
                    image: null,
                    material: null,
                    type: null,
                    durability: null,
                    stackable: false,
                    renewable: false,
                    attack_damage: null,
                    attack_speed: null,
                    defense_points: null
                },
                originalItem: {
                    name: "",
                    image: null,
                    material: null,
                    type: null,
                    durability: null,
                    stackable: false,
                    renewable: false,
                    attack_damage: null,
                    attack_speed: null,
                    defense_points: null
                },
                preview: false,
                error: null,
                show: true,
                materialOptions: [{value: null, text: 'Please select a material'}],
                typeOptions: [{value: null, text: 'Please select a type'}],
                newMaterial: false,
                newType: false,
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
            addMaterial(event) {
                this.newMaterial = this.newMaterial ? false : true;
                this.item.material = null;
            },
            addType(event) {
                this.newType = this.newType ? false : true;
                this.item.type = null;
            },
            async onSubmit(event) {
                try {
                    // Create new material if newMaterial is true
                    if (this.newMaterial) {
                        let res = await this.$axios.$post(`/itemMaterials/`, {name: this.item.material});
                        this.item.material = res.id;
                    }

                    // Create new type if newType is true
                    if (this.newType) {
                        let res = await this.$axios.$post(`/itemTypes/`, {name: this.item.type});
                        this.item.type = res.id;
                    }

                    // Delete image from item object if image wasn't changed
                    if (this.item.image.indexOf("http://") != -1 && !this.newImage)
                        delete this.item["image"];
                    else
                        this.item.image = this.preview;

                    // Create new item
                    await this.$axios.$patch(`/items/${this.item.id}/`, this.item);
                    await this.$router.replace('/wiki/items');
                } catch (e) {
                    this.error = e.response.data;
                }
            },
            onReset(event) {
                for (let key in this.item)
                    this.item[key] = this.originalItem[key];
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
