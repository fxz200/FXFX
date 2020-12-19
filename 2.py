# 鏈結串列 -- 加入、刪除、修改及輸出
# File Name: SingleList.py
# Version

import sys

class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

ptr = None
current = None
prev = None

head = Student()
head.next = None

def insert_f():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.next = None
    ptr.name = input('Student name : ')
    ptr.score = eval(input('Student score: '))
    print()

    prev = head
    current = head.next
    while current != None and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr        
        
def delete_f():
    global head
    global current
    global prev

    del_name = ''
    if head.next == None:
        print(' No student record\n')
    else:
        del_name = input(' Delete student name: ')
        prev = head
        current = head.next
        while current != None and del_name != current.name:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
            current = None
            print('\n Student %s record deleted\n' % del_name)
        else:
            print('\n Student %s not found\n' % del_name)

def modify_f():
    global head
    global current
    global prev
    global ptr

    if head.next == None:
        print(' No student record\n')
    else:
        modify_name = input(' Modify student name: ')
        prev = head
        current = head.next
        while current != None and modify_name != current.name:
            prev = current
            current = current.next
        if current != None:
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.next = current.next # 把舊的資料刪除
            current = None
            # 重新加入新的資料
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.next
            while current != None and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
            print(' Data updated successfully!\n')
        else:
            print('\n Student %s not found!\n' % modify_name)

def display_f():
    global head
    global current

    count = 0
    if head.next == None:
        print(' No student record\n')
    else:
        print('%-15s %-15s' % ('NAME', 'SCORE'))
        for i in range(25):
            print('-', end = '')
        print()
        current = head.next
        while current != None:
            print('%-17s %-15d' % (current.name, current.score))
            count = count + 1
            current = current.next
        for i in range(25):
            print('-', end = '')
        print()
        print('Total %d record(s) found\n' % count)

def main():
    option = 0
    while True:
        print('******  Single list operation  ******')
        print('            <1> Insert               ')
        print('            <2> Delete               ')
        print('            <3> Modify               ')
        print('            <4> Display              ')
        print('            <5> Exit                 ')
        print('*************************************')
        
        try:
            option = int(input('        Choice : '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

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






# 環狀串列的加入、刪除、修改及輸出
# File Name: CircularList.py
# Version

import sys

class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None

ptr = None        
current = None
prev = None

head = Student()        
head.next = head
    
def insert_f():
    global head
    global ptr
    global current
    global prev


    ptr = Student()
    print('\n\n************ Insert Node ************')
    ptr.name = input('  Please enter student name : ')
    ptr.score = eval(input('  Please enter student score : '))
    print('\n***************************************\n')
    prev = head
    current = head.next
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.next
    ptr.next = current
    prev.next = ptr
        
def delete_f():
    global head
    global current
    global prev

    del_name = ''
        
    if head.next == head:
        print('\n     No student record !!')
    else:
        print('\n\n************ Delete Node ************\n')
        del_name = input(' Please enter student name : ')
            
        prev = head
        current = head.next
        while current != head and del_name != current.name:
            prev = current
            current = current.next
        if current != head:
            prev.next = current.next
            current = None
            print(' Student %s record deleted' % del_name)
        else:
            print(' Student %s not found' % del_name)
    print('\n***************************************\n')

def modify_f():
    global head
    global current
    global prev

    if head.next == head:
        print('\n     No student record !!\n')
    else:
        print('\n\n************ Modify Node ************')
        modify_name = input(' Please enter student name: ')

        prev = head
        current = head.next
        while current != head and modify_name != current.name:
            prev = current
            current = current.next
        
        if current != head: # 找到要修改的資料，顯示該筆資料的原始資料
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.next = current.next # 把舊的資料刪除
            current = None
            # 重新加入新的資料
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.next
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.next
            ptr.next = current
            prev.next = ptr
        else:
            print('\n Student %s not found!\n' % modify_name) # 找不到資料

        
def display_f():
    global head
    global current

    count = 0
        
    if head.next == head:
        print('\n     No student record !!')
    else:
        print('\n\n************ Display Node ************')
        print('%-15s %5s' % ("NAME", "SCORE"))
        print('------------------------------------------')
        current = head.next
        while (current != head):
            print('%-15s %-3d' % (current.name, current.score))
            count += 1
            current = current.next
        print('------------------------------------------')
        print(' Total %d record(s) found !!' % count)
    print('\n****************************************\n')
        
def main():
    option = 0
    
    while True:
        print('***** Circular list operation *****')
        print('          <1> Insert               ')
        print('          <2> Delete               ')
        print('          <3> Modify               ')
        print('          <4> List                 ')
        print('          <5> Exit                 ')
        print('***********************************')
        
        try:
            option = int(input('          Choice : '))
        except ValueError:
            print()
            print('Not a correct number.')
            print('Try again\n')
            
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







import sys

# 定義一個Node的資料結構(Class)，其資料包含左、右子鏈結，姓名及分數
class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.llink = None
        self.rlink = None

# 初始化串列，建立一空節點為head，將左右鏈結皆指向本身
prev = None
current = None
ptr = None

head = Student()
head.name = ''
head.llink = head
head.rlink = head

# 新增函數，依分數的高低排序
def insert_f():
    global ptr
    global head
    global current
    global prev

    ptr = Student()
    ptr.name = input('\n  Please enter student name : ')
    ptr.score = eval(input('  Please enter student score : '))
    print()

    prev = head
    current = head.rlink
    while current != head and current.score >= ptr.score:
        prev = current
        current = current.rlink
    ptr.rlink = current
    ptr.llink = prev
    prev.rlink = ptr
    current.llink = ptr
    
# 刪除函數
def delete_f():
    global head
    global current
    global prev

    del_name = ''

    if head.rlink == head: # 無資料顯示錯誤
        print('\n     No student record !!\n')
    else:
        del_name = input('   Delete student name : ')

        prev = head
        current = head.rlink
        while current != head and del_name != current.name:
            prev = current
            current = current.rlink

        if head != current:
            prev.rlink = current.rlink
            current.rlink.llink = prev
            current = None
            print('     Student %s record deleted!!\n' % del_name)
        else:
            print('     Student %s not found!!\n' % del_name)

# 修改函數
def modify_f():
    global head
    global current
    global prev

    if head.rlink == head:
        print('\n     No student record !!\n')
    else:
        modify_name = input('   Modify student name: ')

        prev = head
        current = head.rlink
        while current != head and modify_name != current.name:
            prev = current
            current = current.rlink
        
        if current != head: # 找到要修改的資料，顯示該筆資料的原始資料
            print('\n   Student name: %s' % current.name)
            print('   Student score: %d\n' % current.score)
            prev.rlink = current.rlink # 刪除舊的資料
            current.rlink.llink = prev
            current = None
            # 重新加入新的資料
            newscore = eval(input(' Please enter new score: '))
            ptr = Student()
            ptr.next = None
            ptr.name = modify_name
            ptr.score = newscore
            prev = head
            current = head.rlink
            while current != head and current.score >= ptr.score:
                prev = current
                current = current.rlink
            ptr.rlink = current
            ptr.llink = prev
            prev.rlink = ptr
        else:
            print('\n Student %s not found!\n' % modify_name) # 找不到資料

    
# 輸出函數
def display_f():
    global head
    global current

    count = 0

    if head.rlink == head: # 無資料顯示錯誤
        print('\n     No student record !!\n')
    else:
        print('\n%-15s %-10s' % ('NAME', 'SCORE'))
        print('----------------------------------')
        current = head.rlink
        while current != head:
            print('%-15s %-3d' % (current.name, current.score))
            count += 1
            current = current.rlink
        print('----------------------------------')
        print('There is(are) %d record(s) found !!\n' % count)

# 主函數
def main():
    option = 0
    
    while True:
        print('***** Doubly linked list *****')
        print('          <1> Insert          ')
        print('          <2> Delete          ')
        print('          <3> Modify          ')
        print('          <4> List            ')
        print('          <5> Exit            ')
        print('******************************')
        
        try:
            option = int(input('     Choice : '))
        except ValueError:
            print()
            print('Not a correct number.')
            print('Try again\n')
            
        if option == 1:
            insert_f() # 新增函數
        elif option == 2:
            delete_f() # 刪除函數
        elif option == 3:
            modify_f() # 修改函數
        elif option == 4:
            display_f() # 輸出函數
        elif option == 5:
            sys.exit(0)

main()




import sys

class Poly:
    def __init__(self):
        self.coef = 0 # 多項式係數
        self.exp = 0  # 多項式指數
        self.next = None

ptr = None
eq_h1 = None
eq_h2 = None
ans_h = None

def input_f():
    global ptr

    eq_h = None
    prev = None
    while True:
        ptr = Poly()
        ptr.next = None

        try:
            ptr.coef = int(input('請輸入係數...'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if ptr.coef == 0:
            return eq_h

        try:
            ptr.exp = int(input('請輸入指數...'))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if eq_h == None:
            eq_h = ptr
        else:
            prev.next = ptr
        prev = ptr

def poly_add():
    global ptr
    global eq_h1
    global eq_h2
    global ans_h

    this1 = eq_h1
    this2 = eq_h2
    prev = None
    while this1 != None or this2 != None: # 當兩多項式皆相加完畢則結束
        ptr = Poly()
        ptr.next = None
        # 第一個多項式指數大於第二個多項式
        if (this1 != None and this2 == None) or this1 != None and this1.exp > this2.exp:
            ptr.coef = this1.coef
            ptr.exp = this1.exp
            this1 = this1.next
        elif this1 == None or this1.exp < this2.exp:
        # 第一個多項式指數小於第二個多項式
            ptr.coef = this2.coef
            ptr.exp = this2.exp
            this2 = this2.next
        else:
            ptr.coef = this1.coef + this2.coef
            ptr.exp = this1.exp
            if this1 != None:
                this1 = this1.next
            if this2 != None:
                this2 = this2.next

        if ptr.coef != 0:
            if ans_h == None:
                ans_h = ptr
            else:
                prev.next = ptr
            prev = ptr
        else:
            ptr = None

def show_poly(head, text):
    node = head
    print('%10s' % text, end = '')
    while node != None:
        print('%dx^%d' % (node.coef, node.exp), end = '')
        if node.next != None and node.next.coef >= 0:
            print('+', end = '')
        node = node.next
    print()

def main():
    global eq_h1
    global eq_h2
    global ans_h

    print('*************************************')
    print(' -- 多項式的格式為：ax^b -- ')
    print('*************************************')
    print('\n<< 第一個多項式（若係數為0，則結束）>>')
    eq_h1 = input_f()
    print('\n<< 第二個多項式（若係數為0，則結束）>>')
    eq_h2 = input_f()
    poly_add()
    print()
    show_poly(eq_h1, '第一個多項式為: ')
    show_poly(eq_h2, '第二個多項式為: ')
    show_poly(ans_h, '相加結果為: ')

main()
