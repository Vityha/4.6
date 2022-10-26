from random import randint

rand1=randint(0, 100)
rand2=randint(0, 100)
celo=rand1//rand2
mod=rand1%rand2
print(rand1)
print(rand2)
print(f"{celo},{mod}")
