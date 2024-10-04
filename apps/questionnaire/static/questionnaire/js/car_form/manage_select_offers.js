// Оптимизированный код для вывода оферов в аккордеон
document.addEventListener('DOMContentLoaded', () => {
    const clientId = document.querySelector('input[name="client_id"]').value;
    console.log(`Client ID: ${clientId}`);

    fetch(`/questionnaire/offers/?client_id=${clientId}`)
        .then(response => response.json())
        .then(data => {
            const accordion = document.getElementById('bankOffersAccordion');
            accordion.innerHTML = '';
            const offersByBank = data.offers.reduce((acc, offerHtml) => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(offerHtml, 'text/html');
                const offerElement = doc.body.firstChild;
                const bank = offerElement.querySelector('.offer-bank').textContent.trim();

                if (!acc[bank]) {
                    acc[bank] = [];
                }
                acc[bank].push(offerHtml);
                return acc;
            }, {});

            Object.entries(offersByBank).forEach(([bank, offers], index) => {
                const collapseId = `collapse-${index}`;
                const headingId = `heading-${index}`;

                const accordionItem = document.createElement('div');
                accordionItem.className = 'accordion-item';
                accordionItem.dataset.bank = bank;

                const accordionHeader = document.createElement('h2');
                accordionHeader.className = 'accordion-header';
                accordionHeader.id = headingId;

                const button = document.createElement('button');
                button.className = 'accordion-button';
                button.type = 'button';
                button.dataset.bsToggle = 'collapse';
                button.dataset.bsTarget = `#${collapseId}`;
                button.setAttribute('aria-expanded', index === 0 ? 'true' : 'false');
                button.setAttribute('aria-controls', collapseId);
                button.textContent = bank;

                accordionHeader.appendChild(button);
                accordionItem.appendChild(accordionHeader);

                const collapseDiv = document.createElement('div');
                collapseDiv.id = collapseId;
                collapseDiv.className = 'accordion-collapse collapse';
                collapseDiv.setAttribute('aria-labelledby', headingId);
                collapseDiv.dataset.bsParent = '#bankOffersAccordion';

                const accordionBody = document.createElement('div');
                accordionBody.className = 'accordion-body';

                offers.forEach(offerHtml => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(offerHtml, 'text/html');
                    const offerElement = doc.body.firstChild;
                    accordionBody.appendChild(offerElement);
                });

                collapseDiv.appendChild(accordionBody);
                accordionItem.appendChild(collapseDiv);
                accordion.appendChild(accordionItem);
            });

            addOfferSelectEventListeners();
            addRemoveEventListeners();
        })
        .catch(error => console.error('Ошибка при загрузке оферов:', error));
});


async function saveSelectedOffer(offerId, csrfToken, clientId, totalLoanAmount) {
    const data = {client_id: clientId, offer_id: offerId, total_loan_amount: totalLoanAmount};

    try {
        const response = await fetch('/questionnaire/manage_offers/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        const result = await response.json();
        if (result.status !== 'success') {
            console.error('Error saving offer:', result.message);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function addOfferSelectEventListeners() {
    document.querySelectorAll('.select-offer-button').forEach(button => {
        button.addEventListener('click', async function () {
            const offerId = this.getAttribute('data-offer-id');
            const carPrice = document.getElementById('id_car_price_car_info').value;
            const initialPayment = document.getElementById('id_initial_payment').value;
            const totalLoanAmount = document.getElementById('total_loan_amount_input').value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const clientId = document.querySelector('input[name="client_id"]').value;

            await saveSelectedOffer(offerId, csrfToken, clientId, totalLoanAmount);

            fetch(`/questionnaire/get_card_offer/${offerId}/?car_price=${carPrice}&initial_payment=${initialPayment}&total_loan_amount=${totalLoanAmount}`)
                .then(response => response.text())
                .then(html => {
                    const offersList = document.getElementById('offers_card_list');
                    const newCard = document.createElement('div');
                    newCard.classList.add('col-md-4');
                    newCard.innerHTML = html;
                    newCard.dataset.offerButtonId = offerId;

                    offersList.appendChild(newCard);
                    addRemoveEventListener(newCard);

                    this.disabled = true;
                    this.classList.add('disabled');
                })
                .catch(error => console.error('Ошибка при загрузке предложения:', error));
        });
    });
}

function addRemoveEventListener(card) {
    card.querySelector('.remove-card').addEventListener('click', function () {
        const offerId = card.dataset.offerButtonId;
        const clientId = document.querySelector('input[name="client_id"]').value;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(`/questionnaire/manage_offers/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({offer_id: offerId, client_id: clientId})
        })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    card.remove();
                    const button = document.querySelector(`.select-offer-button[data-offer-id="${offerId}"]`);
                    if (button) {
                        button.disabled = false;
                        button.classList.remove('disabled');
                    }
                } else {
                    console.error('Ошибка при удалении офера');
                }
            })
            .catch(error => console.error('Ошибка при удалении офера:', error));
    });
}

function addRemoveEventListeners() {
    document.querySelectorAll('.remove-card').forEach(button => {
        button.addEventListener('click', function () {
            const offerId = this.getAttribute('data-offer-id');
            const clientId = document.querySelector('input[name="client_id"]').value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(`/questionnaire/manage_offers/`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({offer_id: offerId, client_id: clientId})
            })
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        this.closest('.col-md-4').remove();
                        const selectButton = document.querySelector(`.select-offer-button[data-offer-id="${offerId}"]`);
                        if (selectButton) {
                            selectButton.disabled = false;
                            selectButton.classList.remove('disabled');
                        }
                    } else {
                        console.error('Ошибка при удалении офера');
                    }
                })
                .catch(error => console.error('Ошибка при удалении офера:', error));
        });
    });
}

// Загрузка сохраненных карточек после перезагрузки страницы
document.addEventListener('DOMContentLoaded', () => {
    const clientId = document.querySelector('input[name="client_id"]').value;

    // Загрузка сохраненных карточек
    fetch(`/questionnaire/manage_offers/?client_id=${clientId}`)
        .then(response => response.json())
        .then(data => {
            const offersList = document.getElementById('offers_card_list');
            offersList.innerHTML = '';

            data.offers.forEach(offerHtml => {
                const offerElement = document.createElement('div');
                offerElement.classList.add('col-md-4');
                offerElement.innerHTML = offerHtml;
                offersList.appendChild(offerElement);

                // Отключаем кнопки "Выбрать" для существующих карточек
                const offerId = offerElement.querySelector('.remove-card').getAttribute('data-offer-id');
                const selectButton = document.querySelector(`.select-offer-button[data-offer-id="${offerId}"]`);
                if (selectButton) {
                    selectButton.disabled = true;
                    selectButton.classList.add('disabled');
                }
            });

            addRemoveEventListeners();
        })
        .catch(error => console.error('Ошибка при загрузке оферов:', error));
});

function addCheckboxEventListeners() {
    document.querySelectorAll('.form-check-input').forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const offerId = this.getAttribute('data-offer-id');
            const isChecked = this.checked;
            console.log(`Offer ID: ${offerId}, Checked: ${isChecked}`);
        });
    });
}

// Обновление предложений после перезагрузки страницы
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('show-partner-offers').addEventListener('click', () => {
        const clientId = document.querySelector('input[name="client_id"]').value;
        updateOffers(clientId);
    });

    function updateOffers(clientId) {
        const financingTerm = document.querySelector('[name="financing_term"]').selectedOptions[0].textContent;

        if (financingTerm && financingTerm > 0) {
            const formData = new FormData();
            formData.append('financing_term', financingTerm);
            formData.append('client_id', clientId);
            for (let pair of formData.entries()) {
                console.log(`${pair[0]}: ${pair[1]}`);
            }
            fetch('/questionnaire/offers/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Accept': 'application/json'
                }
            })
                .then(response => response.json())
                .then(offerItems => {
                    const container = document.getElementById('offers-container');
                    container.innerHTML = `<div class="accordion" id="bankOffersAccordion"></div>`;
                    const accordion = document.getElementById('bankOffersAccordion');

                    offerItems.forEach((offerItem, index) => {
                        const parser = new DOMParser();
                        const doc = parser.parseFromString(offerItem, 'text/html');
                        const offerElement = doc.body.firstChild;

                        const bank = offerElement.querySelector('.offer-bank').textContent;
                        if (!accordion.querySelector(`[data-bank="${bank}"]`)) {
                            const collapseId = `collapse-${index}`;
                            const headingId = `heading-${index}`;

                            const accordionItem = document.createElement('div');
                            accordionItem.className = 'accordion-item';
                            accordionItem.dataset.bank = bank;

                            const accordionHeader = document.createElement('h2');
                            accordionHeader.className = 'accordion-header';
                            accordionHeader.id = headingId;

                            const button = document.createElement('button');
                            button.className = 'accordion-button';
                            button.type = 'button';
                            button.dataset.bsToggle = 'collapse';
                            button.dataset.bsTarget = `#${collapseId}`;
                            button.setAttribute('aria-expanded', index === 0 ? 'true' : 'false');
                            button.setAttribute('aria-controls', collapseId);
                            button.textContent = bank;

                            accordionHeader.appendChild(button);
                            accordionItem.appendChild(accordionHeader);

                            const collapseDiv = document.createElement('div');
                            collapseDiv.id = collapseId;
                            collapseDiv.className = `accordion-collapse collapse`;
                            collapseDiv.setAttribute('aria-labelledby', headingId);
                            collapseDiv.dataset.bsParent = `#bankOffersAccordion`;

                            const accordionBody = document.createElement('div');
                            accordionBody.className = 'accordion-body';

                            collapseDiv.appendChild(accordionBody);
                            accordionItem.appendChild(collapseDiv);
                            accordion.appendChild(accordionItem);
                        }

                        const accordionBody = accordion.querySelector(`[data-bank="${bank}"] .accordion-body`);
                        accordionBody.appendChild(offerElement);
                    });

                    addOfferSelectEventListeners();
                    addRemoveEventListeners();
                })
                .catch(error => console.error('Ошибка при загрузке предложений:', error));
        } else {
            enqueueAlert('Неверный срок финансирования');
        }
    }

    addOfferSelectEventListeners();
    addRemoveEventListeners();
});