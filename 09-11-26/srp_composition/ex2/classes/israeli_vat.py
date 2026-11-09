class IsraeliVat:
    VAT_RATE = 0.17
    def apply(self, amount):
        return amount + amount * IsraeliVat.VAT_RATE

    