
x = int(input('num: '))
num_1 = x//1000
num_2 = (x//100)%10
num_3 = (x//10)%10
num_4 = x%10
res = (num_1*1)+(num_2*10)+(num_3*100)+(num_4*1000)
print (res)