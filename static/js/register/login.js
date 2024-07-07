let login_form = document.getElementById('login_form')
let button = document.querySelector('#login_form .form-btn')
console.log(window.location.href)


async function LoadData(username, password) {
    const [user] = await Promise.all([
        fetch(login_path, {
            method: 'POST',
            headers: {"X-CSRFToken": csrf},
            body: JSON.stringify({
                "email": username,
                "password": password
            })
        }),
    ]);
    return await user.json();
}

function invalidData (item_id) {
    document.getElementById(`${item_id}-feedback`).style.display = 'block'
    document.getElementById(item_id).classList.add('is-invalid')
}

function validData(item_id) {
    document.getElementById(`${item_id}-feedback`).style.display = 'none'
    document.getElementById(item_id).classList.remove('is-invalid')
}

function lenValid(element) {

    if (element.value.length === 0) {
        invalidData(element.id)
    } else {
        validData(element.id)
    }
}


login_form.addEventListener('submit', (e)=>{
    e.preventDefault()

    let popup_thank = document.getElementById('popup-thank')
    let thank_text = document.querySelector('#popup-thank .thank-text')
    let email_input = document.getElementById('email-input')
    let password_input = document.getElementById('password-input')
    let thanks_btn = document.querySelector('.thank-btn')

    lenValid(email_input)
    lenValid(password_input)

    LoadData(email_input.value, password_input.value).then((data)=> {
        if (data.result === 'login') {
            popup_thank.classList.add('open')
            thank_text.innerHTML = `Здравствуйте, ${data.user}. Вы успешно авторизовались!`
            thanks_btn.innerHTML = 'Закрыть'
            thanks_btn.setAttribute('href', window.location.pathname)
        } else if (data.result === 'no_active') {
            popup_thank.classList.add('open')
            thank_text.innerHTML = `Здравствуйте, ${data.user}. Ваша учетная запись еще не активированна`
        }
        else {
            console.log('error')
        }
    })
})
