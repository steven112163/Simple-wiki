<template>
    <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
            style="border-bottom-width: 4px">
        <b-card-img v-if="mob.image" :src="mob.image" alt="" top></b-card-img>
        <b-card-img v-else src="https://img.icons8.com/color/480/000000/image.png" alt="" top></b-card-img>
        <b-card-title :title="mob.name" title-tag="h4" class="text-center mt-2"></b-card-title>
        <hr/>
        <b-card-text class="text-center">
            <strong>Height:</strong> {{ mob.height }}
        </b-card-text>
        <b-card-text class="text-center">
            <strong>Width:</strong> {{ mob.width }}
        </b-card-text>
        <nuxt-link is="b-button" block :to="`/wiki/mobs/${mob.id}/`" variant="success" size="sm">View</nuxt-link>
        <nuxt-link is="b-button" block :to="`/wiki/mobs/${mob.id}/edit/`" variant="secondary" size="sm"
                   v-if="isAuthenticated">Edit
        </nuxt-link>
        <template v-slot:footer>
            <small class="text-muted">Last updated: {{ mob.update }}</small>
        </template>
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
