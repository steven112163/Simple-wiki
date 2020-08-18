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
                        <nuxt-link is="b-dropdown-item" to="/wiki">Wiki Home page</nuxt-link>
                        <nuxt-link is="b-dropdown-item" to="/wiki/mobs">Mobs</nuxt-link>
                        <nuxt-link is="b-dropdown-item" to="/wiki/items">Items</nuxt-link>
                        <nuxt-link is="b-dropdown-item" to="/wiki/blocks">Blocks</nuxt-link>
                    </b-nav-item-dropdown>
                </b-navbar-nav>

                <!-- User information -->
                <b-navbar-nav class="ml-auto">
                    <template v-if="!isAuthenticated">
                        <nuxt-link is="b-nav-item" to="/register"><em>Register</em></nuxt-link>
                        <nuxt-link is="b-nav-item" to="/login"><em>Login</em></nuxt-link>
                    </template>
                    <template v-else>
                        <b-nav-item-dropdown right>
                            <template v-slot:button-content>
                                <em>Hi! {{ getUser }}</em>
                            </template>
                            <nuxt-link is="b-dropdown-item" to="#">Profile</nuxt-link>
                            <b-dropdown-item @click="logout">Logout</b-dropdown-item>
                        </b-nav-item-dropdown>
                    </template>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';

    export default {
        name: "navtop",
        computed: {
            ...mapGetters(['isAuthenticated']),
            getUser() {
                this.$auth.$storage.syncUniversal('username');
                return this.$auth.$storage.getUniversal('username');
            }
        },
        methods: {
            async logout() {
                await this.$auth.logout();
                this.$auth.$storage.removeUniversal('username');
                await this.$router.push('/wiki');
            }
        }
    }
</script>

<style scoped>

</style>