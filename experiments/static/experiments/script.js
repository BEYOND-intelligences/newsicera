// تعريف المتغيرات العامة للسلايدر
let currentSlide = 0;
let slides = [];
let autoSlideInterval;

function initSlider() {
    const container = document.getElementById('slider-container');
    if (!container) return; // لا يوجد سلايدر في هذه الصفحة

    slides = container.getElementsByClassName('slide');

    // إذا كان هناك شريحة واحدة فقط، لا داعي للتحريك التلقائي
    if (slides.length > 1) {
        startAutoSlide();
    }
}

function showSlide(index) {
    if (slides.length === 0) return;

    // إخفاء الشريحة الحالية
    slides[currentSlide].classList.remove('active');

    // تحديث المؤشر
    currentSlide = index;

    // التعامل مع الحدود (الدوران)
    if (currentSlide >= slides.length) {
        currentSlide = 0;
    } else if (currentSlide < 0) {
        currentSlide = slides.length - 1;
    }

    // إظهار الشريحة الجديدة
    slides[currentSlide].classList.add('active');
}

function moveSlide(direction) {
    showSlide(currentSlide + direction);

    // إعادة تعيين التوقيت عند التغيير اليدوي
    resetAutoSlide();
}

function startAutoSlide() {
    // تغيير الشريحة كل 5 ثواني
    autoSlideInterval = setInterval(() => {
        moveSlide(1);
    }, 5000);
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    startAutoSlide();
}

// تشغيل عند تحميل الصفحة
document.addEventListener('DOMContentLoaded', () => {
    initSlider();
});
