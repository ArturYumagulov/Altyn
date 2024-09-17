let form = document.querySelector('form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('submit')
    form.submit()
})