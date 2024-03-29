n = int(input())

day_user_dict = {}
day_area_dict = {}
risk_list = {}
risk_in_list = {}

for i in range(n):
    tmp = list(map(int, input().split()))
    r = tmp[0]
    m = tmp[1]
    risk_list[i] = tmp[2::]
    
    for area in risk_list[i]:
        risk_in_list[area] = i

    for j in range(m):
        d, u, r = map(int, input().split())
        if d not in day_user_dict:
            day_user_dict[d] = {}
        if u not in day_user_dict[d]:
            day_user_dict[d][u] = []
        day_user_dict[d][u].append(r)
        
        if d not in day_area_dict:
            day_area_dict[d] = {}
        if r not in day_area_dict[d]:
            day_area_dict[d][r] = []
        day_area_dict[d][r].append(u)
        
    
    
    
        
        