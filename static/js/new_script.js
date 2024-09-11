
"use strict";

//!Menu
window.addEventListener("load", function () {
	if (document.querySelector('.wrapper')) {
		setTimeout(function () {
			document.querySelector('.wrapper').classList.add('_loaded');
		}, 0);
	}
});
let unlock = true;

let iconMenu = document.querySelector(".icon-menu");
if (iconMenu != null) {
	let delay = 500;
	let menuBody = document.querySelector(".menu__body");
	iconMenu.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			iconMenu.classList.toggle("_active");
			menuBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let iconMenu = document.querySelector(".icon-menu");
	let menuBody = document.querySelector(".menu__body");
	iconMenu.classList.remove("_active");
	menuBody.classList.remove("_active");
}

// фильтр голосование
let filtersBtn = document.querySelector(".filters-btn");
if (filtersBtn != null) {
	let delay = 500;
	let filtersbody = document.querySelector(".filters__body");
	filtersBtn.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			filtersBtn.classList.toggle("_active");
			filtersbody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let filtersBtn = document.querySelector(".filters-btn");
	let filtersbody = document.querySelector(".filters__body");
	filtersBtn.classList.remove("_active");
	filtersbody.classList.remove("_active");
}

// /*  Выпадающий список Жанра application_new.html*/
let genreBtn = document.querySelector(".genre-btn");
if (genreBtn != null) {
	let delay = 500;
	let genrebody = document.querySelector(".genre__body");
	genreBtn.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			genreBtn.classList.toggle("_active");
			genrebody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let genreBtn = document.querySelector(".genre-btn");
	let genrebody = document.querySelector(".genre__body");
	genreBtn.classList.remove("_active");
	genrebody.classList.remove("_active");
}

// /* второй Выпадающий список Жанра application_new.html*/
let genreBtnTwo = document.querySelector(".genre-btn_two");
if (genreBtnTwo != null) {
	let delay = 500;
	let genrebodyTwo = document.querySelector(".genre__body_two");
	genreBtnTwo.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			genreBtnTwo.classList.toggle("_active");
			genrebodyTwo.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let genreBtnTwo = document.querySelector(".genre-btn_two");
	let genrebodyTwo = document.querySelector(".genre__body_two");
	genreBtnTwo.classList.remove("_active");
	genrebodyTwo.classList.remove("_active");
}

// /*  Выпадающий список Регион application_new.html*/
let regionBtn = document.querySelector(".region-btn");
if (regionBtn != null) {
	let delay = 500;
	let regionBody = document.querySelector(".region__body");
	regionBtn.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			regionBtn.classList.toggle("_active");
			regionBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let regionBtn = document.querySelector(".region-btn");
	let regionBody = document.querySelector(".region__body");
	regionBtn.classList.remove("_active");
	regionBody.classList.remove("_active");
}

// /*  Выпадающий список Специальность application_new.html*/
let specialityBtn = document.querySelector(".speciality-btn");
if (specialityBtn != null) {
	let delay = 500;
	let specialityBody = document.querySelector(".speciality__body");
	specialityBtn.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			specialityBtn.classList.toggle("_active");
			specialityBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let specialityBtn = document.querySelector(".speciality-btn");
	let specialityBody = document.querySelector(".speciality__body");
	specialityBtn.classList.remove("_active");
	specialityBody.classList.remove("_active");
}

// /*  Выпадающий список регион 2 application_new.html*/
let specialityRegionBtn = document.querySelector(".specialist-region__btn");
if (specialityRegionBtn != null) {
	let delay = 500;
	let specialityRegionBody = document.querySelector(".specialist-region__body");
	specialityRegionBtn.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			specialityRegionBtn.classList.toggle("_active");
			specialityRegionBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let specialityRegionBtn = document.querySelector(".specialist-region__btn");
	let specialityRegionBody = document.querySelector(".specialist-region__body");
	specialityRegionBtn.classList.remove("_active");
	specialityRegionBody.classList.remove("_active");
}

// добавить в плейлист
let tooltipPlaylist = document.querySelector(".playlist-btn");
if (tooltipPlaylist != null) {
	let delay = 500;
	let filmAddBody = document.querySelector(".film__body");
	tooltipPlaylist.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			tooltipPlaylist.classList.toggle("_active");
			filmAddBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let tooltipPlaylist = document.querySelector(".playlist-btn");
	let filmAddBody = document.querySelector(".film__body");
	tooltipPlaylist.classList.remove("_active");
	filmAddBody.classList.remove("_active");
}

// фильтр смотреть и голосовать(регион)
let iconRegion = document.querySelector("._icon-derection-right");
if (iconRegion != null) {
	let delay = 500;
	let filtersBody = document.querySelector(".filters-region__body");
	iconRegion.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			iconRegion.classList.toggle("_active");
			filtersBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let iconRegion = document.querySelector("._icon-derection-right");
	let filtersBody = document.querySelector(".filters-region__body");
	iconRegion.classList.remove("_active");
	filtersBody.classList.remove("_active");
}
// фильтр смотреть и голосовать(Категория)
let iconCategory = document.querySelector("._icon-derection-right");
if (iconCategory != null) {
	let delay = 500;
	let filtersBody = document.querySelector(".filters-category__body");
	iconCategory.addEventListener("click", function (e) {
		if (unlock) {
			body_lock(delay);
			iconCategory.classList.toggle("_active");
			filtersBody.classList.toggle("_active");
		}
	});
};
function menu_close() {
	let iconCategory = document.querySelector("._icon-derection-right");
	let filtersBody = document.querySelector(".filters-category__body");
	iconCategory.classList.remove("_active");
	filtersBody.classList.remove("_active");
}



// checkbox фильтры
// $(document).ready(function () {
// 	$.each($('.filters__item-submenu'), function (index, val) {
// 		if ($(this).find('input').prop('checked') == true) {
// 			$(this).addClass('active');
// 		}
// 	});
// 	$(document).on('click', '.filters__item-submenu', function (event) {
// 		$(this).parents('.filters__sub-item').find('.filters__item-submenu').removeClass('active');
// 		$(this).parents('.filters__sub-item').find('.filters__item-submenu input').prop('checked', false);
// 		$(this).toggleClass('active');
// 		$(this).find('input').prop('checked', true);
// 		return false;
// 	});
// });

// Добавить в плейлист checkbox
// $(document).ready(function () {
// 	$.each($('.film__item-submenu'), function (index, val) {
// 		if ($(this).find('input').prop('checked') == true) {
// 			$(this).addClass('active');
// 		}
// 	});
// 	$(document).on('click', '.film__item-submenu', function (event) {
// 		$(this).parents('.film__sub-item').find('.film__item-submenu').removeClass('active');
// 		$(this).parents('.film__sub-item').find('.film__item-submenu input').prop('checked', false);
// 		$(this).toggleClass('active');
// 		$(this).find('input').prop('checked', true);
// 		return false;
// 	});
// });


// Событие, которое отслеживает скроллит ли человек.
document.addEventListener('scroll', function () {
	if ($(window).scrollTop() > 100) {
		// если больше 1000 → добавляем класс
		$('.js-header').addClass('is-show');
	} else {
		// если меньше 1000 → удаляем класс
		$('.js-header').removeClass('is-show');
	}
})
//=================
//BodyLock
function body_lock(delay) {
	let body = document.querySelector("body");
	if (body.classList.contains('_lock')) {
		body_lock_remove(delay);
	} else {
		body_lock_add(delay);
	}
}
function body_lock_remove(delay) {
	let body = document.querySelector("body");
	if (unlock) {
		let lock_padding = document.querySelectorAll("._lp");
		setTimeout(() => {
			for (let index = 0; index < lock_padding.length; index++) {
				const el = lock_padding[index];
				el.style.paddingRight = '0px';
			}
			body.style.paddingRight = '0px';
			body.classList.remove("_lock");
		}, delay);

		unlock = false;
		setTimeout(function () {
			unlock = true;
		}, delay);
	}
}
function body_lock_add(delay) {
	let body = document.querySelector("body");
	if (unlock) {
		// let lock_padding = document.querySelectorAll("._lp");
		// for (let index = 0; index < lock_padding.length; index++) {
		// 	const el = lock_padding[index];
		// 	el.style.paddingRight = window.innerWidth - document.querySelector('.header').offsetWidth + 'px';
		// }
		// body.style.paddingRight = window.innerWidth - document.querySelector('.header').offsetWidth + 'px';
		// body.classList.add("_lock");

		unlock = false;
		setTimeout(function () {
			unlock = true;
		}, delay);
	}
}


// !Выпадающие меню
let menuArrows = document.querySelectorAll('._icon-derection-right');
if (menuArrows.length > 0) {
	for (let index = 0; index < menuArrows.length; index++) {
		const menuArrow = menuArrows[index];
		menuArrow.addEventListener("click", function (e) {
			menuArrow.parentElement.classList.toggle('_active');
		});
	}
}

let menuLinks = document.querySelectorAll('.menu__link');
if (menuLinks.length > 0) {
	for (let index = 0; index < menuLinks.length; index++) {
		const menuLink = menuLinks[index];
		menuLink.addEventListener("click", function (e) {
			menuLink.parentElement.classList.toggle('_active');
		});
	}
}


//! news slider
$(document).ready(function () {
	$('.slider').slick({
		slidesToShow: 4,
		vertical: true,
		verticalSwiping: true,
		responsive: [
			{
				breakpoint: 1420,
				settings: {
					slidesToShow: 3,
					vertical: true,
					verticalSwiping: true,
				}
			},
			{
				breakpoint: 1100,
				settings: {
					slidesToShow: 3,
					vertical: false,
					verticalSwiping: false,
					arrows: false,
					variableWidth: true,
					// centerMode: true,
				}
			},
			{
				breakpoint: 992,
				settings: {
					slidesToShow: 3,
					vertical: false,
					verticalSwiping: false,
					variableWidth: true,
					arrows: false,
				}
			},
			{
				breakpoint: 697,
				settings: {
					slidesToShow: 2,
					vertical: false,
					verticalSwiping: false,
					variableWidth: true,
					arrows: false,
				}
			},
			{
				breakpoint: 493,
				settings: {
					slidesToShow: 1,
					adaptiveHeight: true,
					vertical: false,
					verticalSwiping: false,
					arrows: false,
					// centerMode: true,
				}
			}
		]
	});
	$('.sliderProject').slick({
		slidesToShow: 3,
		dots: true,
		responsive: [
			{
				breakpoint: 1200,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 840,
				settings: {
					slidesToShow: 1,
				}
			},
		]
	});
	$('.sliderFilmAward').slick({
		slidesToShow: 3,
		responsive: [
			{
				breakpoint: 1089,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 783,
				settings: {
					slidesToShow: 1,
				}
			},
		]
	});
	$('.mediaslider').slick({
		slidesToShow: 1,
		asNavFor: ".mediasliderMin",
	});
	$('.mediasliderMin').slick({
		slidesToShow: 3,
		arrows: false,
		asNavFor: ".mediaslider",
		responsive: [
			{
				breakpoint: 800,
				settings: {
					slidesToShow: 2,
				}
			},
		]
	});
	$('.newsslider').slick({
		slidesToShow: 3,
		dots: true,
		responsive: [
			{
				breakpoint: 750,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 615,
				settings: {
					slidesToShow: 1,
				}
			},
		]
	});
	$('.locationnameslider').slick({
		slidesToShow: 1,
		arrows: false,
		asNavFor: ".locationnamesliderMin",
	});
	$('.locationnamesliderMin').slick({
		slidesToShow: 3,
		asNavFor: ".locationnameslider",
		responsive: [
			{
				breakpoint: 800,
				settings: {
					slidesToShow: 2,
				}
			},
		]
	});
	$('.popuplocation').slick({
		slidesToShow: 1,
	});
	$('.watchslider').slick({
		slidesToShow: 1,
		dots: true,
		responsive: [

			{
				breakpoint: 500,
				settings: {
					dots: false,
				}
			},]
	});
	$('.busibessProgramslider').slick({
		slidesToShow: 1,
		dots: false,
	});
	$('.supportSubpageslider').slick({
		slidesToShow: 3,
		dots: true,
		centerMode: true,
		variableWidth: true,
	});
	$('.personalAccountslider').slick({
		slidesToShow: 5,
		responsive: [
			{
				breakpoint: 1200,
				settings: {
					slidesToShow: 4,
				}
			},
			{
				breakpoint: 914,
				settings: {
					slidesToShow: 3,
				}
			},
			{
				breakpoint: 840,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 1,
					variableWidth: true,
					// centerMode: true,
					arrows: false,
				}
			},
		]
	});
	$('.applications').slick({
		slidesToShow: 5,
		responsive: [

			{
				breakpoint: 914,
				settings: {
					slidesToShow: 3,
				}
			},
			{
				breakpoint: 840,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 600,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 390,
				settings: {
					slidesToShow: 1,

				}
			},
		]
	});
	$('.expertslider').slick({
		slidesToShow: 3,
		responsive: [

			{
				breakpoint: 1470,
				settings: {
					slidesToShow: 2,
				}
			},

			{
				breakpoint: 1030,
				settings: {
					slidesToShow: 1,
				}
			},
			{
				breakpoint: 626,
				settings: {
					slidesToShow: 1,
					variableWidth: true,
					// centerMode: true,
					arrows: false,
				}
			},
		]
	});
	$('.prizesslider').slick({
		slidesToShow: 3,
		responsive: [

			{
				breakpoint: 1030,
				settings: {
					slidesToShow: 2,
				}
			},
			{
				breakpoint: 626,
				settings: {
					slidesToShow: 1,
					variableWidth: true,
					// centerMode: true,
					arrows: false,
				}
			},
		]
	});
});

// !popups
const popupLinks = document.querySelectorAll('.popup-link');
const body = document.querySelector('body');
const lockPadding = document.querySelectorAll('.lock-padding');

let lock = true;
const timeout = 800;

if (popupLinks.length > 0) {
	for (let index = 0; index < popupLinks.length; index++) {
		const popupLink = popupLinks[index];
		popupLink.addEventListener("click", function (e) {
			const popupName = popupLink.getAttribute('href').replace('#', '');
			const curentPopup = document.getElementById(popupName);
			popupOpen(curentPopup);
			e.preventDefault();
		});
	}
}

const popupCloseIcon = document.querySelectorAll('.close-popup');
if (popupCloseIcon.length > 0) {
	for (let index = 0; index < popupCloseIcon.length; index++) {
		const el = popupCloseIcon[index];
		el.addEventListener('click', function (e) {
			popupClose(el.closest('.popup'));
			e.preventDefault();
		});
	}
}

function popupOpen(curentPopup) {
	if (curentPopup && lock) {
		const popupActive = document.querySelector('.popup.open');
		if (popupActive) {
			popupClose(popupActive, false);
		} else {
			bodyLock();
		}
		curentPopup.classList.add('open');
		curentPopup.addEventListener("click", function (e) {
			if (!e.target.closest('.popup__content, .media__content')) {
				popupClose(e.target.closest('.popup'));
			}
		});
	}
}
function popupClose(popupActive, dolock = true) {
	if (lock) {
		popupActive.classList.remove('open');
		if (dolock) {
			bodyLock();
		}
	}
}

function bodyLock() {
	const lockPaddingValue = window.innerWidth - document.querySelector('.wrapper').offsetWidth + 'px';
	if (lockPadding.length > 0) {
		for (let index = 0; index < lockPadding.length; index++) {
			const el = lockPadding[index];
			el.style.paddingRight = lockPaddingValue;
		}
	}
	body.style.paddingRight = lockPaddingValue;
	body.classList.add('lock');

	lock = false;
	setTimeout(function () {
		lock = true;
	}, timeout);
}

function bodyLock() {
	setTimeout(function () {
		if (lockPadding.length > 0) {
			for (let index = 0; index < lockPadding.length; index++) {
				const el = lockPadding[index];
				el.style.paddingRight = '0px';
			}
		}
		body.style.paddingRight = '0px';
		body.classList.remove('lock');
	}, timeout);

	lock = false;
	setTimeout(function () {
		lock = true;
	}, timeout);
}

// закрытие popup по кнопке Esc
document.addEventListener('keydown', function (e) {
	if (e.which === 27) {
		const popupActive = document.querySelector('.popup.open');
		popupClose(popupActive);
	}
});

$(document).ready(function () {
	$('.popup').click(function (event) {
		$('body').toggleClass('lock');
	});
});
// -------------------------

//! popup-tabs
const tabs = document.getElementById('tabs');
const contents = document.getElementById('contents');

const changeClass = el => {
	for (let i = 0; i < tabs.children.length; i++) {
		tabs.children[i].classList.remove('_active')
	}
	el.classList.add('_active');
}

tabs.addEventListener('click', e => {
	const currTab = e.target.dataset.btn;
	changeClass(e.target);
	for (let i = 0; i < contents.children.length; i++) {
		contents.children[i].classList.remove('_active');
		if (contents.children[i].dataset.content == currTab) {
			contents.children[i].classList.add('_active');
		}
	}
})


// checkbox голосование одиночные
$(document).ready(function () {
	$.each($('.application-checked'), function (index, val) {
		if ($(this).find('input').prop('checked') == true) {
			$(this).addClass('active');
		}
	});
	$(document).on('click', '.application-checked', function (event) {
		$(this).parents('.application-checkeds').find('.application-checked').removeClass('active');
		$(this).parents('.application-checkeds').find('.application-checked input').prop('checked', false);
		$(this).toggleClass('active');
		$(this).find('input').prop('checked', true);
		return false;
	});
});


// клик по кнопке видео на странице eventsLandingPage.html
$(document).on('click', '.PlayPauseVideo', function () {
	var video = $(this).closest(".video_with_link").find(".video")[0];
	if (video.paused) {
		video.play();
	} else {
		video.pause();
	}
});



// видеоплеер
var player;
function onYouTubePlayerAPIReady() {
	player = new YT.Player('player');
}

$('#stop').click(function () {
	player.stopVideo()
})

	/* map start */
	; (function () {
		let sectionContacts = document.querySelector('.section-contacts');

		let ymapInit = function () {
			if (typeof ymaps === 'undefined') {
				return;
			}

			ymaps.ready(function () {
				let myMap = new ymaps.Map('ymap', {
					center: [55.799720, 49.037702],
					zoom: 16
				}, {
					searchControlProvider: 'yandex#search'
				}),

					myPlacemark = new ymaps.Placemark(myMap.getCenter(), {
						balloonContent: 'г. Казань , Боевая. 2'
					}, {
						iconLayout: 'default#image',
						iconImageHref: '../img/map.png',
						iconImageSize: [50, 63.2],
						iconImageOffset: [-30, -58]
					});

				myMap.geoObjects.add(myPlacemark);

				myMap.behaviors.disable('scrollZoom');
			});
		};

		let ymapLoad = function () {
			let script = document.createElement('script');
			script.src = 'https://api-maps.yandex.ru/2.1/?lang=en_RU';
			myLib.body.appendChild(script);
			script.addEventListener('load', ymapInit);
		};


	})();

//! eventsLandingPage 
// видео
const knobs = document.getElementById('knobs');
const imgbigs = document.getElementById('imgbigs');


const changesClass = el => {
	for (let i = 0; i < knobs.children.length; i++) {
		knobs.children[i].classList.remove('active')
	}
	el.classList.add('active');
}

// knobs.addEventListener('click', e => {
// 	const currTabs = e.target.dataset.knob;
// 	changesClass(e.target);
// 	for (let i = 0; i < imgbigs.children.length; i++) {
// 		imgbigs.children[i].classList.remove('active');
// 		if (imgbigs.children[i].dataset.imgbig == currTabs) {
// 			imgbigs.children[i].classList.add('active');
// 		}
// 	}
// })



// подсказка
// document.querySelector('.tooltip-btn').addEventListener('mouseenter', function (event) {
// 	var tooltip = this.querySelector('.tooltip');
// 	tooltip.style.visibility = 'visible';
// });

// document.querySelector('.tooltip-btn').addEventListener('mouseleave', function (event) {
// 	var tooltip = this.querySelector('.tooltip');
// 	tooltip.style.visibility = 'hidden';
// });

// document.querySelector('.tooltip-btn').addEventListener('mouseenter', function (event) {
// 	var tooltipPlaylist = this.querySelector('.tooltip-playlist');
// 	tooltipPlaylist.style.visibility = 'visible';
// });

// document.querySelector('.tooltip-btn').addEventListener('mouseleave', function (event) {
// 	var tooltipPlaylist = this.querySelector('.tooltip-playlist');
// 	tooltipPlaylist.style.visibility = 'hidden';
// });

// document.querySelector('.tooltip-btn').addEventListener('mouseenter', function (event) {
// 	var tooltipFavorites = this.querySelector('.tooltip-favorites');
// 	tooltipFavorites.style.visibility = 'visible';
// });

// document.querySelector('.tooltip-btn').addEventListener('mouseleave', function (event) {
// 	var tooltipFavorites = this.querySelector('.tooltip-favorites');
// 	tooltipFavorites.style.visibility = 'hidden';
// });
