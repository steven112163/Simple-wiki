<template>
    <b-card border-variant="dark">
        <b-card-img :src="mob.image" alt="no image" top></b-card-img>
        <b-card-body>
            <b-card-title :title="mob.name" title-tag="h5"></b-card-title>
            <b-card-text>
                <strong>Height:</strong> {{ mob.height }}
            </b-card-text>
            <b-card-text>
                <strong>Width:</strong> {{ mob.width }}
            </b-card-text>
            <b-card-footer>
                <nuxt-link :to="`/wiki/mobs/${mob.id}/`" class="btn btn-sm btn-success"> View</nuxt-link>
                <!--<nuxt-link :to="`/wiki/mobs/${mob.id}/edit/`" class="btn btn-sm btn-primary"> Edit</nuxt-link>-->
            </b-card-footer>
        </b-card-body>
    </b-card>
</template>

<script>
    export default {
        props: ["mob"]
    };
</script>

<style>
    .mob-card {
        box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
    }
</style>
