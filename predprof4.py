import random

def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, namefile
    :return: list of students
    '''
    f=open(namefile, 'r', encoding='utf-8')
    students=[]
    for i in range(501):
        students.append(f.readline().strip().split(','))
    return students

def generatelogin(fio):
    '''
    generate login for student
    :param fio: str, student's name
    :return: str, login
    '''
    f,i,o=fio.split()
    return f+'_'+i[0]+o[0]
def generatepassword(dlina):
    s='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    password = ''.join(random.choice(s) for _ in range(dlina))
    if any(x in '0123456789' for x in password) and any(x in 'qwertyuiopasdfghjklzxcvbnm' for x in password) and any(x in 'QWERTYUIOPASDFGHJKLZXCVBNM' for x in password):
        return password
    else: generatepassword(dlina)
def Writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f=open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0])+'\n')
    for i in range(1,501):
        students[i].append(generatelogin(students[i][1]))
        students[i].append(generatepassword(8))
        f.write(','.join(students[i])+'\n')
        #f.write(','.join(students[i].append(generatelogin(students[i][1])).append(generatepassword(8))+'\n'))
    f.close()

students=readfile('students.csv')
Writefile('/home/student/Документы/Зотеев 11г/students_password.csv')