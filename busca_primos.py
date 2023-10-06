def is_primo(num):
    if(num<=1):
        return False
    
    for i in range(2, round((num**0.5))+1):
        if(num%i == 0):
            return False
    return True
    
def busca_primos(valorInicial, valorFinal):
    for i in range(valorInicial, (valorFinal)):
        if(is_primo(i)):
            print(i)


valorInicial, valorFinal = list(map(int, input().split()))

busca_primos(valorInicial, valorFinal)