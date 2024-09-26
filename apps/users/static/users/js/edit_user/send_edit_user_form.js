document.addEventListener('DOMContentLoaded', function () {
    const editForm = document.getElementById('edit-user-form');
    const submitButton = document.getElementById('submit-edit-user');
    const deleteButton = document.getElementById('delete-user');
    const userId = document.getElementById('user_id').value;
    const formActionUrl = '/users/edit/' + userId + '/';
    const nextUrl = document.querySelector('input[name="next"]').value;

    async function saveField(field) {
        const form = field.closest('form');
        const formData = new FormData(form);
        formData.append('ignore_required', 'true'); // добавим параметр для игнорирования обязательных полей
        const url = formActionUrl;

        try {
            console.log(`Attempting to save field ${field.name} with value ${field.value}`);
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }

            const contentType = response.headers.get('content-type');
            if (!contentType || !contentType.includes('application/json')) {
                throw new Error(`Expected JSON, got ${contentType}`);
            }

            const data = await response.json();
            console.log(`Field ${field.name} saved successfully`, data);
        } catch (error) {
            console.error(`Error saving field ${field.name}`, error);
        }
    }

    // Add event listeners to all input fields for auto-save
    editForm.querySelectorAll('input, select, textarea').forEach(field => {
        if (field.type === 'checkbox' || field.type === 'radio') {
            field.addEventListener('change', () => saveField(field));
        } else {
            field.addEventListener('blur', () => saveField(field));
        }
    });

    submitButton.addEventListener('click', function () {
        const formData = new FormData(editForm);
        formData.append('next', nextUrl);

        fetch(formActionUrl, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Form submitted successfully");
                window.location.href = data.redirect_url;
            } else {
                console.error('Error submitting form:', data.errors);
                enqueueAlert('Ошибка при сохранении изменений');
            }
        })
        .catch(error => {
            console.error('Server error:', error);
            enqueueAlert('Ошибка сервера. Пожалуйста, попробуйте позже.');
        });
    });

    deleteButton.addEventListener('click', function () {
        if (confirm('Вы уверены, что хотите удалить этого пользователя?')) {
            const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

            fetch(formActionUrl + '?next=' + encodeURIComponent(nextUrl), {
                method: 'DELETE',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    csrfmiddlewaretoken: csrfToken
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("User deleted successfully");
                    window.location.href = data.redirect_url;
                } else {
                    console.error('Error deleting user:', data.errors);
                    enqueueAlert('Ошибка при удалении пользователя');
                }
            })
            .catch(error => {
                console.error('Server error:', error);
                enqueueAlert('Ошибка сервера. Пожалуйста, попробуйте позже.');
            });
        }
    });
});
