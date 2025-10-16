(function(){
    'use strict';

    function initCarousel(root){
        const track = root.querySelector('.carousel-track');
        const prev = root.querySelector('.carousel-prev');
        const next = root.querySelector('.carousel-next');
        const slides = Array.from(track.children);

        let index = 0;

        function update(){
            const slideWidth = slides[0]?.getBoundingClientRect().width || 0;
            track.style.transform = `translateX(${-index * (slideWidth + 16)}px)`; // 16px gap
            prev.disabled = index === 0;
            next.disabled = index >= Math.max(0, slides.length - visibleCount());
        }

        function visibleCount(){
            // Estimate how many fit based on container width and slide width
            const containerWidth = root.getBoundingClientRect().width;
            const slideWidth = slides[0]?.getBoundingClientRect().width || 1;
            const count = Math.max(1, Math.floor((containerWidth + 16) / (slideWidth + 16)));
            return count;
        }

        prev.addEventListener('click', function(){
            index = Math.max(0, index - visibleCount());
            update();
        });
        next.addEventListener('click', function(){
            index = Math.min(slides.length - visibleCount(), index + visibleCount());
            update();
        });

        window.addEventListener('resize', update);
        update();
    }

    function init(){
        document.querySelectorAll('.carousel').forEach(initCarousel);
    }

    if (document.readyState === 'loading'){
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();


