n = int(input())

ans = []


def gaussian(ii, jj):
    if len(arr)-1 == ii or len(arr[0])-1 == jj:
        return
    for h in range(len(arr) - ii):
        if arr[ii + h][jj] != 0:
            break
    else:
        gaussian(ii, jj + 1)

    if arr[ii][jj] == 0:
        h = 1 + ii
        while arr[h][jj] == 0:
            h += 1
        arr[ii], arr[h] = arr[h], arr[ii]
    for h in range(ii + 1, len(arr)):
        if arr[h][jj] == 0:
            continue
        bs = arr[h][jj] / arr[ii][jj]
        for l in range(len(arr[h])):
            arr[h][l] = arr[h][l] - bs * arr[ii][l]
    gaussian(ii + 1, jj + 1)


for _ in range(n):
    ele_set = set()
    ele_dict_ls = []
    tmp = input().split()
    for i in range(int(tmp[0])):
        ele_name = ''
        ele_count = ''
        ele_string = tmp[1+i]
        ele_dict = {}
        p = 0
        tag = 0
        while p < len(ele_string):
            if ele_string[p].isalpha() and tag == 0:
                ele_name += ele_string[p]
            elif ele_string[p].isalpha() and tag == 1:
                ele_dict[ele_name] = int(ele_count)
                ele_set.add(ele_name)
                ele_name = ele_string[p]
                tag = 0
            elif ele_string[p].isnumeric() and tag == 0:
                ele_count = ele_string[p]
                tag = 1
            elif ele_string[p].isnumeric() and tag == 1:
                ele_count += ele_string[p]
            p += 1
        ele_dict[ele_name] = int(ele_count)
        ele_set.add(ele_name)
        ele_dict_ls.append(ele_dict)

    arr = [[0]*int(tmp[0]) for _ in range(len(ele_set))]

    ele_list = list(ele_set)
    for i in range(len(ele_set)):
        for j in range(int(tmp[0])):
            if ele_list[i] in ele_dict_ls[j]:
                arr[i][j] = ele_dict_ls[j][ele_list[i]]

    if len(arr) < len(arr[0]):
        ans.append("Y")
        continue

    gaussian(0, 0)

    r = len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:
                break
        else:
            r -= 1

    if r < len(arr[0]):
        ans.append("Y")
    elif r > len(arr[0]):
        ans.append("N")
    else:
        if arr[-1].count(0) == len(arr[-1])-1:
            ans.append("N")
        else:
            ans.append("Y")



for i in ans:
    print(i)