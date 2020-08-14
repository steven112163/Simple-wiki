<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img :src="item.image" alt="no image" top></b-card-img>
        <b-card-body class="text-center">
            <b-card-title :title="item.name" title-tag="h4"></b-card-title>
            <hr/>
            <b-card-text>
                <strong>Stackable:</strong>
                <b-icon v-if="item.stackable" icon="check-square-fill" variant="success"></b-icon>
                <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
            </b-card-text>
            <b-card-text>
                <strong>Renewable:</strong>
                <b-icon v-if="item.renewable" icon="check-square-fill" variant="success"></b-icon>
                <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
            </b-card-text>
            <nuxt-link is="b-button" block :to="`/wiki/items/${item.id}/`" variant="success" size="sm">View</nuxt-link>
            <nuxt-link is="b-button" block :to="`/wiki/items/${item.id}/edit/`" variant="secondary" size="sm"
                       v-if="isAuthenticated">Edit
            </nuxt-link>
            <b-card-footer>
                <small class="text-muted">{{ item.update }}</small>
            </b-card-footer>
        </b-card-body>
    </b-card>
</template>

<script>
    import {BIcon, BIconCheckSquareFill, BIconXSquareFill} from "bootstrap-vue";

    export default {
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
