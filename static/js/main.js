// Функция для перехода на товары
function goToGoodPage(value) {
    window.location.href = value;
}

function goToNewItemPage() {
    window.location.href = "goodspages/furniture1.html"
}

//Переход к вк
function redirectToVk() {
    window.open('https://vk.com/purpleppassion', '_blank');
}

//Переход к тг
function redirectToTg() {
    window.open('https://t.me/murcall', '_blank');
}

// Функция для перехода на страницу с инфораие
function goToMainPage() {
    window.location.href = "index.html";
}

//Переход по рекламе
function redirectToAviasales() {
    window.open('https://www.aviasales.ru', '_blank');
}

//Переход по рекламе
function redirectToDom() {
    window.open('https://www.cian.ru/kupit-dom/', '_blank');
}
//Переход по рекламе
function redirectToWildberries() {
    window.open('https://www.wildberries.ru/', '_blank');
}

//Переход по рекламе
function redirectToOzon() {
    window.open('https://www.ozon.ru/', '_blank');
}

function redirectToAuto() {
    window.open('https://www.auto.ru/', '_blank');
}

window.onscroll = function() {
    scrollFunction();
};

function openBurger() {
    let nav = document.querySelector('nav');
    let burgerContent = document.getElementsByClassName('burger_content');
    let header = document.querySelector('header');
    nav.classList.toggle('show');
    burgerContent[0].classList.toggle('show');
    burgerContent[1].classList.toggle('show');
    header.classList.toggle('show');
}

function scrollFunction() {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        document.getElementById("scrollTopButton").classList.add("show");
    } else {
        document.getElementById("scrollTopButton").classList.remove("show");
    }
}

function scrollToTop() {
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE и Opera
}

// Получаем модальное окно и элементы изображений
var modal = document.getElementById('myModal');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

// Получаем коллекцию изображений
var images = document.querySelectorAll('img[id^="myImg"]');

// Привязываем обработчик клика к каждому изображению
images.forEach(function(img) {
    img.onclick = function() {
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
    };
});

// Получаем элемент для закрытия модального окна
var closeBtn = document.getElementsByClassName("close")[0];

// Привязываем обработчик клика к элементу закрытия модального окна
closeBtn.onclick = function() {
    modal.style.display = "none";
};

// Привязываем обработчик клика к модальному окну для закрытия его при клике вне изображения
modal.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

const showSlides = {
    slideIndex: 0,
    slides: document.getElementsByClassName('slides'),
    changeSlide() {
        let i = 0;
        for (i; i < this.slides.length; i++) {
            this.slides[i].style.display = 'none';
        }
        this.slides[this.slideIndex-1].style.display = 'block';
    },
    nextSlide() {
        this.slideIndex++;
        if (this.slideIndex > this.slides.length) {this.slideIndex = 1};
        this.changeSlide();
    },
    prevSlide() {
        this.slideIndex--;
        if (this.slideIndex < 1) {this.slideIndex = this.slides.length};
        this.changeSlide();
    },
    showTheFirst() {
        let i = 1;
        for (i; i < this.slides.length; i++) {
            this.slides[i].style.display = 'none';
        }
        this.slideIndex++;
    }
}
showSlides.showTheFirst();

function openBurger() {
    let burgerContent = document.getElementsByClassName('burger-content');
    let header = document.getElementsByClassName('header');
    burgerContent[0].classList.toggle('showBurger');
    burgerContent[1].classList.toggle('hide');
    burgerContent[1].classList.toggle('showBurger');
    header[0].classList.toggle('hide');
}

function checkPass() {
    let password = document.getElementById('pass').value;
    let check = document.getElementById('checkpass').value;
    let button = document.querySelector('.customButton');
    let err = document.querySelector('.error');
    if (password !== check) {
        button.setAttribute('disabled', 'disabled');
        err.classList.remove('super_hide');
    }
    else {
        button.removeAttribute('disabled');
        err.classList.add('super_hide');
    }
}

function checkInfo() {
    let name = document.getElementById('name').value;
    let surname = document.getElementById('surname').value;
    let mail = document.getElementById('mail').value;
    let pass = document.getElementById('pass').value;
    let checkpass = document.getElementById('checkpass').value;
    let adress = document.getElementById('adress').value;
    let button = document.querySelector('.customButton');
    let err = document.querySelector('.notification');
    if (name === '' || surname === '' || mail === '' || pass === '' || checkpass === '' || adress === '') {
        button.setAttribute('disabled', 'disabled');
        err.classList.remove('super_hide');
    }
    else {
        button.removeAttribute('disabled');
        err.classList.add('super_hide');
    }
}

function checkInfoLogin() {
    let mail = document.getElementById('mail').value;
    let pass = document.getElementById('pass').value;
    let button = document.querySelector('.customButton');
    let err = document.querySelector('.notification');
    if (mail === '' || pass === '') {
        button.setAttribute('disabled', 'disabled');
        err.classList.remove('super_hide');
    }
    else {
        button.removeAttribute('disabled');
        err.classList.add('super_hide');
    }
}