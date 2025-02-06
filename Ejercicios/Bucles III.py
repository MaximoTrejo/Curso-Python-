#for i in range(5):
    #si se le agrega un f al print python te deja agregar los {} 
    #print(f"valor de la variable {i}")


#for e in range(5,10):
    #si se le agrega un f al print python te deja agregar los {} 
    #print("---------------------------") 
    #print(f"valor de la variable {e}") 

#for e in range(5,50,3):
    #si se le agrega un f al print python te deja agregar los {} 
    #print(f"valor de la variable {e}") 

flag = False
email = input("mail: ")

for i in range(len(email)):
    if(email[i] == "@"):
        flag=True

if(flag):
    print(email)
    print("correcto")
else:
    print(email)
    print("malo")