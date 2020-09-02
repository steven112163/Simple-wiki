<template>
    <b-container class="my-5">
        <b-row class="text-right mb-3">
            <b-col>
                <nuxt-link is="b-button" to="/wiki/items" variant="success">Back</nuxt-link>
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="4">
                <h1>{{ item.name }}</h1>
            </b-col>
            <b-col class="text-right" cols="8">
                <p class="text-muted">Last Modified Date: {{ item.update }}</p>
            </b-col>
        </b-row>
        <hr/>
        <b-row class="mt-5">
            <b-col class="text-center" cols="4">
                <b-img v-if="item.image" fluid rounded :src="item.image" alt=""></b-img>
                <b-img v-else fluid rounded src="https://img.icons8.com/color/480/000000/image.png" alt=""></b-img>
            </b-col>
            <b-col cols="8">
                <table class="table table-hover">
                    <caption>Details of {{ item.name }}</caption>
                    <tbody>
                    <tr v-if="material">
                        <th scope="row">Material</th>
                        <td>{{ material.name }}</td>
                    </tr>
                    <tr v-if="type">
                        <th scope="row">Type</th>
                        <td>{{ type.name }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Durability</th>
                        <td>
                            <b-icon icon="battery-full" variant="primary"></b-icon>
                            <span> {{ item.durability }}</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Stackable</th>
                        <td>
                            <b-icon v-if="item.stackable" icon="check-square-fill" variant="success"></b-icon>
                            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Renewable</th>
                        <td>
                            <b-icon v-if="item.renewable" icon="check-square-fill" variant="success"></b-icon>
                            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
                        </td>
                    </tr>
                    <tr v-if="attack || half_attack">
                        <th scope="row">Attack Damage</th>
                        <td>
                            <template v-for="i in attack">
                                <b-icon icon="lightning-fill" variant="warning"></b-icon>
                            </template>
                            <template v-if="half_attack">
                                <b-icon icon="lightning" variant="warning"></b-icon>
                            </template>
                            <span> ({{ item.attack_damage }})</span>
                        </td>
                    </tr>
                    <tr v-if="item.attack_speed">
                        <th scope="row">Attack Speed</th>
                        <td>{{ item.attack_speed }}</td>
                    </tr>
                    <tr v-if="defense || half_defense">
                        <th scope="row">Defense Points</th>
                        <td>
                            <template v-for="i in defense">
                                <b-icon icon="shield-fill" variant="secondary"></b-icon>
                            </template>
                            <template v-if="half_defense">
                                <b-icon icon="shield-shaded" variant="secondary"></b-icon>
                            </template>
                            <span> ({{ item.defense_points }})</span>
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
        BIconLightning,
        BIconLightningFill,
        BIconBatteryFull,
        BIconCheckSquareFill,
        BIconXSquareFill,
        BIconShieldFill,
        BIconShieldShaded,
    } from "bootstrap-vue";

    export default {
        name: "itemIndex",
        layout: "wiki",
        head() {
            return {
                title: "Wiki | Item Detail"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let item = await $axios.$get(`/items/${params.id}`);

                // Parse date
                let idxDot = item.update.indexOf(".");
                let idxT = item.update.indexOf("T");
                item.update = item.update.substring(0, idxT) + " " + item.update.substring(idxT + 1, idxDot);

                // Get number of attack damage symbols
                let half_attack = false;
                let attack = false;
                if (item.attack_damage !== null) {
                    half_attack = (item.attack_damage % 2) != 0 ? true : false;
                    attack = half_attack ? ((item.attack_damage - 1) / 2) : (item.attack_damage / 2);
                    if (item.attack_damage == 1) {
                        half_attack = true;
                        attack = 1;
                    }
                }

                // Get number of defense symbols
                let half_defense = false;
                let defense = false;
                if (item.defense_points !== null) {
                    half_defense = (item.defense_points % 2) != 0 ? true : false;
                    defense = half_defense ? ((item.defense_points - 1) / 2) : (item.defense_points / 2);
                    if (item.defense_points == 1) {
                        half_defense = true;
                        defense = 0;
                    }
                }

                // Get material
                let material = false;
                if (item.material !== null)
                    material = await $axios.$get(`/itemMaterials/${item.material}`);

                // Get type
                let type = false;
                if (item.type !== null)
                    type = await $axios.$get(`/itemTypes/${item.type}`);

                return {
                    item: item,
                    material: material,
                    type: type,
                    half_attack: half_attack,
                    attack: attack,
                    half_defense: half_defense,
                    defense: defense
                };
            } catch (e) {
                return {
                    item: [],
                    material: [],
                    type: [],
                    half_attack: [],
                    attack: [],
                    half_defense: [],
                    defense: []
                };
            }
        },
        data() {
            return {
                item: [],
                material: [],
                type: [],
                half_attack: [],
                attack: [],
                half_defense: [],
                defense: []
            };
        },
        components: {
            BIcon,
            BIconLightning,
            BIconLightningFill,
            BIconBatteryFull,
            BIconCheckSquareFill,
            BIconXSquareFill,
            BIconShieldFill,
            BIconShieldShaded
        }
    }
</script>

<style scoped>

</style>