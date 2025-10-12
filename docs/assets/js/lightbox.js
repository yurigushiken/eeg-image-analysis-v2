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

        const closeBtn = document.createElement('button');
        closeBtn.className = 'lightbox-close';
        closeBtn.innerHTML = '&times;';
        closeBtn.setAttribute('aria-label', 'Close image viewer');
        closeBtn.onclick = closeLightbox;

        content.appendChild(closeBtn);
        content.appendChild(img);
        overlay.appendChild(content);
        document.body.appendChild(overlay);

        // Close on overlay click (but not on image click)
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) {
                closeLightbox();
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && overlay.classList.contains('active')) {
                closeLightbox();
            }
        });

        return overlay;
    }

    // Open lightbox with image
    function openLightbox(imageSrc, altText) {
        const overlay = document.querySelector('.lightbox-overlay');
        const img = overlay.querySelector('.lightbox-image');

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

    // Initialize on DOM ready
    function init() {
        // Create lightbox overlay
        createLightbox();

        // Attach click handlers to all thumbnail links with data-lightbox attribute
        const thumbnailLinks = document.querySelectorAll('a[data-lightbox]');

        thumbnailLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
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
