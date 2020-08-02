<template>
    <main class="container mt-5">
        <div class="row">
            <div class="col-12 text-right mb-4">
                <div class="d-flex justify-content-between">
                    <h3>Blocks</h3>
                    <nuxt-link to="/blocks/add" class="btn btn-info">Add Block</nuxt-link>
                </div>
            </div>
            <template v-for="block in blocks">
                <b-card-group deck :key="block.id">
                    <block-card :block="block"></block-card>
                </b-card-group>
            </template>
        </div>
    </main>
</template>

<script>
    import BlockCard from "../../../components/block-card";

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
        async asyncData({$axios, params}) {
            try {
                let blocks = await $axios.$get(`/blocks/`);
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

</style>
