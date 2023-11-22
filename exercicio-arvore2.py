""" Escrever uma árvore onde cada nó aponta para seu nó pai """

class NoArvore:
    def __init__(self, info, pai):
        self.info = info
        self.esq = None
        self.dir = None
        self.pai = pai

class Arvore:
    def __init__(self):
        self.raiz = None


    def insere_no(self, x):
        
        if not self.raiz:
            no = NoArvore(x, pai=None)
            self.raiz = no
            return

        p = self.raiz
        q = None
        while p:
            q = p
            if x < p.info:
                p = p.esq
            elif x > p.info:
                p = p.dir
            else:
                print('Elemento já cadastrado')
                return
            
        p = NoArvore(x, pai=q)
        if x < q.info:
            q.esq = p
        else:
            q.dir = p
        

    # Atualizar o remover para tratar a referência do no pai
    def remove_produto(self, x): 
        # no_remover - contem a referencia para o no a ser retirado
        # pai_remover - pai do nó que será retirado
        # substituto - no que vai substituir no_remover
        # pai_substituto - pai do no substituto

        # Buscando qual nó tem o valor x e qual o pai desse nó
        no_remover = self.raiz
        pai_remover = None

        while no_remover and no_remover.info != x:
            pai_remover = no_remover
            if x < no_remover.info:
                no_remover = no_remover.esq
            else:
                no_remover = no_remover.dir

        if not no_remover:              
            print(f'Nó com valor {x} não cadastrado!')    
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
                substituto.dir.pai = substituto 
            substituto.esq = no_remover.esq
            substituto.esq.pai = substituto  

        # Agora, devemos fazer com que o pai_remover aponte para o nó substituto, excluindo a referência do no_remover
        if not pai_remover:         # no_remover é a raiz da arvore
            self.raiz = substituto  
        else:
            if no_remover == pai_remover.esq:  # Se o nó estiver à esquerda do pai
                pai_remover.esq = substituto
            else:  # Se estiver a direita
                pai_remover.dir = substituto

        no_remover = None
        

    #  Em uma árvore onde cada nó aponta para o pai, fazer uma função para percorrer essa árvore sem usar recursividade
    def percorrer_in_order_iterativo(self):
        pilha = []
        atual = self.raiz

        while atual or pilha:
            # Empilhar todos os nós da esquerda
            while atual:
                pilha.append(atual)
                atual = atual.esq

            # Pop do topo da pilha
            atual = pilha.pop()
            print(atual.info, end=" ")

            # Mover para a subárvore direita
            atual = atual.dir
        

arv = Arvore()
arv.insere_no(20)
arv.insere_no(40)
arv.insere_no(30)
arv.insere_no(25)
arv.insere_no(10)
arv.insere_no(35)
arv.insere_no(18)

arv.percorrer_in_order_iterativo()