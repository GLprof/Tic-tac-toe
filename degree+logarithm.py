print("  Вас приветствует программа")
print("         Калкулятор   ")
print(". . . . . . . . . . . . . . . .")
print(
      "если Вам нужно найти корень: выберете '1' ")
print(". . . . . . . . . . . . . . . .")
print(
      "если Вам нужно найти логарифм: выберите '2'")
print(". . . . . . . . . . . . . . . .")
print(
      "если Вам нужно найти произведение: выберите '3'")
print(". . . . . . . . . . . . . . . .")
print(
      "Итак: приступим.")
def main():
    print('Прошу выбрать')
    choice=input('Введите 1, 2 или 3...: ')
    if choice=='1':
        import numpy as np
        def root(a,n):    
            if a<0 and n%2==0:
                print('Так низзя делать!!')
                print('У чётной степени не может быть корня из отрицательного числа')
            
            else:
                return np.round(a**(1/n),1)        
        a=float(input('Дай циферку посчитать...: '))
        n=int(input('А теперь степень коня...: ')) 
        result=root(a, n)
        print('А вот и результат...: ',result)
    elif choice=='2':
        import math
        import numpy as np
        def custom_log(base,a):
            return np.round(math.log(a)/math.log(base),2)
        a=float(input('введите число...: '))
        base=int(input('Основание логарифма...: '))
        result=custom_log(base, a)
        print('Резултат...:',result)
    elif choice=='3':
        def mult(a,n):
            return round(a*n,2)
        a=float(input('Первый множитель...: '))
        n=float(input('Второй множитель...: '))
        result=mult(a, n)
        print('Произведение равно... : ',result)
    else:
        print('Нет такой :-P')
main()



