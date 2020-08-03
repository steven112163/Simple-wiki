<template>
    <main class="container mt-5">
        <div class="row">
            <div class="col-12 text-right mb-4">
                <div class="d-flex justify-content-between">
                    <h3>Items</h3>
                    <nuxt-link to="/items/add" class="btn btn-primary">Add Item</nuxt-link>
                </div>
            </div>
            <template v-for="item in items">
                <b-card-group deck :key="item.id">
                    <item-card :item="item"></item-card>
                </b-card-group>
            </template>
        </div>
    </main>
</template>

<script>
    import ItemCard from "../../../components/item-card";

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

</style>
