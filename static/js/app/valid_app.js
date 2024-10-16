let form = document.querySelector('form')

const requred_fields = [
    'name', 'debut', 'kind', 'category', 'timing', 'logline', 'year', 'rolled_certificate', 'age_limit', ''
]

form.addEventListener('submit', (e) => {
    e.preventDefault()
    console.log('submit')
    form.querySelectorAll('input').forEach(input => {
        console.log(input.name, 'name')
    })
    // form.submit()
})