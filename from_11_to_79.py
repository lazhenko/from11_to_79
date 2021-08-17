def from_11_to_79():
    for num in range(11, 80):
        if num % 3 == 0 and num % 5 == 0:
            print(f"$$")
        elif num % 3 == 0 :
            print(f"$$@@")
        else:
            print(f"{num}")


from_11_to_79()