<template>
    <div class="mb-3">
        <!-- NavBar -->
        <b-navbar toggleable="lg" type="dark" variant="dark">
            <!-- Brand -->
            <nuxt-link is="b-navbar-brand" to="/">
                <img src="~/static/images/minecraft_logo.svg" width="34" height="36" class="d-inline-block align-top"
                     alt="logo">
                Home
            </nuxt-link>

            <!-- Toggler Button -->
            <b-navbar-toggle target="navCollapse"></b-navbar-toggle>

            <b-collapse id="navCollapse" is-nav>
                <b-navbar-nav>
                    <!-- Dropdown -->
                    <b-nav-item-dropdown text="Wiki">
                        <b-dropdown-item href="/wiki">Wiki Home page</b-dropdown-item>
                        <b-dropdown-item href="/wiki/mobs">Mobs</b-dropdown-item>
                        <b-dropdown-item href="/wiki/items">Items</b-dropdown-item>
                        <b-dropdown-item href="/wiki/blocks">Blocks</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "navtop"
    }
</script>

<style scoped>

</style>