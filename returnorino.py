#Returns
from statistics import mean
def temps(temp1, temp2, temp3):
    the_list = {temp1, temp2, temp3}
    the_average = mean(the_list)
    return the_average

average_1 = temps(10, 95, 41)
average_2 = temps(10, 9, 21)
average_3 = temps(10, 955, 101)
average_4 = temps(10, 956, 11)





print(average_1)
print(average_2)
print(average_3)
print(average_4)