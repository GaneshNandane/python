# Demonstrating the use of the break and continue statements with loops.

# In this loop, the range is from 0 to 99. When the value of i becomes 10, the break statement terminates the loop immediately, and the remaining iterations are not executed.
for i in range(0, 100):
    if i == 10:
        break
    print(i)

# In this loop, the range is from 0 to 99. When the value of i becomes 10, the continue statement skips the remaining statements in the current iteration and moves to the next iteration. The loop then continues executing until all iterations are completed.
for i in range(0, 100):
    if i == 10:
        continue
    print(i)
