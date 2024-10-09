required_fields = [
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
    "person.registrationAddress.countryName"
]
field_types = {
    "person.firstName": str,
    "person.dob": str,
    "creditInfo.limit": float,
    "person.factAddressSameAsRegistration": bool
}
field_ranges = {
    "creditInfo.limit": (1, float('inf'))
}
field_enums = {
    "person.sex": ["m", "f"]
}
