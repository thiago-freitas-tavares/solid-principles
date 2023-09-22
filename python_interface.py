# args e kwargs

def sum_args(*args):
  result = 0
  for argument in args:
    result += argument
  return result

print(sum_args(1, 2))
print(sum_args(1, 2, 4, 6))
print(sum_args(1, 2, 4, 6, 8, 10))

def append_kwarg(**kwargs):
  print(f'Valores recebidos: {kwargs}')
  result = ""
  for value in kwargs.values():
    result += f'{value} '
  return result

print(append_kwarg(a="Python", b="Academy",  c="Rules!"))
print(append_kwarg(a="Python", b="é", c="na", d="Python", e="Academy!"))

def arg_args_kwargs(arg_1, arg_2, *args, arg_kw, **kwargs):
    print(f'Parâmetro 1: {arg_1}')
    print(f'Parâmetro 2: {arg_2}')
    print(f'*args: {args}')
    print(f'Argumento nomeado: {arg_kw}')
    print(f'**kwargs: {kwargs}')

arg_args_kwargs( 1, 'a', 'arg1', 'arg2', 2, arg_kw='KW', banana='B', bananas='A')

# Duck Typing

class Deposit:
  def execute(self):
    print("Depósito: realizar")

class Transfer:
  def execute(self):
    print("Transferência: realizar")

class Billing:
  def perform_operation(self, operation):
    try:
      operation.execute()
    except AttributeError:
      print('A operação não pôde ser realizada')

def main():
  billing = Billing()
  deposit = Deposit()
  transfer = Transfer()
  billing.perform_operation(deposit)
  billing.perform_operation(transfer)
  if __name__ == "__main__": # não entendi a necessidade disso
    main()

def perform_operation(operation, **kwargs):
  operation.execute(**kwargs)

transfer = Transfer()
perform_operation(transfer, origin='0123-4', destiny='5678-9', ammount='10_000')

deposit = Deposit()
perform_operation(deposit, destiny='0123-4', ammount='10_000')

# Informal Interface

class InformalParserInterface:
  def load_data_source(self, path: str, file_name: str) -> str:
    """Load in the file for extracting text"""
    pass
  def extract_text(self, full_file_name: str) -> dict:
    """Extract text from the currently loaded file"""
    pass

# EAFP (Easier to Ask for Forgiveness than Permission)

class Billing:
  def payment(self, operation):
    try:
      operation.execute()
    except AttributeError:
      print('A operação não pôde ser realizada.')



# Herança Múltipla e Interface em Python

# Sistema de controle de um Banco, que pode ser acessado pelos diretores e gerentes.

class Employee:
  # retorna tipo de funcionário
  pass

class Director(Employee):
  def authorize(self, passwd):
    # verifica se a senha confere
    pass

class Manager(Employee):
  def authorize(self, passwd):
    # verifica se a senha confere e também se o seu departamento tem acesso.
    pass

# O método de autorização pode variar dependendo do tipo de funcionário.
# A classe InternalSystem deve receber um diretor ou gerente como argumento .

class InternalSystem:
  def login(self, employee):
    if (hasattr(obj, 'authorize')): # verifica se o objeto possui este método
      # chama o método authorize
      pass
    else:
      # imprime mensagem de ação inválida
      pass

# Se futuramente quisermos incluir outro tipo de funcionário autorizável, não
# podemos esquecer de implementar o método authorize dentro da sua classe.

# Não faz sentido colocarmos o método authorize na classe Employee, pois nem
# todo funcionário é autorizável.

# Uma solução mais interessante seria criar uma classe AuthorizedEmployee.

class AuthorizedEmployee(Employee): # forte candidata a classe abstrata
  def authorize(self, passwd): # forte candidato a método abstrato
    # verifica se a senha confere
    pass

# Com isso, as classes Director, Manager e qualquer outro tipo de funcionário
# autorizado que vier a existir em nosso sistema, passaria a estender de
# AuthorizedEmployee ao invés de Employee.

# Neste caso, o uso de herança simples resolve o problema.

# Consideremos agora uma situação em que todos os clientes também devem possuir
# acesso ao InternalSystem.

# Fazer Customer estender de AuthorizedEmployee resolveria o problema, mas traria
# diversos outros, pois cliente não é um funcionário. Com isso, o cliente teria,
# por exemplo, um método get_bonus, um atributo salary e outros, que não fazem o
# menor sentido para esta classe.

# Precisamos arranjar uma forma de referenciar Director, Manager e Customer de uma
# mesma maneira. Uma forma na qual essas classes garantissem a existência de um
# determinado método, através de um contrato.
# Podemos criar um "contrato" que define tudo o que uma classe deve fazer se quiser
# ter um determinado status. Imagine:

# Contrato Authorized: quem quiser ser autorizável precisa saber -> autenticar
# dada uma senha, devolvendo um booleano.

# Quem quiser pode assinar este contrato, sendo assim obrigado a explicar como
# será feita essa autenticação. A vantagem é que, se um Gerente assinar esse
# contrato, podemos nos referenciar a um Gerente como um Autenticavel.

# Como Python admite herança múltipla, podemos criar a classe Autenticavel:

class Authorized:
  def authorize(self, passwd):
    # verifica se a senha confere
    pass

class Director(Employee, Authorized):
  # código omitido
  pass

class Manager(Employee, Authorized):
  # código omitido
  pass

class Customer(Authorized):
  # código omitido
  pass

# Director e Manager, além de funcionários, são autorizados. Assim, podemos
# utilizar o InternalSystem para funcionários autorizados e clientes.

class InternalSystem:
  def login(self, obj):
    if (hasattr(obj, 'authorize')):
      obj.authorize()
      return True
    else:
      print('{} não é autorizável'.format(self.__class__.__name__))
      return False

if __name__ == '__main__':
  director = Director('João', '111111111-11', 3000.0, '1234')
  manager = Manager('José', '222222222-22', 5000.0, '1235')
  customer = Customer('Maria', '333333333-33', '1236')

  system = InternalSystem()
  system.login(director)
  system.login(manager)
  system.login(customer)

# Diamond Problem ("Deadly Diamond of Death"): ambigüidade que surge quando duas
# classes B e C herdam de A, e a classe D herda de B e C.

# O exemplo anterior parece ser uma boa maneira de representar classes autorizáveis,
# mas se começássemos a estender esse sistema, logo encontraríamos complicações.

# Em um banco de verdade, as divisões entre diretores, gerentes e clientes nem
# sempre são claras. Um cliente, por exemplo, pode ser um funcionario, um
# funcionario pode ter outras subcategorias, como fixos e temporários.

# No Python, é possível que uma classe herde de várias outras classes.
# Poderíamos, por exemplo, criar uma classe A, que será superclasse das classes
# B e C. A herança múltipla não é muito difícil de entender se uma classe herda
# de várias classes que possuem propriedades completamente diferentes, mas as
# coisas ficam complicadas se duas superclasses implementam o mesmo método ou
# atributo.

# Se as classes B e C herdarem a classe A e a classe D herdar as classes B e C,
# e as classes B e C têm um método m2(), qual método a classe D herda?

class A:
  def m1(self):
    print('método de A')

class B(A):
  def m2(self):
    print('método de B')

class C(A):
  def m2(self):
    print('método de C')                

class D(B, C):
  pass

# Essa ambiguidade é conhecida como o problema do diamante, ou problema do losango,
# e diferentes linguagens resolvem esse problema de maneiras diferentes.

# O Python segue uma ordem específica para percorrer a hierarquia de classes e
# essa ordem é chamada de MRO: Method Resolution Order (Ordem de Resolução de Métodos).

# Toda classe tem um atributo __mro__ que retorna uma tupla de referências das
# superclasses na ordem MRO - da classe atual até a classe object. Vejamos o MRO da classe D.

print(D.__mro__) # atributo __mro__ retorna tuple
# Saída:
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print(D.mro()) # método mro() retorna list
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# A ordem é sempre da esquerda para direita. Repare que o Python vai procurar a
# chamada do método m2() primeiro na classe D, não encontrando vai procurar em B
# (a primeira classe herdada). Caso não encontre em B, vai procurar em C e só
# então procurar em A - e por último na classe object.

# Portanto, seguindo o MRO, a classe D chama o método m2() da classe B.

d = D()
d.m1() # saída: método de A
d.m2() # saída: método de B

# Felizmente, a função super() sabe como lidar de forma inteligente com herança
# múltipla. Se usá-la dentro do método, todos os métodos das superclasses devem
# ser chamados seguindo o MRO.

class A:
  def m1(self):
    print('método de A')

class B(A):
  def m1(self):
    super().m1()
  def m2(self):
    print('método de B')

class C(A):
  def m1(self):
    super().m1()
  def m2(self):
    print('método de C')

class D(B, C):
  def m1(self):
    super().m1()
  def m2(self):
    super().m2()

if __name__ == '__main__':
  d = D()
  d.m1() # saída: método de A
  d.m2() # saída: método de B
  