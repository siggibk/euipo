from models.db import Db

class Trademark:
    def __init__(
        self,
        application_number,
        trademark_name,
        trademark_type,
        application_language,
        second_language,
        nature,
        status,
        status_date,
        status_milestone,
        expiry_date,
        application_date,
        registration_date = None,
        applicant_identifier = None,
        representative_identifier = None
    ):
        self.application_number = application_number
        self.applicant_identifier = applicant_identifier
        self.representative_identifier = representative_identifier
        self.trademark_name = trademark_name
        self.trademark_type = trademark_type
        self.application_language = application_language
        self.second_language = second_language
        # Word, 2d, fig
        self.nature = nature
        self.status = status
        # Date of status update
        self.status_date = status_date
        self.status_milestone = status_milestone
        self.expiry_date = expiry_date
        self.application_date = application_date
        self.registration_date = registration_date
        
        self.descriptions = []

    def add_description(self, description):
        self.descriptions.append(description)

    def commit(self):
        db = Db()
        with db.conn:
            with db.conn.cursor() as cur:
                cur.execute(self.insert_query, self.values)
        
        db.commit()
        db.close()

    def commit_classes(self):
        db = Db()
        with db.conn:
            with db.conn.cursor() as cur:
                for desc in self.descriptions:
                    cur.execute(desc.insert_query, desc.values(self.application_number))
                    id = cur.fetchone()[0]
                    for language_description in desc.descriptions:
                        cur.execute(language_description.insert_query, language_description.values(id))
                #execute_values(cur, )

    @property
    def insert_query(self):
        return """
            INSERT INTO trademark (
                application_number,
                name,
                type,
                application_language,
                second_language,
                nature,
                status,
                status_date,
                status_milestone,
                expiry_date,
                application_date,
                registration_date,
                applicant_identifier,
                representative_identifier
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    @property
    def values(self):
        return (
            self.application_number,
            self.trademark_name,
            self.trademark_type,
            self.application_language,
            self.second_language,
            self.nature,
            self.status,
            self.status_date,
            self.status_milestone,
            self.expiry_date,
            self.application_date,
            self.registration_date,
            self.applicant_identifier,
            self.representative_identifier
        )
