a=int(input())
array=list(map(int,input().split()))
k=int(input())

k=k%a
rotated= array[-k:] +array[:-k]

print(*rotated)
