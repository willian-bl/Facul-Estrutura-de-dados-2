"""
Trabalho sobre árvores - 11/10/2023
Willian Brito de Lima
"""

from Produtos import ArvoreProdutos


class Cliente:
    """Classe de cliente, que será cadastrado na árvore"""
    
    def __init__(self, id_cliente, nome_cliente, endereco):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.endereco = endereco
        self.saldo_a_pagar = 0
        self.arvore_produto = ArvoreProdutos()
        
        self.esq=None
        self.dir=None


class ArvoreClientes:
    """Árvore binária de busca de clientes, organizada pelo id_cliente"""

    def __init__(self):
        self.raiz = None


    def busca_cliente(self, id_busca, printar=True):
        """
        Retorna o ponteiro do cliente de idpassado como argumento e o ponteiro para o nó pai desse cliente \n
        Caso `printar=True`, printa os dados do cliente encontrado (caso ele esteja na lista) e uma mensagem caso ele não esteja \n
        Caso `printar=False`, apenas retorna os ponteiros sem printar nada

        Ordem do retorno: `(nó, pai do nó)`
        """
        
        pai_no = None
        no = self.raiz
        while no and no.id_cliente != id_busca:
            pai_no = no

            if id_busca < no.id_cliente:
                no = no.esq
            else:
                no = no.dir

        if printar:
            if no and no.id_cliente == id_busca:
                print(f'\nCliente id {no.id_cliente}: \nNome: {no.nome_cliente} | End.: {no.endereco} | Saldo a pagar: {no.saldo_a_pagar}')
            else:
                print('Cliente não cadastrado!')

        return no, pai_no


    def insere_cliente(self, id_cliente, nome, end):
        """Insere um cliente na árvore"""
        
        if self.raiz == None:
            no = Cliente(id_cliente, nome, end)
            self.raiz = no
            return
        
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print('Já existe um cliente com esse id!')
            return
        
        no = Cliente(id_cliente, nome, end)
        if id_cliente < pai_no.id_cliente:
            pai_no.esq = no
        else:
            pai_no.dir = no


    def altera_nome_cliente(self, id_cliente, novo_nome):
        """Altera o nome de um cliente"""
        
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Nome do cliente de id {id_cliente} alterado de {no.nome_cliente} para {novo_nome}')
            no.nome_cliente = novo_nome
        else:
            print('Não existe um cliente com esse id!')
            
            
    def altera_endereco(self, id_cliente, novo_endereco):
        """Altera o endereço de um cliente"""
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Endereço do cliente de id {id_cliente} alterado de {no.endereco} para {novo_endereco}')
            no.endereco = novo_endereco
        else:
            print('Não existe um cliente com esse id!')


    def altera_saldo_a_pagar(self, id_cliente, novo_saldo):
        """Altera o saldo a pagar de um cliente"""

        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Saldo a pagar do cliente de id {id_cliente} alterado de {no.saldo_a_pagar} para {novo_saldo}')
            no.saldo_a_pagar = novo_saldo
        else:
            print('Não existe um cliente com esse id!')
            

    def removeCliente(self, id): 
        """Remove um cliente"""
        # no_remover - contem a referencia para o no a ser retirado
        # pai_remover - pai do nó que será retirado
        # substituto - no que vai substituir no_remover
        # pai_substituto - pai do no substituto

        # Buscando qual nó tem o valor x e qual o pai desse nó
        no_remover, pai_remover = self.busca_cliente(id, printar=False)

        if not no_remover:              
            print(f'Nó com id {id} não cadastrado!')    
            return
        # Terminando essa parte, posicionamos os ponteiros pai_remover e no_remover corretamente

        # posicionar o ponteiro substituto no nó que ira substituir no_remover
        if not no_remover.esq:  
            substituto=no_remover.dir 

        elif not no_remover.dir: 
            substituto=no_remover.esq
        
        else:   
            pai_substituto = no_remover  
            substituto = no_remover.dir    
           
            while substituto.esq: 
                pai_substituto = substituto
                substituto = substituto.esq
            # Nesse ponto substituto esta no sucessor em ordem de no_remover

            if pai_substituto != no_remover: 
                pai_substituto.esq = substituto.dir 
               
                # As próximas duas linhas de código ajustam as subárvores do substituto, movendo a subárvore esquerda
                # e a subárvore direita do nó que estamos removendo para a esquerda/direita do substituto
                substituto.dir = no_remover.dir
            substituto.esq = no_remover.esq  

        # Agora, devemos fazer com que o pai_remover aponte para o nó substituto, excluindo a referência do no_remover
        if not pai_remover:         # no_remover é a raiz da arvore
            self.raiz = substituto  
        else:
            if no_remover == pai_remover.esq:  # Se o nó estiver à esquerda do pai
                pai_remover.esq = substituto
            else:  # Se estiver a direita
                pai_remover.dir = substituto

        no_remover = None


    def contaClientes(self, p):
        """Extra - Conta o número de clientes"""
        if not p:
            return 0
        else:
            return(1 + self.contaClientes(p.esq) + self.contaClientes(p.dir))


    def clientes_cadastrados_emOrdem(self, p):
        """Mostra a lista dos clientes cadastrados utilizando o método em ordem"""

        if p:
            self.clientes_cadastrados_emOrdem(p.esq)
            print(f'Cliente emOrdem: {p.id_cliente, p.nome_cliente, p.endereco, p.saldo_a_pagar}')
            print('Produtos:')
            p.arvore_produto.produtos_cadastrados_emOrdem(p.arvore_produto.raiz)
            print('')
            self.clientes_cadastrados_emOrdem(p.dir)


    def lista_a_pagar(self, p):
        """Lista todos os clientes que possuem saldo a pagar"""
        if p:
            self.lista_a_pagar(p.esq)
            if p.saldo_a_pagar > 0:
                print(f'Devedor id {p.id_cliente}: {p.nome_cliente} deve {p.saldo_a_pagar}')
            self.lista_a_pagar(p.dir)


    def lista_em_dia(self, p):
        """Lista todos os clientes que não possuem saldo a pagar"""
        if p:
            self.lista_em_dia(p.esq)
            if p.saldo_a_pagar == 0:
                print(f'Cliente em dia: {p.id_cliente} - {p.nome_cliente}')
            self.lista_em_dia(p.dir)


    def adiciona_produto(self, id_cliente, id_produto, nome, qtd_consumida, preco):
        no = self.busca_cliente(id_cliente, printar=False)[0]
        arv_prods = no.arvore_produto
        arv_prods.insere_produto(id_produto, nome, qtd_consumida, preco)

        no.saldo_a_pagar = arv_prods.retorna_saldo(arv_prods.raiz)


    def remove_produto(self, id_cliente, id_produto):
        no = self.busca_cliente(id_cliente, printar=False)[0]
        arv_prods = no.arvore_produto
        arv_prods.remove_produto(id_produto)

        no.saldo_a_pagar = arv_prods.retorna_saldo(arv_prods.raiz)


    def altera_nome_produto(self, id_cliente, id_produto, novo_nome):
        no = self.busca_cliente(id_cliente, printar=False)[0]
        arv_prods = no.arvore_produto
        arv_prods.altera_nome_produto(id_produto, novo_nome)


    def altera_quantidade_consumida(self, id_cliente, id_produto, nova_qtd):
        no = self.busca_cliente(id_cliente, printar=False)[0]
        arv_prods = no.arvore_produto
        arv_prods.altera_quantidade_consumida(id_produto, nova_qtd)

        no.saldo_a_pagar = arv_prods.retorna_saldo(arv_prods.raiz)


    def altera_preco_unitario(self, id_cliente, id_produto, novo_preco):
        no = self.busca_cliente(id_cliente, printar=False)[0]
        arv_prods = no.arvore_produto
        arv_prods.altera_preco_unitario(id_produto, novo_preco)

        no.saldo_a_pagar = arv_prods.retorna_saldo(arv_prods.raiz)
    

# Testes
def main():
    
    print('---------- Árvore ----------')
    arv=ArvoreClientes()
    arv.insere_cliente(2, 'Armando', 'Rua ABC')
    arv.insere_cliente(4, 'Beatriz', 'Av DEF')
    arv.insere_cliente(3, 'Carlos', 'Rua GHI')
    arv.insere_cliente(5, 'Daniela', 'Rua JKL')
    arv.insere_cliente(1, 'Estefany', 'Av MNO')

    arv.clientes_cadastrados_emOrdem(arv.raiz)

    print('\n---------- Remoção ----------')
    id = 4
    print(f'Removendo Cliente id {id}: ')
    arv.removeCliente(id)
    print('\nDepois de remover: ')
    arv.clientes_cadastrados_emOrdem(arv.raiz)

    print('\n---------- Busca e alteração ----------')
    id = 3
    novo_end = 'Av Nova Avenida'
    print(f'Buscando e printando cliente de id {id}')
    arv.busca_cliente(id)
    
    arv.altera_endereco(id, novo_end)

    arv.busca_cliente(id)
    
    print('\n---------- Lista de devedores ----------')
    arv.lista_a_pagar(arv.raiz)

    print('\n---------- Lista de clientes em dia ----------')
    arv.lista_em_dia(arv.raiz)


if __name__ == '__main__':
    main()
