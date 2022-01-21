let nextBtn = document.querySelector('#nextSlide');
let prevBtn = document.querySelector('#prevSlide');
let slider = document.querySelector('.slider');
let slide_list = document.querySelector('.slide_list');
let sliderBtns = document.querySelectorAll('.sliderNav > ul > li > button');
let currentSlide = 0;

function nextSlide() {
    currentSlide++;
    if(currentSlide >= slide_list.children.length) {
        currentSlide = 0;
    }
    slide_list.style.transform = `translate(-${currentSlide}00%)`;
}

function prevSlide() {
    currentSlide--;
    if(currentSlide < 0) {
        currentSlide = slide_list.children.length - 1;
    }
    slide_list.style.transform = `translate(-${currentSlide}00%)`;
}

sliderBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
        if(currentSlide != [...sliderBtns].indexOf(this)) {
            currentSlide = [...sliderBtns].indexOf(this);
            slide_list.style.transform = `translate(-${currentSlide}00%)`;
        }
    });
})

nextBtn.onclick = nextSlide;
prevBtn.onclick = prevSlide;

let interval = setInterval(nextSlide, 3000);
slider.addEventListener('mouseover', function() {
    clearInterval(interval);
});
slider.addEventListener('mouseout', function() {
    interval = setInterval(nextSlide, 3000);
});
