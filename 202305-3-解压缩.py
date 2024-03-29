s = int(input())

data = ""
for _ in range(s//8):
    data += input()
if s%8 > 0:
    data += input()

byte_list = []
for i in range(s):
    x = data[2*i:2*i+2]
    # b = bin(int("0x"+x, 16))[2::]
    byte_list.append(x)
    
p = 0

init_length = 0
while p < s:
    b = bin(int("0x"+byte_list[p], 16))[2::].zfill(8)
    if b[0] == '1':
        b = '0' + b[1::]
        init_length += int('0b'+b, 2) * (128 ** p)
        p += 1
    else:
        init_length += int('0b'+b, 2) * (128 ** p)
        p += 1
        break

ans = []
while p < s:
    b = bin(int("0x"+byte_list[p], 16))[2::].zfill(8)
    if b[-2::] == '00':
        h6 = int('0b'+b[0:6], 2)
        if h6 < 60:
            l = h6 + 1
            p += 1
        else:
            tmp_length = h6 - 59
            length_hex = ''
            for _ in range(tmp_length):
                p += 1
                length_hex = byte_list[p] + length_hex
            l = int('0x'+length_hex, 16) + 1
            p += 1
        for _ in range(l):
            ans.append(byte_list[p])
            p += 1
            
    elif b[-2::] == '01':
        b2 = bin(int("0x"+byte_list[p+1], 16))[2::].zfill(8)
        o_bin = b[0:3] + b2
        o = int('0b'+o_bin, 2)
        l = 4 + int('0b'+b[3:6], 2)
        p += 2
        
        tmp_data = ans[len(ans)-o::]
        if l > o:
            ans += (tmp_data * (l//o))
            ans += tmp_data[:l%o:]
        else:
            ans += tmp_data[:l:]
            
    elif b[-2::] == '10':
        l = int('0b'+b[0:6], 2) + 1
        o = int("0x"+byte_list[p+2] + byte_list[p+1], 16)
        p += 3
        
        tmp_data = ans[len(ans)-o::]
        if l > o:
            ans += (tmp_data * (l//o))
            ans += tmp_data[:l%o:]
        else:
            ans += tmp_data[:l:]
        


for i in range(len(ans)//8):
    print("".join(ans[8*i: 8*(i+1)]))

if len(ans) % 8 > 0:
    print("".join(ans[-1 * (len(ans) % 8)::]))


