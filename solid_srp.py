# 1. SRP - Single Responsiblity Principle (classes e funções)

# classe Order viola o SRP, pois realiza três tipos diferentes de tarefas

class Order:
  # informações do pedido
  def calculate_total_sum(): pass
  def get_items(): pass
  def get_item_count(): pass
  def add_item(item): pass
  def delete_item(item): pass
  
  # exibição de dados
  def print_order(): pass
  def show_order(): pass
  
  # manipulação de dados
  def load(): pass
  def save(): pass
  def update(): pass
  def delete(): pass

# aplicando SRP na classe Order

class Order:
  # informações do pedido
  def calculate_total_sum(): pass
  def get_items(): pass
  def get_item_count(): pass
  def add_item(item): pass
  def delete_item(item): pass

class OrderRepository:
  # manipulação de dados
  def load(orderID): pass
  def save(order): pass
  def update(order): pass
  def delete(order): pass

class OrderViewer:
  # exibição de dados
  def print_order(order): pass
  def show_order(order): pass