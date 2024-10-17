function loadNotifications() {
    fetch('/core/get_notifications/')
        .then(response => response.json())
        .then(data => {
            const notificationCountElem = document.getElementById('notification-count');
            const notificationList = document.getElementById('notification-list');

            notificationList.innerHTML = '';
            notificationCountElem.textContent = data.notifications.length;

            data.notifications.forEach(notification => {
                const li = document.createElement('li');
                li.textContent = notification.message;
                li.addEventListener('click', function() {
                    markAsRead(notification.id);  // Отметить как прочитанное
                    li.style.textDecoration = 'line-through';
                });
                notificationList.appendChild(li);
            });
        });
}

function markAsRead(notificationId) {
    fetch(`/core/mark_notification_as_read/${notificationId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        }
    }).then(() => {
        loadNotifications();
    });
}

document.getElementById('notification-bell').addEventListener('click', function() {
    const notificationList = document.getElementById('notification-list');
    notificationList.style.display = notificationList.style.display === 'none' ? 'block' : 'none';
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Опрашиваем сервер каждые 10 секунд
setInterval(loadNotifications, 10000);

// Загружаем уведомления при загрузке страницы
window.onload = loadNotifications;
