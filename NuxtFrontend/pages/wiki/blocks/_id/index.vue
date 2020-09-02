<template>
    <b-container class="my-5">
        <b-row class="text-right mb-3">
            <b-col>
                <nuxt-link is="b-button" to="/wiki/blocks" variant="success">Back</nuxt-link>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="4">
                <h1>{{ block.name }}</h1>
            </b-col>
            <b-col class="text-right" cols="8">
                <p class="text-muted">Last Modified Date: {{ block.update }}</p>
            </b-col>
        </b-row>
        <hr/>
        <b-row class="mt-5">
            <b-col class="text-center" cols="4">
                <b-img v-if="block.image" fluid rounded :src="block.image" alt=""></b-img>
                <b-img v-else fluid rounded src="https://img.icons8.com/color/480/000000/image.png" alt=""></b-img>
            </b-col>
            <b-col cols="8">
                <table class="table table-hover">
                    <caption>Details of {{ block.name }}</caption>
                    <tbody>
                    <tr>
                        <th scope="row">Stackable</th>
                        <td>
                            <b-icon v-if="block.stackable" icon="check-square-fill" variant="success"></b-icon>
                            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">flammable</th>
                        <td>
                            <b-icon v-if="block.flammable" icon="check-square-fill" variant="success"></b-icon>
                            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Transparent</th>
                        <td>
                            <b-icon v-if="block.transparent" icon="check-square-fill" variant="success"></b-icon>
                            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
                        </td>
                    </tr>
                    <tr v-if="texture">
                        <th scope="row">Texture</th>
                        <td>{{ texture.name }}</td>
                    </tr>
                    <tr v-if="luminant || half_luminant">
                        <th scope="row">Luminant</th>
                        <td>
                            <template v-for="i in luminant">
                                <b-icon icon="brightness-high-fill" variant="warning"></b-icon>
                            </template>

                            <template v-if="half_luminant">
                                <b-icon icon="brightness-alt-high-fill" variant="warning"></b-icon>
                            </template>
                            <span> ({{ block.luminant }})</span>
                        </td>
                    </tr>
                    <tr v-if="tools.length">
                        <th scope="row">Tools</th>
                        <td>
                            <b-list-group>
                                <template v-for="tool of tools">
                                    <b-list-group-item :to="`/wiki/items/${tool.id}/`">
                                        {{ tool.name }}
                                    </b-list-group-item>
                                </template>
                            </b-list-group>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import {
        BIcon,
        BIconBrightnessHighFill,
        BIconBrightnessAltHighFill,
        BIconCheckSquareFill,
        BIconXSquareFill
    } from "bootstrap-vue";

    export default {
        name: "blockIndex",
        layout: "wiki",
        head() {
            return {
                title: "Wiki | Block Detail"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let block = await $axios.$get(`/blocks/${params.id}`);

                // Parse date
                let idxDot = block.update.indexOf(".");
                let idxT = block.update.indexOf("T");
                block.update = block.update.substring(0, idxT) + " " + block.update.substring(idxT + 1, idxDot);

                // Get number of luminant symbols
                let half_luminant = false;
                let luminant = false;
                if (block.luminant !== null) {
                    half_luminant = (block.luminant % 2) != 0 ? true : false;
                    luminant = half_luminant ? ((block.luminant - 1) / 2) : (block.luminant / 2);
                    if (block.luminant == 1) {
                        half_luminant = true;
                        luminant = 0;
                    }
                }

                // Get tools
                let tools = [];
                if (block.tool !== [])
                    for (let toolID of block.tool) {
                        let tool = await $axios.$get(`/items/${toolID}`);
                        tools.push(tool);
                    }

                // Get texture
                let texture = false;
                if (block.texture !== null)
                    texture = await $axios.$get(`/blockTextures/${block.texture}`);

                return {
                    block: block,
                    tools: tools,
                    texture: texture,
                    half_luminant: half_luminant,
                    luminant: luminant
                };
            } catch (e) {
                return {
                    block: [],
                    tools: [],
                    texture: [],
                    half_luminant: [],
                    luminant: []
                };
            }
        },
        data() {
            return {
                block: [],
                tools: [],
                texture: [],
                half_luminant: [],
                luminant: []
            };
        },
        components: {
            BIcon,
            BIconBrightnessHighFill,
            BIconBrightnessAltHighFill,
            BIconCheckSquareFill,
            BIconXSquareFill
        }
    }
</script>

<style scoped>

</style>