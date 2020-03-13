#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

# def hash_table_insert(hash_table, key, value):
#     index = hash(key, len(hash_table.storage))
#
#     current_pair = hash_table.storage[index]
#     last_pair = None
#
#     while current_pair is not None and current_pair.key != key:
#         last_pair = current_pair
#         current_pair = last_pair.next
#
#     if current_pair is not None:
#         current_pair.value = value
#     else:
#         new_pair = LinkedPair(key, value)
#         new_pair.next = hash_table.storage[index]
#         hash_table.storage[index] = new_pair

    # Variable to keep track of the destination
    destination = None

    # The ticket for your first flight has a destination with a `source` of `NONE`
    # Therefore find the ticket with NONE
    for ticket in tickets:
        if ticket.source == "NONE":
            destination = ticket.destination
        # Add all the tickets into the hash_table
        hash_table_insert(hashtable, ticket.source, ticket.destination)

# def hash_table_retrieve(hash_table, key):
#     index = hash(key, len(hash_table.storage))
#
#     current_pair = hash_table.storage[index]
#
#     while current_pair is not None:
#         if(current_pair.key == key):
#             return current_pair.value
#         current_pair = current_pair.next

    # Add the new destiantion of each ticket to the route.
    for i in range(len(tickets)):
        route[i] = destination
        destination = hash_table_retrieve(hashtable, destination)

    return route[:-1]
