from django.test import TestCase
from django.contrib.auth.models import User
from apps.questionnaire.models import *


class UserTypeDocumentTest(TestCase):
    def setUp(self):
        self.document_type = UserDocumentType.objects.create(document_type="Passport")

    def test_document_type_creation(self):
        self.assertEqual(self.document_type.document_type, "Passport")


class UserUploadDocumentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.document_type = UserDocumentType.objects.create(document_type="Passport")
        self.document = UserDocument.objects.create(
            user=self.user,
            document_type=self.document_type,
            document_file="test_file.pdf"
        )

    def test_document_creation(self):
        self.assertEqual(self.document.user, self.user)
        self.assertEqual(self.document.document_type, self.document_type)
        self.assertEqual(self.document.document_file, "test_file.pdf")


class PhoneTypeTest(TestCase):
    def setUp(self):
        self.phone_type = PhoneType.objects.create(phone_type="Mobile")

    def test_phone_type_creation(self):
        self.assertEqual(self.phone_type.phone_type, "Mobile")


class PreDataClientTest(TestCase):
    def setUp(self):
        self.phone_type = PhoneType.objects.create(phone_type="Mobile")
        self.client = ClientPreData.objects.create(
            first_name_to_contact_pre_client="John Doe",
            type_pre_client="Физическое лицо",
            product_pre_client="Кредит",
            phone_number_pre_client="1234567890",
            type_phone_pre_client=self.phone_type
        )

    def test_client_creation(self):
        self.assertEqual(self.client.first_name_to_contact_pre_client, "John Doe")
        self.assertEqual(self.client.type_pre_client, "Физическое лицо")
        self.assertEqual(self.client.product_pre_client, "Кредит")
        self.assertEqual(self.client.phone_number_pre_client, "1234567890")
        self.assertEqual(self.client.type_phone_pre_client, self.phone_type)


class TypeDocumentTest(TestCase):
    def setUp(self):
        self.document_type = DocumentType.objects.create(document_type="Passport")

    def test_document_type_creation(self):
        self.assertEqual(self.document_type.document_type, "Passport")


class ClientUploadDocumentTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.document_type = DocumentType.objects.create(document_type="Passport")
        self.document = ClientDocument.objects.create(
            client=self.client,
            document_type=self.document_type,
            document_file="test_file.pdf"
        )

    def test_document_creation(self):
        self.assertEqual(self.document.client, self.client)
        self.assertEqual(self.document.document_type, self.document_type)
        self.assertEqual(self.document.document_file, "test_file.pdf")


class FinancingTermTest(TestCase):
    def setUp(self):
        self.term = FinancingTerm.objects.create(term="12 months")

    def test_financing_term_creation(self):
        self.assertEqual(self.term.term, "12 months")


class FinancingConditionsTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.term = FinancingTerm.objects.create(term="12 months")
        self.conditions = ClientFinancingCondition.objects.create(
            client=self.client,
            initial_payment="1000",
            financing_term=self.term,
            monthly_payment="100",
            deferred_payment=True
        )

    def test_financing_conditions_creation(self):
        self.assertEqual(self.conditions.client, self.client)
        self.assertEqual(self.conditions.initial_payment, "1000")
        self.assertEqual(self.conditions.financing_term, self.term)
        self.assertEqual(self.conditions.monthly_payment, "100")
        self.assertTrue(self.conditions.deferred_payment)


class CarMakeTest(TestCase):
    def setUp(self):
        self.car_make = CarBrand.objects.create(name="Toyota")

    def test_car_make_creation(self):
        self.assertEqual(self.car_make.name, "Toyota")


class CarConditionTest(TestCase):
    def setUp(self):
        self.condition = CarCondition.objects.create(condition="New")

    def test_car_condition_creation(self):
        self.assertEqual(self.condition.condition, "New")


class CarConfigurationTest(TestCase):
    def setUp(self):
        self.configuration = CarConfiguration.objects.create(configuration="Full")

    def test_car_configuration_creation(self):
        self.assertEqual(self.configuration.configuration, "Full")


class EngineTypeTest(TestCase):
    def setUp(self):
        self.engine_type = EngineType.objects.create(engine_type="V6")

    def test_engine_type_creation(self):
        self.assertEqual(self.engine_type.engine_type, "V6")


class EcoClassTest(TestCase):
    def setUp(self):
        self.eco_class = EcoClass.objects.create(name="Euro 6")

    def test_eco_class_creation(self):
        self.assertEqual(self.eco_class.name, "Euro 6")


class CarInfoTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.car_make = CarBrand.objects.create(name="Toyota")
        self.car_condition = CarCondition.objects.create(condition="New")
        self.engine_type = EngineType.objects.create(engine_type="V6")
        self.car_info = ClientCarInfo.objects.create(
            client=self.client,
            brand_car_info=self.car_make,
            condition_car_info=self.car_condition,
            engine_type_car_info=self.engine_type,
            model_car_info="Camry",
            year_car_info="2020",
            engine_volume_car_info=2.5,
            power_car_info="200",
            color_car_info="Black",
            mileage_car_info="0",
            vin_car_info="12345678901234567",
            car_price_car_info="30000",
            dealer_equipment_price_car_info="2000"
        )

    def test_car_info_creation(self):
        self.assertEqual(self.car_info.client, self.client)
        self.assertEqual(self.car_info.brand_car_info, self.car_make)
        self.assertEqual(self.car_info.condition_car_info, self.car_condition)
        self.assertEqual(self.car_info.engine_type_car_info, self.engine_type)
        self.assertEqual(self.car_info.model_car_info, "Camry")
        self.assertEqual(self.car_info.year_car_info, "2020")
        self.assertEqual(self.car_info.engine_volume_car_info, 2.5)
        self.assertEqual(self.car_info.power_car_info, "200")
        self.assertEqual(self.car_info.color_car_info, "Black")
        self.assertEqual(self.car_info.mileage_car_info, "0")
        self.assertEqual(self.car_info.vin_car_info, "12345678901234567")
        self.assertEqual(self.car_info.car_price_car_info, "30000")
        self.assertEqual(self.car_info.dealer_equipment_price_car_info, "2000")


class TypePtsTest(TestCase):
    def setUp(self):
        self.pts_type = TypePts.objects.create(pts_type="Original")

    def test_pts_type_creation(self):
        self.assertEqual(self.pts_type.pts_type, "Original")


class DocumentSaleAutoTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.pts_type = TypePts.objects.create(pts_type="Original")
        self.document = AutoSaleDocument.objects.create(
            client=self.client,
            pts_type_sale_auto=self.pts_type,
            pts_number_sale_auto="123456",
            pts_issue_sale_auto="2020-01-01",
            pts_issued_by_sale_auto="DMV",
            pts_name_sale_auto="Toyota Camry",
            dcp_number_sale_auto="654321",
            dcp_issue_date_sale_auto="2020-01-01"
        )

    def test_document_sale_auto_creation(self):
        self.assertEqual(self.document.client, self.client)
        self.assertEqual(self.document.pts_type_sale_auto, self.pts_type)
        self.assertEqual(self.document.pts_number_sale_auto, "123456")
        self.assertEqual(self.document.pts_issue_sale_auto, "2020-01-01")
        self.assertEqual(self.document.pts_issued_by_sale_auto, "DMV")
        self.assertEqual(self.document.pts_name_sale_auto, "Toyota Camry")
        self.assertEqual(self.document.dcp_number_sale_auto, "654321")
        self.assertEqual(self.document.dcp_issue_date_sale_auto, "2020-01-01")


class ExtraInsuranceTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.insurance = ClientExtraInsurance.objects.create(
            client=self.client,
            kasko_amount="1000",
            kasko_amount_include=True,
            gap_amount="500",
            gap_amount_include=True,
            szh_amount="200",
            szh_term="12 months",
            szh_term_include=True,
            financial_products_amount="300",
            financial_products_amount_include=True,
            installment_commission_include=True,
            sms_notification_include=True
        )

    def test_extra_insurance_creation(self):
        self.assertEqual(self.insurance.client, self.client)
        self.assertEqual(self.insurance.kasko_amount, "1000")
        self.assertTrue(self.insurance.kasko_amount_include)
        self.assertEqual(self.insurance.gap_amount, "500")
        self.assertTrue(self.insurance.gap_amount_include)
        self.assertEqual(self.insurance.szh_amount, "200")
        self.assertEqual(self.insurance.szh_term, "12 months")
        self.assertTrue(self.insurance.szh_term_include)
        self.assertEqual(self.insurance.financial_products_amount, "300")
        self.assertTrue(self.insurance.financial_products_amount_include)
        self.assertTrue(self.insurance.installment_commission_include)
        self.assertTrue(self.insurance.sms_notification_include)


class AllApplicationsTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.financing_conditions = ClientFinancingCondition.objects.create(client=self.client)
        self.car_info = ClientCarInfo.objects.create(client=self.client)
        self.documents = AutoSaleDocument.objects.create(client=self.client)
        self.extra_insurance = ClientExtraInsurance.objects.create(client=self.client)
        self.application = AllApplications.objects.create(
            client=self.client,
            financing_conditions=self.financing_conditions,
            car_info=self.car_info,
            documents=self.documents,
            extra_insurance=self.extra_insurance,
            status="Pending",
            type_all_app="Физическое лицо",
            financing="Кредит",
            manager="manager1",
            dealership_all_app="Dealership1",
            organization="Organization1"
        )

    def test_all_applications_creation(self):
        self.assertEqual(self.application.client, self.client)
        self.assertEqual(self.application.financing_conditions, self.financing_conditions)
        self.assertEqual(self.application.car_info, self.car_info)
        self.assertEqual(self.application.documents, self.documents)
        self.assertEqual(self.application.extra_insurance, self.extra_insurance)
        self.assertEqual(self.application.status, "Pending")
        self.assertEqual(self.application.type_all_app, "Физическое лицо")
        self.assertEqual(self.application.financing, "Кредит")
        self.assertEqual(self.application.manager, "manager1")
        self.assertEqual(self.application.dealership_all_app, "Dealership1")
        self.assertEqual(self.application.organization, "Organization1")


class DealershipTest(TestCase):
    def setUp(self):
        self.dealership = Dealership.objects.create(name="Dealership1", organisation_name="Organization1", is_active=True)

    def test_dealership_creation(self):
        self.assertEqual(self.dealership.name, "Dealership1")
        self.assertEqual(self.dealership.organisation_name, "Organization1")
        self.assertTrue(self.dealership.is_active)


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.dealership = Dealership.objects.create(name="Dealership1", organisation_name="Organization1", is_active=True)
        self.profile = UserProfile.objects.create(
            user=self.user,
            first_name_manager="John",
            last_name_manager="Doe",
            middle_name_manager="Smith",
            role_manager="Manager",
            date_of_birth_manager="1980-01-01",
            phone_number_manager="1234567890",
            status_manager=True,
            passport_series_manager="1234",
            passport_number_manager="567890",
            division_code_manager="123-456",
            issued_by_manager="Office",
            issue_date_manager="2000-01-01"
        )
        self.profile.dealership_manager.add(self.dealership)

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.first_name_manager, "John")
        self.assertEqual(self.profile.last_name_manager, "Doe")
        self.assertEqual(self.profile.middle_name_manager, "Smith")
        self.assertEqual(self.profile.role_manager, "Manager")
        self.assertEqual(self.profile.date_of_birth_manager, "1980-01-01")
        self.assertEqual(self.profile.phone_number_manager, "1234567890")
        self.assertTrue(self.profile.status_manager)
        self.assertEqual(self.profile.passport_series_manager, "1234")
        self.assertEqual(self.profile.passport_number_manager, "567890")
        self.assertEqual(self.profile.division_code_manager, "123-456")
        self.assertEqual(self.profile.issued_by_manager, "Office")
        self.assertEqual(self.profile.issue_date_manager, "2000-01-01")
        self.assertIn(self.dealership, self.profile.dealership_manager.all())


class OffersTest(TestCase):
    def setUp(self):
        self.offer = Offers.objects.create(
            title="Special Offer",
            name_bank="Bank1",
            term=12,
            stavka="10%",
            pay="1000"
        )

    def test_offer_creation(self):
        self.assertEqual(self.offer.title, "Special Offer")
        self.assertEqual(self.offer.name_bank, "Bank1")
        self.assertEqual(self.offer.term, 12)
        self.assertEqual(self.offer.stavka, "10%")
        self.assertEqual(self.offer.pay, "1000")


class OffersClientTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.offer_client = ClientOffer.objects.create(
            client=self.client,
            offer_id=1,
            title_offer="Special Offer",
            name_bank_offer="Bank1",
            term_offer=12,
            stavka_offer="10%",
            pay_offer="1000"
        )

    def test_offer_client_creation(self):
        self.assertEqual(self.offer_client.client, self.client)
        self.assertEqual(self.offer_client.offer_id, 1)
        self.assertEqual(self.offer_client.title_offer, "Special Offer")
        self.assertEqual(self.offer_client.name_bank_offer, "Bank1")
        self.assertEqual(self.offer_client.term_offer, 12)
        self.assertEqual(self.offer_client.stavka_offer, "10%")
        self.assertEqual(self.offer_client.pay_offer, "1000")


class SelectOffersClientTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.select_offer = SelectedClientOffer.objects.create(
            client=self.client,
            offer_id=1,
            total_loan_amount_select="10000",
            car_price_display_select="15000",
            initial_payment_select="5000",
            term_select="12",
            title_select="Special Offer",
            monthly_payment_select="1000",
            stavka_select="10%",
            name_bank_select="Bank1",
            status_select_offer="Pending"
        )

    def test_select_offer_creation(self):
        self.assertEqual(self.select_offer.client, self.client)
        self.assertEqual(self.select_offer.offer_id, 1)
        self.assertEqual(self.select_offer.total_loan_amount_select, "10000")
        self.assertEqual(self.select_offer.car_price_display_select, "15000")
        self.assertEqual(self.select_offer.initial_payment_select, "5000")
        self.assertEqual(self.select_offer.term_select, "12")
        self.assertEqual(self.select_offer.title_select, "Special Offer")
        self.assertEqual(self.select_offer.monthly_payment_select, "1000")
        self.assertEqual(self.select_offer.stavka_select, "10%")
        self.assertEqual(self.select_offer.name_bank_select, "Bank1")
        self.assertEqual(self.select_offer.status_select_offer, "Pending")


class HousingTypeTest(TestCase):
    def setUp(self):
        self.housing_type = HousingType.objects.create(type="Apartment")

    def test_housing_type_creation(self):
        self.assertEqual(self.housing_type.type, "Apartment")


class GenderTest(TestCase):
    def setUp(self):
        self.gender = Gender.objects.create(gender="Male")

    def test_gender_creation(self):
        self.assertEqual(self.gender.gender, "Male")


class SocialStatusTest(TestCase):
    def setUp(self):
        self.social_status = SocialStatus.objects.create(status="Employed")

    def test_social_status_creation(self):
        self.assertEqual(self.social_status.status, "Employed")


class ClientInfoPersonalTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.housing_type = HousingType.objects.create(type="Apartment")
        self.gender = Gender.objects.create(gender="Male")
        self.social_status = SocialStatus.objects.create(status="Employed")
        self.client_info = ClientPersonalInfo.objects.create(
            client=self.client,
            first_name_to_contact_client="John",
            first_name_client="John",
            last_name_client="Doe",
            middle_name_client="Smith",
            type_client="Физическое лицо",
            product_client="Кредит",
            birth_date_client="1980-01-01",
            registration_address_client="123 Main St",
            housing_type_client=self.housing_type,
            registration_date_client="2000-01-01",
            gender_choice_client=self.gender,
            social_status_client=self.social_status
        )

    def test_client_info_personal_creation(self):
        self.assertEqual(self.client_info.client, self.client)
        self.assertEqual(self.client_info.first_name_to_contact_client, "John")
        self.assertEqual(self.client_info.first_name_client, "John")
        self.assertEqual(self.client_info.last_name_client, "Doe")
        self.assertEqual(self.client_info.middle_name_client, "Smith")
        self.assertEqual(self.client_info.type_client, "Физическое лицо")
        self.assertEqual(self.client_info.product_client, "Кредит")
        self.assertEqual(self.client_info.birth_date_client, "1980-01-01")
        self.assertEqual(self.client_info.registration_address_client, "123 Main St")
        self.assertEqual(self.client_info.housing_type_client, self.housing_type)
        self.assertEqual(self.client_info.registration_date_client, "2000-01-01")
        self.assertEqual(self.client_info.gender_choice_client, self.gender)
        self.assertEqual(self.client_info.social_status_client, self.social_status)


class ContactClientTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.phone_type = PhoneType.objects.create(phone_type="Mobile")
        self.housing_type = HousingType.objects.create(type="Apartment")
        self.contact = ClientContact.objects.create(
            client=self.client,
            living_address_contact="123 Main St",
            housing_type_contact=self.housing_type,
            living_start_date_contact="2000-01-01",
            phone_number_contact="1234567890",
            phone_type_contact=self.phone_type,
            email_contact="john@example.com",
            notes_contact="Test notes"
        )

    def test_contact_client_creation(self):
        self.assertEqual(self.contact.client, self.client)
        self.assertEqual(self.contact.living_address_contact, "123 Main St")
        self.assertEqual(self.contact.housing_type_contact, self.housing_type)
        self.assertEqual(self.contact.living_start_date_contact, "2000-01-01")
        self.assertEqual(self.contact.phone_number_contact, "1234567890")
        self.assertEqual(self.contact.phone_type_contact, self.phone_type)
        self.assertEqual(self.contact.email_contact, "john@example.com")
        self.assertEqual(self.contact.notes_contact, "Test notes")


class PassportClientTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.passport = ClientPassport.objects.create(
            client=self.client,
            series_number_passport="1234 567890",
            issue_date_passport="2000-01-01",
            division_code_passport="123-456",
            issued_by_passport="Office"
        )

    def test_passport_client_creation(self):
        self.assertEqual(self.passport.client, self.client)
        self.assertEqual(self.passport.series_number_passport, "1234 567890")
        self.assertEqual(self.passport.issue_date_passport, "2000-01-01")
        self.assertEqual(self.passport.division_code_passport, "123-456")
        self.assertEqual(self.passport.issued_by_passport, "Office")


class DriverLicenseTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.driver_license = ClientDriverLicense.objects.create(
            client=self.client,
            series_number_driver_license="1234 567890",
            issue_date_driver_license="2000-01-01",
            issued_by_driver_license="Office",
            experience_start_date_driver_license="2000-01-01"
        )

    def test_driver_license_creation(self):
        self.assertEqual(self.driver_license.client, self.client)
        self.assertEqual(self.driver_license.series_number_driver_license, "1234 567890")
        self.assertEqual(self.driver_license.issue_date_driver_license, "2000-01-01")
        self.assertEqual(self.driver_license.issued_by_driver_license, "Office")
        self.assertEqual(self.driver_license.experience_start_date_driver_license, "2000-01-01")


class TaxDocumentTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.tax_document = ClientTaxDocument.objects.create(
            client=self.client,
            series_number_tax_document="1234",
            number_tax_document="567890"
        )

    def test_tax_document_creation(self):
        self.assertEqual(self.tax_document.client, self.client)
        self.assertEqual(self.tax_document.series_number_tax_document, "1234")
        self.assertEqual(self.tax_document.number_tax_document, "567890")


class PensionCertificateTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.pension_certificate = ClientPensionCertificate.objects.create(
            client=self.client,
            number_pension_sert="123-456-789 01"
        )

    def test_pension_certificate_creation(self):
        self.assertEqual(self.pension_certificate.client, self.client)
        self.assertEqual(self.pension_certificate.number_pension_sert, "123-456-789 01")


class InternationalPassportTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.international_passport = ClientInternationalPassport.objects.create(
            client=self.client,
            series_number_international_passport="12 345678",
            issue_date_international_passport="2000-01-01",
            issued_by_international_passport="Office"
        )

    def test_international_passport_creation(self):
        self.assertEqual(self.international_passport.client, self.client)
        self.assertEqual(self.international_passport.series_number_international_passport, "12 345678")
        self.assertEqual(self.international_passport.issue_date_international_passport, "2000-01-01")
        self.assertEqual(self.international_passport.issued_by_international_passport, "Office")


class EducationTest(TestCase):
    def setUp(self):
        self.education_level = EducationLevel.objects.create(level="Higher")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.education = ClientEducation.objects.create(
            client=self.client,
            education_level_client=self.education_level
        )

    def test_education_creation(self):
        self.assertEqual(self.education.client, self.client)
        self.assertEqual(self.education.education_level_client, self.education_level)


class EmploymentTest(TestCase):
    def setUp(self):
        self.organization_type = OrganizationType.objects.create(type="LLC")
        self.activity_code = ActivityCode.objects.create(code="A01")
        self.position_type = PositionType.objects.create(type="Manager")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.employment = ClientEmployment.objects.create(
            client=self.client,
            organization_inn="1234567890",
            organization_form="LLC",
            organization_name="Company",
            organization_type=self.organization_type,
            activity_code=self.activity_code,
            position="Manager",
            position_type=self.position_type,
            registration_address_employment="123 Main St",
            phone_number_organization="1234567890",
            current_experience="5 years",
            total_experience="10 years",
            shift_method=True,
            official_position=True
        )

    def test_employment_creation(self):
        self.assertEqual(self.employment.client, self.client)
        self.assertEqual(self.employment.organization_inn, "1234567890")
        self.assertEqual(self.employment.organization_form, "LLC")
        self.assertEqual(self.employment.organization_name, "Company")
        self.assertEqual(self.employment.organization_type, self.organization_type)
        self.assertEqual(self.employment.activity_code, self.activity_code)
        self.assertEqual(self.employment.position, "Manager")
        self.assertEqual(self.employment.position_type, self.position_type)
        self.assertEqual(self.employment.registration_address_employment, "123 Main St")
        self.assertEqual(self.employment.phone_number_organization, "1234567890")
        self.assertEqual(self.employment.current_experience, "5 years")
        self.assertEqual(self.employment.total_experience, "10 years")
        self.assertTrue(self.employment.shift_method)
        self.assertTrue(self.employment.official_position)


class CitizenshipTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(name="Russia")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.citizenship = ClientCitizenship.objects.create(
            client=self.client,
            birth_country_client=self.country,
            russian_citizenship=True,
            residence_permit=True,
            us_citizenship=False,
            birth_place_citizenship="Moscow",
            tax_resident_foreign=False,
            tax_residence_countries="None",
            foreign_inn="None"
        )

    def test_citizenship_creation(self):
        self.assertEqual(self.citizenship.client, self.client)
        self.assertEqual(self.citizenship.birth_country_client, self.country)
        self.assertTrue(self.citizenship.russian_citizenship)
        self.assertTrue(self.citizenship.residence_permit)
        self.assertFalse(self.citizenship.us_citizenship)
        self.assertEqual(self.citizenship.birth_place_citizenship, "Moscow")
        self.assertFalse(self.citizenship.tax_resident_foreign)
        self.assertEqual(self.citizenship.tax_residence_countries, "None")
        self.assertEqual(self.citizenship.foreign_inn, "None")


class FamilyInfoTest(TestCase):
    def setUp(self):
        self.marital_status = MaritalStatus.objects.create(status="Married")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.family_info = ClientFamilyInfo.objects.create(
            client=self.client,
            marital_status=self.marital_status,
            children_under_18=2,
            dependents=3,
            years_married=10,
            official_position_relative=True,
            degree_of_kinship="Brother",
            relative_position="Manager"
        )

    def test_family_info_creation(self):
        self.assertEqual(self.family_info.client, self.client)
        self.assertEqual(self.family_info.marital_status, self.marital_status)
        self.assertEqual(self.family_info.children_under_18, 2)
        self.assertEqual(self.family_info.dependents, 3)
        self.assertEqual(self.family_info.years_married, 10)
        self.assertTrue(self.family_info.official_position_relative)
        self.assertEqual(self.family_info.degree_of_kinship, "Brother")
        self.assertEqual(self.family_info.relative_position, "Manager")


class FinancialInfoTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.financial_info = ClientFinancialInfo.objects.create(
            client=self.client,
            income_amount="1000",
            confirmed_income_amount="800",
            income_proof_document="Payslip",
            income_source="Salary",
            disposable_income="200",
            spouse_income="500"
        )

    def test_financial_info_creation(self):
        self.assertEqual(self.financial_info.client, self.client)
        self.assertEqual(self.financial_info.income_amount, "1000")
        self.assertEqual(self.financial_info.confirmed_income_amount, "800")
        self.assertEqual(self.financial_info.income_proof_document, "Payslip")
        self.assertEqual(self.financial_info.income_source, "Salary")
        self.assertEqual(self.financial_info.disposable_income, "200")
        self.assertEqual(self.financial_info.spouse_income, "500")


class ExpensesTest(TestCase):
    def setUp(self):
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.expenses = ClientExpenses.objects.create(
            client=self.client,
            mandatory_payments="100",
            loan_payments="200",
            mortgage_payments="300"
        )

    def test_expenses_creation(self):
        self.assertEqual(self.expenses.client, self.client)
        self.assertEqual(self.expenses.mandatory_payments, "100")
        self.assertEqual(self.expenses.loan_payments, "200")
        self.assertEqual(self.expenses.mortgage_payments, "300")


class VehicleTest(TestCase):
    def setUp(self):
        self.purchase_method = PurchaseMethod.objects.create(method="Cash")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.vehicle = ClientVehicle.objects.create(
            client=self.client,
            brand_vehicle="Toyota",
            year_vehicle="2020",
            model_vehicle="Camry",
            purchase_year="2020",
            purchase_method_vehicle=self.purchase_method
        )

    def test_vehicle_creation(self):
        self.assertEqual(self.vehicle.client, self.client)
        self.assertEqual(self.vehicle.brand_vehicle, "Toyota")
        self.assertEqual(self.vehicle.year_vehicle, "2020")
        self.assertEqual(self.vehicle.model_vehicle, "Camry")
        self.assertEqual(self.vehicle.purchase_year, "2020")
        self.assertEqual(self.vehicle.purchase_method_vehicle, self.purchase_method)


class RealEstateTest(TestCase):
    def setUp(self):
        self.real_estate_type = RealEstateType.objects.create(type="Apartment")
        self.purchase_method = PurchaseMethod.objects.create(method="Mortgage")
        self.client = ClientPreData.objects.create(first_name_to_contact_pre_client="John Doe")
        self.real_estate = ClientRealEstate.objects.create(
            client=self.client,
            real_estate_type=self.real_estate_type,
            purchase_method_real_estate=self.purchase_method,
            address_real_estate="123 Main St",
            matches_registration_address_real_estate=True
        )

    def test_real_estate_creation(self):
        self.assertEqual(self.real_estate.client, self.client)
        self.assertEqual(self.real_estate.real_estate_type, self.real_estate_type)
        self.assertEqual(self.real_estate.purchase_method_real_estate, self.purchase_method)
        self.assertEqual(self.real_estate.address_real_estate, "123 Main St")
        self.assertTrue(self.real_estate.matches_registration_address_real_estate)
