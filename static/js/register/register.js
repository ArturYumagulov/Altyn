const EMAIL = /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)/g;

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
    return element.length > 0;
}

function inValid(element, text=null) {
    let feedback = element.parentElement.children[1]
    element.classList.add('is-invalid')
    feedback.style.display = 'block'
    feedback.innerHTML = text
}

function valid(element) {
    let feedback = element.parentElement.children[1]
    element.classList.remove('is-invalid')
    feedback.style.display = 'none'
    feedback.innerHTML = ''

}

function valid_data(element, reg) {

    if (lenValidValue(element.value)) {
        if (element.value.match(reg)) {
            valid(element)
            return Boolean(true)
        } else {
            inValid(element, 'Проверьте правильность введенных данных')
            return Boolean(false)
        }
        // return Boolean (true)
    } else {
        inValid(element, 'Данное поле не может быть пустым')
        return Boolean(false)
    }
}

function valid_fetch(value) {
    let feedback = value.parentElement.children[1]
    let valid = valid_fetch_response({'type': value.type, 'value': value.value})
    valid.then((res) => res.json().then((result) => {
        if(result.result) {
            value.classList.add('is-invalid')
            feedback.style.display = 'block'
            feedback.innerHTML = result.text
            return Boolean(false)
        } else {
            value.classList.remove('is-invalid')
            feedback.style.display = 'none'
            feedback.innerHTML = ''
            return Boolean(true)
        }
    }))

}

function blur_valid_input(element){
    element.addEventListener('blur', () => {
        return valid_fetch(element)
    })
}

function get_form_input(form) {
    let list = form.querySelectorAll('input')
    for (let i = 0; i < list.length; i++) {
        let input = list[i]
        blur_valid_input(input)
        valid_data(input, EMAIL)
    }
    return false;
}

let look_form = document.getElementById('look-form')
let look_btn = document.getElementById('look-btn')
look_form.addEventListener('submit', (e) => {

    e.preventDefault()
    get_form_input(look_form)

    if (get_form_input(look_form)) {
        console.log(true)
    } else {
        console.log(false)
    }
}, false)
