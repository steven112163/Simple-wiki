<template>
    <b-container class="my-5">
        <b-row>
            <b-col cols="4">
                <h1>{{ mob.name }}</h1>
            </b-col>
            <b-col class="text-right" cols="8">
                <p class="text-muted">Last Modified Date: {{ mob.update }}</p>
            </b-col>
        </b-row>
        <hr/>
        <b-row>
            <b-col class="text-center" cols="4">
                <b-img fluid rounded :src="mob.image" alt=""></b-img>
            </b-col>
            <b-col cols="8">
                <table class="table table-hover">
                    <tbody>
                    <tr>
                        <th scope="row">Health Points</th>
                        <td>
                            <template v-for="i in heart">
                                <b-icon icon="heart-fill" variant="danger"></b-icon>
                            </template>
                            <template v-if="half_heart">
                                <b-icon icon="heart-half" variant="danger"></b-icon>
                            </template>
                            <span> ({{ mob.health_points }})</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Height</th>
                        <td>{{ mob.height }}</td>
                    </tr>
                    <tr>
                        <th scope="row">Width</th>
                        <td>{{ mob.width }}</td>
                    </tr>
                    <tr v-if="behavior">
                        <th scope="row">Behavior</th>
                        <td>{{ behavior.name }}</td>
                    </tr>
                    <tr v-if="attack">
                        <th scope="row">Attack Strength</th>
                        <td>
                            <template v-for="i in attack">
                                <b-icon icon="lightning-fill" variant="warning"></b-icon>
                            </template>
                            <template v-if="half_attack">
                                <b-icon icon="lightning" variant="warning"></b-icon>
                            </template>
                            <span> ({{ mob.attack_strength }})</span>
                        </td>
                    </tr>
                    <tr>
                        <th scope="row">Spawn</th>
                        <td><span v-html="mob.spawn"></span></td>
                    </tr>
                    </tbody>
                </table>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    import {BIcon, BIconHeartFill, BIconHeartHalf, BIconLightning, BIconLightningFill} from "bootstrap-vue";

    export default {
        name: "mobIndex",
        layout: "wiki",
        head() {
            return {
                title: "Wiki | Mob Detail"
            };
        },
        async asyncData({$axios, params}) {
            try {
                let mob = await $axios.$get(`/mobs/${params.id}`);

                // Parse date
                let idxDot = mob.update.indexOf(".");
                let idxT = mob.update.indexOf("T");
                mob.update = mob.update.substring(0, idxT) + " " + mob.update.substring(idxT + 1, idxDot);

                // Get number of hearts
                let half_heart = (mob.health_points % 2) != 0 ? true : false;
                let heart = half_heart ? ((mob.health_points - 1) / 2) : (mob.health_points / 2);
                if (mob.health_points == 1)
                    heart = 1;
                else if (mob.health_points == 2)
                    heart = 2;

                // Get number of attack symbols
                let half_attack = false;
                let attack = false;
                if (mob.attack_strength !== null) {
                    half_attack = (mob.attack_strength % 2) != 0 ? true : false;
                    attack = half_attack ? ((mob.attack_strength - 1) / 2) : (mob.attack_strength / 2);
                    if (mob.attack_strength == 1)
                        attack = 1;
                    else if (mob.attack_strength == 2)
                        attack = 2;
                }

                // Get behavior
                let behavior = false;
                if (mob.behavior !== null)
                    behavior = await $axios.$get(`/mobBehaviors/${mob.behavior}`);

                return {
                    mob: mob,
                    behavior: behavior,
                    half_heart: half_heart,
                    heart: heart,
                    half_attack: half_attack,
                    attack: attack
                };
            } catch (e) {
                return {mob: [], behavior: [], half_heart: [], heart: [], half_attack: [], attack: []};
            }
        },
        data() {
            return {mob: [], behavior: [], half_heart: [], heart: [], half_attack: [], attack: []};
        },
        components: {
            BIcon,
            BIconHeartFill,
            BIconHeartHalf,
            BIconLightning,
            BIconLightningFill
        }
    }
</script>

<style scoped>

</style>