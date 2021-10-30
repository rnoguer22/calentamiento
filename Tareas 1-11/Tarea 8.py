def bitcoinToEuros (bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros

    if euros_value < 30000:
        print ("Cushaaaa que el bitcoin esta por debajo de 30k !!!")
    else:
        print ("Todo bien, no tiene por que preocuparse")
    
    return euros_value

bitcoinToEuros (1, 25000)