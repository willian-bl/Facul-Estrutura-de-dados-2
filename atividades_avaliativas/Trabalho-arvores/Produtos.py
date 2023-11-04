"""
Trabalho sobre árvores - 11/10/2023
Willian Brito de Lima
"""

class Produto:
    """Classe de produtos, que será cadastrado na árvore"""
    
    def __init__(self, id_produto, nome_produto, quantidade_consumida, preco_unitario):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.quantidade_consumida = quantidade_consumida
        self.preco_unitario = preco_unitario
        
        self.esq=None
        self.dir=None

class ArvoreProdutos:
    """
    Árvore binária de busca de produtos, organizada pelo id_produto
    Será cadastrada na árvore de clientes: cada cliente terá sua lista de produtos comprados
    """

    def __init__(self):
        self.raiz = None


    def busca_produto(self, id_busca, printar=True):
        """
        Retorna o ponteiro do produto de id passado como argumento e o ponteiro para o nó pai desse produto \n
        Caso `printar=True`, printa os dados do produto encontrado (caso ele esteja na lista) e uma mensagem caso ele não esteja \n
        Caso `printar=False`, apenas retorna os ponteiros sem printar nada

        Ordem do retorno: `(nó, pai do nó)`
        """
        
        pai_no = None
        no = self.raiz
        while no and no.id_produto != id_busca:
            pai_no = no

            if id_busca < no.id_produto:
                no = no.esq
            else:
                no = no.dir

        if printar:
            if no and no.id_produto == id_busca:
                print(f'\nProduto id {no.id_produto}: \nNome: {no.nome_produto} | Quantidade consumida: {no.quantidade_consumida} | Preço unitário: {no.preco_unitario}')
            else:
                print('Produto não cadastrado!')

        return no, pai_no


    def insere_produto(self, id_produto, nome, qtd_consumida, preco):
        """Insere um produto na árvore"""
        
        if self.raiz == None:
            no = Produto(id_produto, nome, qtd_consumida, preco)
            self.raiz = no
            return
        
        no, pai_no = self.busca_produto(id_produto, printar=False)

        if no:
            print('Já existe um produto com esse id!')
            return
        
        no = Produto(id_produto, nome, qtd_consumida, preco)
        if id_produto < pai_no.id_produto:
            pai_no.esq = no
        else:
            pai_no.dir = no


    def altera_nome_produto(self, id_produto, novo_nome):
        """Altera o nome de um produto"""
        
        no, pai_no = self.busca_produto(id_produto, printar=False)

        if no:
            print(f'Nome do produto de id {id_produto} alterado de {no.nome_produto} para {novo_nome}')
            no.nome_produto = novo_nome
        else:
            print('Não existe um produto com esse id!')
            
            
    def altera_quantidade_consumida(self, id_produto, nova_qtd):
        """Altera a quantidade consumida de um produto"""
        no, pai_no = self.busca_produto(id_produto, printar=False)

        if no:
            print(f'Quantidade consumida do produto de id {id_produto} alterado de {no.quantidade_consumida} para {nova_qtd}')
            no.quantidade_consumida = nova_qtd
        else:
            print('Não existe um produto com esse id!')


    def altera_preco_unitario(self, id_produto, novo_preco):
        """Altera o preço unitário de um produto"""

        no, pai_no = self.busca_produto(id_produto, printar=False)

        if no:
            print(f'Preço unitário do produto de id {id_produto} alterado de {no.preco_unitario} para {novo_preco}')
            no.preco_unitario = novo_preco
        else:
            print('Não existe um produto com esse id!')
            

    def remove_produto(self, id_produto): 
        """Remove um produto"""
        # no_remover - contem a referencia para o no a ser retirado
        # pai_remover - pai do nó que será retirado
        # substituto - no que vai substituir no_remover
        # pai_substituto - pai do no substituto

        # Buscando qual nó tem o id passado e qual o pai desse nó
        no_remover, pai_remover = self.busca_produto(id_produto, printar=False)

        if not no_remover:              
            print(f'Nó com id {id_produto} não cadastrado!')    
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


    def conta_produtos(self, p):
        """Extra - Conta o número de produtos"""
        if not p:
            return 0
        else:
            return(1 + self.conta_produtos(p.esq) + self.conta_produtos(p.dir))


    def produtos_cadastrados_emOrdem(self, p):
        """Mostra a lista dos produtos cadastrados utilizando o método em ordem"""
        if p:
            self.produtos_cadastrados_emOrdem(p.esq)
            print(f'produto emOrdem: {p.id_produto, p.nome_produto, p.quantidade_consumida, p.preco_unitario}')
            self.produtos_cadastrados_emOrdem(p.dir)


    def retorna_saldo(self, p):
        if not p:
            return 0

        return p.quantidade_consumida * p.preco_unitario + \
               self.retorna_saldo(p.esq) + \
               self.retorna_saldo(p.dir)

# Testes
def main():
    print('---------- Árvore ----------')
    arv=ArvoreProdutos()
    arv.insere_produto(5, 'Salgado', 5, 5)
    arv.insere_produto(4, 'Refrigerante', 2, 6)
    arv.insere_produto(3, 'Sobremesa', 1, 7.5)
    arv.insere_produto(2, 'Sopa', 3, 8)
    arv.insere_produto(1, 'Café', 2, 3.5)

    arv.produtos_cadastrados_emOrdem(arv.raiz)

    print('\n---------- Remoção ----------')
    id = 4
    print(f'Removendo Produto id {id}: ')
    arv.remove_produto(id)
    print('\nDepois de remover: ')
    arv.produtos_cadastrados_emOrdem(arv.raiz)

    print('\n---------- Busca e alteração ----------')
    id = 3
    novo_preco = 6.75
    print(f'Buscando e printando produto de id {id}')
    arv.busca_produto(id)
    
    arv.altera_preco_unitario(id, novo_preco)

    arv.busca_produto(id)

    print('\n---------- Busca e alteração ----------')
    saldo = arv.atualiza_saldo(arv.raiz)
    print(f'Saldo atual: {saldo}')

if __name__ == '__main__':
    main()
