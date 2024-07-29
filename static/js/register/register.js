console.log('register')
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phoneRegex = /^(\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$/;
const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/
// const url = window.location.search


function inValid(element, errorElement, text = null) {
    // добавляет классы невалидности
    element.classList.add('is-invalid')
    errorElement.style.display = 'block'
    errorElement.textContent = text
}

function removeInvalidClass(elements) {
    // Удаляет класс невалидности
    elements.forEach(element => {
        element.classList.remove('is-invalid')
    })
}


function cleanTextContent(elements) {
    // Очищает текст ошибки

    elements.forEach(element => {
        element.textContent = ''
    })
}

const thank = document.getElementById('popup-thank')
let thank_text = document.querySelector('#popup-thank .thank-text')
let thanks_btn = document.querySelector('.thank-btn')

const look_form = document.getElementById('look-form')
const  take_form = document.getElementById('take-form')
const show_form = document.getElementById('show-form')
const organize_form = document.getElementById('organize-form')


look_form.addEventListener('submit', (e) => {
    e.preventDefault()

    const emailInput = look_form.querySelector('input[name=email]')
    const phoneInput = look_form.querySelector('input[name=phone]')
    const password1Input = look_form.querySelector('input[name=password1]')
    const password2Input = look_form.querySelector('input[name=password2]')

    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const password1 = password1Input.value.trim();
    const password2 = password2Input.value.trim();

    const emailError = look_form.querySelector('#emailError')
    const phoneError = look_form.querySelector('#phoneError')
    const password1Error = look_form.querySelector('#password1Error')
    const password2Error = look_form.querySelector('#password2Error')

    removeInvalidClass([emailInput, phoneInput, password1Input, password2Input])
    cleanTextContent([emailError, phoneError, password1Error, password2Error, thank_text])

    let hasError = false;

    if (!emailRegex.test(email)) {
        inValid(emailInput, emailError, 'Неверный формат email')
        hasError = true;
    }

    if (!phoneRegex.test(phone)) {
        inValid(phoneInput, phoneError, 'Неверный формат телефона')
        hasError = true;
    }
    if (!passwordRegex.test(password1)) {
        inValid(password1Input, password1Error, 'Пароль должен содержать минимум восемь символов, одну букву и одну цифру')
        hasError = true;
    }
    if (password1 !== password2) {
        inValid(password2Input, password2Error, 'Пароли не совпадают')
        hasError = true;
    }
    if (hasError) {
        return;
    }

    fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {email: email, phone: phone})
    })
        .then(response => response.json())
        .then(data => {
            if (data.emailExists) {
                inValid(emailInput, emailError, 'Email уже зарегистрирован')
            }
            if (data.phoneExists) {
                inValid(phoneInput, phoneError, 'Телефон уже зарегистрирован')
            }
            if (!data.emailExists && !data.phoneExists) {
                fetch('/users/register/', {
                    method: 'POST',
                    headers: {"X-CSRFToken": csrf},
                    body: JSON.stringify(
                        {type: 'is_looking', email: email, phone: phone, password: password2})
                })
                    .then(res => res.json())
                    .then(result => {
                        console.log(result)
                        if (result.result) {
                            thank.classList.add('open')
                            thank_text.textContent = 'Вы успешно зарегистрировались. На ваш email отправлена ссылка на подтверждение!'

                            if (url.length > 0) {
                                let clean_url = url.slice(1).split('&')
                                clean_url.forEach((param) => {
                                    if (param.split('=')[0] === 'next') {
                                        thanks_btn.innerHTML = 'Продолжить'
                                        thanks_btn.setAttribute('href', `${param.split('=')[1]}`)
                                    }
                                })
                            } else {
                                thanks_btn.innerHTML = 'Закрыть'
                                thanks_btn.setAttribute('href', window.location.pathname)
                            }
                        }
                    })
                    .catch(
                        error => {
                            console.error('Error:', error);
                            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
                            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
                        }
                    )
            }
        })
        .catch(error => {
            console.error('Error:', error);
            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
        })
})

take_form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('take')

    const emailInput = take_form.querySelector('input[name=email]')
    const phoneInput = take_form.querySelector('input[name=phone]')
    const password1Input = take_form.querySelector('input[name=password1]')
    const password2Input = take_form.querySelector('input[name=password2]')

    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const password1 = password1Input.value.trim();
    const password2 = password2Input.value.trim();

    const emailError = take_form.querySelector('#emailError')
    const phoneError = take_form.querySelector('#phoneError')
    const password1Error = take_form.querySelector('#password1Error')
    const password2Error = take_form.querySelector('#password2Error')

    removeInvalidClass([emailInput, phoneInput, password1Input, password2Input])
    cleanTextContent([emailError, phoneError, password1Error, password2Error, thank_text])

    let hasError = false;

    if (!emailRegex.test(email)) {
        inValid(emailInput, emailError, 'Неверный формат email')
        hasError = true;
    }

    if (!phoneRegex.test(phone)) {
        inValid(phoneInput, phoneError, 'Неверный формат телефона')
        hasError = true;
    }
    if (!passwordRegex.test(password1)) {
        inValid(password1Input, password1Error, 'Пароль должен содержать минимум восемь символов, одну букву и одну цифру')
        hasError = true;
    }
    if (password1 !== password2) {
        inValid(password2Input, password2Error, 'Пароли не совпадают')
        hasError = true;
    }
    if (hasError) {
        return;
    }

    fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {email: email, phone: phone})
    })
        .then(response => response.json())
        .then(data => {
            if (data.emailExists) {
                inValid(emailInput, emailError, 'Email уже зарегистрирован')
            }
            if (data.phoneExists) {
                inValid(phoneInput, phoneError, 'Телефон уже зарегистрирован')
            }
            if (!data.emailExists && !data.phoneExists) {
                fetch('/users/register/', {
                    method: 'POST',
                    headers: {"X-CSRFToken": csrf},
                    body: JSON.stringify(
                        {type: 'is_shooting', email: email, phone: phone, password: password2})
                })
                    .then(res => res.json())
                    .then(result => {
                        console.log(result)
                        if (result.result) {
                            thank.classList.add('open')
                            thank_text.textContent = 'Вы успешно зарегистрировались. На ваш email отправлена ссылка на подтверждение!'

                            if (url.length > 0) {
                                let clean_url = url.slice(1).split('&')
                                clean_url.forEach((param) => {
                                    if (param.split('=')[0] === 'next') {
                                        thanks_btn.innerHTML = 'Продолжить'
                                        thanks_btn.setAttribute('href', `${param.split('=')[1]}`)
                                    }
                                })
                            } else {
                                thanks_btn.innerHTML = 'Закрыть'
                                thanks_btn.setAttribute('href', window.location.pathname)
                            }
                        }
                    })
                    .catch(
                        error => {
                            console.error('Error:', error);
                            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
                            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
                        }
                    )
            }
        })
        .catch(error => {
            console.error('Error:', error);
            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
        })
})


take_form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('take')

    const emailInput = take_form.querySelector('input[name=email]')
    const phoneInput = take_form.querySelector('input[name=phone]')
    const password1Input = take_form.querySelector('input[name=password1]')
    const password2Input = take_form.querySelector('input[name=password2]')

    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const password1 = password1Input.value.trim();
    const password2 = password2Input.value.trim();

    const emailError = take_form.querySelector('#emailError')
    const phoneError = take_form.querySelector('#phoneError')
    const password1Error = take_form.querySelector('#password1Error')
    const password2Error = take_form.querySelector('#password2Error')

    removeInvalidClass([emailInput, phoneInput, password1Input, password2Input])
    cleanTextContent([emailError, phoneError, password1Error, password2Error, thank_text])

    let hasError = false;

    if (!emailRegex.test(email)) {
        inValid(emailInput, emailError, 'Неверный формат email')
        hasError = true;
    }

    if (!phoneRegex.test(phone)) {
        inValid(phoneInput, phoneError, 'Неверный формат телефона')
        hasError = true;
    }
    if (!passwordRegex.test(password1)) {
        inValid(password1Input, password1Error, 'Пароль должен содержать минимум восемь символов, одну букву и одну цифру')
        hasError = true;
    }
    if (password1 !== password2) {
        inValid(password2Input, password2Error, 'Пароли не совпадают')
        hasError = true;
    }
    if (hasError) {
        return;
    }

    fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {email: email, phone: phone})
    })
        .then(response => response.json())
        .then(data => {
            if (data.emailExists) {
                inValid(emailInput, emailError, 'Email уже зарегистрирован')
            }
            if (data.phoneExists) {
                inValid(phoneInput, phoneError, 'Телефон уже зарегистрирован')
            }
            if (!data.emailExists && !data.phoneExists) {
                fetch('/users/register/', {
                    method: 'POST',
                    headers: {"X-CSRFToken": csrf},
                    body: JSON.stringify(
                        {type: 'is_shooting', email: email, phone: phone, password: password2})
                })
                    .then(res => res.json())
                    .then(result => {
                        console.log(result)
                        if (result.result) {
                            thank.classList.add('open')
                            thank_text.textContent = 'Вы успешно зарегистрировались. На ваш email отправлена ссылка на подтверждение!'

                            if (url.length > 0) {
                                let clean_url = url.slice(1).split('&')
                                clean_url.forEach((param) => {
                                    if (param.split('=')[0] === 'next') {
                                        thanks_btn.innerHTML = 'Продолжить'
                                        thanks_btn.setAttribute('href', `${param.split('=')[1]}`)
                                    }
                                })
                            } else {
                                thanks_btn.innerHTML = 'Закрыть'
                                thanks_btn.setAttribute('href', window.location.pathname)
                            }
                        }
                    })
                    .catch(
                        error => {
                            console.error('Error:', error);
                            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
                            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
                        }
                    )
            }
        })
        .catch(error => {
            console.error('Error:', error);
            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
        })
})


show_form.addEventListener('submit', (e)=> {
    e.preventDefault()
    const lastnameInput = show_form.querySelector('input[name=last_name]')
    const firstnameInput = show_form.querySelector('input[name=first_name]')
    const surnameInput = show_form.querySelector('input[name=surname]')
    const emailInput = show_form.querySelector('input[name=email]')
    const phoneInput = show_form.querySelector('input[name=phone]')
    const companyNameInput = show_form.querySelector('input[name=company_name]')
    const siteInput = show_form.querySelector('input[name=site]')
    const password1Input = show_form.querySelector('input[name=password1]')
    const password2Input = show_form.querySelector('input[name=password2]')

    const lastname = lastnameInput.value.trim();
    const firstname = firstnameInput.value.trim();
    const surname = surnameInput.value.trim();
    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const companyName = companyNameInput.value.trim();
    const site = siteInput.value.trim();
    const password1 = password1Input.value.trim();
    const password2 = password2Input.value.trim();

    const lastnameError = show_form.querySelector('#lastnameError')
    const firstnameError = show_form.querySelector('#first_nameError')
    const surnameError = show_form.querySelector('#surnameError')
    const emailError = show_form.querySelector('#emailError')
    const phoneError = show_form.querySelector('#phoneError')
    const companyNameError= show_form.querySelector('#company_nameError')
    const siteError = show_form.querySelector('#siteError')
    const password1Error = show_form.querySelector('#password1Error')
    const password2Error = show_form.querySelector('#password1Error')

    removeInvalidClass([
        lastnameInput,
        firstnameInput,
        surnameInput,
        emailInput,
        phoneInput,
        companyNameInput,
        siteInput,
        password1Input,
        password2Input
    ])
    cleanTextContent([
        lastnameError,
        firstnameError,
        surnameError,
        emailError,
        phoneError,
        companyNameError,
        siteError,
        password1Error,
        password2Error,
        thank_text
    ])

    let hasError = false;

    if (lastname === '') {
        inValid(lastnameInput, lastnameError, 'Укажите фамилию')
        hasError = true;
    }

    if (firstname === '') {
        inValid(firstnameInput, firstnameError, 'Укажите имя')
        hasError = true;
    }

    if (surname === '') {
        inValid(surnameInput, surnameError, 'Укажите отчество')
        hasError = true;
    }

    if (!emailRegex.test(email)) {
        inValid(emailInput, emailError, 'Неверный формат email')
        hasError = true;
    }

    if (!phoneRegex.test(phone)) {
        inValid(phoneInput, phoneError, 'Неверный формат телефона')
        hasError = true;
    }

    if (companyName === '') {
        inValid(companyNameInput, companyNameError, 'Укажите название компании')
        hasError = true;
    }

    if (site === '') {
        inValid(siteInput, siteError, 'Укажите сайт компании')
        hasError = true;
    }

    if (!passwordRegex.test(password1)) {
        inValid(password1Input, password1Error, 'Пароль должен содержать минимум восемь символов, одну букву и одну цифру')
        hasError = true;
    }
    if (password1 !== password2) {
        inValid(password2Input, password2Error, 'Пароли не совпадают')
        hasError = true;
    }
    if (hasError) {
        return;
    }

    fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {email: email, phone: phone})
    })
        .then(response => response.json())
        .then(data => {
            if (data.emailExists) {
                inValid(emailInput, emailError, 'Email уже зарегистрирован')
            }
            if (data.phoneExists) {
                inValid(phoneInput, phoneError, 'Телефон уже зарегистрирован')
            }
            if (!data.emailExists && !data.phoneExists) {
                fetch('/users/register/', {
                    method: 'POST',
                    headers: {"X-CSRFToken": csrf},
                    body: JSON.stringify(
                        {
                            type: 'is_show',
                            email: email,
                            phone: phone,
                            password: password2,
                            lastname: lastname,
                            firstname: firstname,
                            surname: surname,
                            companyName: companyName,
                            site: site,
                        })
                })
                    .then(res => res.json())
                    .then(result => {
                        console.log(result)
                        if (result.result) {
                            thank.classList.add('open')
                            thank_text.textContent = 'Вы успешно зарегистрировались. На ваш email отправлена ссылка на подтверждение!'

                            if (url.length > 0) {
                                let clean_url = url.slice(1).split('&')
                                clean_url.forEach((param) => {
                                    if (param.split('=')[0] === 'next') {
                                        thanks_btn.innerHTML = 'Продолжить'
                                        thanks_btn.setAttribute('href', `${param.split('=')[1]}`)
                                    }
                                })
                            } else {
                                thanks_btn.innerHTML = 'Закрыть'
                                thanks_btn.setAttribute('href', window.location.pathname)
                            }
                        }
                    })
                    .catch(
                        error => {
                            console.error('Error:', error);
                            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
                            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
                        }
                    )
            }
        })
        .catch(error => {
            console.error('Error:', error);
            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
        })


})


organize_form.addEventListener('submit', (e)=> {
    e.preventDefault()
    const lastnameInput = organize_form.querySelector('input[name=last_name]')
    const firstnameInput = organize_form.querySelector('input[name=first_name]')
    const surnameInput = organize_form.querySelector('input[name=surname]')
    const emailInput = organize_form.querySelector('input[name=email]')
    const phoneInput = organize_form.querySelector('input[name=phone]')
    const platformNameInput = organize_form.querySelector('input[name=platform_name]')
    const siteInput = organize_form.querySelector('input[name=site]')
    const password1Input = organize_form.querySelector('input[name=password1]')
    const password2Input = organize_form.querySelector('input[name=password2]')

    const lastname = lastnameInput.value.trim();
    const firstname = firstnameInput.value.trim();
    const surname = surnameInput.value.trim();
    const email = emailInput.value.trim();
    const phone = phoneInput.value.trim();
    const platformName = platformNameInput.value.trim();
    const site = siteInput.value.trim();
    const password1 = password1Input.value.trim();
    const password2 = password2Input.value.trim();

    const lastnameError = organize_form.querySelector('#lastnameError')
    const firstnameError = organize_form.querySelector('#first_nameError')
    const surnameError = organize_form.querySelector('#surnameError')
    const emailError = organize_form.querySelector('#emailError')
    const phoneError = organize_form.querySelector('#phoneError')
    const platformNameError= organize_form.querySelector('#platform_nameError')
    const siteError = organize_form.querySelector('#siteError')
    const password1Error = organize_form.querySelector('#password1Error')
    const password2Error = organize_form.querySelector('#password1Error')

    removeInvalidClass([
        lastnameInput,
        firstnameInput,
        surnameInput,
        emailInput,
        phoneInput,
        platformNameInput,
        siteInput,
        password1Input,
        password2Input
    ])
    cleanTextContent([
        lastnameError,
        firstnameError,
        surnameError,
        emailError,
        phoneError,
        platformNameError,
        siteError,
        password1Error,
        password2Error,
        thank_text
    ])

    let hasError = false;

    if (lastname === '') {
        inValid(lastnameInput, lastnameError, 'Укажите фамилию')
        hasError = true;
    }

    if (firstname === '') {
        inValid(firstnameInput, firstnameError, 'Укажите имя')
        hasError = true;
    }

    if (surname === '') {
        inValid(surnameInput, surnameError, 'Укажите отчество')
        hasError = true;
    }

    if (!emailRegex.test(email)) {
        inValid(emailInput, emailError, 'Неверный формат email')
        hasError = true;
    }

    if (!phoneRegex.test(phone)) {
        inValid(phoneInput, phoneError, 'Неверный формат телефона')
        hasError = true;
    }

    if (platformName === '') {
        inValid(platformNameInput, platformNameError, 'Укажите название площадки')
        hasError = true;
    }

    if (site === '') {
        inValid(siteInput, siteError, 'Укажите сайт компании')
        hasError = true;
    }

    if (!passwordRegex.test(password1)) {
        inValid(password1Input, password1Error, 'Пароль должен содержать минимум восемь символов, одну букву и одну цифру')
        hasError = true;
    }
    if (password1 !== password2) {
        inValid(password2Input, password2Error, 'Пароли не совпадают')
        hasError = true;
    }
    if (hasError) {
        return;
    }

    fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {email: email, phone: phone})
    })
        .then(response => response.json())
        .then(data => {
            if (data.emailExists) {
                inValid(emailInput, emailError, 'Email уже зарегистрирован')
            }
            if (data.phoneExists) {
                inValid(phoneInput, phoneError, 'Телефон уже зарегистрирован')
            }
            if (!data.emailExists && !data.phoneExists) {
                fetch('/users/register/', {
                    method: 'POST',
                    headers: {"X-CSRFToken": csrf},
                    body: JSON.stringify(
                        {
                            type: 'is_organize',
                            email: email,
                            phone: phone,
                            password: password2,
                            lastname: lastname,
                            firstname: firstname,
                            surname: surname,
                            platformName: platformName,
                            site: site,
                        })
                })
                    .then(res => res.json())
                    .then(result => {
                        console.log(result)
                        if (result.result) {
                            thank.classList.add('open')
                            thank_text.textContent = 'Вы успешно зарегистрировались. На ваш email отправлена ссылка на подтверждение!'

                            if (url.length > 0) {
                                let clean_url = url.slice(1).split('&')
                                clean_url.forEach((param) => {
                                    if (param.split('=')[0] === 'next') {
                                        thanks_btn.innerHTML = 'Продолжить'
                                        thanks_btn.setAttribute('href', `${param.split('=')[1]}`)
                                    }
                                })
                            } else {
                                thanks_btn.innerHTML = 'Закрыть'
                                thanks_btn.setAttribute('href', window.location.pathname)
                            }
                        }
                    })
                    .catch(
                        error => {
                            console.error('Error:', error);
                            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
                            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
                        }
                    )
            }
        })
        .catch(error => {
            console.error('Error:', error);
            inValid(emailInput, emailError, 'Во время проверки произошла ошибка')
            inValid(phoneInput, phoneError, 'Во время проверки произошла ошибка')
        })


})
