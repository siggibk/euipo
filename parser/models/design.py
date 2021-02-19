from models.db import Db

class Design:
    def __init__(
        self,
        indication,
        original_indication,
        application_number,
        design_identifier,
        application_language,
        second_language,
        status,
        renewal_status = None,
        effective_date = None,
        status_date = None,
        expiry_date = None,
        application_date = None,
        registration_date = None,
        applicant_identifier = None,
        representative_identifier = None
    ):
        self.indication = indication
        self.original_indication = original_indication
        self.application_number = application_number
        self.design_identifier = design_identifier
        self.application_language = application_language
        self.second_language = second_language
        self.status = status
        self.renewal_status = renewal_status
        self.effective_date = effective_date
        # Date of status update
        self.status_date = status_date
        self.expiry_date = expiry_date
        self.application_date = application_date
        self.registration_date = registration_date
        self.applicant_identifier = applicant_identifier
        self.representative_identifier = representative_identifier
        
    def commit(self):
        print(self.values)
        db = Db()
        with db.conn:
            with db.conn.cursor() as cur:
                cur.execute(self.insert_query, self.values)
        
        db.commit()
        db.close()

    @property
    def insert_query(self):
        return """
            INSERT INTO design (
                indication,
                original_indication,
                application_number,
                design_identifier,
                application_language,
                second_language,
                status,
                renewal_status,
                effective_date,
                status_date,
                expiry_date,
                application_date,
                registration_date,
                applicant_identifier,
                representative_identifier
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    @property
    def values(self):
        return (
            self.indication,
            self.original_indication,
            self.application_number,
            self.design_identifier,
            self.application_language,
            self.second_language,
            self.status,
            self.renewal_status,
            self.effective_date,
            # Date of status update
            self.status_date,
            self.expiry_date,
            self.application_date,
            self.registration_date,
            self.applicant_identifier,
            self.representative_identifier
        )
