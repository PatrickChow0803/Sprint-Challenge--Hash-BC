#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

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
#
#
#
# def hash_table_retrieve(hash_table, key):
#     index = hash(key, len(hash_table.storage))
#
#     current_pair = hash_table.storage[index]
#
#     while current_pair is not None:
#         if(current_pair.key == key):
#             return current_pair.value
#         current_pair = current_pair.next

    for index in range(len(weights)):
                        # hash_table, Key, Value
        hash_table_insert(ht, weights[index], index)

    for index in range(len(weights)):
                                    # hash_table, key
        tempHash =  hash_table_retrieve(ht, limit-weights[index])
        if tempHash != None:
            return (max([index, tempHash]), min([index, tempHash]))

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
