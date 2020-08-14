<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img :src="block.image" alt="no image" top></b-card-img>
        <b-card-body class="text-center">
            <b-card-title :title="block.name" title-tag="h4"></b-card-title>
            <hr/>
            <b-card-text>
                <strong>Stackable:</strong>
                <b-icon v-if="block.stackable" icon="check-square-fill" variant="success"></b-icon>
                <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
            </b-card-text>
            <b-card-text>
                <strong>Flammable:</strong>
                <b-icon v-if="block.flammable" icon="check-square-fill" variant="success"></b-icon>
                <b-icon v-else icon="x-square-fill" variant="danger"></b-icon>
            </b-card-text>
            <nuxt-link is="b-button" block :to="`/wiki/blocks/${block.id}/`" variant="success" size="sm"> View
            </nuxt-link>
            <nuxt-link is="b-button" block :to="`/wiki/blocks/${block.id}/edit/`" variant="secondary" size="sm"
                       v-if="isAuthenticated"> Edit
            </nuxt-link>
            <b-card-footer>
                <small class="text-muted">{{ block.update }}</small>
            </b-card-footer>
        </b-card-body>
    </b-card>
</template>

<script>
    import {BIcon, BIconCheckSquareFill, BIconXSquareFill} from "bootstrap-vue";

    export default {
        props: ["block", "isAuthenticated"],
        components: {
            BIcon,
            BIconCheckSquareFill,
            BIconXSquareFill
        }
    };
</script>

<style scoped>

</style>