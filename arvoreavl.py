class NoArvore:
    def __init__(self,info):
        self.info=info
        self.bal=0
        self.esq=None
        self.dir=None

    def getInfo(self):
        return self.info

    def getEsq(self):
        return self.esq

    def setEsq(self,esq):
        self.esq=esq

    def getDir(self):
        return self.dir

    def setDir(self,dir):
        self.dir=dir

class Arvore:

    def __init__(self):
        self.raiz=None

    def montaArvoreAvl(self,x):
        # x é o lemento que será inserido

        # Se não existe nenhum elemento, ele é inserido na raiz
        if self.raiz==None:
            no=NoArvore(x)
            self.raiz=no
            return
        
        # ya aponta para o nó mais próximo que pode ser desbalanceado
        # fya pai de ya
        # Usa p para percorrer a árvore
        # fp pai de p
        # busca e inserção

        p = self.raiz
        fp = None
        ya = p
        fya = None
        
        # Percorrendo a árvore para achar a posição do elemento a ser inserido e do nó que pode ser desbalanceado
        q=None
        while p != None:
            if x == p.info:
                print('elemento já cadastrado')  # Não permite elementos repetidos
                return
            
            if x < p.info:
                q = p.esq
            else:
                q = p.dir
            
            if q != None:  # Mudando o nó que pode ser desbalanceado
                if q.bal != 0:
                    fya=p
                    ya=q
            fp=p
            p=q

        # inserir um novo nó
        q = NoArvore(x)  # Todo nó, inicialmente, tem um fator de balanceamento 0
        if x < fp.info:
            fp.esq = q
        else:
            fp.dir = q
        
        # ALTERANDO O FATOR DE BALANCEAMENTO DOS NÓS AFETADOS
        # o balanceamento em todos os nos entre ya e q deve ser
        # alterado de 0
        if x < ya.info:  # Posicionando o p no filho do nó que pode ser desbalanceado
            p = ya.esq
        else:
            p = ya.dir
        
        # Altera o fator de balanceamento de todos os nós entre ya e o nó que foi inserido
        s = p # s é son - filho do nó desbalanceado (ya)
        while p != q:
            if x < p.info:
                p.bal = 1
                p = p.esq
            else:
                p.bal =- 1
                p = p.dir

        # determinar  se a arvore esta ou nao desbalanceada
        # se estiver, q é o nó inserido que provocou o
        # desbalanceamento no nó ya. fya é o pai de ya e
        # s é o filho de ya na direção do desbalanceamento
        if x < ya.info:  # imbal pega se o fator de balanceamento deve aumentar 1 (quando foi inserido a )
            imbal = 1
        else:
            imbal = -1

        if ya.bal == 0:  # o fator era 0, foi para 1 ou -1. Ou seja, se era 0 não tem como desbalancear
            # outro nivel foi includio na arvore e a
            # arvore continua balanceada
            ya.bal = imbal
            return
        
        if ya.bal != imbal:
            # o nó incluído foi posicionado na direção
            # oposta ao balanceamento
            # a arvore continua balanceada
            ya.bal=0
            return
        
        # CORRIGINDO DESBALANCEAMENTO
        # o nó incluído desbalanceou a arvore
        # precisa ser rebalanceada pelas rotações
        # e ajustar os balanceamentos dos nós envolvidos
        if s.bal == imbal:
            # ya e s ficaram desbalanceados na mesma direcao
            
            p=s
            if imbal == 1:  # Inserido à esquerda
                # rotacao a direita em ya

                aux = ya.esq
                filho = aux.dir
                aux.dir = ya
                ya.esq = filho

            else:  # Inserido à direita
                # rotacao a esquerda em ya
                aux = ya.dir
                filho = aux.esq
                aux.esq = ya
                ya.dir = filho
            
            # Corrigindo fatores de balanceamento
            ya.bal = 0
            s.bal=0

        else:
            # ya e s estão desbalanceados em direcoes opostas
            if imbal == 1:
                p=s.dir
                # rotacao a esquerda
                aux = s.dir
                filho = aux.esq
                aux.esq = s
                s.dir = filho

                ya.esq = p
                # rotacao a direita
                aux = ya.esq
                filho=aux.dir
                aux.dir=ya
                ya.esq=filho

            else:
                p = s.esq
                ya.dir = p

                # rotacao a direita em s
                aux = s.esq
                filho = aux.dir
                aux.dir = s
                s.esq = filho

                # rotacao a esquerda em ya

                aux = ya.dir
                filho = aux.esq
                aux.esq = ya
                ya.dir = filho
            if p.bal == 0 :
                ya.bal = 0
                s.bal = 0
            elif p.bal == imbal:
                ya.bal=-imbal
                s.bal=0
            else:
                ya.bal=0
                s.bal=imbal
            p.bal = 0 # verificar se devemos colocar aqui

        # Corrigindoo o pai do nó que foi desbalanceado
        if fya == None:
            self.raiz = p
        else:
            if ya == fya.dir :
                fya.dir = p
            else:
                fya.esq = p







    def preOrdem(self,p):
        if p:
            print(f'no visitado em preOrdem: {p.getInfo()} bal {p.bal}')
            self.preOrdem(p.getEsq())
            self.preOrdem(p.getDir())

    def emOrdem(self,p):
        if p:
            self.emOrdem(p.getEsq())
            print(f'no visitado em emOrdem: {p.getInfo()}  bal {p.bal}')
            self.emOrdem(p.getDir())


    def posOrdem(self,p):
        if p:
            self.posOrdem(p.getEsq())
            self.posOrdem(p.getDir())
            print(f'no visitado em posOrdem: {p.getInfo()}  bal {p.bal}')



    def contaNos(self,p):

        if not p:
            return 0
        else:
            return(1+self.contaNos(p.getEsq())+self.contaNos(p.getDir()))

    def contaNosPares(self,p):
        if not p:
            return 0
        elif (p.getInfo() % 2) == 0:
            return (1+self.contaNosPares(p.getEsq()) + self.contaNosPares(p.getDir()))
        else:
            return (0+self.contaNosPares(p.getEsq()) + self.contaNosPares(p.getDir()))

    def alturaArvore(self,p):
        if not p:
            return 0
        a1=self.alturaArvore(p.getEsq())
        a2=self.alturaArvore(p.getDir())
        return 1 + (a1 if a1 > a2 else a2)

    def mostraNosFolhas(self,p):

        if not p:
            return

        if not p.getEsq() and not p.getDir():
            print(f'nos folhas: {p.getInfo()}')
            return

        self.mostraNosFolhas(p.getEsq())
        self.mostraNosFolhas(p.getDir())


    def imagemEspelho(self,p):

        if p:
            aux=p.getEsq()
            p.setEsq(p.getDir())
            p.setDir(aux)
            self.imagemEspelho(p.getEsq())
            self.imagemEspelho(p.getDir())

    def contaNosFolhas(self,p):
        if not p:
            return 0

        if not p.getEsq() and not p.getDir():
            return 1
        else:
            return (0 + self.contaNosFolhas(p.getEsq()) + self.contaNosFolhas(p.getDir()))


    def mostraNivel(self, p, nivel):
      if p:
        print(f'valor: {p.getInfo()}  nivel: {nivel}')
        self.mostraNivel(p.getEsq(),nivel+1)
        self.mostraNivel(p.getDir(),nivel+1)



arv3=Arvore()
arv3.montaArvoreAvl(80)
arv3.montaArvoreAvl(40)
arv3.montaArvoreAvl(45)
arv3.montaArvoreAvl(90)
arv3.montaArvoreAvl(120)
arv3.montaArvoreAvl(88)
arv3.montaArvoreAvl(82)
arv3.montaArvoreAvl(95)
arv3.montaArvoreAvl(84)
arv3.montaArvoreAvl(42)
arv3.montaArvoreAvl(43)
arv3.montaArvoreAvl(92)
arv3.montaArvoreAvl(83)
print(f'preordem 1')
arv3.preOrdem(arv3.raiz)
print(f'emordem 1')
arv3.emOrdem(arv3.raiz)
print(f'posordem 1')
arv3.posOrdem(arv3.raiz)
arv3.mostraNivel(arv3.raiz,0)