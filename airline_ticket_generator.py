def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    src = source[:3]
    dest = destination[:3]

    for number in range(101, 101 + no_of_passengers):
        ticket = airline + ":" + src + ":" + dest + ":" + str(number)
        ticket_number_list.append(ticket)

    return ticket_number_list[-5:]


print(generate_ticket("AL1", "Chennai", "Mumbai", 7))
print(generate_ticket("AL1", "Bangalore", "London", 3))
