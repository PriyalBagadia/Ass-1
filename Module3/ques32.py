# Write a Python script to sort (ascending and descending) a dictionary by value.

def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# Example usage:
my_dict = {'a': 100, 'b': 50, 'c': 200}
ascending_sorted = sort_dict_by_value(my_dict)
descending_sorted = sort_dict_by_value(my_dict, ascending=False)

print("Ascending sorted:", ascending_sorted)
print("Descending sorted:", descending_sorted)