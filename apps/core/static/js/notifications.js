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
                li.classList.add('dropdown-item'); // Добавляем класс Bootstrap
                li.innerHTML = notification.message;
                li.addEventListener('click', function () {
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

// Переключение отображения уведомлений
document.getElementById('notification-bell').addEventListener('click', function (event) {
    const notificationList = document.getElementById('notification-list');
    const isVisible = notificationList.style.display === 'block';

    // Переключение видимости вручную
    notificationList.style.display = isVisible ? 'none' : 'block';
    event.stopPropagation(); // Остановка всплытия события
});

// Закрытие уведомлений при клике на пустое место
document.addEventListener('click', function (event) {
    const notificationList = document.getElementById('notification-list');
    const notificationBell = document.getElementById('notification-bell');

    // Если клик был вне колокольчика и списка уведомлений
    if (notificationList.style.display === 'block' &&
        !notificationList.contains(event.target) &&
        event.target !== notificationBell) {
        notificationList.style.display = 'none';
    }
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
