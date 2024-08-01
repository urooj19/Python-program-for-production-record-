sum0 = 0
print("Enter quantity of milk for C001")
for cow1 in range(7):
    cow1=float(input(""))
    sum0+=cow1
avg0=sum0/7
suma=0
print("Enter record of milk for C002")

for cow1 in range(7):
    cow1=float(input(""))
    suma+=cow1
avga=suma/7

sumb=0
print("Enter record of milk for C003")
for cow2 in range(7):
    cow2=float(input(""))
    sumb+=cow2
avgb=sumb/7

sumc=0
print("Enter record of milk for C004")
for cow3 in range(7):
    cow3=float(input(""))
    sumc+=cow3
avgc=sumc/7

sumd=0
print("Enter record of milk for C005")
for cow4 in range(7):
    cow4=float(input(""))
    sumd+=cow4
avgd=sumd/7

sume=0
print("Enter record of milk for C006")
for cow5 in range(7):
    cow5=float(input(""))
    sume+=cow5
avge=sume/7

sumf=0
print("Enter record of milk for C007")
for cow6 in range(7):
    cow6=float(input(""))
    sumf+=cow6
avgf=sumf/7

sumg=0
print("Enter record of milk for C008")
for cow7 in range(7):
    cow7=float(input(""))
    sumg+=cow7
avgg=sumg/7

sumh=0
print("Enter record of milk for C009")
for cow8 in range(7):
    cow8=float(input(""))
    sumh+=cow8
avgh=sumh/7


sumi=0
print("Enter record of milk for C010")
for cow9 in range(7):
    cow9=float(input(""))
    sumi+=cow9
avgi=sumi/7

Total=sum0+suma+sumb+sumc+sumd+sume+sumf+sumg+sumh+sumi
average=Total/10

print('\t\t\t\t\t\tNUST DAIRY CO.')
print('\n')
print('\t\t\t\tMILK PRODUCTION IN NUST DAIRY FARM')
print('\n')
print('\t\t\t***********************************************')
print('\n')
print("Total quantity of milk in 7 days for C001 =",sum0,"liters")
avg0=sum0/7
print("Average:",format(avg0,".2f"))

print('\n')

print ("Total quantity of milk in 7 days for C002 =",suma,"liters")
print("Average:",format(avga,".2f"))

print('\n')

print ("Total quantity of milk in 7 days for C003 =",sumb,"liters")
print("Average:",format(avgb,".2f"))

print('\n')

print ("Total quantity of milk in 7 days for C004 =",sumc,"liters")
print("Average :",format(avgc,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C005 =",sumd,"liters")
print("Average :",format(avgd,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C006 =",sume,"liters")
print("Average :",format(avge,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C007 =",sumf)
print("Average :",format(avgf,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C008 =",sumg,"liters")
print("Average :",format(avgg,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C009 =",sumh,"liters")
print("Average :",format(avgh,".2f"))


print('\n')
print ("Total quantity of milk in 7 days for C010 =",sumi,"liters")
print("Average :",format(avgi,".2f"))


print('\n')
print('\t\t\t******************************************************')
print('Production of Milk In 1 Week :',Total,"liters")
print('Average :',average)
print('\n')
print('list:')
list1=[sum0,suma,sumb,sumc,sumd,sume,sumf,sumg,sumh,sumi]
print(list1)

print('\n')
print("Minimum Production Of This Week:",min(list1))
if sum0==min(list1):
    print("C001 has min value",min(list1))
elif suma==min(list1):
    print("C002 has min value",min(list1))
elif sumb==min(list1):
    print("C003 has min value",min(list1))
elif sumc==min(list1):
    print("C004 has min value",min(list1))
elif sumd==min(list1):
    print("C005 has min value",min(list1))
elif sume==min(list1):
    print("C006 has min value",min(list1))
elif sumf==min(list1):
    print("C007 has min value",min(list1))
elif sumg==min(list1):
    print("C008 has min value",min(list1))
elif sumh==min(list1):
    print("C009 has min value",min(list1))
elif sumi==min(list1):
    print("C010 has min value",min(list1))

print("Maximum Production Of This Week:",max(list1))
if sum0==max(list1):
    print("C001 has max value",max(list1))
elif suma==max(list1):
    print("C002 has max value",max(list1))
elif sumb==max(list1):
    print("C003 has max value",max(list1))
elif sumc==max(list1):
    print("C004 has max value",max(list1))
elif sumd==max(list1):
    print("C005 has max value",max(list1))
elif sume==max(list1):
    print("C006 has max value",max(list1))
elif sumf==max(list1):
    print("C007 has max value",max(list1))
elif sumg==max(list1):
    print("C008 has max value",max(list1))
elif sumh==max(list1):
    print("C009 has max value",max(list1))
elif sumi==max(list1):
    print("C010 has max value",max(list1))

print("\n")
print('\t\t\t*********************************************************')
print('\n')
if sum0<12:
    print("C001 Gave Less Than 12 Liters this week")
elif suma<12:
    print("C002 Gave Less Than 12 Liters this week")
elif sumb<12:
    print("C003 Gave Less Than 12 Liters this week")
elif sumc<12:
    print("C004 Gave Less Than 12 Liters this week")
elif sumd<12:
    print("C005 Gave Less Than 12 Liters this week")
elif sume<12:
    print("C006 Gave Less Than 12 Liters this week")
elif sumf<12:
    print("C007 Gave Less Than 12 Liters this week")
elif sumg<12:
    print("C008 cGave Less Than 12 Liters this week")
elif sumh<12:
    print("C009 Gave Less Than 12 Liters this week")
elif sumi<12:
    print("C010 Gave Less Than 12 Liters this week")
else:
    print("\t\t\tNo one gave less milk !! ") 
