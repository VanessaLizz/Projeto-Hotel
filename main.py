from hotel import hotel

hotel = hotel(nome="Darkside Hotel", cnpj="27.638.554.0001-68", endereco="Avenida Literária, 737, Bairro: Bookside", telefone="40028922")

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
            hotel.cadastrar_cliente()
          case "2":
            hotel.listar_clientes()
          case "3":
            hotel.editar_cliente()
          case "4":
            hotel.excluir_cliente()
          case "0":
            break
          case _:
            print("Opção inválida")

    case "2":
       while True:
        menu_quartos = input("""
==============================
      MENU DOS QUARTOS
  1 - Cadastrar Quarto
  2 - Listar todos os quartos
  3 - Editar quarto
  4 - Verificar Disponibilidade
  0 - Voltar ao menu principal
==============================
""")
        match menu_quartos:
          case "1":
            hotel.cadastrar_quarto()
          case "2":
            hotel.listar_quartos()
          case "3":
            hotel.editar_quarto()
          case "4":
            hotel.verificar_disponibilidade()
          case "0":
            break
          case _:
            print("Opção inválida")


    case "3":
        while True:
          menu_reservas = input("""
==============================
      MENU DAS RESERVAS
  1 - Cadastrar Reserva
  2 - Listar todas as reservas
  3 - Editar reserva
  4 - Cancelar reserva
  0 - Voltar ao menu principal
==============================
""")
          match menu_reservas:
            case "1":
              hotel.cadastrar_reserva()
            case "2":
              hotel.listar_reservas()
            case "3":
              hotel.editar_reserva()
            case "4":
              hotel.cancelar_reserva()
            case "0":
              break
            case _:
              print("Opção inválida")

    case "4":
            print("Encerrando o sistema...")
            break

    case _:
            print("Opção inválida!")