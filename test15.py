#Lesson 15 - Functions 2 

def create_record(name, telephone, address) :
    """"Create Record"""
    record = {
        'name' : name,
        'phone' : telephone,
        'address' : address
    }
    return record


user1 = create_record("Vasya", "+979846466546", "Tinussiya")
user2 = create_record("Petya", "+6456765462463", "Munisiya")

print(user1)
print(user2)    


def give_award(medal, *persons):
    """"Give Medals to persons"""
    for person in persons:
        print("Tovarich " + person.title() + " nagrajdaetsya madaliya " + medal)



give_award("Za Berlin", "vasya", "petya")
give_award("Za Berlin", "petya", "alexander", "valentin")