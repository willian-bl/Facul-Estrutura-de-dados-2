"""
Trabalho sobre árvores - 11/10/2023
Willian Brito de Lima
"""

class Cliente:
    def __init__(self,id_cliente, nome_cliente, endereco, saldo_a_pagar):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.endereco = endereco
        self.saldo_a_pagar = saldo_a_pagar
        
        self.esq=None
        self.dir=None

class Arvore:

    def __init__(self):
        self.raiz=None

    def insere_cliente(self,id, nome, end, saldo):
        if self.raiz==None:
            no=Cliente(id, nome, end, saldo)
            self.raiz=no
            return
        q=None
        p=self.raiz
        while p and p.id_cliente != id :
            q=p
            if (id<p.id_cliente):
                p=p.esq
            else:
                p=p.dir

        if p:
            print('Já existe um cliente com esse id!')
            return
        p=Cliente(id, nome, end, saldo)
        if id<q.id_cliente:
            q.esq = p
        else:
            q.dir = p

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
