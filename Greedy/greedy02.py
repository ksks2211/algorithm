n, m, k = map(int,input().split()) # 입력을 공백으로 구분해서 정수값으로 매핑해서 받기
data = list(map(int,input().split())) # 리스트를 입력받기

data.sort()# 데이터 소팅 내림차순으로
first = data[n-1]
second = data[n-2]


count = (m//(k+1))*k # count는 first를 사용한 개수
count += m%(k+1)

result =first * count
result += second * (m-count)

print(result)