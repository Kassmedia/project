document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('nav ul li a');
    const currentPath = window.location.pathname;

    links.forEach(link => {
        const linkPath = new URL(link.href).pathname; // Extract the full pathname from the link's href

        // Check if the link corresponds to the current page
        if (linkPath === currentPath || (currentPath === '/' && linkPath === '/')) {
            link.classList.add('active'); // Add active class for styling
        } else {
            link.classList.remove('active'); // Remove active class if not matching
        }
    });
});
