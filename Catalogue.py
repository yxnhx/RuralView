import operator

database = []

def get_data():
    return database

def add_item(name, company, price, street_address, suburb, quantity, in_stock, medical):
    data = get_data()
    product = {
        "name": name,
        "company": company,
        "price": price,
        "street_address": street_address,
        "suburb": suburb,
        "quantity": quantity,
        "in-stock": in_stock, 
        "medical": medical,
    }
    if (data == []):
        new_suburb = create_suburb(suburb)
        new_suburb["catalogue"].append(product)
        data.append(new_suburb)
    else:
        for s in data:
            if s["name"] == suburb:
                s["catalogue"].append(product)
                break
    return product

def create_suburb(name):
    new_suburb = {
        "name": name,
        "nearby suburbs": [],
        "catalogue": [],
    }
    return new_suburb
    
def add_neighbour(target, neighbour, distance):
    # assume that target and neighbour exist in the database
    data = get_data()
    for suburb in data:
        if suburb["name"] == target:
            # does not check duplicates
            new = {
                "name": neighbour,
                "distance": distance,
            }
            suburb["nearby suburbs"].append(new)
            # sort by distance, ascending order
            suburb["nearby suburbs"].sort(key=operator.itemgetter('distance'))
        elif suburb["name"] == neighbour:
            new = {
                "name": target,
                "distance": distance,
            }
            suburb["nearby suburbs"].append(new)
            suburb["nearby suburbs"].sort(key=operator.itemgetter('distance'))

def sell(name, company, street_address, suburb, number):
    data = get_data()
    for suburb in data:
        if suburb["name"] == suburb:
            for item in suburb["catalogue"]:
                if item["name"] == name and item["company"] == company and item["street_address"] == street_address:
                    item["quantity"] -= number
                    if item["quantity"] == 0:
                        item["in-stock"] = False
                    break

def add_stock(name, company, street_address, suburb, number):
    data = get_data()
    for suburb in data:
        if suburb["name"] == suburb:
            for item in suburb["catalogue"]:
                if item["name"] == name and item["company"] == company and item["street_address"] == street_address:
                    item["quantity"] += number
                    break


