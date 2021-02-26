import datetime as dt


class Position:
    # positions: {name, purchase_date, purchase_price, current_price, gain/loss}
    def __init__(self, name, purchase_date, purchase_price, amount=1, current_price=0.0):
        self.name = name
        self.purchase_date = purchase_date
        self.purchase_price = float(purchase_price)
        self.amount = amount
        self.current_price = current_price
        self.net = 0

        if self.current_price:
            self.net = self.current_price - self.purchase_price

    def __str__(self):
        net = round(self.net, 2) * self.amount
        if net < 0:
            net = f'-${net * -1}'
        else:
            net = f'${net}'

        return f'{self.name.upper()} | {self.purchase_date}' \
               f'\nPurchase: {self.purchase_price} | Current: {self.current_price}' \
               f'\nAmount: {self.amount}\,Current Profit: {net}\n'


class Ledger:
    def __init__(self):
        self.transactions = []

    def purchase(self, symbol_name=str, symbol_price=float, amount=1):
        entry = Position(symbol_name, dt.date.today(), symbol_price, amount)
        print(f'Purchsed:\n{entry}')
        self.transactions.append({'name': entry.name, 'purchase_date': entry.purchase_date,
                                  'purchase_price': entry.purchase_price, 'amount': entry.amount})
        return entry


class Portfolio:
    def __init__(self):
        self.positions = []

    def alter_positions(self, position_data):
        for position in self.positions:
            if position.name == position_data.name:
                position.avg_purchase_price = (position.avg_purchase_price + position_data.purchase_price) / 2
                position.amount = position.amount + position_data.amount
                position.net = position.current_price * position.amount - position.current_price * position.amount
            else:
                self.positions.append(position_data)
        print(self.positions)


if __name__ == "__main__":
    ledge = Ledger()
    ledge.purchase('tqqq', 123.24)
    ledge.purchase('tqqq', 121.01)
    print('\n')
    print(ledge.transactions)
