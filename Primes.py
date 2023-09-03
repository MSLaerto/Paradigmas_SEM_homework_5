def GetInt(str):
    n = int(input(f"Введите {str}: "))
    while n <= 0:
        print(f"Простые числа положительны , повторите ввод : ")
        n = int(input())
    return n 
def Primes_founder(a, b):
    if a > b :
        a , b = b , a
    primes_list = []
    flag = 0 
    for i in range(a,b+1) :
        for j in range(2,i):
            if i%j == 0 :
                flag = 1
        if flag == 0:
            if i > 1 :
                primes_list.append(i)
        else : 
            flag = 0
    if len(primes_list)>0:        
        return primes_list
    else :
        return "Не найдено простых чисел на данном промежутке"            

print(Primes_founder(GetInt("начало промежутка: ") , GetInt("конец промежутка: ")))