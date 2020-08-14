<template>
    <b-alert show variant="danger">
        <h4>Following errors happened!</h4>
        <template v-for="e in error">
            <p>{{ e }}</p>
        </template>
    </b-alert>
</template>

<script>
    export default {
        name: "notification",
        props: ['error']
    }
</script>

<style scoped>

</style>