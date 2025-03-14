class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, rg, raca, genero, endereco, telefone,conta_atual ,CTPS,trabalhando=False, estudando=True):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__registro_geral = rg
        self._raca = raca
        self._genero = genero
        self.__endereco = endereco
        self.__telefone = telefone
        self._trabalhando = trabalhando
        self._salario = 1800
        self._conta_atual = conta_atual
        self._carteira_trabalho = CTPS
        self._estudando = estudando

    def apresentar(self):
        print(f"Eu me chamo {self.__nome},"
              f"\nNasci em {self.__data_nascimento},"
              f"\nMeu CPF é {self.__cpf},"
              f"\nMeu RG {self.__registro_geral},"
              f"\nMinha raça é {self._raca},"
              f"\nMeu gênero é {self._genero},"
              f"\nMeu endereço é  {self.__endereco}, "
              f"\nMeu telefone: {self.__telefone},"
              )
        if self._estudando:
            print("Eu estudo")
        else:
            print(f"Eu não estudo")

        if self._trabalhando:
            print(f"Eu Trabalho")
        else:
            print(f"Eu não trabalho")

    def get_estudando(self):
        return self._estudando

    def get_trabalhando(self):
        if self._trabalhando:
            aumento = (self._salario + self._conta_atual)
            print(f"Meu saldo anterior é de R${self._conta_atual},mas como trabalho agora tenho R${aumento}")
        else:
            print(f"Eu não trabalho")

p1 = Pessoa("Júlia", "23/09/2007", "123","1269", "preto", "feminino",
            "rua naomi sanomyia 230","18 991925870","2456","1520")
print('-' * 100)


class Funcionario(Pessoa):
    def __init__(self, nome, data_nascimento, cpf,telefone,endereco,genero,raca, codigo,carteira_trabalho,trabalhando=True,estudando=False, ativo=True, habilidade_comunicacao=True):
        super().__init__(nome, data_nascimento,cpf, raca, genero, endereco, telefone, CTPS=True)
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__telefone=telefone
        self.__endereco=endereco
        self._genero=genero
        self._raca=raca
        self.__codigo = codigo
        self._habilidade_comunicacao = True
        self._trabalhando = trabalhando
        self._salario = 1800
        self._estudando = estudando
        self.__carteira_trabalho = carteira_trabalho
        self._ativo = True

    def apresentar(self):
        print(f"Eu me chamo {self.__nome},"
              f"\nNasci em {self.__data_nascimento},"
              f"\nMeu CPF é {self.__cpf},"
              f"\nMeu telefone é {self.__telefone},"
              f"\nMeu endereço é {self.__endereco},"
              f"\nMeu genero é {self._genero},"
              f"\nMinha raça é {self._raca},"
              f"\nMeu código{self.__codigo}"
              )
        if self._habilidade_comunicacao:
            print(f"Eu tenho habilidade de comunição")
        else:
            print(f"Eu não tenho habilidade de comunicação")

        if self._ativo:
            print(f"Estou ativo")
        else:
            print(f"Não estou ativo")

        if self._ativo:
            self._trabalhando = True
            print(f"Estou ativo")
        else:
            print(f"Não estou ativo")

    def get_trabalhando(self):
        if self._trabalhando:
            aumento = (self._salario + self._conta_atual)
            print(f"Meu saldo anterior é de R${self._conta_atual},mas como trabalho agora tenho R${aumento}")
        else:
            print(f"Eu não trabalho")

    def get_carteira_trabalho(self):
        if self._trabalhando:
            print(f"Eu tenho carteira de trabalho")
        elif self._trabalhando and self._carteira_trabalho:
            print(f"A caminha carteira de trabalho é {self._carteira_trabalho}")
        else:
            print(f"Eu não tenho carteira de trabalho")

    def get_habilidade_comunicacao(self):
        if self._habilidade_comunicacao:
            print(f"tenho habilidade")
            self._habilidade_comunicacao = True
        else:
            print(f"Eu não tenho habilidade")

    def set_ativar(self):
        if self._ativo:
            print(f"Estou ativo")
            self._trabalhando = True
        else:
            print(f"Não estou ativo")

f1 = Pessoa("Roberta","25/08/2000","1254","162","branca","feminino",
            "rua Doutor Alvino Alves da Costa  122","18 99188-1748","1254", "1527")

# set verifica e passa a informação / get recebe/pega irm=formacao / is fazer algo