<template>
    <b-container class="mt-5">
        <b-row>
            <b-col></b-col>
            <b-col cols="6">
                <b-card border-variant="dark" class="border-top-0 border-right-0 border-left-0 shadow-lg"
                        style="border-bottom-width: 4px">
                    <b-card-title style="text-align: center">
                        <img src="~/static/images/minecraft_logo.svg" width="34" height="36"
                             class="d-inline-block align-top"
                             alt="logo">
                        <em>Welcome to my webpage</em>
                    </b-card-title>
                    <hr/>
                    <notification :error="error" v-if="error"></notification>
                    <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show">
                        <b-form-group label="Account" label-for="account-input">
                            <b-form-input
                                    id="account-input"
                                    v-model="form.username"
                                    placeholder="Enter your account"
                            ></b-form-input>
                        </b-form-group>
                        <b-form-group label="Password" label-for="password-input">
                            <b-form-input
                                    id="password-input"
                                    v-model="form.password"
                                    type="password"
                                    placeholder="Enter your password"
                                    :state="state"
                                    aria-describedby="feedback"
                            ></b-form-input>
                            <b-form-invalid-feedback id="feedback">
                                At least 6 characters
                            </b-form-invalid-feedback>
                        </b-form-group>
                        <b-button block type="submit" variant="success">Log In</b-button>
                        <b-button block type="reset" variant="secondary">Reset</b-button>
                    </b-form>
                    <br>
                    <p style="text-align: center">Don't have an account?
                        <nuxt-link to="/register">Register</nuxt-link>
                    </p>
                </b-card>
            </b-col>
            <b-col></b-col>
        </b-row>
    </b-container>
</template>

<script>
    import notification from "@/components/common/notification";

    export default {
        name: "login",
        head() {
            return {
                title: 'Wiki | Login'
            }
        },
        layout: 'wiki',
        components: {
            notification
        },
        data() {
            return {
                form: {
                    username: '',
                    password: ''
                },
                show: true,
                error: null
            }
        },
        methods: {
            async onSubmit(event) {
                try {
                    await this.$auth.loginWith('local', {
                        data: this.form
                    });
                    this.$auth.setUser({username: this.form.username});
                    await this.$router.push('/wiki');
                } catch (e) {
                    this.error = e.response.data;
                }
            },
            onReset(event) {
                this.form.username = '';
                this.form.password = '';
                this.show = false;
                this.$nextTick(() => {
                    this.show = true;
                });
            }
        },
        computed: {
            state() {
                return this.form.password.length > 6;
            }
        }
    }
</script>

<style scoped>

</style>