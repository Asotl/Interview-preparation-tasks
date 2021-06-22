
"""
Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.
Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

a = int(input())
b = list(map(int,input().strip().split()))[:a]
k = int(input())
def opt_sum(timeseries, K):
    result = []
    sumk = 0  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    for num in b[0:K]:
        sumk += num
    result.append(sumk/K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
        print(result)
    return result 

sum( b, k)
-------------------------------------------------------------------------------------------

Рита и Гоша играют в игру. 
У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. 

a = int(input())
b = list(map(int,input().strip().split()))[:a]
k = int(input())



def Siski(number, numbers, X):
    for i in range(0, number - 1):
        for j in range(i+1, number):
            print(numbers[i],"+", numbers[j], '=', numbers[i] + numbers[j])
            if numbers[i] + numbers[j] == X:
                print(numbers[i], numbers[j])
                return numbers[i], numbers[j]
    print("None")
    return None

Siski(a, b, k)
-------------------------------------------------------------------------------------------
"""

# a = int(input())
# b = list(map(int,input().strip().split()))[:a]
# k = int(input())
a = 6
b = [-9, -7, -6, -1, -1, 3]
k = 2

def twosum_with_sort(number, numbers, X):
    numbers.sort()
    #print(numbers)
    left = 0
    right = number - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        #print(current_sum)
        if current_sum == X:
            print(numbers[left], numbers[right])
            return numbers[left], numbers[right]
        if current_sum < X:
            #print(current_sum, " < ", X)
            left += 1
        else:
            #print(current_sum, " > ", X)
            right += 1
    print('None')
    return None

twosum_with_sort(a, b, k)
       