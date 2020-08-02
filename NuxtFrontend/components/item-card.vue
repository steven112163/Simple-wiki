<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img :src="item.image" alt="no image" top></b-card-img>
        <b-card-body class="text-center">
            <b-card-title :title="item.name" title-tag="h4"></b-card-title>
            <hr/>
            <b-card-text>
                <strong>Stackable:</strong> {{ item.stackable }}
            </b-card-text>
            <b-card-text>
                <strong>Renewable:</strong> {{ item.renewable }}
            </b-card-text>
            <b-card-footer>
                <nuxt-link :to="`/wiki/items/${item.id}/`" class="btn btn-sm btn-success"> View</nuxt-link>
                <!--<nuxt-link :to="`/wiki/items/${item.id}/edit/`" class="btn btn-sm btn-primary"> Edit</nuxt-link>-->
            </b-card-footer>
        </b-card-body>
    </b-card>
</template>

<script>
    export default {
        props: ["item"]
    };
</script>

<style scoped>

</style>