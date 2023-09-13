"""
Willian Brito de Lima
Exercício A2 – Estrutura de Dados II – 30/08/2023
Recursividade
"""

"""
1) Escrever uma função recursiva em python para retornar quantas vezes um dígito d aparece em um número inteiro n. Por exemplo se o número n for igual a 10332 e o d for igual a 3, a função deve retornar 2, pois o digito 3 aparece 2 vezes no número 10332. 
A função deve ser declarada como:
def apareceDigito ( n , d ):
"""
def apareceDigito(n, d):
    if n == 0:  # Condição de parada
        return 0

    if n % 10 == d:
        return 1 + apareceDigito(n//10, d)
    else:
        return apareceDigito(n//10, d)

print('--------------- Teste Exercício 1 ---------------')

n = 154454
d = 4
print(f'n={n}; d={d}')
print('Resultado:', apareceDigito(n, d))
print()

n = 10332
d = 3
print(f'n={n}; d={d}')
print('Resultado:', apareceDigito(n, d))
print()

"""
2) Escrever uma função recursiva em python para mostrar uma string em ordem inversa.
"""
def mostraInverso(s, tam_s):
    if tam_s == 0:
        return 

    char = s[tam_s-1]
    print(char)
    
    mostraInverso(s[:tam_s-1], tam_s-1)

print('--------------- Teste Exercício 2 ---------------')

string = "abcdef ghi"
print(f'String: {string}')
mostraInverso(string, len(string))
