

def main():
    items = ['hello', 'world']
    s = items[0] + items[1] # Slow performance, very frirendly, Scalable
    s1 = f'{items[0]}{items[1]}' # Using the f-strings, Fast performance, friendly, not scalable
    s2 = ''.join(items) # The '' means that nothing will be added between the items, Fast performance, less friendly, Scalable

main()