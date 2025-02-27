class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, rg, raca, genero, endereco, telefone,conta_atual ,CTPS,trabalhando=False, estudando=True):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.registro_geral = rg
        self.raca = raca
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone
        self.trabalhando = trabalhando
        self.salario = 1800
        self.conta_atual = conta_atual
        self.carteira_trabalho = CTPS
        self.estudando = estudando

    def apresentar(self):
        print(f"Eu me chamo {self.nome},"
              f"\nNasci em {self.data_nascimento},"
              f"\nMeu CPF é {self.cpf},"
              f"\nMeu RG {self.registro_geral},"
              f"\nMinha raça é {self.raca},"
              f"\nMeu gênero é {self.genero},"
              f"\nMeu endereço é  {self.endereco}, "
              f"\nMeu telefone: {self.telefone},"
              )
        if self.estudando:
            print("Eu estudo")
        else:
            print(f"Eu não estudo")

        if self.trabalhando:
            print(f"Eu Trabalho")
        else:
            print(f"Eu não trabalho")

    def estudar(self):
        if self.estudando:
            print("Eu estudo")
        else:
            print(f"Eu não estudo")

    def trabalhar(self):
        if self.trabalhando:
            aumento = (self.salario + self.conta_atual)
            print(f"Meu saldo anterior é de R${self.conta_atual},mas como trabalho agora tenho R${aumento}")
        elif self.trabalhando:
            print(f"Eu Trabalho")
        else:
            print(f"Eu não trabalho")

p1 = Pessoa("Júlia", "23/09/2007", "123","1269", "preto", "feminino",
            "rua naomi sanomyia 230","18 991925870","245756","152")
print('-' * 100)





class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, cpf,telefone,endereco,genero,raca, codigo,carteira_trabalho,trabalhando=True,estudando=False, ativo=True, habilidade_comunicacao=True):
        super().__init__(nome, data_nascimento,cpf, raca, genero, endereco, telefone, CTPS=True)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.telefone=telefone
        self.endereco=endereco
        self.genero=genero
        self.raca=raca
        self.codigo = codigo
        self.habilidade_comunicacao = True
        self.trabalhando = trabalhando
        self.salario = 1800
        self.estudando = estudando
        self.carteira_trabalho = carteira_trabalho
        self.ativo = True

    def apresentar(self):
        print(f"Eu me chamo {self.nome},"
              f"\nNasci em {self.data_nascimento},"
              f"\nMeu CPF é {self.cpf},"
              f"\nMeu telefone é {self.telefone},"
              f"\nMeu endereço é {self.endereco},"
              f"\nMeu genero é {self.genero},"
              f"\nMinha raça é {self.raca},"
              f"\nMeu código{self.codigo}"
              )
        if self.habilidade_comunicacao:
            print(f"Eu tenho habilidade de comunição")
        else:
            print(f"Eu não tenho habilidade de comunicação")

        if self.ativo:
            print(f"Estou ativo")
        else:
            print(f"Não estou ativo")

        if self.ativo:
            self.trabalhando = True
            print(f"Estou ativo")
        else:
            print(f"Não estou ativo")

    def trabalhar(self):
        if self.trabalhando:
            aumento = (self.salario + self.conta_atual)
            print(f"Meu saldo anterior é de R${self.conta_atual},mas como trabalho agora tenho R${aumento}")
        elif self.trabalhando:
            print(f"Eu Trabalho")
        else:
            print(f"Eu não trabalho")

    def carteira_trabalho(self):
        if self.trabalhando:
            print(f"Eu tenho carteira de trabalho")
        elif self.trabalhando and self.carteira_trabalho:
            print(f"A caminha carteira de trabalho é {self.carteira_trabalho}")
        else:
            print(f"Eu não tenho carteira de trabalho")

    def habilidade_comunicacao(self):
        if self.habilidade_comunicacao:
            print(f"tenho habilidade")
            self.habilidade_comunicacao = True
        else:
            print(f"Eu não tenho habilidade")

    def ativar(self):
        if self.ativo:
            print(f"Estou ativo")
            self.trabalhando = True
        else:
            print(f"Não estou ativo")

f1 = Pessoa("Roberta","25/08/2000","1254","162","branca","feminino",
            "rua jjghioug 122","1254555565845","1254", "1527")