REQUIRED_FIELDS = [
    "applicationInfo.partnerId",
    "sourceSystemInfo.idSystem",
    "creditInfo.product",
    "creditInfo.period",
    "creditInfo.limit",
    "person.firstName",
    "person.lastName",
    "person.sex",
    "person.birthplace",
    "person.dob",
    "person.factAddressSameAsRegistration",
    "person.primaryDocument.docType",
    "person.primaryDocument.docNumber",
    "person.primaryDocument.docSeries",
    "person.primaryDocument.issueOrg",
    "person.primaryDocument.issueDate",
    "person.primaryDocument.issueCode",
    "person.registrationAddress.countryName",
    "person.registrationAddress.region",
    "person.registrationAddress.postCode",
    # "goods[].goodCost",
    # "person.incomes[].incomeType",
    # "person.incomes[].incomeAmount"
]

FIELD_TYPES = {
    "applicationInfo.partnerId": str,
    "sourceSystemInfo.idSystem": str,
    "creditInfo.product": str,
    "creditInfo.period": str,
    "creditInfo.limit": float,
    "person.firstName": str,
    "person.lastName": str,
    "person.sex": str,
    "person.birthplace": str,
    "person.dob": str,
    "person.factAddressSameAsRegistration": bool,
    "person.primaryDocument.docType": str,
    "person.primaryDocument.docNumber": str,
    "person.primaryDocument.docSeries": str,
    "person.primaryDocument.issueOrg": str,
    "person.primaryDocument.issueDate": str,
    "person.primaryDocument.issueCode": str,
    "person.registrationAddress.countryName": str,
    "person.registrationAddress.region": str,
    "person.registrationAddress.postCode": str,
    # "goods[].goodCost": float,
    # "person.incomes[].incomeType": str,
    # "person.incomes[].incomeAmount": float
}

# Диапазоны значений для полей
FIELD_RANGES = {
    "creditInfo.limit": (10, float('inf')),
    # "person.incomes[].incomeAmount": (0, float('inf'))
}

# Допустимые значения (enumerations)
FIELD_ENUMS = {
    "person.sex": ["m", "f"],
    "person.primaryDocument.docType": [
        "Паспорт", "Старый паспорт", "Водительское удостоверение", "Военный билет",
        "Свидетельство ИНН", "Загранпаспорт", "Новое Водительское удостоверение",
        "Пенсионное страховое свидетельство", "Полис ОМС единого образца",
        "Удостоверение личности офицера"
    ],
    # "goods[].goodType": ["Новый", "Подержанный"]
}
