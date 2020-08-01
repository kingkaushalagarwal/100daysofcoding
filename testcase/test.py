import sys
# from testInput import input,input2
def main():
    # Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
    # Print your final output to console. Do not redirect to another file.
    # E.g. Suppose the question is to print the content of a file.
    #	Your solution should be 'os.system("cat input")'(without single quotes) instead of 'os.system("cat input > output")'. That's it!
    # Your code starts from here...
    l = list(sys.stdin.read().split('\n'))
    for i in range(len(l)):
        l[i]=list(l[i].split(','))
        l[i][6]="+"+l[i][4]+"-"+l[i][6]
        for j in range(len(l[i])-1):
            if j==4:
                continue
            print(l[i][j],end=",")
        print(l[i][-1])

    return 0

if __name__ == '__main__':
    main()
