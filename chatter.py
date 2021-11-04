# Function is based off an example found in Stack Overflow

# Chatter imports
import time
import sys
from random import randrange


# List to hold chatter messages. Useful for repetitive phrases
npc_chatter = []


# Function
def chatter(npc_chatter):
    print()
    for c in npc_chatter:
        sys.stdout.write(c)
        sys.stdout.flush()
        secs = '0.00' + str(randrange(10,20,1))
        secs = float(secs)
        time.sleep(secs)
    print()
    time.sleep(1)
# `secs`: time between when characters print. '0.01' = 10 milliseconds.
# `str(randrange(10, 20, 1)`: adds an integer to `secs`, randomly chosen from the specified range.
# `randrange(start, stop, step)`:
    # `start`: lowest number in the range (default for function is 10).
    # `stop`: highest number in the range (default for function is 20).
    # `step`: incrementation of the index of range (default for function is 1).
        # If `step` = 2, `randrange()` will select from every second value in
        # the range [10, 12, 14, 16, 18, 20].
        # `step` cannot equal 0
# `time.sleep()` at the end: sets delay (in sec) before running the next script. This gives time for the reader to catch up during heavy dialog. Set to 0 for no delay.


# Function test. Function can print quoted text or one from the `npc_chatter` list
# Double-Tab to align text after line break (\n)
test_chatter = 'NPC: "This is a test to see if the function functions,\n      and it functions just fine, friend!"'
npc_chatter.append(test_chatter)
test_chatter2 = 'NPC: "Just so we\'re clear, have another test here!"'
npc_chatter.append(test_chatter2)
chatter(npc_chatter[0])
chatter(npc_chatter[1])


# Prompt user to toggle chatter on or off
chatter('Would you like to keep the "chatter" feature on?')
print('Or would you like to turn it off and have text print instantly?')
chatter_io = input('Disable chatter function? (y/n): ')
if chatter_io.lower() == 'y':
    def chatter(npc_chatter):
        print(npc_chatter)
    chatter('Chatter is disabled.')
else:
    pass