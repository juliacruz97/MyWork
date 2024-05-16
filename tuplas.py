#Understanding how tuples work
# lunch is my tuple
# Tuples are immutable

lunch = ("Hamburguer","Suco","Pizza","Pudim")
#print(lunch)
#print(lunch [2])
#print(lunch[-1])
#print(lunch[0:2])
#print(lunch[1:]);
#print(len(lunch))
#lunch [1] = soda  (Tuples are immutable)

#for comida in lunch:
    #print(f' Eu vou comer {comida} ')
    
#for cont in range (0, len(lunch)):
    #print('Por favor eu quero',lunch [cont])
    
#for pos,comida in enumerate (lunch):
    #print (f'Eu vou comer {comida} na posicao {pos}')
    
#print ('Comi pra caramba! ')

#print (sorted (lunch))

a= (2,5,4)
b= (5,8,1,2)
c= b + a
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2))
print(c.index(5,1))

pessoa = ("Julia", "44" , "Fem", "99.9")
#del(pessoa)
del(pessoa (1)) # dont work
print(pessoa)

