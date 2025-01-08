document.addEventListener('DOMContentLoaded', () => {
    const notifications = document.querySelectorAll('.notification-item.unread');

    notifications.forEach(notification => {
        notification.addEventListener('click', () => {
            notification.classList.remove('unread');
            notification.classList.add('read');
        });
    });
});
