let currentPage = 1;

function loadNotifications(page = currentPage) {
    fetch(`/core/get_notifications/?page=${page}&per_page=5`)
        .then(response => response.json())
        .then(data => {
            const notificationCountElem = document.getElementById('notification-count');
            const notificationList = document.getElementById('notification-list');

            notificationList.innerHTML = '';
            notificationCountElem.textContent = data.notifications.filter(notification => !notification.is_read).length;

            // Обновляем список уведомлений
            data.notifications.forEach(notification => {
                const li = document.createElement('li');
                li.classList.add('dropdown-item');
                li.innerHTML = notification.message;
                li.style.fontWeight = notification.is_read ? 'normal' : 'bold';

                li.addEventListener('click', function () {
                    if (!notification.is_read) {
                        markAsRead(notification.id);
                        li.style.fontWeight = 'normal';
                        notificationList.removeChild(li);
                        notificationList.appendChild(li);
                    }
                });

                notificationList.appendChild(li);
            });

            // Добавляем кнопки пагинации, если нужно
            if (data.total_pages > 1) {
                addPaginationButtons(data.has_previous, data.has_next);
            }
        });
}

function addPaginationButtons(hasPrevious, hasNext) {
    const paginationContainer = document.createElement('div');
    paginationContainer.className = 'pagination-buttons';

    if (hasPrevious) {
        const prevButton = document.createElement('button');
        prevButton.textContent = 'Предыдущая';
        prevButton.onclick = () => {
            currentPage -= 1;
            loadNotifications(currentPage);
        };
        paginationContainer.appendChild(prevButton);
    }

    if (hasNext) {
        const nextButton = document.createElement('button');
        nextButton.textContent = 'Следующая';
        nextButton.onclick = () => {
            currentPage += 1;
            loadNotifications(currentPage);
        };
        paginationContainer.appendChild(nextButton);
    }

    const notificationList = document.getElementById('notification-list');
    notificationList.appendChild(paginationContainer);
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
setInterval(() => loadNotifications(currentPage), 10000);

// Загружаем уведомления при загрузке страницы
window.onload = loadNotifications;
