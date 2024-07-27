const EMAIL = /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)/g;

let VALID = false;

function register_fetch(data) {
    return fetch('/users/register/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(data)
    })
}


function valid_fetch_response(data) {
    return fetch('/users/valid-data/', {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(data)
    })
}

function lenValidValue(element) {
    // проверка на длину
    return element.length > 0;
}

function inValid(element, text=null) {
    // добавляет классы невалидности
    let feedback = element.parentElement.children[1]
    element.classList.add('is-invalid')
    feedback.style.display = 'block'
    feedback.innerHTML = text
}

function valid(element) {
    // удаляет классы невалидности
    let feedback = element.parentElement.children[1]
    element.classList.remove('is-invalid')
    feedback.style.display = 'none'
    feedback.innerHTML = ''

}
function reg_valid(element, reg) {
    // проверка на регулярку
    return element.value.match(reg)
}

function valid_data(element, reg) {

    if (lenValidValue(element.value) && reg_valid(element, reg)) {
        valid(element)
        return true;
    } else {
        inValid(element, 'Проверьте правильность введенных данных')
        return false;
    }
}


function blurValid(form) {
   // написать функцию проверки поля при блюре
}

let look_form = document.getElementById('look-form')

look_form.addEventListener('submit', (e) => {
    e.preventDefault()

    let list = look_form.querySelectorAll('input')

    for (let i = 0; i < list.length; i++) {
        let input = list[i]
        if (input.name === 'email') {
            valid_data(input, EMAIL)
        }
    }

})
