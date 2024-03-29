from elGamal import ElGamal


def main():
    # Create an ElGamal object with p = 257 and g = 3
    eg = ElGamal(257, 3, False)
    print()

    # Add users Alice, Bob, and Eve
    eg.add_user("Alice")
    eg.add_user("Bob")
    eg.add_user("Eve")

    # Print the status of the ElGamal object
    eg.print_status()
    print()

    # Send messages between users
    eg.receive_message("Bob", eg.send_message("Alice", "Bob", "Alice to Bob"))
    eg.receive_message("Alice", eg.send_message("Bob", "Alice", "Bob to Alice"))
    eg.receive_message("Eve", eg.send_message("Alice", "Eve", "Alice to Eve"))
    eg.receive_message("Eve", eg.send_message("Bob", "Eve", "Bob to Eve"))
    eg.receive_message("Alice", eg.send_message("Eve", "Alice", "Eve to Alice"))

    # Print the status of the ElGamal object
    eg.print_status()
    print()


if __name__ == "__main__":
    main()
