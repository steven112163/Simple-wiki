<template>
    <div>
        <navtop/>
        <Nuxt/>
        <my-footer/>
    </div>
</template>

<script>
    import navtop from "../components/common/navtop";
    import myFooter from "../components/common/footer";

    export default {
        components: {
            navtop,
            myFooter
        }
    }
</script>

<style></style>
