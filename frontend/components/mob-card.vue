<template>
    <div class="card">
        <img class="card-img-top" :src="mob.image" alt="no image">
        <div class="card-body">
            <h5 class="card-title">{{ mob.name }}</h5>
            <p class="card-text">
                <strong>Height:</strong> {{ mob.height }}
            </p>
            <p class="card-text">
                <strong>Width:</strong> {{ mob.width }}
            </p>
            <div class="card-footer">
                <nuxt-link :to="`/wiki/mobs/${mob.id}/`" class="btn btn-sm btn-success"> View</nuxt-link>
                <!--<nuxt-link :to="`/wiki/mobs/${mob.id}/edit/`" class="btn btn-sm btn-primary"> Edit</nuxt-link>-->
            </div>
        </div>
    </div>
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
