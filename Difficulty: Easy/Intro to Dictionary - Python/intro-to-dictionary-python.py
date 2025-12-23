# Function to create dictionary
# arr is list of tuple. tuple contain name and marks.


def create_dict(arr):

    dict = {}
    for name, marks in arr:
        dict[name] = marks

    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict

    return dict