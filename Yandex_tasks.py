#a = int(input())
#b = list(map(int,input().strip().split()))[:a]
#k = int(input())
a = 7
b = [1, 2, 3, 4, 5, 6, 7]
k = 4

# def ShiftChar(timeseries, K):
#     result = []  # Пустой массив.
#     for begin_index in range(0,len(timeseries) - K):
#         end_index = begin_index + K
#         # Просматриваем окно шириной K.
#         current_sum = 0
#         for  v in range(begin_index, end_index): #timeseries[begin_index .. end_index):
#             current_sum += timeseries[v]
#         current_avg = current_sum / K
#         result.append(current_avg)
#     return result 
    
# ShiftChar(b, k)




# a = int(input())
# b = list(map(int,input().strip().split()))[:a]
# k = int(input())

# def sum(a, b, k):
# 	result = []
# 	sumk = 0 
# 	for num in b[0:k]:
# 		sumk += num
# 	result.append(sumk/k)
# 	for i in range(0, a-k+1):
# 		k -= b[i]
# 		sumk += b[i+1]
# 		sum_avg = sumk/k
# 		result.append(sum_avg)
# 	print(*result)


# sum(a, b, k)




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