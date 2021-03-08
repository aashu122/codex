num = int(input("Enter a number:"))
n = num
ctr = 2
flag = 0
while (ctr < num):
    if (num%ctr==0):
        flag = 1
        break
    ctr = ctr + 1
if (flag == 0 and num>=2):
    print(num,"is not a smith no")
else:
    sum1 = 0
    sum2 = 0
    #sum of digits


    while (num>0):
        rem = num%10
        sum1 = sum1 + rem
        num = num // 10
    #sum of prime factors
    num = n
    c = 2
    while (c<=num):
        while(num%c==0):
            pf = c
            while(pf>0):
                r = pf%10
                sum2 = sum2 + r
                pf = pf//10
            num = num // c
        c = c + 1
    print(sum1)
    print(sum2)
    if (sum1 == sum2):
        print(n, "is a smith number")
    else:
        print(n, "is not a smith number")
