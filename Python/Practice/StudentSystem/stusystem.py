import os
def main():
    while True :
        menum()
        choice = int(input('请选择:'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('请确定要退出系统吗：y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢你的使用！！！')
                    break
                else :
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def menum():
    print('========================学生信息管理系统========================')
    print('--------------------------功能菜单----------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------')
# menum()
def insert():
    student_list=[]
    while True:
        id=input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            english=int(input('请输入英语成绩：'))
            python=int(input('请输入Python成绩：'))
            java= int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入！')
            continue
        # 将录入的成绩保存到字典中
        student={'id':id,'name':name,'english':english,'python':python,'java':java}
        student_list.append(student)
        answer=input('是否继续添加？y/n')
        if answer=='y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕！！！')
filename='student.txt'
def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')

    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_quert=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按ID查询请输入1，按姓名查找请输入2：')
            if mode=='1':
                id=input('请输入学生ID：')
            elif mode=='2':
                name=input('请输入学生姓名：')
            else:
                print('你输入的信息有误，请重新输入')
                continue
            with open(filename,'r',encoding='utf-8') as rfile:
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_quert.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_quert.append(d)
            show_student(student_quert)
            student_quert.clear()
            answer=input('是否要继续查询？y/n\n')
            if answer=='y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息，无数据显示！！')
        return
    # 定义标题显示格式
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','java成绩','总成绩'))
    # 定义内容显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))
def delete():
    while True:
        student_id=input('请输入要删除的学生的ID：')
        if  student_id!='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))#将字符串转为字典
                        if d['id']!=student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag :
                        print(f"id为{student_id}的学生信息已经被删除！")
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()#删除后显示所有学生信息
            answer=input('是否继续删除？y\n')
            if answer == 'y':
                continue
            else:
                break

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生的ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d= dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息，可以修改他的相关信息！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['english']=int(input('请输入英语成绩：'))
                        d['python']=int(input('请输入Python成绩：'))
                        d['java']=int(input('请输入Java成绩：'))
                    except:
                        print('你输入的信息有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('信息修改成功！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他学生信息？y/n\n')
        if answer=='y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list = rfile.readlines()
            students_new=[]
            for item in student_list:
                d=dict(eval(item))
                students_new.append(d)
    else:
        return
    asc_or_dasc=input('请选择（0：升序，1：降序)')
    if asc_or_dasc=='0':
        asc_or_dasc_bool=False
    elif asc_or_dasc=='1':
        asc_or_dasc_bool=True
    else:
        print('你的输入有误，请重新输入！！')
        sort()
    mode =input('请输入排序方式（1.按英语成绩排序 2.按Python成绩排序 3.按Java成绩排序 0.按总成绩排序）')
    if mode=='1':
        students_new.sort(key=lambda x:int(x['english']),reverse=asc_or_dasc_bool)
    elif mode=='2':
        students_new.sort(key=lambda x: int(x['python']), reverse=asc_or_dasc_bool)
    elif mode=='3':
        students_new.sort(key=lambda x: int(x['java']), reverse=asc_or_dasc_bool)
    elif mode=='4':
        students_new.sort(key=lambda x: int(x['english'])+int(x['python'])+int(x['java']), reverse=asc_or_dasc_bool)
    else:
        print('您输入的信息有误请重新输入！！！')
        sort()
    show_student(students_new)



def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print(f'一共有{len(student)}名学生')
            else:
                print('还没有录入学生信息！！')
    else:
        print('暂未保存数据信息。。。。')

def show():
    student_list=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print('暂未保存数据信息。。。。')

if __name__ == '__main__':
    main()