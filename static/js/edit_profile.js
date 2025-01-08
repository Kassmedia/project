document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('edit-profile-form');
    form.addEventListener('submit', (event) => {
        alert('Your profile has been updated successfully!');
    });
});
