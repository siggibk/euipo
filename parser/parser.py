import xml.etree.ElementTree as ET
from datetime import datetime
from models.trademark import Trademark
from models.design import Design
from models.class_description import ClassDescription
from models.language_description import LanguageDescription

def format_date(date_string):
    if date_string:
        return datetime.strptime(date_string, '%Y-%m-%d')
    return None

class Parser:
    def __init__(self, file_path):
        tree = ET.parse(file_path)
        self.root = tree.getroot()

class TrademarkParser(Parser):
    namespaces = {'tm': 'http://euipo.europa.eu/trademark/data'}

    def parse(self):
        """Return a TradeMark object"""
        transaction_details = self.root.find('./tm:TradeMarkTransactionBody/tm:TransactionContentDetails', self.namespaces)

        transaction_identifier = transaction_details.find('tm:TransactionIdentifier', self.namespaces).text
        transaction_code = transaction_details.find('tm:TransactionCode', self.namespaces).text
        trademark_el = transaction_details.find('./tm:TransactionData/tm:TradeMarkDetails/tm:TradeMark', self.namespaces)

        operation_code = trademark_el.get('operationCode')
        application_number = trademark_el.find('tm:ApplicationNumber', self.namespaces).text

        application_date = trademark_el.find('tm:ApplicationDate', self.namespaces)
        application_date = application_date.text if application_date is not None else None

        registration_date = trademark_el.find('tm:RegistrationDate', self.namespaces)
        registration_date = registration_date.text if registration_date is not None else None

        registration_office_code = trademark_el.find('tm:RegistrationOfficeCode', self.namespaces).text

        application_language = trademark_el.find('tm:ApplicationLanguageCode', self.namespaces)
        application_language = application_language.text if application_language is not None else None

        second_language = trademark_el.find('tm:SecondLanguageCode', self.namespaces)
        second_language = second_language.text if second_language is not None else None

        expiry_date = trademark_el.find('tm:ExpiryDate', self.namespaces)
        expiry_date = expiry_date.text if expiry_date is not None else None

        status_el = trademark_el.find('tm:MarkCurrentStatusCode', self.namespaces)
        status_txt = status_el.text
        status_milestone = status_el.get('milestone')
        status_id = status_el.get('status')
        status_date = trademark_el.find('tm:MarkCurrentStatusDate', self.namespaces).text

        # individual/collective
        nature = trademark_el.find('tm:KindMark', self.namespaces).text

        # Word, 2d, fig
        trademark_type = trademark_el.find('tm:MarkFeature', self.namespaces).text

        distinctiveness_indicator = trademark_el.find('tm:TradeDistinctivenessIndicator', self.namespaces).text

        trademark_name = trademark_el.find('./tm:WordMarkSpecification/tm:MarkVerbalElementText', self.namespaces)
        trademark_name = trademark_name.text if trademark_name is not None else None

        # Applicant and Representative details
        applicant_details = trademark_el.find('tm:ApplicantDetails', self.namespaces)
        applicant_identifier = applicant_details.find('./tm:ApplicantKey/tm:Identifier', self.namespaces).text if applicant_details else None

        representative_details = trademark_el.find('./tm:RepresentativeDetails', self.namespaces)
        representative_identifier = representative_details.find('tm:RepresentativeKey/tm:Identifier', self.namespaces).text if representative_details else None

        trademark = Trademark(
            application_number=application_number,
            trademark_name=trademark_name,
            trademark_type=trademark_type,
            application_language=application_language,
            second_language=second_language,
            nature=nature,
            status=status_txt,
            status_date=format_date(status_date),
            status_milestone=status_milestone,
            expiry_date=format_date(expiry_date),
            application_date=format_date(application_date),
            registration_date=format_date(registration_date),
            applicant_identifier=applicant_identifier,
            representative_identifier=representative_identifier
        )

        """
        Parse trademark classes and descriptions in all languages
        and add them to the trademark
        """
        goods_services_details = trademark_el.find('tm:GoodsServicesDetails', self.namespaces)
        goods_services = goods_services_details.find('tm:GoodsServices', self.namespaces)

        description_details = goods_services.find('tm:ClassDescriptionDetails', self.namespaces)

        class_descriptions = description_details.findall('tm:ClassDescription', self.namespaces)

        for class_description in class_descriptions:
            class_number = class_description.find('tm:ClassNumber', self.namespaces).text
            language_description_c = LanguageDescription(number=class_number)

            language_descriptions = class_description.findall('tm:GoodsServicesDescription', self.namespaces)
            for language_description in language_descriptions:
                language = language_description.get('languageCode')
                description = language_description.text
                class_description = ClassDescription(lang=language, description=description)
                language_description_c.add_description(description=class_description)
            
            trademark.add_description(language_description_c)
        return trademark


class DesignParser(Parser):
    namespaces = {'ds': 'http://euipo.europa.eu/design/data'}

    def parse(self):
        """Return a Design object"""
        design_el = self.root.find('ds:DesignTransactionBody/ds:TransactionContentDetails/ds:TransactionData/ds:DesignDetails/ds:Design', self.namespaces)

        application_date = design_el.find('ds:ApplicationDate', self.namespaces)
        application_date = application_date.text if application_date is not None else None

        registration_date = design_el.find('ds:RegistrationDate', self.namespaces)
        registration_date = registration_date.text if registration_date is not None else None

        publication_date = design_el.find('ds:PublicationDate', self.namespaces)
        publication_date = publication_date.text if publication_date is not None else None

        status = design_el.find('ds:DesignCurrentStatusCode', self.namespaces)
        status = status.text if status is not None else None

        status_date = design_el.find('ds:DesignCurrentStatusDate', self.namespaces)
        status_date = status_date.text if status_date is not None else None

        renewal_status = design_el.find('ds:RenewalCurrentStatusCode', self.namespaces)
        renewal_status = renewal_status.text if renewal_status is not None else None

        application_language = design_el.find('ds:ApplicationLanguageCode', self.namespaces)
        application_language = application_language.text if application_language is not None else None

        second_language = design_el.find('ds:SecondLanguageCode', self.namespaces)
        second_language = second_language.text if second_language is not None else None

        expiry_date = design_el.find('ds:ExpiryDate', self.namespaces)
        expiry_date = expiry_date.text if expiry_date is not None else None

        effective_date = design_el.find('ds:EffectiveDate', self.namespaces)
        effective_date = effective_date.text if effective_date is not None else None

        application_number = design_el.find('ds:ApplicationNumber', self.namespaces)
        application_number = application_number.text if application_number is not None else None

        design_identifier = design_el.find('ds:DesignIdentifier', self.namespaces).text

        # Applicant and Representative details
        applicant_details = design_el.find('ds:ApplicantDetails', self.namespaces)
        applicant_identifier = applicant_details.find('./ds:Applicant/ds:ApplicantIdentifier', self.namespaces).text if applicant_details else None

        representative_details = design_el.find('./ds:RepresentativeDetails', self.namespaces)
        representative_identifier = representative_details.find('ds:Representative/ds:RepresentativeIdentifier', self.namespaces).text if representative_details else None

        indication_product = design_el.findall('./ds:IndicationProductDetails/ds:IndicationProduct', self.namespaces)
        design_indication = None
        original_indication = None

        for i in indication_product:
            language_code = i.get('languageCode')
            if language_code == 'en':
                design_indication = i.text
            elif language_code == application_language:
                original_indication = i.text

        design = Design(
            indication = design_indication,
            original_indication = original_indication,
            application_number = application_number,
            design_identifier=design_identifier,
            application_language = application_language,
            second_language = second_language,
            status = status,
            renewal_status = renewal_status,
            effective_date = effective_date,
            status_date = status_date,
            expiry_date = expiry_date,
            application_date = application_date,
            registration_date = registration_date,
            applicant_identifier = applicant_identifier,
            representative_identifier = representative_identifier
        )

        return design