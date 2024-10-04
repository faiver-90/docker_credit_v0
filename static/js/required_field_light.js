document.addEventListener('DOMContentLoaded', function () {
    // Функция для подсветки обязательных полей, если они пустые
    function highlightEmptyRequiredFields() {
        document.querySelectorAll('input[required], select[required], textarea[required]').forEach(field => {
            if (!field.value.trim()) {
                field.style.borderColor = 'red';
                field.style.backgroundColor = '#ffcccc'; // устанавливаем красный фон
                field.style.outline = 'none';
            } else {
                field.style.borderColor = '';
                field.style.backgroundColor = ''; // убираем красный фон
            }
        });
    }

    // Функция для удаления подсветки при вводе данных
    function removeHighlightOnInput() {
        document.querySelectorAll('input[required], select[required], textarea[required]').forEach(field => {
            field.addEventListener('input', () => {
                if (field.value.trim()) {
                    field.style.borderColor = '';
                    field.style.backgroundColor = ''; // убираем красный фон
                } else {
                    field.style.borderColor = 'red';
                    field.style.backgroundColor = '#ffcccc'; // устанавливаем красный фон
                }
            });
        });
    }

    // Функция для инициализации прослушивателей на формах
    function initializeFormListeners() {
        highlightEmptyRequiredFields();
        removeHighlightOnInput();

        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', (event) => {
                highlightEmptyRequiredFields();
                const invalidFields = form.querySelectorAll('input[required][style*="border-color: red"], select[required][style*="border-color: red"], textarea[required][style*="border-color: red"]');
                if (invalidFields.length > 0) {
                    event.preventDefault(); // Предотвращаем отправку формы, если есть незаполненные обязательные поля
                    alert('Пожалуйста, заполните все обязательные поля.');
                }
            });
        });
    }

    // Создаем наблюдатель за изменениями в DOM
    const observer = new MutationObserver((mutationsList, observer) => {
        mutationsList.forEach(mutation => {
            if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                mutation.addedNodes.forEach(node => {
                    if (node.nodeType === 1 && node.matches('form')) {
                        initializeFormListeners();
                    }
                });
            }
        });
    });

    // Конфигурация наблюдателя: следить за всеми изменениями дочерних элементов и их атрибутов
    const config = { childList: true, subtree: true };

    // Начинаем наблюдение за 'body'
    observer.observe(document.body, config);

    // Инициализация прослушивателей на уже существующих формах
    initializeFormListeners();
});
