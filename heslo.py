heslo = "Polyna1956"
pokusy = 3

while pokusy !=0:
    zadane_heslo = input("Zadej heslo: ")
    if zadane_heslo == heslo:
        print("Heslo je správné!")
        break
    
    else:
        pokusy -= 1
        print(f"Heslo je nesprávné. Zkus to znovu. Máš {pokusy} pokusy.")
        

if pokusy == 0:
    print("Překročili jste maximální počet pokusů. Heslo je nesprávné.")