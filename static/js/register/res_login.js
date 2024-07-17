let login_form = document.getElementById('login_form')
let button = document.querySelector('#login_form .form-btn')
// console.log(window.location.search)


function get_next_page(url) {
    if (window.location.search.length > 0) {
        let clean_url = url.slice(1).split('&')
        clean_url.forEach((param) => {
            if (param.split('=')[0] === 'next') {
                return `/${param.split('=')[1]}/`
            }
        })
    } else {
        return ('/')
    }
}


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
    let reg_popup = document.getElementById('popup-registration')

    lenValid(email_input)
    lenValid(password_input)

    LoadData(email_input.value, password_input.value).then((data)=> {
        if (data.result === 'login') {
            popup_thank.classList.add('open')
            thank_text.innerHTML = `Здравствуйте, ${data.user}. Вы успешно авторизовались!`
            thanks_btn.innerHTML = 'Вернуться'
            console.log(window.location.search)

            if (window.location.search.length > 0) {
                let clean_url = window.location.search.slice(1).split('&')
                clean_url.forEach((param) => {
                    if (param.split('=')[0] === 'next') {
                        thanks_btn.setAttribute('href', param.split('=')[1])
                    }
                })}

        } else if (data.result === 'no_active') {
            popup_thank.classList.add('open')
            thank_text.innerHTML = `Здравствуйте, ${data.user}. Ваша учетная запись еще не активированна`
        }
        else {
            console.log('error')
            popup_thank.classList.add('open')
            thank_text.innerHTML = 'Проверьте правильность логина и пароля. Если вы забыли пароль, <a href="/reset/" style="color: #d49e3d">восстановить</a>'
            thanks_btn.innerHTML = 'Зарегистрироваться'
            thanks_btn.classList.add('popup-link')
            thanks_btn.addEventListener('click', ()=> {
                console.log('click')
                popup_thank.classList.remove('open')
                reg_popup.classList.add('open')

            })
        }
    })
})

// get_next_page(window.location.search)

