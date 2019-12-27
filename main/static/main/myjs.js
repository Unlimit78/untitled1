/* Индекс слайда по умолчанию */

var slideIndex = 1;
showSlides(slideIndex);


/* Функция увеличивает индекс на 1, показывает следующй слайд*/
function plusSlide() {
    showSlides(slideIndex += 1);
}

/* Функция уменьшяет индекс на 1, показывает предыдущий слайд*/
function minusSlide() {
    showSlides(slideIndex -= 1);
}

/* Устанавливает текущий слайд */
function currentSlide(n) {
    showSlides(slideIndex = n);
}

/* Основная функция слайдера */
function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("item");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";

}

function scrollToTop(){
    var windowWidth = $(window).width(),
        didScroll = false;

    var $arrow = $('#back-to-top');

    $arrow.click(function(e) {
        $('body,html').animate({ scrollTop: "0" }, 750, 'easeOutExpo' );
        e.preventDefault();
    });

    $(window).scroll(function() {
        didScroll = true;
    });

    setInterval(function() {
        if( didScroll ) {
            didScroll = false;

            if( $(window).scrollTop() > 1000 ) {
                $arrow.css('display', 'block');
            } else {
                $arrow.css('display', 'none');
            }
        }
    }, 250);
}

scrollToTop();

$(document).ready(function(){



    var $menu = $(".sticky-nav");
    var $h = $(".slider").outerHeight();
    var $s = $("#slider");

    $(window).scroll(function(){
        if ( $(this).scrollTop() > $h && $menu.hasClass("sticky-nav")  ){
            $menu.addClass("stuck");

        }else if($(this).scrollTop() <= $h && $menu.hasClass("stuck")) {

            $menu.removeClass("stuck");

        }



    });//scroll

});

