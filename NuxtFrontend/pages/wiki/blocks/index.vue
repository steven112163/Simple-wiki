<template>
    <div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../../static/images/blocks_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <h1>Blocks</h1>
                </div>
            </div>
        </div>
        <b-container class="mt-5">
            <b-row class="mb-4 d-flex justify-content-between">
                <h3>Blocks</h3>
                <nuxt-link is="b-button" to="/wiki/blocks/add" variant="primary" v-if="isAuthenticated">Add Block</nuxt-link>
            </b-row>
            <b-row>
                <template v-for="block in blocks">
                    <b-card-group deck :key="block.id">
                        <block-card :block="block" :is-authenticated="isAuthenticated"></block-card>
                    </b-card-group>
                </template>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import BlockCard from "../../../components/block-card";
    import {mapGetters} from "vuex";

    export default {
        name: "blocksIndex",
        head() {
            return {
                title: "Wiki | Blocks"
            };
        },
        layout: 'wiki',
        components: {
            BlockCard
        },
        computed: {
            ...mapGetters(['isAuthenticated'])
        },
        async asyncData({$axios, params}) {
            try {
                let blocks = await $axios.$get(`/blocks/`);
                for (let res of blocks.results) {
                    let idxDot = res.update.indexOf(".");
                    let idxT = res.update.indexOf("T");
                    res.update = res.update.substring(0, idxT) + " " + res.update.substring(idxT + 1, idxDot);
                }
                return {blocks: blocks.results};
            } catch (e) {
                return {blocks: []};
            }
        },
        data() {
            return {
                blocks: []
            };
        }
    }
</script>

<style scoped>
    @import "assets/css/wiki-each.css";
</style>
