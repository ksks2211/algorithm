# 명령어 기반으로 표의 행을 선택, 삭제, 복구하는 프로그램을 작성하는 과제를 맡았습니다.
# 삭제된 행을 stack 에 담기
# 최종으로 삭제된행과 존재하는행 O X 표시하기
# n은 표의 행개수, k 는 현재 행 위치,
n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
def solution(n, k, cmd):
    delete=[]
    arr = [True]*(n)
    for c in cmd:
        if c[0]=='C':
            delete.append(k)
            arr[k]=False
            tmp = k+1
            while tmp < n and arr[tmp]==False: tmp+=1
            if tmp >=n:
                tmp=k-1
                while tmp >0 and arr[tmp]==False: tmp-=1
            k = tmp
            continue
        elif c[0]=='Z':
            arr[delete.pop()]=True
            continue
        ch,num = c.split()
        num= int(num)
        g = -1 if ch=='U'  else 1
        cnt = 0
        while cnt < num :
            k+=g
            if arr[k]:cnt+=1
    answer = "".join(["O" if e else "X" for e in arr])
    return answer
solution(n,k,cmd)