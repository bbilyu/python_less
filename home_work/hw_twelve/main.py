import csv


class NameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Invalid name format")
        instance.__dict__[self.name] = value


class Student:
    name = NameValidator()

    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: {'scores': [], 'tests': []} for subject in self.subjects}

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def add_grade(self, subject, score, test_result):
        if subject not in self.subjects:
            raise ValueError("Invalid subject")
        if score < 2 or score > 5:
            raise ValueError("Invalid score")
        if test_result < 0 or test_result > 100:
            raise ValueError("Invalid test result")
        self.grades[subject]['scores'].append(score)
        self.grades[subject]['tests'].append(test_result)

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError("Invalid subject")
        scores = self.grades[subject]['scores']
        if not scores:
            return 0
        return sum(scores) / len(scores)

    def average_total_score(self):
        scores = sum([self.grades[subject]['scores'] for subject in self.subjects], [])
        if not scores:
            return 0
        return sum(scores) / len(scores)


if __name__ == '__main__':

    student = Student('subjects.csv')
    student.name = 'John'


    student.add_grade('Math', 4, 80)
    student.add_grade('Math', 5, 90)
    student.add_grade('English', 3, 75)
    student.add_grade('English', 4, 85)


    print(student.average_test_score('Math'))
    print(student.average_test_score('English'))


    print(student.average_total_score())
