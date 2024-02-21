print("Hello word")

def Amro(n):

    n=0
   
    # n=input("what is the number ?")

    while n==0:

        try:

            n=int(input(" what is the number of Amro Robin ? "))

        except:

            print("Vous devez entrer un nombre entier")

    return n

Ba=1
n=Amro(Ba)

# n=input(" what is the number of Amro Robin ? ")

# n=input(" what is the number of AC grid ? ")