S = str(input())

cnt = 0

if S[0] == 'R' and S[1] == 'R' and S[2] == 'R':
    cnt = 3
elif S[0] == 'R' and S[1] == 'R' and S[2] == 'S':
    cnt = 2
elif S[0] == 'R' and S[1] == 'S' and S[2] == 'S':
    cnt = 1
elif S[0] == 'R' and S[1] == 'S' and S[2] == 'R':
    cnt = 1
elif S[0] == 'S' and S[1] == 'S' and S[2] == 'R':
    cnt = 1
elif S[0] == 'S' and S[1] == 'R' and S[2] == 'R':
    cnt = 2
elif S[0] == 'S' and S[1] == 'R' and S[2] == 'S':
    cnt = 1
elif S[0] == 'S' and S[1] == 'S' and S[2] == 'S':
    cnt = 0

print(cnt)