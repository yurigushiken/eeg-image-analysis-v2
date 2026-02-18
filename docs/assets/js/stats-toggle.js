/**
 * Statistics Toggle Handler
 * Handles expand/collapse functionality for statistics sections
 */

(function() {
    'use strict';

    function init() {
        // Generic expandable section buttons (stats + topo + legacy stats-only).
        const toggleButtons = document.querySelectorAll('.expand-toggle, .stats-toggle');

        toggleButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const targetId = (
                    button.getAttribute('data-target') ||
                    (button.getAttribute('data-analysis-id') ? 'stats-' + button.getAttribute('data-analysis-id') : null)
                );
                const targetContent = targetId ? document.getElementById(targetId) : null;

                if (!targetContent) {
                    console.warn('Expandable content not found for target:', targetId);
                    return;
                }

                // Toggle expanded state
                const isExpanded = button.classList.contains('expanded');
                const showLabel = button.getAttribute('data-show-label') || 'Show Statistics';
                const hideLabel = button.getAttribute('data-hide-label') || 'Hide Statistics';

                if (isExpanded) {
                    // Collapse
                    button.classList.remove('expanded');
                    targetContent.classList.remove('show');
                    button.setAttribute('aria-expanded', 'false');
                    button.textContent = showLabel;
                } else {
                    // Expand
                    button.classList.add('expanded');
                    targetContent.classList.add('show');
                    button.setAttribute('aria-expanded', 'true');
                    button.textContent = hideLabel;
                }
            });
        });

        console.log(`Initialized expandable toggles for ${toggleButtons.length} sections`);
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
