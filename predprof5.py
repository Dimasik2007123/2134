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


def hash(fio):
    '''
    Generate hash-key for student/Delaet has dla uchenika
    :param fio: str, student's fio
    :return: int, hash-key
    '''
    hu=0
    st=0
    litter = '\ёйцукенгшщзхъфывапролджэячсмитьбю ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
    p = 67
    m = 10 ** 9 + 9
    for x in fio:
        hu+=(litter.index(x)*p**st)%m
        st+=1
    return hu

def Writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f=open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0])+'\n')
    for i in range(1,501):
        students[i][0]=str(hash(students[i][1]))
        f.write(','.join(students[i]) + '\n')
    f.close()


students=readfile('students.csv')
Writefile('/home/student/Документы/Зотеев 11г/students_with_hash.csv')





