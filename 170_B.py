#X,Y = map(int,input().split())

#for i in range(1, X+1):
#    # 足の数
#    f = 2 * i + 4 * (X - i)
#    if f == Y:
#        print('Yes')
#        break
#    else:
#        f = 2*i
#        if f == Y:
#            print('Yes')
#            break
#        else:
#            f = 4*i
#            if f == Y:
#                print('Yes')      
#                break
#else:
#    print('No')

X, Y = map(int,input().split())
crain = (4 * X - Y) / 2
turtle = (Y- 2*X) /2
if crain.is_integer() and crain >= 0 and turtle.is_integer() and turtle >= 0 :
    crain = int(crain)
    print('Yes')
else:
    print('No')
