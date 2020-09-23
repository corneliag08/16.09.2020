print ("Problema 6")
n=938
print ("Ultima cifra a acestui numar :" ,n%10)
print ("Penultima cifra a acestui numar :" , (n//10)%10 )
print ("Restul si citul impartirii la 9 :" , n%9 , "," , n//9)
print ("Suma cifrelor :" , (n//100) + (n//10)%10 +n%10 )
print ("Rasturnatul numarului :" , (n%10)*100 + (n//10)%10*10 + (n//100)%10 )  