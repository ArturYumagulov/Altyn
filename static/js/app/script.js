let show_list_rolled_cert = ['igrovoj-korotkometrazhnyj-film', 'igrovoj-polnometrazhnyj-film', 'animacionnyj-film']
let other_region = document.getElementById('other-region')
let group_1 = document.querySelector('.genregroup_1')
let group_2 = document.querySelector('.genregroup_2')
let rolled_certificate_num = document.querySelector('.rolled_certificate_num')
let rolled_certificate_num_input = rolled_certificate_num.querySelector('input[type=number]')
let regionOther = document.getElementById('other')
let regionRussia = document.getElementById('russia')
let regionBlock = document.getElementById('region-block')
let regionItems = document.querySelectorAll('#region-item')

// console.log(regionItems)

let observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.attributeName === 'class') {
            let classList = mutation.target.classList;
            if (!classList.contains('active')) {
                mutation.target.childNodes[1].removeAttribute('value')
            }

        }
    });
});

let targetElement = document.querySelectorAll('.application-checked.checkbox');
targetElement.forEach((elem) => {
    // observer.observe(elem, {attributes: true});
    elem.addEventListener('click', () => {
        let element = elem.childNodes[1]
        element.setAttribute('value', element.dataset.type)
        // Жанры
        if (show_list_rolled_cert.includes(element.dataset.type)) {
            group_1.style.display = 'block'
            group_2.style.display = 'none'
        } else {
            group_2.style.display = 'block'
            group_1.style.display = 'none'

        }

        // Номер прокатного удостоверения
        if (element.getAttribute('value') === 'est') {
            rolled_certificate_num.style.display = 'block'
            rolled_certificate_num_input.setAttribute('required', '')
        } else {
            rolled_certificate_num.style.display = 'none'
            rolled_certificate_num_input.removeAttribute('required')
            rolled_certificate_num_input.removeAttribute('value')
        }
    })
})

// Начало другие регионы
regionOther.addEventListener('change', (e) => {
    if (e.target.checked) {
        e.target.setAttribute('name', 'other_country')
        other_region.style.display = 'block'
        other_region.childNodes[1].setAttribute('required', '')
        other_region.childNodes[1].setAttribute('name', 'other_country_name')
    } else {
        e.target.removeAttribute('name')
        other_region.style.display = 'none'
        other_region.childNodes[1].removeAttribute('required')
        other_region.childNodes[1].removeAttribute('name')
    }
})
// Конец другие регион

// -------------------------

// Если регион Россия
regionRussia.addEventListener('change', (e) => {
    if (e.target.checked) {
        regionBlock.style.display = 'block'
        // regionItems.forEach((item) => {
        //     item.childNodes[1].setAttribute('required', '')
        // })
    } else {
        regionBlock.style.display = 'none'
        // regionItems.forEach((item) => {
        //     item.childNodes[1].removeAttribute('required')
        // })
    }
})
// Конец если регион Россия


const buttons = document.querySelectorAll('.btn._icon-derection-right')
buttons.forEach((button) => {
    button.addEventListener('click', (e) => {
        e.preventDefault()
    })
})
