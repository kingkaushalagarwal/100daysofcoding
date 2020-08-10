from testInput import input
ll =[]
def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    global ll
    if position<=len(ll)+1:
        ll.insert(position-1,value)


def delete_node(position):
    # @param position, integer
    # @return an integer
    global ll
    if position<=len(ll):
        ll.pop(position-1)

def print_ll():
    # Output each element followed by a space
    global ll
    print(*ll)
ll =[]
def insert_node(position, value):
    # @param position, an integer
    # @param value, an integer
    global ll
    if position<=len(ll)+1:
        ll.insert(position-1,value)


def delete_node(position):
    # @param position, integer
    # @return an integer
    global ll
    if position<=len(ll):
        ll.pop(position-1)

def print_ll():
    # Output each element followed by a space
    global ll
    print(*ll)
def main():
    cases, position, value = 0, 0, 0
    cases = int(input())
    while (cases > 0):
        inp = input().split()
        ch = inp[0]
        if ch == 'i':
            position = int(inp[1])
            value = int(inp[2])
            insert_node(position, value)
        elif ch == 'd':
            position = int(inp[1])
            delete_node(position)
        elif ch == 'p':
            print_ll()
        else:
            print("Check your input")
        cases -= 1

if __name__ == '__main__':
    main()