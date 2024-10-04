$(document).ready(function () {
    // console.log("jQuery и Inputmask загружены и готовы к использованию");

    // Функция для инициализации маски
    function applyMask(selectors, maskOptions) {
        if (typeof selectors === 'string') {
            selectors = [selectors]; // Преобразуем строку в массив
        }

        selectors.forEach(function (selector) {
            function applyMaskToElement() {
                if ($(selector).length) {
                    $(selector).inputmask(maskOptions);
                    // console.log(`Маска для ${selector} применена`);
                } else {
                    // console.log(`Элемент ${selector} не найден, продолжаю ожидать...`);
                    const observer = new MutationObserver((mutationsList, observer) => {
                        if (document.querySelector(selector)) {
                            $(selector).inputmask(maskOptions);
                            // console.log(`Маска для ${selector} применена после появления элемента`);
                            observer.disconnect();
                        }
                    });
                    observer.observe(document.body, {childList: true, subtree: true});
                }
            }

            applyMaskToElement();
        });
    }

    applyMask(["#id_passport_number_manager"], {
        mask: "999999",
        placeholder: "______",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
    applyMask(["#id_passport_series_manager"], {
        mask: "9999",
        placeholder: "____",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
    applyMask(["#id_organization_inn"], {
        mask: "9999999999",
        placeholder: "__________",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
    applyMask(["#id_series_number_international_passport"], {
        mask: "99 9999999",
        placeholder: "__ _______",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });

    applyMask(["#id_number_pension_sert"], {
        mask: "999-999-999 99",
        placeholder: "___-___-___ __",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
    applyMask(["#id_series_number_tax_document"], {
        mask: "9999 999999",
        placeholder: "____ ______",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });

    applyMask(["#id_number_tax_document"], {
        mask: "999999999999",
        placeholder: "____________",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });
    applyMask(["#id_series_number_driver_license"], {
        mask: "99 99 999999",
        placeholder: "__ __ ______",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });

    applyMask(['#id_division_code_passport', '#id_division_code_manager'], '999-999')
    applyMask("#id_series_number_passport", {
        mask: "9999 999999",
        placeholder: "____ ______",
        clearMaskOnLostFocus: true,
        showMaskOnHover: false,
        showMaskOnFocus: true
    });

    applyMask("#id_vin_car_info", "99999999999999999")
    applyMask(["#id_engine_volume_car_info", "#id_power_car_info"], {
        alias: 'decimal',
        radixPoint: ".",
        rightAlign: false,
        groupSeparator: "",
        autoGroup: false,
        digits: 2,
        digitsOptional: true,
        allowMinus: false,
        placeholder: "",
    });

    applyMask(["#id_phone_number_pre_client", "#id_phone_number_contact", "#id_phone_number_organization", "#id_phone_number_manager"], "+7 (999) 999-99-99");


    var currentYear = new Date().getFullYear();

    function checkYearInput(selectors) {
        if (typeof selectors === 'string') {
            selectors = [selectors];
        }
        selectors.forEach(function (selector) {
            // Ограничиваем ввод года
            $(selector).attr('min', 1900);
            $(selector).attr('max', currentYear);

            // Добавляем обработчик события для дополнительной проверки
            $(selector).on('input', function () {
                var value = $(this).val();
                if (value < 1900 || value > currentYear) {
                    alert("Пожалуйста, введите год в диапазоне от 1900 до " + currentYear);
                    $(this).val('');
                }
            });
        });
    }

    var yearSelectors = ["#id_year_car_info", "#id_year_vehicle", "#id_purchase_year"];

    applyMask(yearSelectors, {mask: "9999", placeholder: "____"});
    checkYearInput(yearSelectors);
    //
    //
    // // Применяем маски к полям примеры
    // applyMask("#phone_number", "+7 (999) 999-99-99");
    // applyMask("#division_code", "999-999");
    // applyMask("#amount", {
    //     alias: 'decimal',
    //     radixPoint: ",",
    //     rightAlign: false,
    //     groupSeparator: "",
    //     autoGroup: false,
    //     digits: 2,
    //     digitsOptional: true,
    //     allowMinus: false,
    //     placeholder: "",
    //     definitions: {
    //         ',': {
    //             validator: "[,\\.]",
    //             cardinality: 1,
    //             prevalidator: null,
    //             definitionSymbol: "."
    //         }
    //     }
    // });
    // applyMask("#income", {
    //     alias: "decimal",
    //     rightAlign: false,
    //     radixPoint: ".",
    //     groupSeparator: "",
    //     autoGroup: false,
    //     digits: 2,
    //     digitsOptional: false,
    //     placeholder: ""  // Устанавливаем пустую строку для плейсхолдера
    // });
    // applyMask("#letters", {
    //     mask: "AAA-999",
    //     placeholder: "___-___",  // Устанавливаем плейсхолдер
    //     definitions: {
    //         'A': {
    //             validator: "[А-Яа-я]",
    //             casing: "upper"  // Преобразование в верхний регистр
    //         },
    //         '9': {
    //             validator: "[0-9]",
    //             casing: "upper"
    //         }
    //     }
    // });
});
