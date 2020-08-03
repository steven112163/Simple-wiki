<template>
    <main class="container mt-5">
        <div class="row">
            <div class="col-12 text-right mb-4">
                <div class="d-flex justify-content-between">
                    <h3>Mobs</h3>
                    <nuxt-link to="/mobs/add" class="btn btn-primary">Add Mob</nuxt-link>
                </div>
            </div>
            <template v-for="mob in mobs">
                <b-card-group deck :key="mob.id">
                    <mob-card :mob="mob"></mob-card>
                </b-card-group>
            </template>
        </div>
    </main>
</template>

<script>
    import MobCard from "../../../components/mob-card";

    export default {
        name: "mobsIndex",
        head() {
            return {
                title: "Wiki | Mobs"
            };
        },
        layout: 'wiki',
        components: {
            MobCard
        },
        async asyncData({$axios, params}) {
            try {
                let mobs = await $axios.$get(`/mobs/`);
                for (let res of mobs.results) {
                    let idxDot = res.update.indexOf(".");
                    let idxT = res.update.indexOf("T");
                    res.update = res.update.substring(0, idxT) + " " + res.update.substring(idxT + 1, idxDot);
                }
                return {mobs: mobs.results};
            } catch (e) {
                return {mobs: []};
            }
        },
        data() {
            return {
                mobs: []
            };
        }
    }
</script>

<style scoped>

</style>
