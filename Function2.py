def create_record(name, phone, adress):
    record = {
        'name':name,
        'phone':phone,
        'adress':adress,
    }
    return record


user1 = create_record("Vasya", "+30675321231","Lvov" )
print(user1)

def awards(medal, *persons):
    for person in persons:
        print("Mr " + person.title() + " got medal " +medal)


awards("Gold", "mike", "petro", "sergio")
awards("Bronze", "stepan", "Dima", "Oleg", "Kostya")