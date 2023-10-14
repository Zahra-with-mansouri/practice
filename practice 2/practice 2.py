def dictionary_function():
    my_dict = {"a": 1, "b": 2, "c": 3}
    print("Before deletion:", my_dict)

    if "b" in my_dict:
        del my_dict["b"]

    print("After deletion:", my_dict)


def list_function():
    my_list = [1, 2, 3, 4, 5]
    print("Before deletion:", my_list)

    if len(my_list) > 1:
        del my_list[1]

    print("After deletion:", my_list)


def tuple_function():
    my_tuple = (1, 2, 3, 4, 5)
    print("Before deletion:", my_tuple)

  delete an element.
    the element, and then convert it back to a tuple.
    temp_list = list(my_tuple)
    if len(temp_list) > 1:
        del temp_list[1]

    my_tuple = tuple(temp_list)

    print("After deletion:", my_tuple)

dictionary_function()
list_function()
tuple_function()
