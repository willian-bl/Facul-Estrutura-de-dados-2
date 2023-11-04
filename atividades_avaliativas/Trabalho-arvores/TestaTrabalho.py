"""
Trabalho sobre árvores - 11/10/2023
Willian Brito de Lima
"""

from Clientes import ArvoreClientes

arv_clientes = ArvoreClientes()

arv_clientes.insere_cliente(5, 'João', 'Rua ABC')
arv_clientes.insere_cliente(2, 'Maria', 'Rua XYZ')

arv_clientes.adiciona_produto(5, 5, 'Salgado', 5, 5)
arv_clientes.adiciona_produto(5, 4, 'Refrigerante', 2, 6)
arv_clientes.adiciona_produto(5, 3, 'Sobremesa', 1, 7.5)
arv_clientes.adiciona_produto(5, 2, 'Sopa', 3, 8)
arv_clientes.adiciona_produto(5, 1, 'Café', 2, 3.5)

arv_clientes.adiciona_produto(2, 5, 'Salgado', 2, 5)
arv_clientes.adiciona_produto(2, 4, 'Refrigerante', 3, 6)
arv_clientes.adiciona_produto(2, 3, 'Sobremesa', 2, 7.5)

arv_clientes.clientes_cadastrados_emOrdem(arv_clientes.raiz)

arv_clientes.lista_a_pagar(arv_clientes.raiz)

print('\nRemovendo produto de id 3 do cliente de id 2 e printando o saldo novamente')
arv_clientes.remove_produto(id_cliente=2, id_produto=3)
arv_clientes.lista_a_pagar(arv_clientes.raiz)

print('\nAlterando a quantidade de produtos de id 4 consumido pelo cliente de id 5')
arv_clientes.altera_quantidade_consumida(id_cliente=5, id_produto=4, nova_qtd=8)
arv_clientes.lista_a_pagar(arv_clientes.raiz)
