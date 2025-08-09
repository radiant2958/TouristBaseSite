
'use strict';

// Загрузка фоновых изображений
document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.details-item img');
    images.forEach(img => {
        img.addEventListener('click', function() {
            enlargeImage(this.getAttribute('src'));
        });
    });

    // Подсветка активного пункта меню
    const currentUrl = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-menu ul li a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.parentElement.classList.add('active');
        } else {
            link.parentElement.classList.remove('active');
        }
    });
});
var currentImgSrc = '';
// Открывает модальное окно с увеличенным изображением
function openModal() {
    var modalImg = document.getElementById("modalImg");
    modalImg.src = currentImgSrc;
    document.getElementById("myModal").style.display = "block";
}

// Закрывает модальное окно
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

// Получает изображение и устанавливает его в модальное окно
function enlargeImage(imgSrc) {
    currentImgSrc = imgSrc; // Устанавливаем текущий путь к изображению
    var modalImg = document.getElementById("modalImg");
    modalImg.src = currentImgSrc;
    openModal();
}

