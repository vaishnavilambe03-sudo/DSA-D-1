# class Student:
#     # by using class name we can access static method

#     @staticmethod      # decorator
#     def get_personal_detail(firstname, lastname):
#         print("your personal detail=", firstname, lastname)

#     @staticmethod
#     def contact_detail(mobil_no, rollno):
#         print("your contact detail=", mobil_no, rollno)

# Student.get_personal_detail("prashant", "jha")
# Student.contact_detail(5456454646, 1001)

#destructor = resoruce deallocation

# Single level inheritance

# class College:      # parent class
#     def college_name(self):      # member function of college
#         print("Modern College")

# class Student(College):      # child class

#     def student_info(self):      # member function
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")

# obj = Student()      # object create child class
# obj.college_name()
# obj.student_info()

# Multilevel inheritance

# class College:      # first class (first level)

#     def college_name(self):
#         print("Modern College")

# # ====================================
# class Student(College):      # second class (second level)

#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Branch: Mechanical")

# # ====================================
# class Exam(Student):      # child class

#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")


# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# Multiple inheritance

# class SubMarks:      # class-1

#     math = int(input("Enter paper marks of math : "))
#     DE = int(input("Enter paper marks of design engineering : "))
#     c = int(input("Enter paper marks of c language : "))
#     english = int(input("Enter paper marks of english : "))

# # ==========================================
# # parent class -1

# class PractMarks:      # class-2

#     cpract = int(input("Enter practical marks of c language : "))

# # ==========================================
# # parent class -2

# class Result(SubMarks, PractMarks):      # child class

#     def total(self):

#         if self.math >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cpract >= 20:

#             print("pass")

#         else:
#             print("fail")

# obj = Result()
# obj.total()

#phython supports only operator overloading (compile time)
# phython supports method and constructor overidding (run time)

# class Rbi:
#     def home_loan(self):
#         print("Home loan ROI = 8%")

#     def education_loan(self):
#         print("Education loan = 9%")

# class Sbi(Rbi):
#     def education_loan(self):
#         print("Education loan = 10%")
#         #super().education_loan()

# obj = Sbi()
# obj.education_loan( )

class Rbi:
    def __init__(self):
        print("Parent class constructor")

class Sbi(Rbi):
   def __init__(self):
        print("Child class constructor")
    
obj = Sbi()
