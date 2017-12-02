# -*- coding: utf-8 -*
'''
S → aU | bV    
U → bV | aQ  
V → aU |bQ   
Q → aQ | bQ |e
'''


from DFA import dists
str3 = []



def error():
    print('Error')
    exit()


def masterctrl(str,dists):
    stack = []
    for x in (str):
        stack.append(x)

    # str1 = raw_input("请输入初态：")
    # if(type(str1) == int):
    #     str1 = char(str1) 
    str1 = dists["Start_Symbol"]

    c = dists[(str1,stack[0])]
    

    # a = input("你想输入几个终态:")
    # for x in range(a):
    #     str2 = raw_input("请输入终态:")
    #     str3.append(str2)

    str3 = dists["Final_Symbols"]

    d = len(stack)

    d = d - 1

    i = 1

    while d != 0:
        c = dists[(c,stack[i])]
        i = i + 1
        d = d - 1

    if c in str3:
        print("符合本文法!")
    else:
        print("不符合本文法!")
    


def main():
    print('本文法为:')
    print('S → aU | bV ')
    print('U → bV | aQ ')
    print('V → aU |bQ')
    print('Q → aQ | bQ |e')
    str = raw_input("请输入要检测的串：");
    masterctrl(str,dists)


if __name__ == '__main__':
    main()


