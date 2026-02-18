document.addEventListener('DOMContentLoaded', function () {
    const wrapper = document.getElementById('sliderWrapper');
    const dots = document.querySelectorAll('.dot');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevSlide');
    const nextBtn = document.getElementById('nextSlide');

    if (!wrapper || slides.length === 0) return;

    let currentIndex = 0;
    const slideCount = slides.length;
    let autoSlideInterval;

    // Function to update slider position
    function goToSlide(index) {
        if (index < 0) index = slideCount - 1;
        if (index >= slideCount) index = 0;

        // Since CSS forces direction: ltr on the container, we must always use LTR logic
        // regardless of the document direction.
        wrapper.style.transform = `translateX(-${index * 100}%)`;

        // Update dots
        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });
        currentIndex = index;
    }

    // Event listeners for dots
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            goToSlide(index);
            resetTimer(); // Reset timer on manual interaction
        });
    });

    // Event listeners for arrows
    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            goToSlide(currentIndex - 1);
            resetTimer();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            goToSlide(currentIndex + 1);
            resetTimer();
        });
    }

    // Auto sliding
    function startTimer() {
        autoSlideInterval = setInterval(() => goToSlide(currentIndex + 1), 5000);
    }

    function resetTimer() {
        clearInterval(autoSlideInterval);
        startTimer();
    }

    // Initialize
    if (slideCount > 0) {
        goToSlide(0);
        startTimer();
    }
});
