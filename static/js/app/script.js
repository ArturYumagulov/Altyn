let inviteCount = document.getElementById('invite_count')
let show_list_rolled_cert = ['igrovoj-korotkometrazhnyj-film', 'igrovoj-polnometrazhnyj-film', 'animacionnyj-film']
let other_region = document.getElementById('other-region')
let group_1 = document.querySelector('.genregroup_1')
let group_2 = document.querySelector('.genregroup_2')
let rolled_certificate_num = document.querySelector('.rolled_certificate_num')
let rolled_certificate_num_input = rolled_certificate_num.querySelector('input[type=number]')
let regionOther = document.getElementById('other')
let regionRussia = document.getElementById('russia')
let regionBlock = document.getElementById('region-block')
let compositor = document.querySelector('.composer')
let passButton = document.getElementById('pass')
let regionMapBlock = document.querySelector('.specialist-block')
let otherSpecialityCheckbox = document.getElementById('other_speciality')
let otherSpecialityInput = document.getElementById('other_speciality_input')
let sendInviteButton = document.getElementById('send_invite_1')
let inviteBody = document.querySelector('.invite-body')

let musicBlock = document.querySelector('.music-block')

// Contract

let contractNow = document.getElementById('contract_now')
let contractLater = document.getElementById('contract_later')
let questBody = document.querySelector('.contract-quest')


let individualButton = document.getElementById('individual')
let legalButton = document.getElementById('legal')


let agreement_to_placement = document.getElementById('agreement_to_placement')
let agreement_to_vote = document.getElementById('agreement_to_vote')
let agreement_to_no_commerce_show = document.getElementById('agreement_to_no_commerce_show')


// console.log(individualButton)

function deleteInvite(count) {
    let invite = document.getElementById(`specialist-region_${count}`)
    invite.remove()
}

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
    observer.observe(elem, {attributes: true});
    elem.addEventListener('click', () => {
        let element = elem.childNodes[1]
        element.setAttribute('value', element.dataset.type)

        if (element.id === "true-debut") {
            document.getElementById('false-debut').removeAttribute('required')
            document.getElementById('true-debut').setAttribute('required', '')
        }
        if (element.id === "false-debut") {
            document.getElementById('true-debut').removeAttribute('required')
            document.getElementById('false-debut').setAttribute('required', '')
        }


        // Жанры
        if (show_list_rolled_cert.includes(element.dataset.type)) {
            group_1.style.display = 'block'
            group_2.style.display = 'none'
        } else {
            group_2.style.display = 'block'
            group_1.style.display = 'none'

        }

        // Музыка

        // if (element.id === 'true-music'){
        //     compositor.style.display = 'block'
        //     compositor.querySelectorAll('input').forEach((compositor_input)=> {
        //         compositor_input.setAttribute('required', '')
        //     })
        // } else {
        //     compositor.style.display = 'none'
        //     compositor.querySelectorAll('input').forEach((compositor_input)=> {
        //         compositor_input.removeAttribute('required')
        //     })
        // }
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

let rolledCertificate = document.querySelector('.rolled-certificate')


rolledCertificate.addEventListener('click', (event)=> {
    let child_id = event.target.childNodes[1].value
    if (child_id === 'est') {
        rolled_certificate_num.style.display = 'block'
        rolled_certificate_num_input.setAttribute('required', '')
    } else {
        rolled_certificate_num.style.display = 'none'
        rolled_certificate_num_input.removeAttribute('required')
        rolled_certificate_num_input.removeAttribute('value')
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

// выключение отправки
const buttons = document.querySelectorAll('.btn._icon-derection-right')
buttons.forEach((button) => {
    button.addEventListener('click', (e) => {
        e.preventDefault()
    })
})

// Пропустить регион
passButton.addEventListener('click', ()=> {
    document.getElementById('region_count').value = "0"
    document.querySelector('.region-app-block').textContent = ''
})
/// Другое Специалист
otherSpecialityCheckbox.addEventListener('change', (e)=> {
    if(e.target.checked) {
        otherSpecialityInput.style.display = 'block'
        otherSpecialityInput.setAttribute('required', '')
        otherSpecialityInput.setAttribute('name', 'other_speciality')

    } else {
        otherSpecialityInput.style.display = 'none'
        otherSpecialityInput.removeAttribute('required')
        otherSpecialityInput.removeAttribute('name')
    }
})

//  Первая кнопка приглашения
sendInviteButton.addEventListener('change', (e) => {
    if (e.target.checked) {
        inviteCount.value = Number(inviteCount.value) + 1
        createInvite(1)
    } else {
        deleteInvite(1)
        inviteCount.value = Number(inviteCount.value) - 1
    }
})

// генерация последующих приглашений
inviteBody.addEventListener('click', (event) => {
    if (event.target.classList.contains('send-invite')) {
        if (event.target.checked) {
            inviteCount.value = Number(inviteCount.value) + 1
            createInvite(Number(event.target.id.split('_')[2]))
        } else {
            deleteInvite(Number(event.target.id.split('_')[2]))
            inviteCount.value = Number(inviteCount.value) - 1
        }
    }
})

// кнопки появления договора
contractNow.addEventListener('click', ()=>{
    questBody.classList.add('show')
    document.getElementById('contract_status').value = 'now'
    let quest_input = questBody.querySelectorAll('input')
    if (quest_input.length > 0) {
        quest_input.forEach((input) => {
            input.setAttribute('required', '')
        })
    }
})

// кнопки исчезания договора
contractLater.addEventListener('click', ()=>{
    questBody.classList.remove('show')
    document.getElementById('contract_status').value = 'later'
    let quest_input = questBody.querySelectorAll('input')
    if (quest_input.length > 0) {
        quest_input.forEach((input) => {
            input.removeAttribute('required')
            input.parentNode.classList.remove('active')
        })
    }
    document.querySelector('.individual-block').textContent = ''
    document.querySelector('.legal-entity').textContent = ''
})


// Договор
questBody.addEventListener('click', (event) => {
    let child_id = event.target.childNodes[1]

    if (child_id.id === 'individual') {
        createIndividualBlock()
        legalButton.removeAttribute('required')
    } else {
        legalButton.setAttribute('required', '')
        document.querySelector('.individual-block').textContent = ''
    }

    if (child_id.id === 'legal') {
        createLegalBlock()
        console.log(individualButton)
        individualButton.removeAttribute('required')
    } else {
        individualButton.setAttribute('required', '')
        document.querySelector('.legal-entity').textContent = ''

    }
})


// Оригинальная музыка
musicBlock.addEventListener('click', (event) => {
    let child_id = event.target.childNodes[1]
    document.getElementById('false-music').removeAttribute('required')
    document.getElementById('true-music').setAttribute('required', '')
    if (child_id.value === '1') {
        console.log(child_id)
        compositor.style.display = 'block'
        compositor.querySelectorAll('input').forEach((compositor_input) => {
            compositor_input.setAttribute('required', '')
            compositor_input.value = ''
        })
    } else if (child_id.value === '0') {
        document.getElementById('false-music').setAttribute('required', '')
        document.getElementById('true-music').removeAttribute('required')
        console.log(compositor)
        compositor.style.display = 'none'
        compositor.querySelectorAll('input').forEach((compositor_input) => {
            compositor_input.removeAttribute('required')
            compositor_input.value = ''
        })
    }
})

// Согласия
agreement_to_placement.addEventListener('change', (e)=> {
    if (e.target.checked === true) {
        agreement_to_placement.value = 1
    } else {
        agreement_to_placement.value = 0
    }
})


agreement_to_vote.addEventListener('change', (e)=> {
    if (e.target.checked === true) {
        agreement_to_vote.value = 1
    } else {
        agreement_to_vote.value = 0
    }
})


agreement_to_no_commerce_show.addEventListener('change', (e)=> {
    if (e.target.checked === true) {
        agreement_to_no_commerce_show.value = 1
    } else {
        agreement_to_no_commerce_show.value = 0
    }
})