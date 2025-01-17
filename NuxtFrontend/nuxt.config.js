export default {
    /*
    ** Nuxt rendering mode
    ** See https://nuxtjs.org/api/configuration-mode
    */
    mode: 'universal',
    /*
    ** Nuxt target
    ** See https://nuxtjs.org/api/configuration-target
    */
    target: 'server',
    /*
    ** Headers of the page
    ** See https://nuxtjs.org/api/configuration-head
    */
    head: {
        title: process.env.npm_package_name || '',
        meta: [
            {charset: 'utf-8'},
            {name: 'viewport', content: 'width=device-width, initial-scale=1'},
            {hid: 'description', name: 'description', content: process.env.npm_package_description || ''}
        ],
        link: [
            {rel: 'icon', type: 'image/x-icon', href: '/images/minecraft_icon.ico'}
        ]
    },
    /*
    ** Global CSS
    */
    css: [
        "@/assets/css/wiki-jarallax.css",
        "@/assets/css/transition.css"
    ],
    /*
    ** Plugins to load before mounting the App
    ** https://nuxtjs.org/guide/plugins
    */
    plugins: [
        {src: '~/plugins/jarallax.js', ssr: false}
    ],
    /*
    ** Auto import components
    ** See https://nuxtjs.org/api/configuration-components
    */
    components: true,
    /*
    ** Nuxt.js dev-modules
    */
    buildModules: [],
    /*
    ** Nuxt.js modules
    */
    modules: [
        // Doc: https://bootstrap-vue.js.org
        'bootstrap-vue/nuxt',
        // Doc: https://axios.nuxtjs.org/usage
        '@nuxtjs/axios',
        '@nuxtjs/pwa',
        '@nuxtjs/auth'
    ],
    /*
    ** Axios module configuration
    ** See https://axios.nuxtjs.org/options
    */
    axios: {
        baseURL: "http://localhost:8000/api"
    },
    /*
    ** Auth module configuration
    ** See https://auth.nuxtjs.org/
    */
    auth: {
        strategies: {
            local: {
                endpoints: {
                    login: {
                        url: '/token/',
                        method: 'post',
                        propertyName: 'access',
                        altProperty: 'refresh'
                    },
                    logout: false,
                    user: false
                }
            }
        },
        redirect: {
            login: '/login',
            logout: '/wiki'
        }
    },
    /*
    ** Build configuration
    ** See https://nuxtjs.org/api/configuration-build/
    */
    build: {}
}
