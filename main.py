from hotel import hotel

hotel1 = hotel(nome="Hilton Palace", cnpj="27.638.554.0001-68", endereco="Rua Tangará, 17", telefone="32302750")

while True:
  menu = input("""
===========================
      MENU PRINCIPAL
  1 - Lista de Clientes
  2 - Lista de Quartos
  3 - Lista de Reservas
  4 - Sair
===========================
""")
  match menu:
    case "1":
      while True:
        menu_clientes = input("""
==============================
      MENU DOS CLIENTES
  1 - Cadastrar Cliente
  2 - Listar todos os clientes
  3 - Editar cadastro de cliente
  4 - Excluir cadastro de cliente
  0 - Voltar ao menu principal
""")
  match menu_clientes:
    case "1":



class cliente:
    def __init__(self, nome, telefone, email, id_unico):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id_unico = id_unico




from cliente import cliente
from quarto import quarto

class hotel:
  def __init__(self, nome: str, endereco: str, cnpj: str, telefone: str):
    self.nome = nome
    self.endereco = endereco
    self.cnpj = cnpj
    self.telefone = telefone
    self.lista_de_clientes = []
    self.lista_de_quartos = []
    self.numero_de_reservas = 0
    self.id_unico_cliente = 1

#CLIENTES
  def cadastrar_cliente(self):
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    novo_cliente = cliente(id_unico=self.id_unico_cliente, nome=nome, telefone=telefone, email=email)
    self.id_unico_cliente += 1
    self.lista_de_clientes.append(novo_cliente)
    print("Cliente cadastrado com sucesso!")

  def listar_clientes(self):
    for element in self.lista_de_clientes:
      print(f"""
      *********************************
      INFORMAÇÕES DO CLIENTE
      Id de cadastro: {element.id_unico_cliente}
      Nome: {element.nome}
      E-mail: {element.email}
      Contato: {element.telefone}

      *********************************
""")
  def editar_clientes(self):
    ...
  def excluir_cliente(self):
    ...


#RESERVAS
  def listar_reservas(self):
    ...
  def criar_reserva(self):
    ...
  def editar_reserva(self):
    ...
  def verificar_disponibilidade(self):
    ...

#QUARTOS
  def cadastrar_quarto(self):
    ...
  def listar_quartos(self):
    ...
  def editar_quarto(self):
    ...
  def excluir_quarto(self):
    ...





class quarto():
  def __init__(self, numero_quarto: int, tipo_quarto: str, preco_diaria: float):
    self.numero_quarto = numero_quarto
    self.tipo_quarto = tipo_quarto
    self.preco_diaria = preco_diaria
    self.disponibilidade = True



from cliente import cliente
from quarto import quarto

class reserva:
  def __init__(self, cliente: cliente, quarto: quarto, data_checkin: str, data_checkout: str):
    self.cliente = cliente
    self.quarto = quarto
    self.data_checkin = data_checkin
    self.data_checkout = data_checkout



