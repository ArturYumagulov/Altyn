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

function valid_data(element) {
    let feedback = element.parentElement.children[1]

    if (lenValidValue(element.value)) {
        if (element.value.match(EMAIL)) {
            element.classList.remove('is-invalid')
            feedback.style.display = 'none'
            return Boolean(true)
        } else {
            element.classList.add('is-invalid')
            feedback.style.display = 'block'
            feedback.innerHTML = 'Проверьте правильность введенных данных'
            return Boolean(false)
        }
        return Boolean (true)
    } else {
        element.classList.add('is-invalid')
        feedback.style.display = 'block'
        feedback.innerHTML = 'Данное поле не может быть пустым'
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
        valid_data(input)
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
    }

    // let response = register_fetch({
    //     'email': email.val{}ue,
    //     'phone': phone.value,
    //     'password1': password1.value,
    //  if    'password2': password2.value,
    //     'type': 'is_looking'
    // })

    // register_data.then((res) => res.json().then((result)=> {
    //     console.log(result)
    // }))
})
