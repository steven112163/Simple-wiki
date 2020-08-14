<template>
    <b-alert show variant="danger">
        <h4>Following errors happened!</h4>
        <p>{{ error }}</p>
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