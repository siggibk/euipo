import psycopg2

class Db:
    def __init__(self):
        # TODO set parameters in env
        self.conn = psycopg2.connect(
            host="localhost",
            database="ip_db",
            user="postgres",
            password="postgres"
        )
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()