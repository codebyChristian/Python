# Aula 4
class BST(object):
    def _init_(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL(object):
    def inserir(self, root, dado):
        # Passo 1
        if not root:
            return BST(dado)
        elif dado < root.dado:
            root.esquerda = self.inserir(root.esquerda, dado)
        else:
            root.direita = self.inserir(root.direita, dado)

        # Passo 2
        root.altura = 1 + max(self.getAltura(root.esquerda),
                              self.getAltura(root.direita))
        
        # Passo 3
        balanceamento = self.getBalanceamneto(root)

        # Passo 4 - rotacoes
        # direita
        if balanceamento > 1 and dado < root.esquerda.dado:
            return self.direitaRotacao(root)
        
        # esquerda
        if balanceamento < -1 and dado > root.direita.dado:
            return self.esquerdaRotacao(root)
        
        # dupla - esquerda direita
        if balanceamento > 1 and dado > root.esquerda.dado:
            root.esquerda = self.esquerdaRotacao(root.esquerda)
            return self.direitaRotacao(root)
        
        # dupla - direita esquerda
        if balanceamento < -1 and dado < root.direita.dado:
            root.direita = self.dreitaRotacao(root.direita)
            return self.esquerdaRotacao(root)
        
        return root
    
    def esquerdaRotacao(self, z):

        y = z.direita
        T2 = y.esquerda

        # rotacionando
        y.esquerda = z
        z.direita = T2

        # atualiza os valores das alturas
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        
        # retorna novo root
        return y
    
    def direitaRotacao(self, z):

        y = z.esquerda
        T3 = y.direita

        # rotacionando
        y.direita = z
        z.esquerda = T3

        # atualiza as alturas
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        
        # return
        return y
    
    def getAltura(self, root):
        if not root:
            return 0
        
        return root.altura
    
    def getBalanceamento(self, root):
        if not root:
            return 0
        
        return self.getAltura(root.esquerda) - self.getAltura(root.direita)
    
    def emOrdem(self, root):

        if not root:
            return
        
        self.emOrdem(root.esquerda)
        print("{0}".format(root.dado), end="")
        self.emOrdem(root.direita)


# Main

Teste = AVL()
root = None

root = Teste.inserir(root, 10)
root = Teste.inserir(root, 20)
root = Teste.inserir(root, 30)
root = Teste.inserir(root, 40)
root = Teste.inserir(root, 50)
root = Teste.inserir(root, 25)

Teste.emOrdem(root)
print()

