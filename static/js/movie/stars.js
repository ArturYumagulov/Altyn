const ratings = document.querySelectorAll('.rating')
const movie_info = document.querySelector('.name-film')
const movie_slug = movie_info.getAttribute('data-slug')
const get_action = movie_info.getAttribute('data-action')
const valid_ip = movie_info.getAttribute('data-valid')
const get_rating = movie_info.getAttribute('data-rating')
const rating_count = document.querySelector('.film-vote span')


if (ratings.length > 0) {
    initRatings();
    validUserIp();
}

async function getRatingValue() {
    let value = await fetch(get_rating, {
        method: 'GET'
    })
    if (value.ok) {
        let rating_data = await value.json()
        return rating_data.rating
    } else {
        return 0
    }
}

async function validUserIp() {
    let valid = await fetch(valid_ip, {
        method: 'POST',
        headers: {"X-CSRFToken": csrf},
        body: JSON.stringify({
            slug: movie_slug,
        })
    })
    if (valid.ok) {
        let valid_data = await valid.json()
        if (!valid_data.valid) {
            let rating = ratings[0]
            rating.classList.add('rating_sending')
        }
    }
}

async function initRatings() {
    let ratingActive
    let movieRatingValue = await getRatingValue()

    for (let index = 0; index < ratings.length; index++) {
        const rating = ratings[index];
        initRating(rating);
    }
    function initRating (rating) {
        initRatingVars(rating);

        setRatingActiveWidth();

        if (rating.classList.contains('rating_set')) {
            setRating(rating);
        }
    }
    function initRatingVars(rating) {
        ratingActive = rating.querySelector('.rating__active');
        ratingValue = document.querySelector('.rating__value');

    }
    function setRatingActiveWidth(index = ratingValue.innerHTML) {
        const ratingActiveWidth = index / 0.05;
        ratingActive.style.width = `${ratingActiveWidth}%`
    }
    function setRating(rating) {
        const ratingItems = rating.querySelectorAll('.rating__item');
        for (let index = 0; index < ratingItems.length; index++) {
            const ratingItem = ratingItems[index];
            ratingItem.addEventListener("mouseenter", function (e) {
                initRatingVars(rating);
                setRatingActiveWidth(ratingItem.value)
            });
            ratingItem.addEventListener("mouseleave", function (e) {
                setRatingActiveWidth()
            });
            console.log(ratingItem.value, 'value')
            ratingItem.addEventListener("click", function (e) {
                initRatingVars(rating);
                if(rating.dataset.ajax){
                    setRatingValue(ratingItem.value, rating);
                }else {
                    movieRatingValue = index + 1;
                    setRatingActiveWidth();
                }
            })
        }
    }

    async function setRatingValue (value, rating) {
        if(!rating.classList.contains('rating_sending')) {
            rating.classList.add('rating_sending');

            let response = await fetch(get_action, {
                method: "POST",
                headers: {
                    'content-type': 'application/json',
                },
                body: JSON.stringify({
                    userRating: value,
                    movieSlug: movie_slug,
                })
            });
            if (response.ok){
                const result = await response.json();
                ratingValue.innerHTML = result.result;
                setRatingActiveWidth();
                rating_count.textContent = Number(rating_count.innerHTML) + 1;
                rating.classList.add('rating_sending');
            }
        }
    }

}