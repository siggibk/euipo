class LanguageDescription:
    def __init__(self, number):
        self.number = number
        self.descriptions = []
    
    def add_description(self, description):
        self.descriptions.append(description)

    @property
    def insert_query(self):
        return """
            INSERT INTO trademark_class (number, application_number)
            VALUES (%s, %s)
            RETURNING id
        """

    def values(self, application_number):
        return (self.number, application_number)