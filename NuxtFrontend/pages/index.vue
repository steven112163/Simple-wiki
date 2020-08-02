<template>
    <header>
        <div class="text-box">
            <h1>My Website</h1>
            <p class="mt-3">NuxtJS and Django REST ❤️ ️</p>
            <nuxt-link class="btn btn-outline btn-large btn-info" to="/wiki">
                View Wiki <span class="ml-2">&rarr;</span>
            </nuxt-link>
        </div>
    </header>
</template>
<script>
    export default {
        name: "home",
        head() {
            return {
                title: "Home page"
            };
        },
    };
</script>
<style scoped>
    @import "assets/css/home.css";
</style>
