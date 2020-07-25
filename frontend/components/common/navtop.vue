<template>
    <div class="mb-3">
        <nav class="navbar navbar-expand-lg navbar-dark bg-success">
            <nuxt-link class="navbar-brand" to="/">
                <!--<img src="../../static/images/minecraft_icon.ico" alt="">-->
                Home
            </nuxt-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="navCollapse"
                    aria-controls="navCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navCollapse">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item dropdown">
                        <nuxt-link class="nav-link dropdown-toggle" to="/wiki" id="navDropdown" role="button"
                                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Wiki
                        </nuxt-link>
                        <div class="dropdown-menu" aria-labelledby="navDropdown">
                            <nuxt-link class="dropdown-item" to="/wiki/mobs">Mobs</nuxt-link>
                            <nuxt-link class="dropdown-item" to="/wiki/items">Items</nuxt-link>
                            <nuxt-link class="dropdown-item" to="/wiki/blocks">Blocks</nuxt-link>
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        name: "navtop"
    }
</script>

<style scoped>

</style>