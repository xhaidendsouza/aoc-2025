test_input="""
987654321111111
811111111111119
234234234234278
818181911112111
"""
input = test_input

input = input.strip().split("\n")
total = 0
for num in input:
    num = [int(digit) for digit in num]
    d1 = max(num[:-11])
    i1 = num.index(d1)+1
    d2 = max(num[i1:-10])
    i2 = num.index(d2, i1)+1
    d3 = max(num[i2:-9])
    i3 = num.index(d3, i2)+1
    d4 = max(num[i3:-8])
    i4 = num.index(d4, i3)+1
    d5 = max(num[i4:-7])
    i5 = num.index(d5, i4)+1
    d6 = max(num[i5:-6])
    i6 = num.index(d6, i5)+1
    d7 = max(num[i6:-5])
    i7 = num.index(d7, i6)+1
    d8 = max(num[i7:-4])
    i8 = num.index(d8, i7)+1
    d9 = max(num[i8:-3])
    i9 = num.index(d9, i8)+1
    d10 = max(num[i9:-2])
    i10 = num.index(d10, i9)+1
    d11 = max(num[i10:-1])
    i11 = num.index(d11, i10)+1
    d12 = max(num[i11:])
    #print(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12)

    total += d12 + d11*10 + d10*100 + d9*1000 + d8*10**4 + d7*10**5 + d6*10**6 + d5*10**7 + d4*10**8 + d3*10**9 + d2*10**10 + d1*10**11
print(total)
