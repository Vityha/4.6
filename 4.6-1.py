from random import randint

rand1=randint(0, 100)
rand2=randint(0, 100)
rand3=randint(0, 100)
print(rand1)
print(rand2)
print(rand3)
sred=(rand1+rand2+rand3)/3
print('{0:.2f}'.format(sred))