"""
Um ano é bissexto se for divisível por 4, 
exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

se um ano nao é divisivel por 4 -> ele nao é bissexto

divisivel por 4 mas nao por 100 -> bissexto

divisivel por 4 e por 100 e divisivel por 400 -> bissexto
"""
ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print (f"{ano} é bissexto")
        else:
            print(f"{ano} não é bissexto")
    else:
        print(f"{ano} é bissexto")    
else:
    print(f"{ano} não é bissexto")