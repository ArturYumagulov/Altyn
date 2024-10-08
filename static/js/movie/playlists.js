const playlists_block = document.querySelector('.playlist-block')
const playlist_btn = document.querySelector('.playlist-btn')
const playlist_url = playlist_btn.getAttribute('data-playlist')
const add_playlist = document.querySelector('.add-playlist')
const add_playlist_input = document.querySelector('.add-playlist-input')

function createPlaylistElement(block, pk, name, has){
    let li = document.createElement('li')
    li.classList.add('application-checkbox', 'checkbox', 'genre__item-submenu')

    let input = document.createElement('input')
    input.setAttribute('type', 'checkbox')
    input.classList.add('playlist-result')
    input.setAttribute('id', pk)
    input.setAttribute('value', pk)
    if (has) {
        input.checked = true
    }

    let label = document.createElement('label')
    label.setAttribute('for', pk)
    label.textContent = name

    li.append(input, label)
    block.append(li)
}

playlist_btn.addEventListener('click', (e) => {
    if (e.target.parentElement.classList.contains('_active')) {
        fetch(`${playlist_url}`, {
            method: "POST", headers: {
                'content-type': 'application/json',
                "X-CSRFToken": csrf,
            }, body: JSON.stringify({slug: movie_slug})
        }).then(response => response.json()).then(data => {
            playlists_block.innerHTML = ""
            if (data.result) {
                if (data.playlists.length > 0) {
                    data.playlists.forEach(playlist => {
                        createPlaylistElement(playlists_block, playlist.pk, playlist.name, playlist.has_to_playlist)
                    })

                    let results = playlists_block.querySelectorAll('.playlist-result')

                    results.forEach(result => {
                        result.addEventListener('change', (e) => {
                            if (result.checked) {
                                fetch(add_to_playlist, {
                                    method: "POST", headers: {
                                        'content-type': 'application/json',
                                        "X-CSRFToken": csrf,
                                    }, body: JSON.stringify({slug: movie_slug, playlist_id: result.value})
                                }).then(response => response.json()).then(data => {
                                    if (!data.result) {
                                        result.checked = false;
                                    }
                                })
                            } else {
                                fetch(remove_from_playlist, {
                                    method: "POST", headers: {
                                        'content-type': 'application/json',
                                        "X-CSRFToken": csrf,
                                    }, body: JSON.stringify({slug: movie_slug, playlist_id: result.value})
                                }).then(response => response.json()).then(data => {
                                    result.checked = !data.result;
                                })

                            }
                        })
                    })

                } else {
                    playlists_block.innerHTML = "<p style='color: #ebebeb'>Вы не создали плейлистов</p>"
                }
            }
        })
    }
})

function cleanInput(){
    add_playlist_input.value = ""
}
add_playlist.addEventListener('click', () => {
    if (add_playlist_input.value.length > 0) {
        fetch(add_playlist_url, {
            method: "POST", headers: {
                'content-type': 'application/json',
                "X-CSRFToken": csrf,
            }, body: JSON.stringify({slug: movie_slug, playlist_name: add_playlist_input.value})
        }).then(response => response.json()).then(data => {
            if (data.result) {
                playlists_block.insertAdjacentHTML(
                    "afterbegin",
                    `<li class="application-checkbox checkbox genre__item-submenu">
                          <input type="checkbox" checked id="${data.playlist_pk}" class="playlist-result">
                          <label for="${data.playlist_pk}">${add_playlist_input.value}</label></li>`)
                add_playlist_input.value = `плейлист создан`
                setTimeout(cleanInput, 2000)
            } else {
                console.error("Ошибка при получении результата")
            }
        })
    }
})