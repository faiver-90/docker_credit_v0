document.addEventListener('DOMContentLoaded', function() {
    function addInputListener(id) {
        const addressInput = document.getElementById(id);
        const resultsList = document.getElementById(id + 'Results');

        if (addressInput && resultsList) {
            addressInput.addEventListener('input', function() {
                const query = this.value;
                if (query.length > 2) {
                    fetch(`/questionnaire/get-address-suggestions/?query=${query}`)
                        .then(response => {
                            if (!response.ok) {
                                throw new Error(`HTTP error! status: ${response.status}`);
                            }
                            return response.json();
                        })
                        .then(data => {
                            resultsList.innerHTML = '';
                            if (data.suggestions) {
                                data.suggestions.forEach(item => {
                                    const listItem = document.createElement('li');
                                    listItem.classList.add('dropdown-item');
                                    listItem.textContent = item.value;
                                    listItem.addEventListener('click', function() {
                                        addressInput.value = item.value;
                                        resultsList.innerHTML = '';
                                    });
                                    resultsList.appendChild(listItem);
                                });
                                resultsList.style.width = 'auto';
                                resultsList.style.minWidth = addressInput.offsetWidth + 'px';
                                resultsList.classList.add('show'); // Показать список
                            } else {
                                resultsList.appendChild(document.createElement('li')).textContent = 'Ничего не найдено';
                            }
                        })
                        .catch(error => {
                            console.error('Error fetching data:', error);
                            resultsList.innerHTML = '';
                            resultsList.appendChild(document.createElement('li')).textContent = 'Ошибка поиска';
                        });
                } else {
                    resultsList.innerHTML = '';
                }
            });

            addressInput.addEventListener('keydown', function(event) {
                if (event.key === 'Tab') {
                    const firstItem = resultsList.querySelector('.dropdown-item');
                    if (firstItem) {
                        addressInput.value = firstItem.textContent;
                        resultsList.innerHTML = '';
                        resultsList.classList.remove('show'); // Скрыть список
                    }
                }
            });
        } else {
            console.error(`Element with id "${id}" or "${id}Results" not found.`);
        }
    }

    const addressFields = [
        'id_registration_address_client',
        'id_living_address_contact',
        'id_registration_address_employment',
        'id_address_real_estate'
    ];

    function observeAndApplyListeners() {
        addressFields.forEach(id => {
            if (document.getElementById(id) && document.getElementById(id + 'Results')) {
                addInputListener(id);
            } else {
                // console.log(`Waiting for element with id "${id}" and "${id}Results" to appear...`);
                const observer = new MutationObserver(function(mutations, observer) {
                    const addressInput = document.getElementById(id);
                    const resultsList = document.getElementById(id + 'Results');
                    if (addressInput && resultsList) {
                        addInputListener(id);
                        observer.disconnect(); // Stop observing once the element is found
                    }
                });
                observer.observe(document.body, { childList: true, subtree: true });
            }
        });
    }

    observeAndApplyListeners();

    // Добавление обработчика для скрытия выпадающего списка при клике вне его
    document.addEventListener('click', function(event) {
        addressFields.forEach(id => {
            const addressInput = document.getElementById(id);
            const resultsList = document.getElementById(id + 'Results');
            if (resultsList && !addressInput.contains(event.target) && !resultsList.contains(event.target)) {
                resultsList.innerHTML = '';
                resultsList.classList.remove('show'); // Скрыть список
            }
        });
    });
});
