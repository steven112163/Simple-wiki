import 'object-fit-images'
import { jarallax, jarallaxVideo } from 'jarallax'

window.addEventListener('load', function(event) {
    jarallaxVideo()
    jarallax(document.querySelectorAll('.jarallax'), {
        speed: 1.5
    })
})