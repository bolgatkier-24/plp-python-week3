# The three bugs are:

# Missing : after the while condition.
# count < 5 stops before adding 5, so it needs to be count <= 5.
# The final print tries to concatenate a string and an integer; converting total to a string fixes that.



count = 1
total = 0

# BUG: The while statement was missing a colon at the end, so I added `:`.

# BUG: The condition stopped at 4, so I changed `< 5` to `<= 5` to include 5.

while count <= 5:
total = total + count
count = count + 1

# BUG: total is an integer, so I converted it to a string before joining it with the message.

print("Sum of 1 to 5 is: " + str(total))
