#Name:Pratik Singh
#Student id: 1001670417

class Employee:
    def __init__(self, name, IdNum, dept, jobtitle) :
        self.__name = name;
        self.__ID_Number = IdNum;
        self.__department = dept;
        self.__job_title = jobtitle;

    def set_name(self, name):
        self.__name = name

    def set_Id(self, Idum):
        self.__Id_Number = IdNum

    def set_dept(self, dept):
        self.__department = dept

    def set_jobtitle(self, jobtitle):
        self.__job_title = jobtitle

    def get_name(self):
        return self.__name

    def get_Id(self):
        return self.__Id_Number

    def get_dept(self):
        return self.__department

    def get_jobtitle(self):
        return self.__job_title

    def __str__(self):
        return "The name is " + self.__name + \
               "\nThe ID Number is " + self.__ID_Number + \
               "\nThe department is " + self.__department + \
               "\nThe job title is " + self.__job_title
