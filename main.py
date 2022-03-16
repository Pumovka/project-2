from msilib.schema import PublishComponent


marks = {}
class Student:
    def __init__(self, name, last_name, year, number_course, number_group, marks):
        self.name  = name
        self.last_name = last_name
        self.year = year 
        self.number_course = number_course 
        self.number_group = number_group 
        self.marks = marks
       #print(name, last_name, year, number_course, number_group, marks)
    pass
    def printStudent(self):
        print(self.name, self.last_name, self.year, self.number_course, self.number_group, self.marks)
    pass

student1 = Student("Василий", "Васильев", 1995, 3, "ВПИ-20",{"Математика": 5, "Русский": 3, "Химия": 3, "Экология": 3, "Экономика": 3  } )
student2 = Student("Иван", "Иванов", 1998, 1, "ВПИ-21", {"Математика": 5, "Русский": 5, "Химия": 5, "Экология": 2, "Экономика": 2  } )
student3 = Student("Петр", "Петров", 1994, 3, "ВПИ-20", {"Математика": 4, "Русский": 2, "Химия": 2, "Экология": 2, "Экономика": 2  } )
student4 = Student("Егоров", "Егор", 1999, 1, "ВПИ-21", {"Математика": 5, "Русский": 5, "Химия": 5, "Экология": 5, "Экономика": 5  } )
student5 = Student("Максимов", "Максим", 1997, 1, "ВПИ-21", {"Математика": 3, "Русский": 3, "Химия": 3, "Экология": 2, "Экономика": 2  } )
list = [student1,student2,student3,student4,student5] 

def printStuds(list):#вывод списка студентов
    for i in range(len(list)): 
        list[i].printStudent()
pass


def sort_by_course(list):#выбор номера курса
    return list.number_course

def funcSortCourse(list):#сортировка по номеру курса
    try:
        list.sort(key = sort_by_course)
    except TypeError as te:
        print(te)
    printStuds(list)
pass


def max_year(list): #поиск самого старшего в списке
    max_ = list[0].year
    for i in range(len(list)):
        if max_ > list[i].year:
           max_ = list[i].year
           name = list[i].name +" " +  list[i].last_name
    return max_, name

def min_year(list): #поиск самого младшего в списке
    min_ = list[0].year
    for i in range(len(list)):
        if min_ < list[i].year:
           min_ = list[i].year
           name = list[i].name +" " +  list[i].last_name
    return min_, name

list_VPI20 = []
list_VPI21 = [] 
# def Gpa(list):
#     for i in list:
#         if list[i].number_group == "ВПИ-20":
#             list_VPI20.append(list[i])
#         else:
#              list_VPI21.append(list[i])
# pass
# Gpa(list)





funcSortCourse(list)
print("Самый старший", max_year(list))
print("Самый младший", min_year(list))