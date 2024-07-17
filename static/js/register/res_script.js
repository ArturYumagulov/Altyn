
"use strict";

//!Menu

let register_popup = document.querySelector('.popup-authorization')

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
		let lock_padding = document.querySelectorAll("._lp");
		for (let index = 0; index < lock_padding.length; index++) {
			const el = lock_padding[index];
			el.style.paddingRight = window.innerWidth - document.querySelector('.header').offsetWidth + 'px';
		}
		body.style.paddingRight = window.innerWidth - document.querySelector('.header').offsetWidth + 'px';
		body.classList.add("_lock");

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
				breakpoint: 1200,
				settings: {
					slidesToShow: 4,
					vertical: false,
					verticalSwiping: false,
				}
			},
			{
				breakpoint: 992,
				settings: {
					slidesToShow: 3,
					vertical: false,
					verticalSwiping: false,
				}
			},
			{
				breakpoint: 697,
				settings: {
					slidesToShow: 2,
					vertical: false,
					verticalSwiping: false,
				}
			},
			{
				breakpoint: 493,
				settings: {
					slidesToShow: 1,
					adaptiveHeight: true,
					vertical: false,
					verticalSwiping: false,
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
	})
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
			register_popup.classList.add('open')
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
			if (!e.target.closest('.popup__content')) {
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
		register_popup.classList.add('open')
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
document.querySelector('.tooltip-btn').addEventListener('mouseenter', function (event) {
	var tooltip = this.querySelector('.tooltip');
	tooltip.style.visibility = 'visible';
});

document.querySelector('.tooltip-btn').addEventListener('mouseleave', function (event) {
	var tooltip = this.querySelector('.tooltip');
	tooltip.style.visibility = 'hidden';
});

// видеоплеер
var player;
function onYouTubePlayerAPIReady() {
	player = new YT.Player('player');
}

$('#stop').click(function () {
	player.stopVideo()
})

// // библиотека lightGallery для страницы media-subpage
// lightGallery(document.getElementById('mediasubpage-img'), {
// 	animateThumb: false,
// 	zoomFromOrigin: false,
// 	allowMediaOverlap: true,
// 	toggleThumb: true,
// 	thumbnail: true,
//
// });

