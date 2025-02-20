class Pessoa:
    def __init__(self, nome, data_nascimento, idade, cpf, rg, raca, genero, endereco, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.idade_atual = idade
        self.cpf = cpf
        self.registro_geral = rg
        self.raca = raca
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone

    def apresentar(self):
        print(f"Eu me chamo{self.nome},"
              f"\nnasci em: {self.data_nascimento},"
              f"\ntenho {self.idade_atual} anos,"
              f"\nmeu CPF é {self.cpf},"
              f"\nmeu RG {self.registro_geral},"
              f"\nminha raça é {self.raca},"
              f"\nmeu gênero é {self.genero},"
              f"\nmeu endereço é  {self.endereco} e "
              f"\nmeu telefone: {self.telefone}"
              )