# A program that supports customer service in an office
# Write a program that supports customer service in an office. 
# Use the queue. Each new customer receives a ticket with an 
# automatically assigned consecutive number and is added to the 
# end of the queue. The next customer to be served is taken from 
# the beginning of the queue.
import queue

customer_queue = queue.Queue()
ticket_number = 0

def add_customer():
    global ticket_number
    ticket_number += 1
    customer_queue.put(ticket_number)
    print('Customer',ticket_number)
    print()

def serve_customer():
    if customer_queue.empty():
        print('The queue is empty')
        print()
    else:
        current_customer = customer_queue.get(ticket_number)
        print('Serving customer',current_customer)
        print()

def display_queue():
    displayed = list(customer_queue.queue)
    print('The queue:',displayed)
    print()

while True:
    print("1. Add a customer")
    print("2. Serve a customer")
    print("3. Display queue")
    print("4. Exit")
    choice = input("Select an option: ")
    print()

    if choice == '1':
        add_customer()
    elif choice == '2':
        serve_customer()
    elif choice == '3':
        display_queue()
    elif choice == '4':
        break