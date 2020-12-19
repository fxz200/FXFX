
import sys
#定義一個Node資料結構(class)
#資料包含姓名分數學號
class Student:
    def __init__(self):#新增__ini__函式
        self.name = ''#資料
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.num=''
        self.next = None #指向下一個節點的指標


        
#初始化串列       
ptr = None
current = None
prev = None
head = Student()#建立空節點head
head.next = None#指向下一個節點的指標

def insert_f():#新增insert_f函式
    global ptr #使ptr可以在函數中進行處理(全域變數)
    global head
    global current
    global prev

    ptr = Student()
    ptr.next = None#指向下一個節點的指標
    ptr.num=(input('學號:'))#新增學號
    ptr.name = input('姓名 : ')
    ptr.score1 = eval(input('計概成績: '))#新增計概成績
    ptr.score2 = eval(input('微積分成績: '))#新增微積分成績
    ptr.score3 = eval(input('程式設計成績: '))#新增程式設計成績
    ptr.total=(ptr.score1+ptr.score2+ptr.score3)#新增總分
    ptr.aver=round((ptr.score1+ptr.score2+ptr.score3)/3)#新增平均分數
    
    print()

    prev = head
    current = head.next
    while current != None and current.score1 >= ptr.score1:
        prev = current
        current = current.next
    while current != None and current.score2 >= ptr.score2:
        prev = current
        current = current.next
    while current != None and current.score3 >= ptr.score3:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr        

#新增"刪除"函數
def delete_f():
    global head
    global current
    global prev

    del_name = ''
    if head.next == None:
        print(' 沒有學生成績\n')
    else:
        del_name = input(' 要刪除的學生姓名: ')
        prev = head
        current = head.next
        while current != None and del_name != current.name:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            print('\n 學生 %s 成績已刪除\n' % del_name)
        else:
            print('\n 無 %s 學生\n' % del_name)
#新增"修改"函數
def modify_f():
    global head
    global current
    global prev
    global ptr

    if head.next == None:
        print(' 沒有學生成績\n')
    else:
        modify_name = input(' 修改的學生姓名: ')
        prev = head
        current = head.next
        while current != None and modify_name != current.name:
            prev = current
            current = current.next
        if current != None:
            print('\n   學生姓名: %s' % current.name)
            print('  學生計概成績: %d\n' % current.score1)
            print('  學生微積分成績: %d\n' % current.score2)
            print('  學生程式設計成績: %d\n' % current.score3)
            prev.next = current.next # 把舊的資料刪除
            current = None
            # 重新加入新的資料
            newnum=ptr.num
            newscore1 = eval(input(' 輸入新的計概成績: '))
            newscore2 = eval(input(' 輸入新的微積分成績: '))
            newscore3 = eval(input(' 輸入新的程式設計成績: '))
            newtotal= newscore1+ newscore2+ newscore3
            newaver=round((newscore1+ newscore2+ newscore3)/3)
            
            ptr = Student()
            ptr.next = None
            ptr.num=newnum
            ptr.name = modify_namessss
            ptr.score1 = newscore1
            ptr.score2 = newscore2
            ptr.score3 = newscore3
            ptr.total=newtotal
            ptr.aver=newaver
            
            prev = head
            current = head.next
            while current != None and current.score1 >= ptr.score1:
                prev = current
                current = current.next
            while current != None and current.score2 >= ptr.score2:
                prev = current
                current = current.next
            while current != None and current.score3 >= ptr.score3:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
            print(' 資料更新成功!\n')
        else:
            print('\n 無 %s 學生!\n' % modify_name)
#新增"顯示"函數
def display_f():
    global head
    global current

    count = 0
    if head.next == None:
        print(' 無此成績\n')
    else:
        print('%-13s %-10s %-8s %-8s %-10s %-8s %-8s' % ('學號','姓名','計概成績','微積分成績','程式設計成績','總成績','平均成績'))
        for i in range(100):
            print('-', end = '')
        print()
        current = head.next
        while current != None:
            print('%-15s %-15s %-14d %-14d %-11d %-10d %-10d' % (current.num,current.name, current.score1,current.score2,current.score3,current.total,current.aver))
            count = count + 1
            current = current.next
        for i in range(100):
            print('-', end = '')
        print()
        print('總共 %d 筆成績\n' % count)
#新增"選單"函數
def main():
    option = 0
    while True:
        print('******        選單           ******')
        print('            <1> 輸入               ')
        print('            <2> 刪除              ')
        print('            <3> 修改               ')
        print('            <4> 顯示             ')
        print('            <5> 退出                 ')
        print('*************************************')
        
        try:
            option = int(input('        選擇 : '))
        except ValueError:
            print('非選單號碼')
            print('重試\n')

        print()
        if option == 1:
            insert_f()
        elif option == 2:
            delete_f()
        elif option == 3:
            modify_f()
        elif option == 4:
            display_f()
        elif option == 5:
            sys.exit(0)

main()







print(x)
main()
