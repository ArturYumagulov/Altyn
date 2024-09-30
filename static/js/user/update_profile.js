const edit = document.querySelector('.personalAccount-information__title')
const main_contact = document.querySelector('.personalAccount-information')
let save = document.querySelector('.save>button')
let form = document.querySelector('.contact-form')
const emailError = document.getElementById('email_error')
const phoneError = document.getElementById('phone_error')
const verify_error = document.getElementById('verify_error')

function changeTag(element, newTag) {
    // Создаем новый элемент с новым тегом
    const newElement = document.createElement(newTag);

    // Копируем все атрибуты из старого элемента в новый
    for (const attr of element.attributes) {
        newElement.setAttribute(attr.name, attr.value);
    }

    // Копируем содержимое (текст или HTML) старого элемента в новый
    newElement.innerHTML = element.innerHTML;

    // Заменяем старый элемент на новый
    element.parentNode.replaceChild(newElement, element);

    return newElement; // Возвращаем новый элемент, если нужно работать с ним дальше
}


function validateProfileData(email, phone, birthDate, gender) {

    // Валидация email
    if (!emailRegex.test(email)) {
        return {valid: false, message: "Неверный формат email"};
    }

    // Валидация телефона
    if (!phoneRegex.test(phone)) {
        return {valid: false, message: "Неверный формат телефона"};
    }

    // Если все данные валидны
    return {valid: true, message: "Данные валидны"};
}


// Подтверждение емайл
async function verifyEmail(email) {
    let verify_block = document.querySelector('.verify-block')
    let email_input = document.querySelector('.email')

    fetch(email_verify, {
        method: "POST", headers: {"X-CSRFToken": csrf}, body: JSON.stringify({
            "email": email_input.value,
        })

    });

    email_input.style.display = 'none'
    verify_block.style.display = 'block'
}

async function isPhoneExist(phone) {
    try {
        const response = await fetch(edit_user_phone, {
            method: "POST", headers: {"X-CSRFToken": csrf}, body: JSON.stringify({
                "phone": phone,
                'type': 'phone'
            })
        });
        const result = await response.json();
        return result.exists;
    } catch (error) {
        console.error('Ошибка при проверке телефона:', error.message);
        return false;
    }
}

async function verify_code(code, email, old_email) {
    if (email !== old_email) {
        try {
            const response = await fetch(verify_code_url, {
                method: "POST", headers: {"X-CSRFToken": csrf}, body: JSON.stringify({
                    email: email,
                    code: code,
                })
            });
            const result = await response.json()
            return result.exists;
        } catch (error) {
            console.error('Ошибка при проверке кода:', error.message)
            return false;
        }
    } else {
        return true;
    }
}

async function isEmailExist(email) {
    try {
        const response = await fetch(edit_user_phone, {
            method: "POST", headers: {"X-CSRFToken": csrf}, body: JSON.stringify({
                "email": email,
                'type': 'email'
            })
        });
        const result = await response.json();
        return result.exists;
    } catch (error) {
        console.error('Ошибка при проверке email:', error.message);
        return false;
    }
}

async function updateProfile(email, phone, birthDate, gender, code, old_email) {
    // Валидация данных перед отправкой
    const validation = validateProfileData(email, phone, birthDate, gender);

    if (!validation.valid) {
        console.error(validation.message);
        return;
    }

    // Проверка существования email
    const emailExists = await isEmailExist(email);
    if (emailExists) {
        emailError.textContent = 'Email уже существует в базе данных'
        emailError.style.display = 'block'
        console.error('Email уже существует в базе данных');
        return;
    }

    let verify = await verify_code(code, email, old_email)
    if (!verify) {
        return;
    }


    // Проверка существования телефона
    const phoneExists = await isPhoneExist(phone);
    if (phoneExists) {
        phoneError.textContent = 'Телефон уже существует в базе данных'
        phoneError.style.display = 'block'
        console.error('Телефон уже существует в базе данных');
        return;
    }

    // Подготовка данных для отправки
    const data = {
        phone: phone,
        email: email,
        birthday: birthDate,
        male: gender
    };

    try {
        const response = await fetch(edit_user_profile, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                "X-CSRFToken": csrf
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Ошибка при обновлении профиля');
        }
        const result = await response.json();
        console.log('Профиль успешно обновлен:', result);
        location.reload()
    } catch (error) {
        console.error('Ошибка:', error.message);
    }
}


edit.addEventListener('click',
    (e) => {
        if (e.target.classList.contains('personalAccount-information__title')) {
            save.parentElement.style.display = 'block'

            // Email
            let email = main_contact.querySelector('.email')
            let verify_code_input = main_contact.querySelector('.verify_email')
            let email_value = email.innerHTML.trim()
            let new_email = changeTag(email, 'input')
            new_email.style.marginTop = '5px'
            new_email.value = email_value

            new_email.addEventListener('blur', (e) => {
                isEmailExist(new_email.value).then(
                    res => res
                ).then((data) => {
                    if (!data) {
                        verifyEmail(new_email.value)
                        verify_error.style.display = 'block'
                        verify_error.textContent = 'Вам на почту отправлен проверочный код'
                        emailError.style.display = 'none'
                        emailError.textContent = ""
                        verify_code_input.addEventListener('blur', () => {
                            if (verify_code_input.value.length > 0) {
                                fetch(verify_code_url, {
                                    method: "POST", headers: {"X-CSRFToken": csrf}, body: JSON.stringify({
                                        email: new_email.value,
                                        code: verify_code_input.value
                                    })
                                }).then(res => res.json()).then(data => {
                                    console.log(data, 'data')
                                    if (data.exists) {
                                        verify_error.textContent = 'Код верен'
                                        verify_error.classList.add('is-valid')
                                    } else {
                                        verify_error.textContent = "Код неверен"
                                        verify_error.classList.remove('is-valid')
                                    }
                                })
                            }
                        })
                    } else {
                        emailError.style.display = 'block'
                        emailError.textContent = "Такой email есть в базе данных"
                    }
                })
            })

            // Phone

            let phone = main_contact.querySelector('.phone')
            let phone_value = phone.innerHTML.trim()
            let new_phone = changeTag(phone, 'input')
            new_phone.style.marginTop = '5px'
            new_phone.value = phone_value
            // Birthday


            let birthday = main_contact.querySelector('.birthday')
            let new_birthday = changeTag(birthday, 'input')
            new_birthday.style.marginTop = '5px'
            new_birthday.setAttribute('type', 'date')
            new_birthday.value = birthday.dataset.date

            // Male
            let male_block = main_contact.querySelector('.male')
            let male_check_block = main_contact.querySelector('.male-check-block')
            male_block.style.display = 'none'
            male_check_block.style.display = 'block'

            save.addEventListener('click', (e) => {
                e.preventDefault()
                updateProfile(new_email.value, new_phone.value, new_birthday.value, male_type, verify_code_input.value, email_value)
            })
        }
    }
)