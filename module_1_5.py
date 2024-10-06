immutable_var="apple", "coconut", 123 , 1.4 #создаю переменную и присваиваю ей кортеж
print(immutable_var) # вывожу в консоль
#immutable_var[2]=321  TypeError: 'tuple' object does not support item assignment
#print(immutable_var)  --числа и строки в кортеже неизменяемы
mutable_list=["apple","coconut",1.4,123]  #создаю список
print(mutable_list)
mutable_list[0]="coconut"
mutable_list[1]="apple"
mutable_list[2]=321
mutable_list[-1]=4.1
mutable_list.append("Modified")
print(mutable_list)
