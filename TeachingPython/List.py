# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:39:58 2016

@author: amylo
"""

print("你好！\ndoudou")


#创建list

number_list = [1, 3, 5, 7, 9]
print("number_list: " + str(number_list))

number_list[1]

string_list = ["abc", "bbc", "python"]

mix_list = ["python", "java", 3, 12]

print("string_list："+str(string_list) )
print("mix_list："+str(mix_list) )

second_num = number_list[1]
third_num = string_list[2]
fourth_num = mix_list[3]
print("second_num: {0} third_num: {1} fourth_num :{2}".format(second_num,third_num,fourth_num))

number_list[1] = 30
print("number_list after: "+str(number_list))

del number_list[1]
print("number_list after del: "+str(number_list))

print(len(number_list))
print(number_list + string_list)
print("abc" in string_list)
print(["hello"]*4)

print(number_list[1])
print(number_list[-2])
print(number_list[1:])
print(number_list[0:])