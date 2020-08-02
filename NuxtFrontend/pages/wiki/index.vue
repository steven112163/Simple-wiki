<template>
    <nav-top></nav-top>
</template>

<script>
    import NavTop from "../../components/common/navtop";

    export default {
        name: "index",
        head() {
            return {
                title: "Wiki"
            };
        },
        components: {NavTop}
    }
</script>

<style scoped>

</style>
