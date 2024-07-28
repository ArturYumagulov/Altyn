const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phoneRegex = /^(\+7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$/;
const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/
const url = window.location.search


function inValid(element, errorElement, text=null) {
    // добавляет классы невалидности
    element.classList.add('is-invalid')
    errorElement.style.display = 'block'
    errorElement.textContent = text
}

const thank = document.getElementById('popup-thank')
let thank_text = document.querySelector('#popup-thank .thank-text')
let thanks_btn = document.querySelector('.thank-btn')
const look_form = document.getElementById('look-form')

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

    emailInput.classList.remove('is-invalid')
    phoneInput.classList.remove('is-invalid')
    password1Input.classList.remove('is-invalid')
    password2Input.classList.remove('is-invalid')

    emailError.textContent = ''
    phoneError.textContent = ''
    password1Error.textContent = ''
    password2Error.textContent = ''
    thank_text.textContent = ''

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
