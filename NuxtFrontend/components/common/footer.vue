<template>
    <footer class="footer mt-5 py-4" style="background-color: #343a40">
        <div class="container text-center" style="color: white">
            <h5>
                <b-icon icon="file-person"></b-icon>
                Author: Yu-Hsun Yuan (Steven Yuan)
            </h5>
            <p>
                <b-icon icon="envelope"></b-icon>
                Email: steven112163@gmail.com
            </p>
            <a href="https://github.com/steven112163">
                <b-icon icon="tag"></b-icon>
                My GitHub
            </a>
        </div>
    </footer>
</template>

<script>
    import { BIcon, BIconTag, BIconEnvelope, BIconFilePerson } from 'bootstrap-vue';
    export default {
        name: "myFooter",
        components: {
            BIcon,
            BIconTag,
            BIconEnvelope,
            BIconFilePerson
        }
    }
</script>

<style scoped>

</style>