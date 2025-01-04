n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list2=list(map(int,input().split()))
list1.sort()
list2.sort()
if n<m:
    for i in list2:
        if i not in list1:
          print(i,end=" ")
        else:
          list1.remove(i)
else:
    for i in list1:
        if i not in list2:
          print(i,end=" ")
        else:
          list2.remove(i)
