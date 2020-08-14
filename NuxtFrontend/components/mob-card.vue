<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img :src="mob.image" alt="no image" top></b-card-img>
        <b-card-body class="text-center">
            <b-card-title :title="mob.name" title-tag="h4"></b-card-title>
            <hr/>
            <b-card-text>
                <strong>Height:</strong> {{ mob.height }}
            </b-card-text>
            <b-card-text>
                <strong>Width:</strong> {{ mob.width }}
            </b-card-text>
            <nuxt-link is="b-button" block :to="`/wiki/mobs/${mob.id}/`" variant="success" size="sm">View</nuxt-link>
            <nuxt-link is="b-button" block :to="`/wiki/mobs/${mob.id}/edit/`" variant="secondary" size="sm"
                       v-if="isAuthenticated">Edit
            </nuxt-link>
            <b-card-footer>
                <small class="text-muted">{{ mob.update }}</small>
            </b-card-footer>
        </b-card-body>
    </b-card>
</template>

<script>
    export default {
        name: "mobCard",
        props: ["mob", "isAuthenticated"]
    };
</script>

<style scoped>

</style>
