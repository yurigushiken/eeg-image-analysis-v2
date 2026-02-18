/**
 * Statistics Toggle Handler
 * Handles expand/collapse functionality for statistics sections
 */

(function() {
    'use strict';

    function init() {
        // Find all statistics toggle buttons
        const toggleButtons = document.querySelectorAll('.stats-toggle');

        toggleButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const analysisId = button.getAttribute('data-analysis-id');
                const statsContent = document.getElementById('stats-' + analysisId);

                if (!statsContent) {
                    console.warn('Stats content not found for analysis:', analysisId);
                    return;
                }

                // Toggle expanded state
                const isExpanded = button.classList.contains('expanded');

                if (isExpanded) {
                    // Collapse
                    button.classList.remove('expanded');
                    statsContent.classList.remove('show');
                    button.setAttribute('aria-expanded', 'false');
                    button.textContent = 'Show Statistics';
                } else {
                    // Expand
                    button.classList.add('expanded');
                    statsContent.classList.add('show');
                    button.setAttribute('aria-expanded', 'true');
                    button.textContent = 'Hide Statistics';
                }
            });
        });

        console.log(`Initialized statistics toggles for ${toggleButtons.length} analyses`);
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
