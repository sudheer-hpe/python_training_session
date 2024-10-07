import sys

print(sys.path)


from import_statements import write_names


for name in ["Alice", "Bob", "Charlie"]:
    write_names(name)


# from <path/of/the/file> import <function_name>
