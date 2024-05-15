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

for comida in lunch:
    print(f' Eu vou comer {comida} ')
    
for cont in range (0, len(lunch)):
    print('Por favor eu quero',lunch [cont])
    
for pos,comida in enumerate (lunch):
    print (f'Eu vou comer {comida} na posicao {pos}')
    
print ('Comi pra caramba! ')

print (sorted (lunch))
