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


// When page loads, log a message
window.onload = function() {
    console.log("Help & Support and Messages pages loaded successfully.");
}

// Handle 'Compose New Message' button click
document.querySelector('.compose-btn').addEventListener('click', function() {
    alert("Compose New Message button clicked!");
});

// Handle form submission on Help & Support page
document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting to simulate submission
    alert("Your issue has been submitted. We will get back to you soon!");
});
