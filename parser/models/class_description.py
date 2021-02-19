class ClassDescription:
    def __init__(self, lang, description):
        self.lang = lang
        self.description = description

    @property
    def insert_query(self):
        return """
            INSERT INTO trademarkclass_description (language, description, trademark_class_id)
            VALUES (%s, %s, %s)
        """

    def values(self, trademark_class_id):
        return (self.lang, self.description, trademark_class_id)