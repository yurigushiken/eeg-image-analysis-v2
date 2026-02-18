/**
 * Lightweight Lightbox for ERP Figure Viewing
 * No dependencies - pure vanilla JavaScript
 */

(function() {
    'use strict';

    // Create lightbox overlay on page load
    function createLightbox() {
        const overlay = document.createElement('div');
        overlay.className = 'lightbox-overlay';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-label', 'Image viewer');

        const content = document.createElement('div');
        content.className = 'lightbox-content';

        const img = document.createElement('img');
        img.className = 'lightbox-image';
        img.alt = 'Full-size ERP plot';

        // Navigation buttons
        const prevBtn = document.createElement('button');
        prevBtn.className = 'lightbox-nav prev';
        prevBtn.setAttribute('aria-label', 'Previous image');
        prevBtn.innerHTML = '&#8249;'; // ‹

        const nextBtn = document.createElement('button');
        nextBtn.className = 'lightbox-nav next';
        nextBtn.setAttribute('aria-label', 'Next image');
        nextBtn.innerHTML = '&#8250;'; // ›

        const closeBtn = document.createElement('button');
        closeBtn.className = 'lightbox-close';
        closeBtn.innerHTML = '&times;';
        closeBtn.setAttribute('aria-label', 'Close image viewer');
        closeBtn.onclick = closeLightbox;

        content.appendChild(closeBtn);
        content.appendChild(prevBtn);
        content.appendChild(img);
        content.appendChild(nextBtn);
        overlay.appendChild(content);
        document.body.appendChild(overlay);

        // Close on overlay click (but not on image click)
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeLightbox();
            }
        });

        // Close on Escape key and navigate with arrows
        document.addEventListener('keydown', function(e) {
            if (!overlay.classList.contains('active')) return;
            if (e.key === 'Escape') return closeLightbox();
            if (e.key === 'ArrowLeft') return navigateRelative(-1);
            if (e.key === 'ArrowRight') return navigateRelative(1);
        });

        prevBtn.addEventListener('click', function(){ navigateRelative(-1); });
        nextBtn.addEventListener('click', function(){ navigateRelative(1); });

        return overlay;
    }

    // Open lightbox with image
    function openLightbox(imageSrc, altText) {
        const overlay = document.querySelector('.lightbox-overlay');
        const img = overlay.querySelector('.lightbox-image');

        // Reset loading state for fade-in after the new image loads
        img.classList.remove('loaded');
        img.onload = function() {
            img.classList.add('loaded');
        };

        img.src = imageSrc;
        img.alt = altText || 'ERP plot';
        overlay.classList.add('active');

        // Prevent body scroll when lightbox is open
        document.body.style.overflow = 'hidden';
    }

    // Close lightbox
    function closeLightbox() {
        const overlay = document.querySelector('.lightbox-overlay');
        overlay.classList.remove('active');

        // Restore body scroll
        document.body.style.overflow = '';
    }

    // Navigate to previous/next thumbnail target relative to current
    function navigateRelative(delta) {
        const overlay = document.querySelector('.lightbox-overlay');
        if (!overlay.classList.contains('active')) return;
        const anchors = Array.from(document.querySelectorAll('a[data-lightbox]'));
        if (anchors.length === 0) return;

        // Determine current index by matching current image src
        const img = overlay.querySelector('.lightbox-image');
        const currentSrc = img.getAttribute('src');
        let idx = anchors.findIndex(a => a.getAttribute('href') === currentSrc);
        if (idx === -1) {
            idx = 0;
        }

        const nextIdx = (idx + delta + anchors.length) % anchors.length;
        const nextA = anchors[nextIdx];
        const href = nextA.getAttribute('href');
        const ariaLabel = nextA.getAttribute('aria-label');
        openLightbox(href, ariaLabel);
    }

    // Initialize on DOM ready
    function init() {
        // Create lightbox overlay
        createLightbox();

        // Attach click handlers to all thumbnail links with data-lightbox attribute
        const thumbnailLinks = document.querySelectorAll('a[data-lightbox]');

        thumbnailLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                // Preserve Ctrl/Meta/middle-click to open in new tab
                const isNewTab = e.ctrlKey || e.metaKey || e.button === 1;
                if (isNewTab) {
                    return; // let browser handle default
                }

                e.preventDefault();
                const href = link.getAttribute('href');
                const ariaLabel = link.getAttribute('aria-label');
                openLightbox(href, ariaLabel);
            });
        });

        console.log(`Initialized lightbox for ${thumbnailLinks.length} images`);
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose closeLightbox globally for the close button
    window.closeLightbox = closeLightbox;
})();
