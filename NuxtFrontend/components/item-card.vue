<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img v-if="item.image" :src="item.image" alt="no image" top></b-card-img>
        <b-card-img v-else src="https://img.icons8.com/color/480/000000/image.png" alt="" top></b-card-img>
        <b-card-title :title="item.name" title-tag="h4" class="text-center mt-2"></b-card-title>
        <hr/>
        <b-card-text class="text-center">
            <strong>Stackable:</strong>
            <b-icon v-if="item.stackable" icon="check-square-fill" variant="success"></b-icon>
            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
        </b-card-text>
        <b-card-text class="text-center">
            <strong>Renewable:</strong>
            <b-icon v-if="item.renewable" icon="check-square-fill" variant="success"></b-icon>
            <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
        </b-card-text>
        <nuxt-link is="b-button" block :to="`/wiki/items/${item.id}/`" variant="success" size="sm">View</nuxt-link>
        <nuxt-link is="b-button" block :to="`/wiki/items/${item.id}/edit/`" variant="secondary" size="sm"
                   v-if="isAuthenticated">Edit
        </nuxt-link>
        <template v-slot:footer>
            <small class="text-muted">Last updated: {{ item.update }}</small>
        </template>
    </b-card>
</template>

<script>
    import {BIcon, BIconCheckSquareFill, BIconXSquareFill} from "bootstrap-vue";

    export default {
        name: "itemCard",
        props: ["item", "isAuthenticated"],
        components: {
            BIcon,
            BIconCheckSquareFill,
            BIconXSquareFill
        }
    };
</script>

<style scoped>

</style>
