let inviteCount = document.getElementById('invite_count')
let show_list_genres = ['igrovoj-korotkometrazhnyj-film', 'igrovoj-polnometrazhnyj-film', 'animacionnyj-film']
let other_region = document.getElementById('other-region')
let group_1 = document.querySelector('.genregroup_1')
let group_2 = document.querySelector('.genregroup_2')
let genre_body = document.querySelector('.genre__body')
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

let specialists_id = {
    'producer': {
        'specialist': 'producer',
        'name': 'Продюсер:',
        'subname': 'продюсера',
    },
    'stage-director': {
        'specialist': 'stage-director',
        'name': 'Режиссер-постановщик:',
        'subname': 'режиссера-постановщика:',
    },
    'screenwriter': {
        'specialist': 'screenwriter',
        'name': 'Сценарист:',
        'subname': 'сценариста:',
    },
    'operator': {
        'specialist': 'operator',
        'name': 'Оператор - постановщик:',
    },
    'compositor': {
        'specialist': 'compositor',
        'name': ' Композитор:',
    }
}

const sub_spec= ['operator', 'compositor']

function createSubSpecialistBlock(specialist, name, subname) {

    let specialist_count = document.getElementById(`${specialist}_count`)
    specialist_count.value = Number(specialist_count.value) + 1
    let count = specialist_count.value

    let specialist_block = document.querySelector(`.new-${specialist}`)

    let div = document.createElement('div')
    div.classList.add(specialist)

    let specH4 = document.createElement('h4')
    specH4.textContent = name

    let namesDiv = document.createElement('div')
    namesDiv.classList.add(`${specialist}-person`, 'person')

    div.append(specH4, namesDiv)

    let names1Input = document.createElement('input')
    names1Input.setAttribute('type', 'text')
    names1Input.setAttribute('placeholder', 'Имя')
    names1Input.setAttribute('name', `${specialist}_first_name_${count}`)
    names1Input.setAttribute('required', ``)

    let names2Input = document.createElement('input')
    names2Input.setAttribute('type', 'text')
    names2Input.setAttribute('placeholder', 'Фамилия')
    names2Input.setAttribute('name', `${specialist}_last_name_${count}`)
    names2Input.setAttribute('required', ``)

    namesDiv.append(names1Input, names2Input)

    let addButton = document.createElement('div')
    addButton.classList.add('speciality-add')
    let addButtonA = document.createElement('a')
    addButtonA.classList.add('btn', 'speciality-add__btn')
    addButtonA.setAttribute('id', `${specialist}_add`)
    addButtonA.setAttribute('data-count', `${Number(count) + 1}`)
    // addButtonA.setAttribute("data-type", "add")
    let addSpan = document.createElement('span')
    addSpan.setAttribute("data-type", "add")
    addSpan.textContent = "+"
    addButtonA.append(addSpan)

    addButton.append(addButtonA)

    specialist_block.append(
        div,
        addButton
    )
}

function createSpecialistBlock(specialist, name, subname) {
    let specialist_count = document.getElementById(`${specialist}_count`)
    specialist_count.value = Number(specialist_count.value) + 1
    let count = specialist_count.value

    let specialist_block = document.querySelector(`.new-${specialist}`)

    let div = document.createElement('div')
    div.classList.add(specialist)

    let specH4 = document.createElement('h4')
    specH4.textContent = name

    let namesDiv = document.createElement('div')
    namesDiv.classList.add(`${specialist}-person`, 'person')

    div.append(specH4, namesDiv)

    let names1Input = document.createElement('input')
    names1Input.setAttribute('type', 'text')
    names1Input.setAttribute('placeholder', 'Имя')
    names1Input.setAttribute('name', `${specialist}_first_name_${count}`)
    names1Input.setAttribute('required', ``)

    let names2Input = document.createElement('input')
    names2Input.setAttribute('type', 'text')
    names2Input.setAttribute('placeholder', 'Фамилия')
    names2Input.setAttribute('name', `${specialist}_last_name_${count}`)
    names2Input.setAttribute('required', ``)

    namesDiv.append(names1Input, names2Input)

    let specialistBirthdayDiv = document.createElement('div')
    specialistBirthdayDiv.classList.add(`${specialist}-date`)
    let specialistBirthdayH4 = document.createElement('h4')
    specialistBirthdayH4.textContent = `Дата рождения ${subname}:`
    let specialistBirthdayInput = document.createElement('input')
    specialistBirthdayInput.setAttribute('type', 'date')
    specialistBirthdayInput.setAttribute('value', '01.08.1998')
    specialistBirthdayInput.setAttribute('name', `${specialist}_birthday_${count}`)
    specialistBirthdayInput.setAttribute('required', '')

    specialistBirthdayDiv.append(specialistBirthdayH4, specialistBirthdayInput)

    let biographyDiv = document.createElement('div')
    biographyDiv.classList.add(`biography-${specialist}`, 'textarea')
    let biographyH4 = document.createElement('h4')
    biographyH4.textContent = `Биография/Фильмография ${subname}:`
    let biographyTextArea = document.createElement('textarea')
    biographyTextArea.setAttribute('spellcheck', 'true')
    biographyTextArea.setAttribute('title', 'до 25 слов')
    biographyTextArea.setAttribute('autocapitalize', 'sentences')
    biographyTextArea.setAttribute('cols', '30')
    biographyTextArea.setAttribute('rows', '10')
    biographyTextArea.setAttribute('required', '')
    biographyTextArea.setAttribute('name', `${specialist}_biography_${count}`)

    biographyDiv.append(biographyH4, biographyTextArea)

    let addButton = document.createElement('div')
    addButton.classList.add('speciality-add')
    let addButtonA = document.createElement('a')
    addButtonA.classList.add('btn', 'speciality-add__btn')
    addButtonA.setAttribute('id', `${specialist}_add`)
    addButtonA.setAttribute('data-count', `${Number(count) + 1}`)
    // addButtonA.setAttribute("data-type", "add")
    let addSpan = document.createElement('span')
    addSpan.setAttribute("data-type", "add")
    addSpan.textContent = "+"
    addButtonA.append(addSpan)

    addButton.append(addButtonA)

    specialist_block.append(
        div,
        specialistBirthdayDiv,
        biographyDiv,
        addButton
    )
}

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

function createGenre(block, data) {

    let ul = document.createElement('ul')
    ul.classList.add('genre-add__list')

    let li = document.createElement('li')
    li.classList.add('genre-add__item')

    let checkbox_ul = document.createElement('ul')
    checkbox_ul.classList.add('application-checkboxs', 'genre__sub-item')

    data.forEach(item => {
        let li = document.createElement('li')
        li.classList.add('application-checkbox', 'checkbox', 'genre__item-submenu')
        let input = document.createElement('input')
        input.setAttribute('type', 'checkbox')
        input.setAttribute('value', item.slug)
        input.setAttribute('name', 'genre')
        input.setAttribute('id', `genre_${item.pk}`)

        let label = document.createElement('label')
        label.setAttribute('for', `genre_${item.pk}`)
        label.textContent = item.name

        li.append(input, label)
        checkbox_ul.append(li)
    })

    li.append(checkbox_ul)

    ul.append(li)

    // nav.append(ul)

    block.append(ul)
    // console.log(block)
}

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
        if (element.name === 'category') {
            if (show_list_genres.includes(element.dataset.type)) {
                // console.log(element.name, 'genre')
                genre_body.innerHTML = "";
                createGenre(genre_body, genres_1);
            } else {
                genre_body.innerHTML = "";
                createGenre(genre_body, genres_2);
            }
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
        // console.log(individualButton)
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
        // console.log(child_id)
        compositor.style.display = 'block'
        compositor.querySelectorAll('input').forEach((compositor_input) => {
            compositor_input.setAttribute('required', '')
            compositor_input.value = ''
        })
    } else if (child_id.value === '0') {
        document.getElementById('false-music').setAttribute('required', '')
        document.getElementById('true-music').removeAttribute('required')
        // console.log(compositor)
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

//  Съемочная группа - первый элемент

let add_specialists = document.querySelectorAll('.btn.speciality-add__btn')

add_specialists.forEach((add) => {
    add.addEventListener('click', (e) => {
        console.log(add.id)
        let block_id = add.id.split('_')[0]
        let specialist = specialists_id[block_id].specialist
        let name = specialists_id[block_id].name
        let subname = specialists_id[block_id].subname
        if (!sub_spec.includes(block_id)) {
            createSpecialistBlock(specialist, name, subname)
        } else {
            createSubSpecialistBlock(specialist, name)
        }
    })
})

//  Съемочная группа - след. элементы
let shooting_group = document.querySelector('.film-grew')
shooting_group.addEventListener('click', (e) => {
    // console.log(e.target.dataset.type)
    if (e.target.dataset.type === 'add') {
        let block_id = e.target.parentNode.id.split('_')[0]
        let specialist = specialists_id[block_id].specialist
        let name = specialists_id[block_id].name
        let subname = specialists_id[block_id].subname
        if (!sub_spec.includes(block_id)) {
            createSpecialistBlock(specialist, name, subname)
        } else {
            createSubSpecialistBlock(specialist, name)
        }

    }
})