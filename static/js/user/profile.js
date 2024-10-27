const popup_thank = document.querySelector('.popup-thank')
const exit = document.querySelector('.exit-btn')
const thank_btn = popup_thank.querySelector('.thank-btn')
const popup_content = popup_thank.querySelector('.popup__content')
const close_popup = popup_thank.querySelector('.close-popup')

function exitProfile() {
    fetch(logout, {
        method: 'GET',
    }).then(response => response.json()).then(data => {
        if (data.detail) {
            document.location.href = "/"
        }
    })

}

function createThankText(block) {
    let div = document.createElement('div')
    div.classList.add('exit-block')

    let yes = document.createElement('a')
    yes.classList.add('form-btn', 'exit-thank-btn', 'yes')
    yes.textContent = "Да"

    div.append(yes)

    block.append(div)
}

function closeThank() {
    popup_thank.classList.remove('open')
    popup_content.removeChild(popup_content.lastElementChild)
}
exit.addEventListener('click', (e) => {
    popup_thank.classList.toggle('open');
    thank_text.textContent = "Вы уверены, что хотите выйти из учетной записи?"
    thank_btn.remove();
    createThankText(popup_content);

    let yes = popup_content.querySelector('.yes')
    let no =  popup_content.querySelector('.no')

    yes.addEventListener('click', (e) => {
        exitProfile();
    })
})

close_popup.addEventListener('click', (e) => {
    closeThank();
})

document.addEventListener("keydown", function(event) {
    if (event.key === "Escape") {
        closeThank();
    }
});
