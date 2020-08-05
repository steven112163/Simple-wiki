<template>
    <div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../static/images/Minecraft.jpeg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <h1>Mobs, Items, Blocks</h1>
                </div>
            </div>
        </div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../static/images/mobs_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <nuxt-link to="/wiki/mobs">Mobs</nuxt-link>
                </div>
            </div>
        </div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../static/images/items_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <nuxt-link to="/wiki/items">Items</nuxt-link>
                </div>
            </div>
        </div>
        <div class="jarallax">
            <img class="jarallax-img" src="../../static/images/blocks_para.jpg" alt="">
            <div class="img-block">
                <div class="img-words">
                    <nuxt-link to="/wiki/blocks">Blocks</nuxt-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "index",
        head() {
            return {
                title: "Wiki"
            };
        },
        layout: 'wiki'
    }
</script>

<style scoped>
    @import "assets/css/wiki-index.css";
</style>
