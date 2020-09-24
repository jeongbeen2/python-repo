import random
input("고민을 입력하세요 : ")

ans1 = "자! 해보세요"
ans2 = "됐네요, 이사람아"
ans3 = "뭐라고? 다시 생각해보세요"
ans4 = "모르니 두려운 것입니다."
ans5 = "제 정신이 아니군요"
ans6 = "당신이라면 할 수 있어요"
ans7 = "해도 그만 안해도 그만! 아니겠어요"
ans8 = "맞아요. 올바른 선택입니다."
answer = (ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8)
print("고민중..."*4, "\n", answer[random.randint(1, 8)])
