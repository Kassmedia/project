document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('change-password-form');
    form.addEventListener('submit', (event) => {
        alert('Password changed successfully!');
    });
});
