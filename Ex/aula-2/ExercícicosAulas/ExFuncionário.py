# criação da classe funcionário
# a classe sempre precisa ser iniciada pela instância de algum objeto
# Sozinha e sendo invocada em um objeto, ela não faz nada

class Funcionario:
    def __init__(self, in_nome: str, in_cargo: str, in_salario: int):
        self.nome: str = in_nome
        self.cargo: str = in_cargo
        self.salario: int = in_salario


def mostrareg(self):
    print(f'O nome do funcionário é {self.nome}')
    print(f'O cargo do funcionário {self.nome} é {self.cargo}')
    print(f'O salário do funcionário {self.cargo} {self.nome} é {self.salario}')
    print()  # precisa-se pular uma linha


func1 = Funcionario(in_nome='Neemias', in_cargo='diretor', in_salario=20000)

func1.mostrareg(self):
