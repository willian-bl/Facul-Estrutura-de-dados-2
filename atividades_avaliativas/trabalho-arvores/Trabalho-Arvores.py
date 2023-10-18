"""
Trabalho sobre árvores - 11/10/2023
Willian Brito de Lima
"""

class Cliente:
    """Classe de cliente, que será cadastrado na árvore"""
    
    def __init__(self, id_cliente, nome_cliente, endereco, saldo_a_pagar):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.endereco = endereco
        self.saldo_a_pagar = saldo_a_pagar
        
        self.esq=None
        self.dir=None

class Arvore:
    """Árvore binária de busca de clientes, organizada pelo id_cliente"""

    def __init__(self):
        self.raiz = None


    def busca_cliente(self, id_busca, printar=True):
        """
        Retorna o ponteiro do cliente de idpassado como argumento e o ponteiro para o nó pai desse cliente \n
        Caso `printar=True`, printa os dados do cliente encontrado (caso ele esteja na lista) e uma mensagem caso ele não esteja \n
        Caso `printar=False`, apenas retorna os ponteiros sem printar nada
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
            if no.id_cliente == id_busca:
                print(f'\nCliente id {no.id_cliente}: \nNome: {no.nome_cliente} | End.: {no.endereco} | Saldo a pagar: {no.saldo_a_pagar}')
            else:
                print('Cliente não cadastrado!')

        return no, pai_no


    def insere_cliente(self, id_cliente, nome, end, saldo):
        """Insere um cliente na árvore"""
        
        if self.raiz == None:
            no = Cliente(id_cliente, nome, end, saldo)
            self.raiz = no
            return
        
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print('Já existe um cliente com esse id!')
            return
        
        no = Cliente(id_cliente, nome, end, saldo)
        if id_cliente < pai_no.id_cliente:
            pai_no.esq = no
        else:
            pai_no.dir = no


    def altera_nome_cliente(self, id_cliente, novo_nome):
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Nome do cliente de id {id_cliente} alterado de {no.nome_cliente} para {novo_nome}')
            no.nome_cliente = novo_nome
        else:
            print('Não existe um cliente com esse id!')
            
            
    def altera_endereco(self, id_cliente, novo_endereco):
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Endereço do cliente de id {id_cliente} alterado de {no.endereco} para {novo_endereco}')
            no.endereco = novo_endereco
        else:
            print('Não existe um cliente com esse id!')


    def altera_saldo_a_pagar(self, id_cliente, novo_saldo):
        no, pai_no = self.busca_cliente(id_cliente, printar=False)

        if no:
            print(f'Saldo a pagar do cliente de id {id_cliente} alterado de {no.saldo_a_pagar} para {novo_saldo}')
            no.saldo_a_pagar = novo_saldo
        else:
            print('Não existe um cliente com esse id!')
            

    def lista_preOrdem(self,p):
        if p:
            print(f'no visitado em preOrdem: {p.id_cliente, p.nome_cliente, p.endereco, p.saldo_a_pagar}')
            self.lista_preOrdem(p.esq)
            self.lista_preOrdem(p.dir)

    def lista_emOrdem(self,p):
        if p:
            self.lista_emOrdem(p.esq)
            print(f'no visitado em emOrdem: {p.id_cliente, p.nome_cliente, p.endereco, p.saldo_a_pagar}')
            self.lista_emOrdem(p.dir)

    def lista_posOrdem(self,p):
        if p:
            self.lista_posOrdem(p.esq)
            self.lista_posOrdem(p.dir)
            print(f'no visitado em posOrdem: {p.id_cliente, p.nome_cliente, p.endereco, p.saldo_a_pagar}')


    def removeCliente(self,id):
        # p - contem a referencia para o no a ser retirado
        # q - pai do no p
        # v - no que vai substituir p
        # t - pai do no v
        # s - filho a esquerda de v
        p = self.raiz
        q = None
        while p and p.id_cliente != id:
            q = p
            if id < p.id_cliente:
                p = p.esq
            else:
                p = p.dir

        if not p:
            print(f'Nao cadastrado')
            return

        # posicionar o ponteiro v no no que ira substituir p

        if not p.esq:
            v=p.dir
        elif not p.dir:
            v=p.esq
        else:
            # p possui 2 subarvores. Posicionar v no sucessor emordem
            # emOrdem de p (no mais a esquerda da subarvore direita) e
            # e t no pai de v
            t = p
            v = p.dir
            s = v.esq
            while s:
                t = v
                v = s
                s = v.esq
            # Nesse ponto v esta no sucessor em orDem de p
            if t != p:
                # p nao é pai de v e v esta a esquerda de t
                t.esq = v.dir
                # remove o no v de sua posicao atual e
                # coloca no lugar do no p
                v.dir = p.dir
            v.esq = p.esq

        if not q:
            # p e a raiz da arvore
            self.raiz = v
        else:
            if p == q.esq:
                q.esq = v
            else:
                q.dir = v
        p = None

    def contaNos(self,p):

        if not p:
            return 0
        else:
            return(1+self.contaNos(p.esq)+self.contaNos(p.dir))

    def lista_a_pagar(self,p):
        if p:
            self.lista_a_pagar(p.esq)
            if p.saldo_a_pagar > 0:
                print(p.id_cliente, p.nome_cliente, p.saldo_a_pagar)
            self.lista_a_pagar(p.dir)


arv=Arvore()
arv.insere_cliente(80, 'Cliente1', 'Rua ABC', 55.3)
arv.insere_cliente(40, 'Cliente2', 'Rua DEF', 22)
arv.insere_cliente(45, 'Cliente3', 'Rua GHI', 0)
arv.insere_cliente(90, 'Cliente4', 'Rua JKL', 220.2)
arv.insere_cliente(120, 'Cliente5', 'Rua MNO', 0)

print('Árvore: ')
arv.lista_preOrdem(arv.raiz)

print('\nRemovendo Cliente id 40: ')
arv.removeCliente(40)

print('\nDepois de remover: ')
arv.lista_preOrdem(arv.raiz)

print('\nLista de devedores:')
arv.lista_a_pagar(arv.raiz)

arv.busca_cliente(45)

arv.altera_endereco(45, 'rua 123abc')

arv.busca_cliente(45)