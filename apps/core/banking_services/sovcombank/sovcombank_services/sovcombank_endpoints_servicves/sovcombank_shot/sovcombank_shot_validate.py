REQUIRED_FIELDS_SHOT = [
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

FIELD_TYPES_SHOT = {
    "applicationInfo.partnerId": str,
    "applicationInfo.type": str,
    "applicationInfo.entryDateTime": str,  # YYYY-MM-DD
    "applicationInfo.dateSendWeb": str,  # yyyy-MM-dd HH:mm:ss
    "applicationInfo.dateReceiveWeb": str,  # yyyy-MM-dd HH:mm:ss
    "applicationInfo.secretWord": str,
    "applicationInfo.visualRating": str,
    "applicationInfo.gos": bool,
    "applicationInfo.fz": bool,

    "partnerInfo.merchantID": str,
    "partnerInfo.terminalID": str,
    "partnerInfo.officeName": str,
    "partnerInfo.entryCity": str,
    "partnerInfo.entryRegion": str,

    "sourceSystemInfo.idSystem": str,
    "sourceSystemInfo.operator.name": str,
    "sourceSystemInfo.operator.login": str,

    "creditInfo.product": str,
    "creditInfo.target": str,
    "creditInfo.period": str,
    "creditInfo.limit": float,
    "creditInfo.yearPercent": str,
    "creditInfo.shopInfo": str,
    "creditInfo.tradeInPayment": float,
    "creditInfo.creditPayment": float,
    "creditInfo.downPayment": float,

    # "goods[].goodCost": float,
    # "goods[].goodModel": str,
    # "goods[].goodsDescription": str,
    # "goods[].goodType": str,

    "person.firstName": str,
    "person.lastName": str,
    "person.middleName": str,
    "person.sex": str,  # Enum (m, f)
    "person.citezenship": str,
    "person.birthplace": str,
    "person.dob": str,  # YYYY-MM-DD
    "person.factAddressSameAsRegistration": bool,
    "person.socialStatus": str,
    "person.maritalStatus": str,
    "person.lastNameChangeDeny": str,
    "person.previousLastName": str,
    "person.lastNameChangeReason": str,
    "person.lastNameChangeYear": str,
    "person.education": str,
    "person.institution": str,
    "person.disability": str,
    "person.livingType": str,
    "person.dependentCount": int,
    "person.dependentCountChild": int,
    "person.dependentChildOldYears": str,

    "person.spouse.firstName": str,
    "person.spouse.lastName": str,
    "person.spouse.middleName": str,
    "person.spouse.sex": str,  # Enum (m, f)
    "person.spouse.citezenship": str,
    "person.spouse.birthplace": str,
    "person.spouse.dob": str,  # YYYY-MM-DD
    "person.spouse.factAddressSameAsRegistration": bool,
    "person.spouse.socialStatus": str,
    "person.spouse.maritalStatus": str,
    "person.spouse.lastNameChangeDeny": str,
    "person.spouse.previousLastName": str,
    "person.spouse.lastNameChangeReason": str,
    "person.spouse.lastNameChangeYear": str,
    "person.spouse.education": str,
    "person.spouse.institution": str,
    "person.spouse.disability": str,
    "person.spouse.livingType": str,
    "person.spouse.dependentCount": int,
    "person.spouse.dependentCountChild": int,
    "person.spouse.dependentChildOldYears": str,

    "person.primaryDocument.docType": str,
    "person.primaryDocument.docNumber": str,
    "person.primaryDocument.docSeries": str,
    "person.primaryDocument.issueOrg": str,
    "person.primaryDocument.issueDate": str,  # YYYY-MM-DD
    "person.primaryDocument.issueCode": str,

    "person.registrationAddress.countryName": str,
    "person.registrationAddress.region": str,
    "person.registrationAddress.postCode": str,

    # "person.incomes[].incomeType": str,
    # "person.incomes[].incomeAmount": float,

    "job.employerName": str,
    "job.employerAge": int,
    "job.countEmployee": str,
    "job.workPeriod.year": int,
    "job.workPeriod.month": int,
    "job.employerType": str,
    "job.employerOwnership": str,
    "job.workSector": str,
    "job.workPosition": str,
    "job.workOccupation": str,
    "job.workManagerName": str,
    "job.workAddress.countryName": str,
    "job.workAddress.region": str,
    "job.workAddress.city": str,
    "job.workAddress.street": str,
    "job.workAddress.house": str,
    "job.workAddress.flat": str,
    "job.workAddress.postCode": str,
}

# Диапазоны значений для полей
FIELD_RANGES_SHOT = {
    "creditInfo.limit": (10, float('inf')),
    # "person.incomes[].incomeAmount": (0, float('inf'))
}

# Допустимые значения (enumerations)
FIELD_ENUMS_SHOT = {
    "person.sex": ["m", "f"],
    "person.primaryDocument.docType": [
        "Паспорт", "Старый паспорт", "Водительское удостоверение", "Военный билет",
        "Свидетельство ИНН", "Загранпаспорт", "Новое Водительское удостоверение",
        "Пенсионное страховое свидетельство", "Полис ОМС единого образца",
        "Удостоверение личности офицера"
    ],
    # "goods[].goodType": ["Новый", "Подержанный"]
}
