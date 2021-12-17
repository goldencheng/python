
def mean(a):
    total=0
    
    for i in range(people):
        total=total+a[i][1]
    average=total/people   
    return average
        
def maxi(a):
    h=-1
    for i in range(people):
        if a[i][1]>h:
            h=a[i][1]
            #hn=a[i][0]
            highi=i
    return highi
        
        
def mini(a):
    l=101
    for i in range(people):
        if a[i][1]<l:
            l=a[i][1]
            #ln=a[i][0]
            lowi=i
    return lowi

a=[]
people = int(input("人數: "))

    
for i in range(people):
    name = input("名字: ")
    score = int(input("分數: "))
    a.append([name,score])
average=mean(a)
imax=maxi(a)
imin=mini(a)
print("平均分數是: "+ str(average))
print("最高分是: "+ a[imax][0]+" " + str(a[imax][1])+"分")
print("最低分是: "+ a[imin][0]+" " + str(a[imin][1])+"分")

  
