products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return get_product(code)[property]

def main():
    orders = {}

    #get orders
    while True:
        order = input("Input Order (code,quantity): ")
        if order == '/':
            break
        if order.split(',')[0] in orders:
            orders[order.split(',')[0]] += int(order.split(',')[1])
        elif order.split(',')[0] in products:
            orders[order.split(',')[0]] = int(order.split(',')[1])
        else:
            print('Invalid Input.')

    #sort orders
    sorted_orders = sorted(orders.items())

    #output orders
    with open('receipt.txt','w') as t:
        total = 0
        t.write('CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL')
        for o in sorted_orders:
            line = f'''
{o[0]}\t\t{get_property(o[0],'name')}\t\t{o[1]}\t\t\t\t{o[1]*get_property(o[0],'price')}'''
            total += o[1]*get_property(o[0],'price')
            t.write(line)
        t.write(f'\n\nTotal:\t\t\t\t\t\t\t\t\t\t{total}')

main()
