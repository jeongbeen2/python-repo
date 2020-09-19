# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def F_to_C(F):
    C = ((F-32)*5)/9
    return C



T_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(T_list))  # 화씨 온도 출력

i = 0
N_list = []
while i<len(T_list):
    N_list.append(round(F_to_C(T_list[i]),1))
    i += 1

print("섭씨 온도 리스트: " + str(N_list))  # 섭씨 온도 출력
