<template>
    <div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../../static/images/items_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <h1>Items</h1>
                </div>
            </div>
        </div>
        <b-container class="mt-5">
            <b-row class="mb-4 d-flex justify-content-between">
                <h3>Items</h3>
                <nuxt-link is="b-button" to="/items/add" variant="primary" v-if="isAuthenticated">Add Item</nuxt-link>
            </b-row>
            <b-row>
                <template v-for="item in items">
                    <b-card-group deck :key="item.id" >
                        <item-card :item="item" :is-authenticated="isAuthenticated"></item-card>
                    </b-card-group>
                </template>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import ItemCard from "../../../components/item-card";
    import {mapGetters} from 'vuex';

    export default {
        name: "itemsIndex",
        head() {
            return {
                title: "Wiki | Items"
            };
        },
        layout: 'wiki',
        components: {
            ItemCard
        },
        computed: {
            ...mapGetters(['isAuthenticated'])
        },
        async asyncData({$axios, params}) {
            try {
                let items = await $axios.$get(`/items/`);
                for (let res of items.results) {
                    let idxDot = res.update.indexOf(".");
                    let idxT = res.update.indexOf("T");
                    res.update = res.update.substring(0, idxT) + " " + res.update.substring(idxT + 1, idxDot);
                }
                return {items: items.results};
            } catch (e) {
                return {items: []};
            }
        },
        data() {
            return {
                items: []
            };
        }
    }
</script>

<style scoped>
    @import "assets/css/wiki-each.css";
</style>
