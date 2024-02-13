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
        if students[i][4]=='None':
            students[i][4]='0'
    return students

def aver(clas):
    '''
    Finding average mean
    :param clas: str, class name
    :return: float, average mean
    '''
    n=0
    s=0
    for i in range(1, 501):
        if students[i][3]==clas and students[i][4]!='0':
            s+=int(students[i][4])
            n+=1
    return format(s/n, '.3f')

def replac():
    '''
    Меняет ошибочные оценки на среднее значение по классу
    '''
    for i in range(1,501):
        if students[i][4]=='0':
            students[i][4]=str(aver(students[i][3]))

def writefile(name):
    '''
    Write new file with correct marks
    :param name: str, name file
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0]) + '\n')
    for i in range(1, 501):
        f.write(','.join(students[i])+'\n')
    f.close()
students=readfile('students.csv')
replac()
writefile('/home/student/Документы/Зотеев 11г/students_new.csv')