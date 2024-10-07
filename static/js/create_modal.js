            // <div class="overlay" id="video2"></div>
            // <div class="modal">
            //     <iframe src="https://vk.com/video_ext.php?oid=-184436599&id=456240190&hd=2&autoplay=1" width="853"
            //             height="480"
            //             allow="autoplay; encrypted-media; fullscreen; picture-in-picture; screen-wake-lock;"
            //             frameBorder="0" allowFullScreen></iframe>
            //     <a href="" id="stop" class="close-sliderProject"></a>
            // </div>
function createModal(block, slug, iframe) {
    let overlay = document.createElement('div')
    overlay.classList.add('overlay')
    overlay.setAttribute('id', slug)

    let modal = document.createElement('div')
    modal.classList.add('modal')
    modal.innerHTML = iframe + `<a href="" id="stop" class="close-sliderProject"></a>`
    block.append(overlay, modal)
}