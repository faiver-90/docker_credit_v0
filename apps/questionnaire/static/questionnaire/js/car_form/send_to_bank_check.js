document.getElementById('send-to-bank-form').addEventListener('submit', function(event) {
    event.preventDefault(); // предотвращаем отправку формы

    // Проверка всех полей формы с атрибутом required на заполненность
    const form = document.getElementById('initial_information');
    const requiredFields = form.querySelectorAll('[required]');
    let allFieldsFilled = true;

    requiredFields.forEach(field => {
        if (field.value.trim() === '') {
            allFieldsFilled = false;
            field.classList.add('is-invalid'); // Добавляем класс для отображения ошибки
        } else {
            field.classList.remove('is-invalid'); // Убираем класс ошибки, если поле заполнено
        }
    });

    if (!allFieldsFilled) {
        enqueueAlert("Все обязательные поля должны быть заполнены.");
        return;
    }

    const selectedOffers = [];
    document.querySelectorAll('#offers_card_list input[type="checkbox"]:checked').forEach(function(checkbox) {
        selectedOffers.push(checkbox.getAttribute('data-offer-id'));
    });

    if (selectedOffers.length === 0) {
        enqueueAlert("Не выбрано ни одно предложение в 'Предварительные расчеты'. Выберите хотя бы одно предложение");
        return;
    }

    document.getElementById('selected_offers').value = selectedOffers.join(',');

    this.submit(); // отправляем форму
});