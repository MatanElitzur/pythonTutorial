# two possiable approches
import random


def first_approch(oreders):
    fl = []
    for o in oreders:
        if o > 100:
            fl.append(o * 2)

def second_approch_list_comprehension(oreders): # List comprehension
    # List very flexible
    # List iterate many times
    # List access any items
    # List high memory usage
    lc = [ o * 2 for o in oreders if o> 100]

def thired_approch_generator_comprehension(oreders): # Generator comprehension expression
    # Generator less flexible
    # Generator allow only once to iterate on its items
    # Generator has a very low memory usage
    # Generator access only next item
    gn = (o * 2 for o in oreders if o > 100)

def main():
    oreders = [random.randint(0, 100) for _ in range(100_000)]  # Items to process
    first_approch(oreders)
    second_approch_list_comprehension(oreders)
    thired_approch_generator_comprehension(oreders)

main()