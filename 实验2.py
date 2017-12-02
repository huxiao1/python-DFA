# -*- coding: utf-8 -*

'''
E->TH
H->+TH | e
T->FJ
J->*FJ|e
F->(E)|i
'''


#手动构造预测分析表
#e代表空
dists = {
    ('E', 'i'): 'TH',
    ('E', '('): 'TH',
    ('H', '+'): '+TH',
    ('H', ')'): 'e',
    ('H', '#'): 'e',
    ('T', 'i'): 'FJ',
    ('T', '('): 'FJ',
    ('J', '+'): 'e',
    ('J', '*'): '*FJ',
    ('J', ')'): 'e',
    ('J', '#'): 'e',
    ('F', 'i'): 'i',
    ('F', '('): '(E)',
}

# 构造终结符集合
Vt = ('i', '+', '*', '(', ')')

# 构造非终结符集合
Vh = ('E', 'H', 'T', 'J', 'F')


# 获取输入栈中的内容
def printstack(stack):
    neirong = ''
    for i in stack:
        neirong += i
    return neirong


# 得到输入串剩余串
def printstr(str, location):
    neirong = ''
    for i in range(location, len(str), 1):
        neirong += str[i]
    return neirong


'''
总控程序
'''

def masterctrl(str):
    # 用列表模拟栈
    stack = []
    location = 0
    # 将#号入栈
    stack.append('#')

    # 将文法开始符入栈
    stack.append('E')

    # 将输入串第一个字符读进a中
    #a用来存放该比较的元素(右边）x用来存放出来的最后一个（左边）
    #str时输入的串
    location += 1
    a = str[location]
    flag = True
    count = 0
    print('%d\t\t%s\t\t%s' % (count, printstack(stack), printstr(str, location)))
    
    while flag:

    #跳过0步
        if count == 0:
            pass
    #不是终结符正常输出
        else:
            if x in Vt:
                print('%d\t\t%s\t\t%s' % (count, printstack(stack), printstr(str, location)))
    #是终结符就要输出所用产生式
            else:
                print('%d\t\t%s\t\t%s\t\t%s->%s' % (count, printstack(stack), printstr(str, location), x, s))
        
        x = stack.pop()



    #最后一个为终结符的情况
        if x in Vt:
            if x == str[location]:
                location += 1
                a = str[location]
            else:
                print('Error')
                exit()
    
    #最后一个为非终结符的情况 入栈程序 
        elif (x, a) in dists.keys():
            s = dists[(x, a)]
            for i in range(len(s) - 1, -1, -1):
                if s[i] != 'e':
                    stack.append(s[i])
                    
    #最后判断结束
        elif x == '#':
            if x == a:
                flag = False
            else:
                print('Error')
                exit()

        count += 1


def main():
    str = '#i*i+i#'
    print("步骤\t\t符号栈\t\t输入串\t\t\t所用产生式")
    masterctrl(str)


if __name__ == '__main__':
    main()
