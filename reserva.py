from cliente import cliente
from quarto import quarto

class reserva:
  def __init__(self, cliente: cliente, quarto: quarto, data_checkin: str, data_checkout: str):
    self.cliente = cliente
    self.quarto = quarto
    self.data_checkin = data_checkin
    self.data_checkout = data_checkout