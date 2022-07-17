import self as self
from pymongo import MongoClient


class DataBase():
    #    def build(self):
    #        return Builder.load_file('login.kv')

    def get_database(self):
        CONNECTION_STRING = "mongodb+srv://dawn-user-01:dawn-password-01@cluster01.vlzzyf3.mongodb.net/test1"
        client = MongoClient(CONNECTION_STRING)
        return client['dawn']

    def patient_db(self):
        dbname = self.get_database()
        patient_coll = dbname["patients"]
        return patient_coll

    def add_patient(self, firstname, email, username, password, date_of_birth, height, weight, diagnose):
        document = {
            'First name': firstname,
            'Email': email,
            'Username': username,
            'Password': password,
            'Date of birth': date_of_birth,
            #        'Date': datetime.datetime.now(),
            'Height': height,
            'Weight': weight,
            'Diagnose': diagnose
        }

        return self.patient_db().insert_one(document)



"""




def add_patient(self, firstname, email, username, password, date_of_birth, height, weight, diagnose):
    questions = []
    for i in questions:
        questions.append(i)
    document = {
        'First name': firstname,
        'Email': email,
        'Username': username,
        'Password': password,
        'Date of birth': date_of_birth,
        #        'Date': datetime.datetime.now(),
        'Height': height,
        'Weight': weight,
        'Diagnose': diagnose,
        'Questions': questions

    }

    return self.patient_db().insert_one(document)

add_patient(self,'lilo', '2@gmail.com', 'lili', '22222', '33333', '132', '43', 'ADS')\
    """
