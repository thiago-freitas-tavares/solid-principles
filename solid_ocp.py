# 1. OCP - Open-Closed Principle (objetos e entidades)

# classe PayRoll viola o OCP, pois caso a empresa comece a trabalhar com PJ,
# por exemplo, seria necessário alterar esta classe.

class CltContract:
  def salary(): pass

class Intern:
  def grant_aid(): pass

class PayRoll:
  def calculate(employee):
    if isinstance(employee, CltContract):
      balance = CltContract.salary()
    elif isinstance(employee, Intern):
      balance = Intern.grant_aid()

# aplicando OCP na classe Payroll

class Payable:
  def payment(): pass

class CltContract (Payable):
  def payment():
    # code
    pass

class Intern (Payable):
  def payment():
    # code
    pass

class PayRoll:
  def calculate(Payable, employee):
      balance = Payable.payment()
