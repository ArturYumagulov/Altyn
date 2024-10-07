const vote_btn = document.querySelector('.vote-btn')
async function sendVote(url){
    const response = fetch(`${url}`, {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify(
            {slug: movie_slug})

    }).then(res => res.json()).then(data => {
        if (data.result) {
            vote_btn.classList.add('voting-sending')
            vote_btn.textContent = "Проголосовано"
        }
    })
}

vote_btn.addEventListener('click', () => {
    sendVote(vote_btn.dataset.url);
})
