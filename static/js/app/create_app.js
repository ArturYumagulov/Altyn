function createInvite(count) {

    let specialist_region_class = document.createElement('div')
    specialist_region_class.classList.add(`specialist-region`)
    specialist_region_class.id = `specialist-region_${count}`

    let Emailh4 = document.createElement('h4')
    Emailh4.textContent = "Email:"

    let EmailInput = document.createElement('input')
    EmailInput.setAttribute('name', `invite_email_${count}`)
    EmailInput.setAttribute('type', 'email')
    EmailInput.setAttribute('placeholder', 'Email:')

    let NameH4 = document.createElement('h4')
    NameH4.textContent = "Имя Фамилия:"

    let specialist_name_div = document.createElement('div')
    specialist_name_div.classList.add('specialist-region__person', 'person')

    let first_name_input = document.createElement('input')
    let last_name_input = document.createElement('input')

    first_name_input.setAttribute('name', `invite_first_name_${count}`)
    first_name_input.setAttribute('type', 'text')
    first_name_input.setAttribute('placeholder', 'Имя')

    last_name_input.setAttribute('name', `invite_last_name_${count}`)
    last_name_input.setAttribute('type', 'text')
    last_name_input.setAttribute('placeholder', 'Фамилия')

    specialist_name_div.append(first_name_input, last_name_input)

    let whoIsH4 = document.createElement('h4')
    whoIsH4.textContent = 'Кем является этот человек на вашем проекте? (фильме, который вы подаёте на кинопремию).'

    let whoIsInput = document.createElement('input')
    whoIsInput.setAttribute('name', `invite_who_is_${count}`)
    whoIsInput.setAttribute('type', 'text')

    let inviteH4 = document.createElement('h4')
    inviteH4.classList.add('application-subtitle')
    inviteH4.textContent = "Отправить приглашение ещё одному члену съемочной команды"

    let inviteUl = document.createElement('ul')
    inviteUl.classList.add('application-checkboxs')

    let inviteUlLi = document.createElement('li')
    inviteUlLi.classList.add('application-checkbox', 'checkbox')

    let inviteInput = document.createElement('input')
    inviteInput.classList.add('send-invite')
    inviteInput.setAttribute('id', `send_invite_${count + 1}`)
    inviteInput.setAttribute('type', 'checkbox')

    let inviteInputLabel = document.createElement('label')
    inviteInputLabel.textContent = "Отправить"
    inviteInputLabel.setAttribute('for', `send_invite_${count + 1}`)

    inviteUlLi.append(inviteInput, inviteInputLabel)
    inviteUl.append(inviteUlLi)

    let inviteP = document.createElement('p')
    inviteP.classList.add('send-invitation__text')
    inviteP.textContent = "Отправление приглашения члену съемочной команды даёт возможность расширить базу " +
        "специалистов, а также расширить информацию о вашем фильме в кинотеке."

    specialist_region_class.append(
        Emailh4,
        EmailInput,
        NameH4,
        specialist_name_div,
        whoIsH4,
        whoIsInput,
        inviteH4,
        inviteUl
    )
    inviteBody.append(specialist_region_class)
}


function create_person_inputs(block) {
    let first_name = document.createElement('input')
    first_name.setAttribute('text', 'text')
    first_name.setAttribute('placeholder', 'Фамилия')
    first_name.setAttribute('name', 'contract_first_name')
    first_name.setAttribute('required', '')

    let last_name = document.createElement('input')
    last_name.setAttribute('text', 'text')
    last_name.setAttribute('placeholder', 'Имя')
    last_name.setAttribute('name', 'contract_last_name')
    last_name.setAttribute('required', '')

    let surname = document.createElement('input')
    surname.setAttribute('text', 'text')
    surname.setAttribute('placeholder', 'Отчество')
    surname.setAttribute('name', 'contract_surname')
    surname.setAttribute('required', '')

    block.append(first_name, last_name, surname)

    // return first_name.append(first_name, last_name, surname)
}


function createIndividualBlock() {
    let main = document.querySelector('.individual-block')

    let mainH3 = document.createElement('h3')
    mainH3.classList.add('application-title')
    mainH3.textContent = "Физическое лицо"
    mainH3.setAttribute('style', 'margin-top: 15px')

    let mainH4 = document.createElement('h4')
    mainH4.textContent = "Фамилия Имя Отчество правообладателя"

    let mainSpan = document.createElement('span')
    mainSpan.classList.add('agreement-subtitle')
    mainSpan.textContent = "в именительном падеже"

    let person_individual_block = document.createElement('div')
    person_individual_block.classList.add('individual-person', 'person')
    create_person_inputs(person_individual_block)

    let movie_nameH4 = document.createElement('h4')
    movie_nameH4.classList.add('application-title')
    movie_nameH4.textContent = "Название фильма"

    let movie_span = document.createElement('span')
    movie_span.textContent = 'без кавычек'

    let movie_input = document.createElement('input')
    movie_input.setAttribute('type', 'text')
    movie_input.setAttribute('name', 'movie_name')
    movie_input.setAttribute('required', '')


    let passport_H4 = document.createElement('h4')
    passport_H4.classList.add('application-subtitle')
    passport_H4.textContent = "Номер и серия паспорта"

    let passport_input = document.createElement('input')
    passport_input.setAttribute('type', 'text')
    passport_input.setAttribute('name', 'passport_number')

    let birthdayH4 = document.createElement('h4')
    birthdayH4.classList.add('application-subtitle')
    birthdayH4.textContent = "Дата рождения:"

    let birthdayInput = document.createElement('input')
    birthdayInput.setAttribute('type', 'date')
    birthdayInput.setAttribute('value', '01.08.1998')
    birthdayInput.setAttribute('name', 'contract_birthday')

    main.append(
        mainH3,
        mainH4,
        mainSpan,
        person_individual_block,
        passport_H4,
        passport_input,
        birthdayH4,
        birthdayInput,
        movie_nameH4,
        movie_span,
        movie_input,
    )
}


function createLegalBlock() {
    let main = document.querySelector('.legal-entity')

    let mainH3 = document.createElement('h3')
    mainH3.classList.add('application-title')
    mainH3.textContent = "Юридическое лицо"

    let entityDiv = document.createElement('div')
    entityDiv.classList.add('entity')

    let org_nameH4 = document.createElement('h4')
    org_nameH4.textContent = 'Наименование организации:'
    let entitySpan = document.createElement('span')
    entitySpan.classList.add('agreement-subtitle')
    entitySpan.textContent = "В соответствии с уставом/лицензией"
    let entityInput = document.createElement('input')
    entityInput.setAttribute('type', 'text')
    entityInput.setAttribute('name', 'organization_name')

    entityDiv.append(org_nameH4, entitySpan, entityInput)

    let div = document.createElement('div')

    let divH4 = document.createElement('h4')
    divH4.classList.add('application-subtitle')
    divH4.textContent = "Фамилия Имя Отчество: "

    let divSpan = document.createElement('span')
    divSpan.classList.add('agreement-subtitle')
    divSpan.textContent = 'В соответствии с уставом/лицензией'

    let divSubDiv = document.createElement('div')
    divSubDiv.classList.add('legal-person', 'person')
    create_person_inputs(divSubDiv)

    div.append(divH4, divSpan, divSubDiv)

    let MovieNameDiv = document.createElement('div')
    let movieNameH4 = document.createElement('h4')
    movieNameH4.textContent = 'Название фильма:'
    let movieNameSpan = document.createElement('span')
    movieNameSpan.textContent = "(без кавычек)"

    let movieNameInput = document.createElement('input')
    movieNameInput.setAttribute('type', 'text')
    movieNameInput.setAttribute('name', 'movie_name')

    MovieNameDiv.append(movieNameH4, movieNameSpan, movieNameInput)

    let addressH4 = document.createElement('h4')
    addressH4.classList.add('agreement-subtitle')
    addressH4.textContent = "Адрес регистрации (индекс, регион, населенный пункт, улица, дом)"

    let addressTextAreaDiv = document.createElement('div')
    addressTextAreaDiv.classList.add('textarea')
    addressTextAreaDiv.innerHTML = `<textarea spellcheck="true" title="до 25 слов" ` +
    `autocapitalize="sentences" name="address" cols="30" placeholder="" rows="10"></textarea> </div>` +
    `<div><h4 class="agreement-subtitle">ИНН / КПП</h4><input type="text" name="inn"></div>` +
`<div><h4>Расчётный счёт: </h4><input type="number" name="payroll"></div><div><h4>Название банка: </h4>` +
`<input type="text" name="bank"></div><div><h4>БИК: </h4><input type="number" name="bik">` +
`</div><div><h4>Коррекционный счет: </h4> <input type="number" name="correction">`

    main.append(
        mainH3,
        entityDiv,
        div,
        MovieNameDiv,
        addressH4,
        addressTextAreaDiv
    )
}