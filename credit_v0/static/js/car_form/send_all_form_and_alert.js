document.addEventListener('DOMContentLoaded', function () {
    const saveButton = document.getElementById('submit-offers');
    let blurTimeout; // Объявление переменной blurTimeout
    const clientId = document.querySelector('input[name="client_id"]').value;

    async function saveField(field) {
        const form = field.closest('form');
        if (!form) {
            console.error('Не удалось найти форму для поля:', field);
            return;
        }

        const formData = new FormData(form);
        formData.append('ignore_required', 'true'); // добавим параметр для игнорирования обязательных полей
        let url;

        if (form.id === 'initial_information') {
            url = '/credit/car-form/'; // URL для initial_information
        } else if (form.id === 'additional_information') {
            url = `/credit/load_all_data_client/${clientId}/`; // URL для additional_information
        } else {
            console.error('Unknown form ID');
            return;
        }

        const csrfToken = formData.get('csrfmiddlewaretoken');
        if (!csrfToken) {
            console.error('CSRF токен не найден в форме:', form);
            return;
        }

        console.log(`Saving field: ${field.name} at URL: ${url}`);

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });

            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }

            const data = await response.json();
            console.log(`Field ${field.name} saved successfully`, data);
        } catch (error) {
            console.error(`Error saving field ${field.name}:`, error);
        }
    }

    // Add event listeners to all input fields for auto-save
    function addAutoSaveListeners(form) {
        form.querySelectorAll('input, select, textarea').forEach(field => {
            if (field.type === 'checkbox' || field.type === 'radio') {
                field.addEventListener('change', () => saveField(field));
            } else {
                field.addEventListener('blur', () => {
                    clearTimeout(blurTimeout);
                    blurTimeout = setTimeout(() => saveField(field), 1000);
                });
            }
        });
    }

    // Initially add listeners to InitialForm
    addAutoSaveListeners(document);

    saveButton.addEventListener('click', async function (event) {
        event.preventDefault(); // предотвращаем отправку формы

        const allForms = document.querySelectorAll('form');
        let missingFields = [];

        allForms.forEach(function (form) {
            const requiredFields = form.querySelectorAll('[required]');

            requiredFields.forEach(function (field) {
                console.log(`Проверка поля: ${field.name}, значение: ${field.value}`);
                if (!field.value.trim()) {
                    const label = form.querySelector(`label[for=${field.id}]`);
                    const labelText = label ? label.innerText : field.name;
                    missingFields.push(labelText);
                    console.log(`Поле ${labelText} не заполнено`);
                }
            });
        });

        if (missingFields.length > 0) {
            enqueueAlert('Пожалуйста, заполните следующие поля: ' + missingFields.join(', '));
            console.log('Незаполненные поля: ' + missingFields.join(', '));
            return;
        }

        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        const clientId = document.querySelector('input[name="client_id"]').value;
        console.log('CSRF Token: ' + csrfToken);
        console.log('Client ID: ' + clientId);

        const otherDataClient = document.getElementById('all_other_data_client');
        if (otherDataClient && otherDataClient.innerHTML.trim()) {
            try {
                console.log('Отправка дополнительной формы');
                const additionalForm = document.getElementById('additional_information');
                if (additionalForm && additionalForm.tagName === 'FORM') {
                    await sendAdditionalForm(csrfToken, clientId);
                } else {
                    console.error('Ошибка: элемент additional_information не является формой.');
                }
            } catch (error) {
                enqueueAlert('Error in sending additional form: ' + error.message);
                console.log('Error in sending additional form: ' + error.message);
                return;
            }
        }

        try {
            console.log('Отправка начальной формы');
            await sendInitialForm(csrfToken);
        } catch (error) {
            enqueueAlert('Error in sending initial form: ' + error.message);
            console.log('Error in sending initial form: ' + error.message);
        }
    });

    // Add listeners to newly loaded AdditionalForm using MutationObserver
    const observer = new MutationObserver(function (mutationsList) {
        for (const mutation of mutationsList) {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(node => {
                    if (node.id === 'additional_information') {
                        console.log('Additional form detected, adding auto-save listeners.');
                        addAutoSaveListeners(node);
                    }
                });
            }
        }
    });

    observer.observe(document.body, {childList: true, subtree: true});
});

async function sendInitialForm(csrfToken) {
    try {
        const form1 = document.getElementById('initial_information');
        const formData1 = new FormData(form1);
        formData1.append('ignore_required', 'true'); // добавим параметр для игнорирования обязательных полей

        console.log('Отправка initial_information формы');
        const response1 = await fetch('/credit/car-form/', { // URL для initial_information
            method: 'POST',
            body: formData1,
            headers: {
                'X-CSRFToken': csrfToken,
                'Accept': 'application/json'
            }
        });

        const data1 = await response1.json();
        const formEntries = {};
        for (const [key, value] of formData1.entries()) {
            formEntries[key] = value;
        }
        console.log('Отправленные данные формы initial_information:', formEntries);

        if (data1.success) {
            enqueueAlert('Данные initial_information формы сохранены');
            console.log('Данные initial_information формы успешно сохранены');
            return true;
        } else {
            throw new Error('Ошибка при сохранении данных первой формы.');
        }

    } catch (error) {
        enqueueAlert('Ошибка при сохранении данных initial_information формы: ' + error.message);
        console.error('Ошибка:', error);
        return false;
    }
}

async function sendAdditionalForm(csrfToken, clientId) {
    try {
        const form2 = document.getElementById('additional_information');
        const formData2 = new FormData(form2);
        formData2.append('ignore_required', 'true'); // добавим параметр для игнорирования обязательных полей

        const formEntries = {};
        for (const [key, value] of formData2.entries()) {
            formEntries[key] = value;
        }

        console.log('Отправка additional_information формы');
        const response2 = await fetch(`/credit/load_all_data_client/${clientId}/`, { // URL для additional_information
            method: 'POST',
            body: formData2,
            headers: {
                'X-CSRFToken': csrfToken,
                'Accept': 'application/json'
            }
        });

        const data2 = await response2.json();
        console.log('Отправленные данные формы additional_information:', formEntries);

        if (data2.success) {
            enqueueAlert('Данные формы additional_information успешно сохранены');
            console.log('Данные additional_information формы успешно сохранены');
            return true;
        } else {
            enqueueAlert('Ошибка при сохранении данных формы additional_information.');
            console.log('Ошибка при сохранении данных формы additional_information.');
            return false;
        }
    } catch (error) {
        enqueueAlert('Ошибка при сохранении данных additional_information формы: ' + error.message);
        console.error('Ошибка:', error);
        return false;
    }
}
