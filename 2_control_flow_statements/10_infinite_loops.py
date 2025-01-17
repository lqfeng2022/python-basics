while True:
    command = input("> ")
    print("GOT ", command)
    # As long as we don't type the particular strings,
    #  this program is gonna run forever
    if command.lower() == "quit":
        break
