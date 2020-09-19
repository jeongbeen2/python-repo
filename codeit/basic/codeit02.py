prise_money = 50000000

start_year = 1988
new_year = 1988




while new_year<=2016:
    year_gap = new_year - start_year
    future_money = prise_money*(1.12**(year_gap))

    
    if future_money > 1100000000:
        money_gap = round(future_money)-1100000000
        print(f"{year_gap}년차에는 {money_gap}원 차이로 동일 아저씨 말씀이 맞습니다.")

    elif future_money <1100000000:
        money_gap = 1100000000 - round(future_money)
        print(f"{year_gap}년차에는 {money_gap}원 차이로 미란 아주머니 말씀이 맞습니다.")
    new_year += 1
