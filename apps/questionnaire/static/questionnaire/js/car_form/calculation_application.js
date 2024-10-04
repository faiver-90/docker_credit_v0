document.addEventListener('DOMContentLoaded', function () {
    const carPriceInput = document.getElementById('id_car_price_car_info');
    const dealerEquipmentPriceInput = document.getElementById('id_dealer_equipment_price_car_info');
    const kaskoAmountInput = document.getElementById('id_kasko_amount');
    const gapAmountInput = document.getElementById('id_gap_amount');
    const szhAmountInput = document.getElementById('id_szh_amount');
    const szhTermInput = document.getElementById('id_szh_term');
    const financialProductsAmountInput = document.getElementById('id_financial_products_amount');
    const initialPaymentInput = document.getElementById('id_initial_payment');

    const kaskoIncludeCheckbox = document.getElementById('id_kasko_amount_include');
    const gapIncludeCheckbox = document.getElementById('id_gap_amount_include');
    const szhTermIncludeCheckbox = document.getElementById('id_szh_term_include');
    const financialProductsIncludeCheckbox = document.getElementById('id_financial_products_amount_include');
    const smsNotificationIncludeCheckbox = document.getElementById('sms_notification_include_checkbox');
    const installmentCommissionIncludeCheckbox = document.getElementById('id_installment_commission_include');

    const totalLoanAmountDisplay = document.getElementById('total_loan_amount');
    const carPriceDisplay = document.getElementById('car_price_display');
    const additionalEquipmentPriceDisplay = document.getElementById('additional_equipment_price_display');
    const kaskoDisplay = document.getElementById('kasko_display');
    const gapDisplay = document.getElementById('gap_display');
    const szgDisplay = document.getElementById('szg_display');
    const financialProductsDisplay = document.getElementById('financial_products_display');
    const smsNotificationDisplay = document.getElementById('sms_notification_display');
    const installmentCommissionDisplay = document.getElementById('installment_commission_display');

    function calculateTotalLoanAmount() {
        const carPrice = parseFloat(carPriceInput.value) || 0;
        const dealerEquipmentPrice = parseFloat(dealerEquipmentPriceInput.value) || 0;
        const kaskoAmount = parseFloat(kaskoAmountInput.value) || 0;
        const gapAmount = parseFloat(gapAmountInput.value) || 0;
        const szhAmount = parseFloat(szhAmountInput.value) || 0;
        const szhTerm = parseFloat(szhTermInput.value) || 0;
        const financialProductsAmount = parseFloat(financialProductsAmountInput.value) || 0;
        const initialPayment = parseFloat(initialPaymentInput.value) || 0;

        const szhTotalAmount = (szhAmount / 12) * szhTerm;

        let totalLoanAmount = carPrice + dealerEquipmentPrice;

        if (kaskoIncludeCheckbox.checked) {
            totalLoanAmount += kaskoAmount;
        }
        if (gapIncludeCheckbox.checked) {
            totalLoanAmount += gapAmount;
        }
        if (szhTermIncludeCheckbox.checked) {
            totalLoanAmount += szhTotalAmount;
        }
        if (financialProductsIncludeCheckbox.checked) {
            totalLoanAmount += financialProductsAmount;
        }

        totalLoanAmount -= initialPayment;

        // Обновление значений на правой панели
        carPriceDisplay.textContent = carPrice.toFixed(2);
        additionalEquipmentPriceDisplay.textContent = dealerEquipmentPrice.toFixed(2);
        kaskoDisplay.textContent = kaskoAmount.toFixed(2);
        gapDisplay.textContent = gapAmount.toFixed(2);
        szgDisplay.textContent = szhTotalAmount.toFixed(2);
        financialProductsDisplay.textContent = financialProductsAmount.toFixed(2);

        // Обновление отображения галочек
        smsNotificationDisplay.textContent = smsNotificationIncludeCheckbox.checked ? '✔️' : '';
        installmentCommissionDisplay.textContent = installmentCommissionIncludeCheckbox.checked ? '✔️' : '';

        totalLoanAmountDisplay.textContent = totalLoanAmount.toFixed(2);

        // Также обновим скрытые поля формы
        document.getElementById('total_loan_amount_input').value = totalLoanAmount.toFixed(2);
        document.getElementById('car_price_display_input').value = carPrice.toFixed(2);
        document.getElementById('additional_equipment_price_display_input').value = dealerEquipmentPrice.toFixed(2);
    }

    carPriceInput.addEventListener('input', calculateTotalLoanAmount);
    dealerEquipmentPriceInput.addEventListener('input', calculateTotalLoanAmount);
    kaskoAmountInput.addEventListener('input', calculateTotalLoanAmount);
    gapAmountInput.addEventListener('input', calculateTotalLoanAmount);
    szhAmountInput.addEventListener('input', calculateTotalLoanAmount);
    szhTermInput.addEventListener('input', calculateTotalLoanAmount);
    financialProductsAmountInput.addEventListener('input', calculateTotalLoanAmount);
    initialPaymentInput.addEventListener('input', calculateTotalLoanAmount);

    kaskoIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);
    gapIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);
    szhTermIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);
    financialProductsIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);
    smsNotificationIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);
    installmentCommissionIncludeCheckbox.addEventListener('change', calculateTotalLoanAmount);

    document.querySelector('form').addEventListener('submit', calculateTotalLoanAmount);

    calculateTotalLoanAmount();
});
