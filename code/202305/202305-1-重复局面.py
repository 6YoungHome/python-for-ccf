n = int(input())

res_list = []
for _ in range(n):
    board = ''
    for __ in range(8):
        board += input()
    res_list.append(board)
    print(res_list.count(board))