a=int(input())
reversed= int(str(abs(a))[::-1])
if (-2**31<= reversed<= 2**31-1):
    print(reversed)
else:
    print(0)

# 2 testcases are failed even though checked every possibility
