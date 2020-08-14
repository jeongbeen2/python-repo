vote = ["김정빈","김정빈","박서현","박서현","김정빈","최동혁","이민수","김철민","황득연","오워니"]


voteBox = {}

for v in vote:
    if v in voteBox:
        voteBox[v] = voteBox[v] + 1
    else:
        voteBox[v] = 1
print(voteBox)