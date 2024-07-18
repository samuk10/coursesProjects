# Classe encapsula os atributos e métodos:
class Mecanico:
	# atributos são características;
    def __init__(self, nome, idade, cidade, qtd_ferramentas, pais="Brasil", ):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.pais = pais
        self.qtd_ferramentas = qtd_ferramentas
	# métodos são ações;
    # não esquecer o self
    # o nome "self" é uma convenção, indica que o primeiro argumento é o proprio objeto;
    def consertar(self):
        print("ação consertando")

    def cobrar_valor(self):
        print("ação cobrando")

    def comprar_ferramentas(self, nro_ferramentas):
        def _comprar_ferramentas():
            if nro_ferramentas > self.qtd_ferramentas:
                self.qtd_ferramentas = nro_ferramentas
                print("Ferramentas compradas, agora você tem: ", self.qtd_ferramentas)
            else:
                print("Ferramentas não compradas!")
        _comprar_ferramentas()

    # modo estático
    # def __str__(self):
    #     return f"Mecanico: Nome={self.nome}, Idade={self.idade}, Cidade={self.cidade}"

    # modo dinâmico
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " \
               f"{', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"

mecanico1 = Mecanico("Samuel", 31, "rio bonito", 5)
Mecanico.consertar(mecanico1) # Mecanico.consertar(mecanico1)
mecanico1.consertar()
mecanico1.cobrar_valor()
mecanico1.comprar_ferramentas(10)
print(mecanico1.nome, mecanico1.idade, mecanico1.cidade)
print(mecanico1)
