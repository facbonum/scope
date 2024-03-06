name = "Dave"
count = 1

# def greeting(name): # global scope
#     color = "blue"
#     print(color)
#     print(name)
# greeting("John")

# def another():
#     greeting("Dave") # printed from a global scope function
# another()

def another():
    color = "blue"
    global count
    count = 5 # without global <var>, this creates another variable, not reassigning the global var
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("Dave")
another()