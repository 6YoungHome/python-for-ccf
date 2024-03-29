def my_assert(f, v, feature_value_dn_dict):
    if f in feature_value_dn_dict and v in feature_value_dn_dict[f]:
        return set(feature_value_dn_dict[f][v])
    return set()
def my_re_assert(f, v, feature_value_dn_dict):
    all_user = set()
    if f in feature_value_dn_dict:
        for v1 in feature_value_dn_dict[f]:
            all_user = all_user.union(set(feature_value_dn_dict[f][1]))
        all_user = all_user.difference(set(feature_value_dn_dict[f][v]))
    return all_user
def my_and(ans1, ans2):
    return ans1.intersection(ans2)
def my_or(ans1, ans2):
    return ans1.union(ans2)
def parse_cmd(cmd):
    if cmd[0] == "&":
        cmd = cmd[1::]
        flag = 1
        p = 1
        while flag != 0:
            if cmd[p] == '(':
                flag += 1
            elif cmd[p] == ')':
                flag -= 1
            p += 1
        return my_and(parse_cmd(cmd[1:p-1]), parse_cmd(cmd[p+1:-1]))
    elif cmd[0] == "|":
        cmd = cmd[1::]
        flag = 1
        p = 1
        while flag != 0:
            if cmd[p] == '(':
                flag += 1
            elif cmd[p] == ')':
                flag -= 1
            p += 1
        return my_or(parse_cmd(cmd[1:p-1]), parse_cmd(cmd[p+1:-1]))
    elif ":" in cmd:
        f, v = map(int, cmd.split(":"))
        return my_assert(f, v, feature_value_dn_dict)
    elif "~" in cmd:
        f, v = map(int, cmd.split("~"))
        return my_re_assert(f, v, feature_value_dn_dict)
    

n = int(input())
user = []
feature_value_dn_dict = {}
dn_feature_value_dict = {}

for _ in range(n):
    tmp = list(map(int, input().split()))
    dn = tmp[0]
    c = tmp[1]
    dn_feature_value_dict[dn] = {}
    for i in range(c):
        feature = tmp[2+2*i]
        value = tmp[3+2*i]
        if feature not in feature_value_dn_dict:
            feature_value_dn_dict[feature] = {}
        if value not in feature_value_dn_dict[feature]:
            feature_value_dn_dict[feature][value] = []
        feature_value_dn_dict[feature][value].append(dn)
        
        dn_feature_value_dict[dn][feature] = value

m = int(input())
fl = []
for _ in range(m):
    cmd = input()
    ans = parse_cmd(cmd)
    if ans:
        ans = list(ans)
        ans.sort()
        fl.append(" ".join([str(i) for i in ans]))
    else:
        fl.append("")
        
for i in fl:
    print(i)
        