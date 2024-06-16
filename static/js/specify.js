const carouselItems = document.querySelectorAll('.carousel-item');
let currentIndex = 0;
const totalItems = carouselItems.length;

carouselItems.forEach(item => {
    item.addEventListener('mouseover', function() {
        document.body.style.backgroundColor = this.getAttribute('data-color');
    });

    item.addEventListener('mouseout', function() {
        document.body.style.backgroundColor = '';
    });
});

function showItem(index) {
    const offset = -index * 100;
    carouselItems.forEach(item => {
        item.style.transform = `translateX(${offset}%)`;
    });
}

function nextItem() {
    currentIndex = (currentIndex + 1) % totalItems;
    showItem(currentIndex);
}

function prevItem() {
    currentIndex = (currentIndex - 1 + totalItems) % totalItems;
    showItem(currentIndex);
}

document.addEventListener('DOMContentLoaded', () => {
    showItem(currentIndex);
});
