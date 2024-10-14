document.addEventListener('DOMContentLoaded', function () {
    const clientId = document.querySelector('input[name="client_id"]').value;
    console.log(`Client ID: ${clientId}`);

    // Загрузка данных при клике по аккордиону "Дополнительная информация"
    const additionalInfoAccordion = document.getElementById('collapseAllOtherDataClient');
    additionalInfoAccordion.addEventListener('show.bs.collapse', function () {
        const contentContainer = document.getElementById('all_other_data_client');
        if (!contentContainer.getAttribute('data-loaded')) {
            loadAllDataClient(clientId);
            contentContainer.setAttribute('data-loaded', 'true'); // Помечаем, что данные загружены
        }
    });
});

function loadAllDataClient(clientId) {
    console.log("Загрузка шаблона all_data_client.html...");
    fetch(`/questionnaire/load_all_data_client/${clientId}/`, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(response => {
        console.log("Fetch response status:", response.status);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log("Шаблон загружен, обновление HTML");
        document.getElementById('all_other_data_client').innerHTML = data.html;
        if (data.partner_offers_shown) {
            console.log('Предложения партнеров уже показаны, скрипт не будет работать снова.');
            document.getElementById('show-partner-offers').setAttribute('data-shown', 'true');
        }
    })
    .catch(error => console.error('Ошибка загрузки шаблона all_data_client:', error));
}
