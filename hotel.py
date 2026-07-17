from cliente import cliente
from quarto import quarto
from reserva import reserva

class hotel:
    def __init__(self, nome: str, endereco: str, cnpj: str, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.telefone = telefone
        self.lista_de_clientes = []
        self.lista_de_quartos = []
        self.numero_de_reservas = []
        self.id_unico_cliente = 1

    def cadastrar_cliente(self):
        nome = input("Digite o nome do cliente: ")
        telefone = input("Digite o telefone do cliente: ")
        email = input("Digite o email do cliente: ")

        novo_cliente = cliente(id_unico=self.id_unico_cliente, nome=nome, telefone=telefone, email=email)
        self.id_unico_cliente += 1
        self.lista_de_clientes.append(novo_cliente)

        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        if len(self.lista_de_clientes) == 0:
            print("Nenhum cliente cadastrado.")

        for element in self.lista_de_clientes:
            print(f"""
            *********************************
                INFORMAÇÕES DO CLIENTE
            Id de cadastro: {element.id_unico}
            Nome: {element.nome}
            E-mail: {element.email}
            Contato: {element.telefone}

            *********************************
        """)
            
    def editar_clientes(self):
        if len(self.lista_de_clientes) == 0:
            print("Nenhum cliente cadastrado!")
        else:
            pesquisa_editar = input("Digite o ID ou o Nome do cliente: ")

            for e in self.lista_de_clientes:
                if str(e.id_unico) == pesquisa_editar or e.nome.lower() == pesquisa_editar.lower():
                    edicao = input("Digite a opção que deseja editar: 1. Nome - 2. Telefone - 3. Email - 4. Cadastro Completo")
                    match edicao:
                        case "1":
                            e.nome = input("Digite o nome do cliente: ")
                        case "2":
                            e.telefone = input("Digite o nº de telefone do cliente: ")
                        case "3":
                            e.email = input("Digite o email do cliente: ")
                        case "4":
                            e.nome = input("Digite o nome do cliente: ")
                            e.telefone = input("Digite o nº de telefone do cliente: ")
                            e.email = input("Digite o email do cliente: ")

                    print("Cadastro do cliente atualizado!")
                    break

    def excluir_cliente(self):
        if len(self.lista_de_clientes) == 0:
            print("Nenhum cliente cadastrado!")
        else:
            excluir = input("Digite o ID ou o Nome do cliente: ")

            for e in self.lista_de_clientes:
                if str(e.id_unico) == excluir or e.nome.lower() == excluir.lower():
                    self.lista_de_clientes.remove(e)
                    print("Cadastro excluído!")
                    break

    
    def cadastrar_quarto(self):
        numero = input("Digite o nº do quarto: ")
        tipo = input("Digite a categoria do quarto: ")
        preco = float(input("Digite o valor da diária do quarto: "))

        novo_quarto = quarto(numero=numero, tipo=tipo, preco_diaria=preco)
        self.lista_de_quartos.append(novo_quarto)
        print("Novo quarto cadastrado!")

    def listar_quartos(self):
        if len(self.lista_de_quartos) == 0:
            print("Nenhum quarto cadastrado.")
        else:
            for e in self.lista_de_quartos:
               if e.disponivel == True:
                print(f"Quarto: {e.numero} | Tipo: {e.tipo} | Diária: R${e.preco_diaria} | Status: Disponível")
               else:
                print(f"Quarto: {e.numero} | Tipo: {e.tipo} | Diária: R${e.preco_diaria} | Status: Ocupado") 

    def editar_quarto(self):
        if len(self.lista_de_quartos) == 0:
            print("Nenhum quarto cadastrado.")
        else:
            pesquisa_editar = input("Digite o nº do quarto que deseja editar: ")

            for e in self.lista_de_quartos:
                if e.numero == pesquisa_editar:
                    edicao = input("Digite a opção que deseja editar: 1. Tipo - 2. Preço da Diária - 3. Número do Quarto - 4. Cadastro Completo: ")
                    match edicao:
                        case "1":
                            e.tipo = input("Digite a nova categoria do quarto: ")
                        case "2":
                            e.preco_diaria = float(input("Digite o novo valor da diária: "))
                        case "3":
                            e.numero = input("Digite o novo nº do quarto: ")
                        case "4":
                            e.tipo = input("Digite a nova categoria do quarto: ")
                            e.preco_diaria = float(input("Digite o novo valor da diária: "))

                    print("Cadastro do quarto atualizado!")
                    break   

    def excluir_quarto(self):
        if len(self.lista_de_quartos) == 0:
            print("Nenhum quarto cadastrado!")
        else:
            excluir = input("Digite o número do quarto que deseja excluir: ")

            for e in self.lista_de_quartos:
                if e.numero == excluir:
                    self.lista_de_quartos.remove(e)
                    print("Quarto excluído!")
                    break


    def criar_reserva(self):
        if len(self.lista_de_clientes) == 0 or len(self.lista_de_quartos) == 0:
            print("Cliente ou quarto não cadastrado. Tente novamente informando os dados!")
        else:
            id_cliente = input("Digite o ID do cliente: ")
            
            cliente_encontrado = [e for e in self.lista_de_clientes if str(e.id_unico) == id_cliente]
            if len(cliente_encontrado) == 0:
                print("Cliente não encontrado!")
                opcao = input("Deseja cadastrar esse cliente? (S/N): ")
                if opcao.lower() == 's':
                    self.cadastrar_cliente()
                else:
                    print("Não foi possível finalizar a reserva.")
                return 

            quarto_busca = input("Digite o nº do quarto a ser reservado: ")
            quarto_encontrado = [e for e in self.lista_de_quartos if e.numero == quarto_busca]

            if len(quarto_encontrado) == 0:
                print("Quarto não encontrado!")

            print(f"--- Verificar disponibilidade {quarto_busca} ---")
            entrada = input("Digite a data de check-in (DD/MM/AAAA): ")
            saida = input("Digite a data de check-out (DD/MM/AAAA): ")

            conflito_datas = False
            for e in self.numero_de_reservas:
                if e.quarto.numero == quarto_busca:
                    if entrada == e.data_entrada or saida == e.data_saida:
                        conflito_datas = True
                        break

            if conflito_datas == True:
                print(f"O quarto {quarto_busca} já está ocupado neste período!")
            else:
                nova_reserva = reserva(
                    id_reserva=self.id_unico_cliente, 
                    cliente=cliente_encontrado[0], 
                    quarto=quarto_encontrado[0], 
                    data_entrada=entrada, 
                    data_saida=saida
                )
                self.numero_de_reservas.append(nova_reserva)
                print("Reserva realizada com sucesso!")

    def listar_reservas(self):
        if len(self.numero_de_reservas) == 0:
            print("Nenhuma reserva encontrada!")
        else:
            for e in self.numero_de_reservas:
               print(f"Reserva ID: {e.id_reserva} | Cliente: {e.cliente.nome} | Quarto: {e.quarto.numero} | Dias: {e.quantidade_dias} | Total: R${e.valor_total}") 
    
    def editar_reserva(self):
        if len(self.numero_de_reservas) == 0:
            print("Nenhuma reserva encontrada!")
        else:
            pesquisa_editar = input("Digite o ID da reserva que deseja editar: ")

            for e in self.numero_de_reservas:
                if str(e.id_reserva) == pesquisa_editar:
                    edicao = input("Digite a opção que deseja editar: 1. Data de Entrada - 2. Data de Saída - 3. Período Completo: ")
                    match edicao:
                        case "1":
                            e.data_entrada = input("Digite a nova data de entrada (DD/MM/AAAA): ")
                        case "2":
                            e.data_saida = input("Digite a nova data de saída (DD/MM/AAAA): ")
                        case "3":
                            e.data_entrada = input("Digite a nova data de entrada (DD/MM/AAAA): ")
                            e.data_saida = input("Digite a nova data de saída (DD/MM/AAAA): ")

                    print("Reserva atualizada com sucesso!")
                    break

    def verificar_disponibilidade(self):
        if len(self.lista_de_quartos) == 0:
            print("Nenhum quarto cadastrado no sistema!")
            return

        def formatar_data(data_str):
            partes = data_str.split('/')
            return partes[2] + partes[1] + partes[0]

        print("--- CONSULTAR DISPONIBILIDADE ---")
        print("1. Ver todas as datas disponíveis de um Quarto X")
        print("2. Ver quais quartos estão disponíveis em um Período X")
        
        escolha = input("Digite o número da opção desejada (1 ou 2): ")

        match escolha:
            case "1":
                num_quarto = input("Digite o nº do quarto que deseja verificar a disponibilidade: ")
                quarto_existe = [e for e in self.lista_de_quartos if e.numero == num_quarto]
                
                if len(quarto_existe) == 0:
                    print("Quarto não encontrado!")
                else:
                    reservas_quarto = [e for e in self.numero_de_reservas if e.quarto.numero == num_quarto]
                    
                    if len(reservas_quarto) == 0:
                        print(f"O quarto {num_quarto} não possui reservas no momento.")
                    else:
                        def ver_data_crescente(res):
                            partes = res.data_entrada.split('/')
                            return partes[2] + partes[1] + partes[0]
                        
                        reservas_ordenadas = sorted(reservas_quarto, key=ver_data_crescente)
                        print(f"--- Datas Disponíveis {num_quarto} ---")
                        
                        for i in range(len(reservas_ordenadas) - 1):
                            fim_reserva_atual = reservas_ordenadas[i].data_saida
                            inicio_proxima_reserva = reservas_ordenadas[i+1].data_entrada
                            
                            if fim_reserva_atual != inicio_proxima_reserva:
                                print(f"• Disponível de {fim_reserva_atual} até {inicio_proxima_reserva}")
                        
                        print(f"• Disponível: De {reservas_ordenadas[-1].data_saida} em diante (Sem limite)")

            case "2":
                print("\n--- Pesquisar por Período ---")
                entrada_busca = formatar_data(input("Digite a data de entrada (DD/MM/AAAA): "))
                saida_busca = formatar_data(input("Digite a data de saída (DD/MM/AAAA): "))
                
                print(f"\n--- Quartos DISPONÍVEIS no período selecionado ---")
                quarto_disponivel = False
                
                for q in self.lista_de_quartos:
                    ocupado = False
                    
                    for r in self.numero_de_reservas:
                        if r.quarto.numero == q.numero:
                            reserva_entrada = formatar_data(r.data_entrada)
                            reserva_saida = formatar_data(r.data_saida)
                            
                            if entrada_busca < reserva_saida and saida_busca > reserva_entrada:
                                ocupado = True
                                break
                    
                    if ocupado == False:
                        print(f"Quarto: {q.numero} | Tipo: {q.tipo} | Diária: R${q.preco_diaria}")
                        quarto_disponivel = True
                
                if quarto_disponivel == False:
                    print("Sem quartos disponíveis no período escolhido. Selecione outra data")
            
            case _:
                print("Opção inválida!")