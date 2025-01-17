successful = False

for number in range(3):
    print("Winter Is Coming")
    if successful:
        print("Successful")
        break
else:
    print("Sent 3 times and failed")

# `break`: To terminate the loop earlier
# `else`: Only run if the loop completes without an early exit
