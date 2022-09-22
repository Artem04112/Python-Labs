a=int(input("Введите 1-е число: "))
b=int(input("Введите 2-е число: "))
c=int(input("Введите 3-е число: "))
if a!=b and b!=c and a!=c:
    print(3, " - все числа уникальны")
elif (a==b and b!=c) or (a==c and a!=b) or (b==c and c!=a):
    print(1, " - только одно число уникально")
elif a==b==c:
    print(0, " - все числа одинаковы")