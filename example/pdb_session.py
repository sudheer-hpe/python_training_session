def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def main():
    x = 5
    y = 10

    # Set a breakpoint here
    import pdb
    pdb.set_trace()

    sum_result = add(x, y)
    product_result = multiply(x, y)

    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")


if __name__ == "__main__":
    main()
