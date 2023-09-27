"""
Willian Brito de Lima
Exercício A2 – Estrutura de Dados II – 20/09/2023
Ordenação
"""

"""
1) Alterar o método de ordenação quicksort, dado em sala de aula, para classificar um vetor em ordem decrescente.
"""
def particao(x,li,ls):
    a=x[li]
    acima=ls
    abaixo=li
    while abaixo < acima:
        while x[abaixo] >= a and abaixo < ls:  # Usando >= ao invés do <=
            abaixo += 1
        while x[acima] < a:  # USando < ao invés do >
            acima -= 1
        if abaixo < acima:
            x[abaixo],x[acima]=x[acima],x[abaixo]
    x[li]=x[acima]
    x[acima]=a
    print("\n",x)

    return acima

def quick(x,li,lf):

    if (li >= lf):
        return
    ret = particao(x,li,lf)  # retorna 5
    quick(x,li,ret-1)  # quick (x, 0, 4)
    quick(x,ret+1,lf)  # quick (x, 6, 15)

print('---------- Teste questão 1 ----------')
x=[12,30,15,4,5,3,70,10,2,40,50,45,25,21,23,24]
print(f'Nao ordenado: {x} \n\n')
quick(x,0,len(x)-1)
print(f'\nOrdenado quick: {x} \n\n')


"""
2) Escrever uma função em python para verificar se um vetor de números está classificado em ordem crescente.
"""
def esta_crescente(vet):
    for i in range(len(vet) - 1):
        if vet[i] > vet[i + 1]:
            return False
    
    return True

print('\n\n---------- Teste questão 2 ----------')
print(esta_crescente([0, 5, 8, 8, 9, 11, 20]))
print(esta_crescente([0, 5, 8, 8, 9, 11, 10, 20]))
print(esta_crescente([10, 9, 8, 7]))
