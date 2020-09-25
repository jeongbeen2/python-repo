def trapping_rain(buildings):
    total_rain = 0
    
    for i in range(1,len(buildings)-1):
        left_max = max(buildings[:i])
        right_max = max(buildings[i:])
        upper_water = min(left_max,right_max)
        
        total_rain += max(0,upper_water-buildings[i])
    return total_rain

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))