 #создаю класс студентов, последнее поле пустое для суммы всех оценок 
class Student:
    def __init__(self, name, last_name, year, number_course, number_group, marks, allmarks):
        self.name  = name
        self.last_name = last_name
        self.year = year 
        self.number_course = number_course 
        self.number_group = number_group 
        self.marks = marks
        self.allmarks = allmarks
       #print(name, last_name, year, number_course, number_group, marks)
    pass
    def printStudent(self):
        print(self.name, self.last_name, self.year, self.number_course, self.number_group, self.marks )
    pass

student1 = Student("Василий", "Васильев", 1995, 3, "ВПИ-20",[5,5,5,5,5], 0 )
student2 = Student("Иван", "Иванов", 1998, 1, "ВПИ-21", [5,4,4,5,5],  0 )
student3 = Student("Петр", "Петров", 1994, 3, "ВПИ-20", [3,3,3,3,3] , 0 )
student4 = Student("Егоров", "Егор", 1999, 1, "ВПИ-21", [5,3,4,3,2] , 0 )
student5 = Student("Максимов", "Максим", 1997, 1, "ВПИ-21", [2,3,2,3,3] , 0 )
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
def separationGroup(list): #Разделение в списки на две группы
    for i in range(len(list)): 
        if list[i].number_group == "ВПИ-20":
            list_VPI20.append(list[i])
        else:
             list_VPI21.append(list[i])
pass
separationGroup(list)
# printStuds(list_VPI20) #вывод по группам
# printStuds(list_VPI21)
gpaMarksGroup =[]
gpaMarksStuds =[]
def GPA(list):
    gpaMarksGroup =[0,0,0,0,0]
    len_list = len(list)
    for i in range(len_list):
        for j in range(5):
            gpaMarksGroup[j] = gpaMarksGroup[j] +list[i].marks[j] 

    for i in range(len(gpaMarksGroup)):
        print(i, "предмет:", gpaMarksGroup[i]/len_list)
pass
# printStuds(list_VPI20) #вывод по группам
# printStuds(list_VPI21)

def searchBest(list):
    for i in range(len(list)):
        for j in range(5):
            list[i].allmarks = list[i].allmarks + list[i].marks[j]   
            # print(list[i].allmarks) 
    max_marks = list[0].allmarks
    for i in range(len(list)):
        if max_marks < list[i].allmarks:
            print(list[i].name) #Не видит эту строку :( 
            max_marks = list[i].allmarks
         
    return max_marks

# printStuds(list_VPI20) #вывод по группам
# printStuds(list_VPI21)
#Вызов всех функций:
print("ЗАДАНИЕ 1. Сортировка по курсу (от меньшего к большему)")
funcSortCourse(list)
print("ЗАДАНИЕ 2. Средний балл")
print("Средний балл для первой группы по каждому предмету")
GPA(list_VPI20)
print("Средний балл для второй группы по каждому предмету")
GPA(list_VPI21)
print("ЗАДАНИЕ 3. Найти старшего и младшего")
print("Самый старший", max_year(list))
print("Самый младший", min_year(list))
print("ЗАДАНИЕ 4. Поиск самого умного в группе")
print("Самый большой рейтинг в ВПИ-20", searchBest(list_VPI20))
print("Самый большой рейтинг в ВПИ-21", searchBest(list_VPI21))

