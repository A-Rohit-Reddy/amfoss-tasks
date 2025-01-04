n=int(input())
list1=list(map(int,input().split()))
dict1={}
for i in list1:
  if i in dict1:
    dict1[i]+=1
  else:
    dict1[i]=1
for i in dict1:
  if dict1[i]!=n:
    print(i)
