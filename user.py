
class Question:
    def __init__(self, number, question, answer):
        self.q_number = number
        self.question = question
        self.answer = answer


class User:
    def __init__(self, height, weight, dob, first, last, username, password, email=''):
        self.height = height
        self.weight = weight
        self.date_of_birth = dob
        self.first_name = first
        self.last_name = last
        self.username = username
        self.password = password
        self.email = email
        self.diagnose = []

    def create_diagnose(self, q_arr, a_arr):
        num = 1
        for q, a in zip(q_arr, a_arr):
            self.diagnose.append([num, q, a])
            num += 1

    def print_user_info(self):
        print()
        print(f'    First name: {self.first_name}')
        print(f'    Last name: {self.last_name}')
        print(f'    Username: {self.username}')
        print(f'    Email: {self.email}')
        print(f'    Password: {self.password}')
        print(f'    Date of birth: {self.date_of_birth}')
        print(f'    Height: {self.height} , Weight: {self.weight}')
        print()

