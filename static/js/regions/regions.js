let region_select = document.getElementById('regionselect')
let regions_resources = document.querySelector('.regionaresources-res')
const region_slug = new URLSearchParams(document.location.search).get('region');

function createScreeningPoints(main, data, region_slug) {
    function createArticle(block, item) {
        let article = document.createElement('article')
        article.classList.add('card', 'filmlocations-card')

        let filmlocations_img = document.createElement('div')
        filmlocations_img.classList.add('filmlocations__img')

        let figure = document.createElement('figure')

        let img = document.createElement('img')
        img.setAttribute('alt', item.name)
        img.setAttribute('src', '/media/'+ item.image)

        figure.append(img)
        filmlocations_img.append(figure)

        let filmlocations_details = document.createElement('div')
        filmlocations_details.classList.add('filmlocations__details')

        let h3 = document.createElement('h3')
        h3.textContent = item.name

        let icon_bi_geo_alt = document.createElement('p')
        icon_bi_geo_alt.classList.add('_icon-bi_geo-alt')
        icon_bi_geo_alt.textContent = item.address

        let filmlocations_contact = document.createElement('div')
        filmlocations_contact.classList.add('filmlocations__contact')

        if (item.phone) {
            let icon_mdi_phone = document.createElement('a')
            icon_mdi_phone.classList.add('_icon-mdi_phone')
            icon_mdi_phone.setAttribute('href', `tel:${item.phone}`)
            icon_mdi_phone.textContent = item.phone
            filmlocations_contact.append(icon_mdi_phone)
        }

        if (item.social_net) {
            let icon_youtube = document.createElement('a')
            icon_youtube.classList.add('_icon-youtube')
            icon_youtube.setAttribute('href', item.social_net)
            icon_youtube.textContent = item.social_net
            filmlocations_contact.append(icon_youtube)
        }

        if (item.site) {
            let icon_web_solid = document.createElement('a')
            icon_web_solid.classList.add('_icon-web-solid')
            icon_web_solid.setAttribute('href', item.site)
            icon_web_solid.textContent = item.site
            filmlocations_contact.append(icon_web_solid)
        }

        if (item.email) {
            let icon_mail_outline = document.createElement('a')
            icon_mail_outline.classList.add('_icon-mail-outline')
            icon_mail_outline.setAttribute('href', item.email)
            icon_mail_outline.textContent = item.email
            filmlocations_contact.append(icon_mail_outline)
        }

        // -------------

        filmlocations_details.append(h3, icon_bi_geo_alt, filmlocations_contact)

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/screening-points/' + region_slug)
        a.textContent = "Подробнее"

        article.append(filmlocations_img, filmlocations_details, a)
        block.append(article)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let filmlocations = document.createElement('div')
    filmlocations.classList.add('filmlocations')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Точки кинопоказов'

    let filmlocations_cards = document.createElement('div')
    filmlocations_cards.classList.add('filmlocations-cards')

    data.forEach(dt => {
        createArticle(filmlocations_cards, dt)
    })

    filmlocations.append(region_title, filmlocations_cards)

    region_content_res.append(filmlocations)

    main.append(region_content_res)

}

function createInternetResources(main, data, region_slug) {

    function createArticle(block, item) {
        let article = document.createElement('article')
        article.classList.add('card', 'internetresources-card')

        let internetresources__img = document.createElement('div')
        internetresources__img.classList.add('internetresources__img')

        let figure = document.createElement('figure')
        let figure_img = document.createElement('img')
        figure_img.setAttribute('src', '/static/img/regionsmap/export.png')

        let internetresources__details = document.createElement('div')
        internetresources__details.classList.add('internetresources__details')

        let h3 = document.createElement('h3')
        h3.textContent = item.name

        let p = document.createElement('p')
        p.classList.add('_icon-bi_geo-alt')
        p.textContent = item.region__name

        internetresources__details.append(h3, p)

        let a = document.createElement('a')
        a.classList.add('morelink','internetresources-morelink',  '_icon-ring-arrow')
        a.setAttribute('href', 'detail/internet-resources/' + region_slug) // link
        a.textContent = "Перейти на сайт"

        figure.append(figure_img)

        internetresources__img.append(figure)

        article.append(internetresources__img, internetresources__details, a)
        block.append(article)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let filmlocations = document.createElement('div')
    filmlocations.classList.add('filmlocations-res')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Региональные интернет ресурсы'

    let filmlocations_cards = document.createElement('div')
    filmlocations_cards.classList.add('filmlocations-cards-res')

    data.forEach(dt => {
        createArticle(filmlocations_cards, dt)
    })

    filmlocations.append(region_title, filmlocations_cards)

    region_content_res.append(filmlocations)

    main.append(region_content_res)
}

function createProduction(main, data, region_slug) {

    function createArticle(block, item) {
        let article = document.createElement('article')
        article.classList.add('card', 'production-card')

        let production__img = document.createElement('div')
        production__img.classList.add('production__img')

        let figure = document.createElement('figure')

        let figure_img = document.createElement('img')
        figure_img.setAttribute('src', '/media/' + item.logo)
        figure_img.setAttribute('alt', item.name)

        figure.append(figure_img)

        production__img.append(figure)

        let production__details = document.createElement('div')
        production__details.classList.add('production__details')

        let h3 = document.createElement('h3')
        h3.textContent = item.name
        let p = document.createElement('p')
        p.textContent = item.services_type

        let production__contact = document.createElement('div')
        production__contact.classList.add('production__contact')


        if (item.phone) {
            let icon_mdi_phone = document.createElement('a')
            icon_mdi_phone.classList.add('_icon-mdi_phone')
            icon_mdi_phone.setAttribute('href', `tel:${item.phone}`)
            icon_mdi_phone.textContent = item.phone
            production__contact.append(icon_mdi_phone)
        }

        if (item.social_net) {
            let icon_youtube = document.createElement('a')
            icon_youtube.classList.add('_icon-youtube')
            icon_youtube.setAttribute('href', item.social_net)
            icon_youtube.textContent = item.social_net
            production__contact.append(icon_youtube)
        }

        if (item.site) {
            let icon_web_solid = document.createElement('a')
            icon_web_solid.classList.add('_icon-web-solid')
            icon_web_solid.setAttribute('href', item.site)
            icon_web_solid.textContent = item.site
            production__contact.append(icon_web_solid)
        }

        if (item.email) {
            let icon_mail_outline = document.createElement('a')
            icon_mail_outline.classList.add('_icon-mail-outline')
            icon_mail_outline.setAttribute('href', item.email)
            icon_mail_outline.textContent = item.email
            production__contact.append(icon_mail_outline)
        }

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/productions/' + region_slug)
        a.textContent = "Перейти на сайт"

        production__details.append(h3, p, production__contact)

        article.append(production__img, production__details, a)

        block.append(article)

    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let filmlocations = document.createElement('div')
    filmlocations.classList.add('filmlocations-res')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Производство'

    let filmlocations_cards = document.createElement('div')
    filmlocations_cards.classList.add('filmlocations-cards-res')

    data.forEach(dt => {
        createArticle(filmlocations_cards, dt)
    })

    filmlocations.append(region_title, filmlocations_cards)

    region_content_res.append(filmlocations)

    main.append(region_content_res)
}

function createSpecialists(main, data, region_slug) {
    function createArticle(block, item) {
        let article = document.createElement('article')
        article.classList.add('card', 'personal-card')

        let personal__img = document.createElement('div')
        personal__img.classList.add('personal__img')

        let figure = document.createElement('figure')
        let figure_img = document.createElement('img')
        figure_img.setAttribute('src', item.photo)

        figure.append(figure_img)
        personal__img.append(figure)

        let personal_details = document.createElement('div')
        personal_details.classList.add('personal__details')
        let h3 = document.createElement('h3')
        h3.textContent = `${item.first_name} ${item.last_name}`

        let h4 = document.createElement('h4')
        item.speciality.forEach(speciality => {
            h4.textContent = speciality.name
        })
        let personal_contact = document.createElement('div')
        personal_contact.classList.add('personal__contact')

        if (item.phone) {
            let a = document.createElement('a')
            a.setAttribute('href', `tel:${item.phone}`)
            a.textContent = `Тел: ${item.phone}`
            personal_contact.append(a)
        }
        if (item.email) {
            let email = document.createElement('a')
            email.setAttribute('href', `mailto:${item.email}`)
            email.textContent = `E-mail: ${item.email}`
            personal_contact.append(email)
        }

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/specialists/' + region_slug)
        a.textContent = "Перейти на сайт"

        personal_details.append(h3, h4, personal_contact)

        article.append(personal__img, personal_details, a)

        block.append(article)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let specialists_block = document.createElement('div')
    specialists_block.classList.add('specialists-block')

    let h2 = document.createElement('h2')
    h2.classList.add('region-title')
    h2.textContent = 'Специалисты'

    let personal_cards = document.createElement('div')
    personal_cards.classList.add('personal-cards')

    data.forEach(dt => {
        createArticle(personal_cards, dt)
    })



    specialists_block.append(h2, personal_cards)
    region_content_res.append(specialists_block)

    main.append(region_content_res)
}

function createRegionalProfile(main, data, region_slug) {
    function createArticle(block, item) {
        let article = document.createElement('article')
        article.classList.add('card', 'portrait-card')

        let portrait__img = document.createElement('div')
        portrait__img.classList.add('portrait__img')

        let img = document.createElement('img')
        img.setAttribute('src', '/media/' + item.photo)
        img.setAttribute('alt', item.name)

        portrait__img.append(img)

        let portrait_block = document.createElement('div')
        portrait_block.classList.add('portrait__block')

        let p = document.createElement('p')
        p.classList.add('portrait__block-text')
        p.textContent = item.citation

        let author = document.createElement('div')
        author.classList.add('portrait__block-athor')

        let author_p = document.createElement('p')
        author_p.textContent = item.author

        let author_p_p = document.createElement('p')
        author_p_p.textContent = item.author_city__name
        author_p_p.classList.add('_icon-bi_geo-alt')

        author.append(author_p, author_p_p)

        portrait_block.append(p, author)

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/portrait/' + region_slug)
        a.textContent = "Узнать больше"

        article.append(portrait__img, portrait_block, a)

        block.append(article)
    }
    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let portrait_block = document.createElement('div')
    portrait_block.classList.add('portrait-block')

    let region_title = document.createElement('div')
    region_title.classList.add('region-title')
    region_title.textContent = 'Портрет региона'

    let portrait_cards = document.createElement('div')
    portrait_cards.classList.add('portrait-cards')

    data.forEach(dt => {
        createArticle(portrait_cards, dt)
    })

    let wrap = document.createElement('div')
    wrap.classList.add('portrait-wrap')

    wrap.append(portrait_cards)

    portrait_block.append(region_title, wrap)
    region_content_res.append(portrait_block)

    main.append(region_content_res)
}

function createChats(main, data, region_slug) {
    function createArticle(block, item) {
        let wrap = document.createElement('div')
        wrap.classList.add('portrait-wrap')

        let article = document.createElement('article')
        article.classList.add('card', 'filmmakers-card')

        let filmmakers_card_text = document.createElement('p')
        filmmakers_card_text.classList.add('filmmakers-card__text')
        filmmakers_card_text.textContent = item.name

        let filmmakers_link = document.createElement('div')
        filmmakers_link.classList.add('filmmakers-link')

        let filmmakers_list = document.createElement('ul')
        filmmakers_list.classList.add('filmmakers-list')

        let li_one = document.createElement('li')
        li_one.classList.add('filmmakers-list__social')

        let a_one = document.createElement('a')
        a_one.classList.add('_icon-telegram-white')

        filmmakers_list.append(li_one)

        filmmakers_link.append(filmmakers_list)


        let filmmakers_list__city = document.createElement('div')
        filmmakers_list__city.classList.add('_icon-bi_geo-alt', 'filmmakers-list__city')
        filmmakers_list__city.textContent = item.region__name

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/chats/' + region_slug)
        a.textContent = "Узнать больше"

        article.append(filmmakers_card_text, filmmakers_link, filmmakers_list__city, a)

        wrap.append(article)

        block.append(wrap)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let block = document.createElement('div')
    block.classList.add('filmmakers-block')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Чаты кинематографистов'

    let filmakers_cards = document.createElement('div')
    filmakers_cards.classList.add('filmmakers-cards')

    data.forEach(dt => {
        createArticle(filmakers_cards, dt)
    })

    block.append(region_title, filmakers_cards)


    region_content_res.append(block)

    main.append(region_content_res)
}

function createLocation(main, data, region_slug) {
    function createArticle(block, item){

        let article = document.createElement('article')
        article.classList.add('card', 'location-card')

        let location__img = document.createElement('div')
        location__img.classList.add('location__img')

        let figure = document.createElement('figure')
        let figure_img = document.createElement('img')
        figure_img.setAttribute('src', '/media/' + item.main_photo)
        figure.append(figure_img)

        location__img.append(figure)

        let location_details = document.createElement('div')
        location_details.classList.add('location__details')

        let h3 = document.createElement('h3')
        h3.textContent = item.name

        location_details.append(h3)

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/locations/' + region_slug)
        a.textContent = "Узнать больше"

        article.append(location__img, location_details, a)

        block.append(article)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let block = document.createElement('div')
    block.classList.add('location-block')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Локации'

    let wrap = document.createElement('div')
    wrap.classList.add('portrait-wrap')

    let locations_cards = document.createElement('div')
    locations_cards.classList.add('location-cards')

    wrap.append(locations_cards)

    data.forEach(dt => {
        createArticle(locations_cards, dt)
    })

    block.append(region_title, wrap)


    region_content_res.append(block)

    main.append(region_content_res)
}

function createEvent(main, data, region_slug) {

    function createArticle(block, item){

        let article = document.createElement('article')
        article.classList.add('card', 'events-card')

        let events__img = document.createElement('div')
        events__img.classList.add('events__img')

        let figure_img = document.createElement('img')
        figure_img.setAttribute('src', '/media/' + item.photo)


        events__img.append(figure_img)

        let events__block = document.createElement('div')
        events__block.classList.add('events__block')

        let h3 = document.createElement('h3')
        h3.textContent = item.name

        let p = document.createElement('p')
        p.textContent = item.description

        events__block.append(h3)

        let a = document.createElement('a')
        a.classList.add('morelink', 'regionaresources-morelink', '_icon-ring-arrow')
        a.setAttribute('href', 'detail/events/' + region_slug)
        a.textContent = "Узнать больше"

        article.append(events__img, events__block, a)

        block.append(article)
    }

    let region_content_res = document.createElement('div')
    region_content_res.classList.add('region-content-res')

    let block = document.createElement('div')
    block.classList.add('events-block')

    let region_title = document.createElement('h2')
    region_title.classList.add('region-title')
    region_title.textContent = 'Мероприятия'

    let wrap = document.createElement('div')
    wrap.classList.add('events-wrap')

    let locations_cards = document.createElement('div')
    locations_cards.classList.add('events-cards')

    wrap.append(locations_cards)

    data.forEach(dt => {
        createArticle(locations_cards, dt)
    })

    block.append(region_title, wrap)


    region_content_res.append(block)

    main.append(region_content_res)
}

region_select.addEventListener('change', (e) => {
    fetch(get_resources, {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify({
            slug: e.target.value,
        })
    }).then(res => res.json()).then(data => {
        if (data.detail) {
            regions_resources.innerHTML = ""
            let result = data.result
            if (result.screening_points.length > 0) {
                createScreeningPoints(regions_resources, result.screening_points, e.target.value)
            }
            if (result.internet_resources.length > 0) {
                createInternetResources(regions_resources, result.internet_resources, e.target.value)
            }

            if (result.productions.length > 0) {
                createProduction(regions_resources, result.productions, e.target.value)
            }
            if (result.specialists.length > 0) {
                createSpecialists(regions_resources, result.specialists, e.target.value)
            }
            if (result.regional_profile.length > 0) {
                createRegionalProfile(regions_resources, result.regional_profile, e.target.value)
            }
            if (result.chats.length > 0) {
                createChats(regions_resources, result.chats, e.target.value)
            }
            if (result.locations.length > 0) {
                createLocation(regions_resources, result.locations, e.target.value)
            }
            if (result.event.length > 0) {
                createEvent(regions_resources, result.event, e.target.value)
            }

        }
    }).catch(
        error => {
            console.error(error)
        }
    )
})
