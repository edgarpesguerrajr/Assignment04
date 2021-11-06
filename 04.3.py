def FirstGroup():
    MoneyMoney = int(input('ENTER YOUR AVAILABLE MONEY: '))
    PricePrice = int(input('ENTER YOUR DESIRED PRICE OF AN APPLE: '))
    return MoneyMoney, PricePrice

def SecondGroup(Money1, Price1):
    TotalTotal = (Money1 // Price1)
    return TotalTotal

def ThirdGroup(Price1, Total1):
    AmountAmount = (Price1 * Total1)
    return AmountAmount

def FourthGroup(Money1, Amount1):
    ChangeChange = (Money1 - Amount1)
    return ChangeChange

def FinalOutput(Total1, Change1):
    print (f'You can buy {Total1} apples and your change is {Change1} pesos.')

Money, Price = FirstGroup()
Total = SecondGroup(Money, Price)
Amount = ThirdGroup(Price, Total)
Change = FourthGroup (Money, Amount)
FinalOutput (Total, Change)