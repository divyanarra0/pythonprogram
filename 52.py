def switch11_demo(argument):
    switcher1 = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    print switcher1.get(argument, "Invalid Input")
a=int(raw_input())
switch11_demo(a)
