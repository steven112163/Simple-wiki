<template>
    <div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../../static/images/mobs_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <h1>Mobs</h1>
                </div>
            </div>
        </div>
        <b-container class="mt-5">
            <b-row class="mb-4 d-flex justify-content-between">
                <h3>Mobs</h3>
                <nuxt-link is="b-button" to="/wiki/mobs/add" variant="primary" v-if="isAuthenticated">Add Mob
                </nuxt-link>
            </b-row>
            <b-row>
                <b-card-group deck>
                    <mob-card v-for="mob in mobs" :key="mob.id" :mob="mob"
                              :is-authenticated="isAuthenticated"></mob-card>
                </b-card-group>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import MobCard from "../../../components/mob-card";
    import {mapGetters} from 'vuex';

    export default {
        name: "mobsIndex",
        head() {
            return {
                title: "Wiki | Mobs"
            };
        },
        layout: 'wiki',
        components: {
            MobCard
        },
        computed: {
            ...mapGetters(['isAuthenticated'])
        },
        async asyncData({$axios, params}) {
            try {
                let mobs = await $axios.$get(`/mobs/`);
                for (let res of mobs.results) {
                    let idxDot = res.update.indexOf(".");
                    let idxT = res.update.indexOf("T");
                    res.update = res.update.substring(0, idxT) + " " + res.update.substring(idxT + 1, idxDot);
                }
                return {mobs: mobs.results};
            } catch (e) {
                return {mobs: []};
            }
        },
        data() {
            return {
                mobs: []
            };
        }
    }
</script>

<style scoped>
    @import "assets/css/wiki-each.css";
</style>
