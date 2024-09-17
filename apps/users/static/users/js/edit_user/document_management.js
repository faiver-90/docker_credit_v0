document.addEventListener("DOMContentLoaded", function () {
    const userId = document.querySelector('input[name="user_id"]').value;
    const uploadDocumentUrl = `/users/user_upload/${userId}/`;

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

    const csrftoken = getCookie('csrftoken');

    // Функция для обновления списка загруженных документов
    function loadUploadedDocuments() {
        fetch(uploadDocumentUrl, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('upload_file_user').innerHTML = data.html_form;
                attachDeleteEventListeners(); // Прикрепить обработчики событий для кнопок удаления
            })
            .catch(error => {
                console.error('An error occurred:', error);
            });
    }

    // Обработка отправки формы загрузки документов
    document.addEventListener('submit', function (event) {
        if (event.target && event.target.id === 'uploadForm') {
            event.preventDefault();
            const form = event.target;
            const formData = new FormData(form);
            const submitButton = form.querySelector('button[type="submit"]');

            // Блокируем кнопку
            submitButton.disabled = true;

            // Проверка наличия типа документа
            const documentType = form.querySelector('select[name="document_type"]').value;
            if (!documentType) {
                enqueueAlert('Пожалуйста, выберите тип загружаемого документа.');
                submitButton.disabled = false; // Разблокируем кнопку

                return;
            }

            // Проверка наличия выбранных файлов
            const files = form.querySelector('input[name="document_files"]').files;
            if (files.length === 0) {
                enqueueAlert('Пожалуйста, выберите файлы для загрузки.');
                submitButton.disabled = false; // Разблокируем кнопку

                return;
            }

            fetch(uploadDocumentUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                }
            })
                .then(response => response.json())
                .then(data => {
                    submitButton.disabled = false; // Разблокируем кнопку

                    if (data.status === 'success') {
                        enqueueAlert(data.message);
                        loadUploadedDocuments(); // Загрузить обновленный список документов
                    } else {
                        if (data.errors) {
                            enqueueAlert('Errors: ' + JSON.stringify(data.errors));
                        } else if (data.message) {
                            enqueueAlert('Error: ' + data.message);
                        } else {
                            enqueueAlert('An unknown error occurred.');
                        }
                    }
                })
                .catch(error => {
                    submitButton.disabled = false; // Разблокируем кнопку
                    enqueueAlert('An error occurred: ' + error);
                });
        }
    });

    // Функция для удаления документа
    function deleteDocument(documentId) {
        fetch(uploadDocumentUrl, {
            method: 'DELETE',
            body: JSON.stringify({document_id: documentId}),
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    enqueueAlert(data.message);
                    loadUploadedDocuments(); // Загрузить обновленный список документов
                } else {
                    enqueueAlert('Error: ' + data.message);
                }
            })
            .catch(error => {
                enqueueAlert('An error occurred: ' + error);
            });
    }

    // Функция для отображения модального окна подтверждения удаления
    function showDeleteConfirmModal(documentId) {
        const confirmButton = document.getElementById('confirmDeleteDocumentButton');
        confirmButton.setAttribute('data-document-id', documentId);
        $('#deleteDocumentModal').modal('show');
    }

    // Обработчик события для кнопки подтверждения удаления
    document.getElementById('confirmDeleteDocumentButton').addEventListener('click', function () {
        const documentId = this.getAttribute('data-document-id');
        deleteDocument(documentId);
        $('#deleteDocumentModal').modal('hide');
    });

    // Функция для прикрепления обработчиков событий для кнопок удаления
    function attachDeleteEventListeners() {
        document.querySelectorAll('.btn-delete').forEach(button => {
            button.addEventListener('click', function () {
                const documentId = this.getAttribute('data-document-id');
                showDeleteConfirmModal(documentId);
            });
        });
    }

    // Начальная загрузка загруженных документов
    loadUploadedDocuments();
});
