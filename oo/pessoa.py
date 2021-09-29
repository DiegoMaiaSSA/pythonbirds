class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    p = Pessoa('Renzo')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)