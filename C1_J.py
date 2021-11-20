while True:
    try:
        c1 = float(input("\n\nINPUT C1 Value: "))
        print("\nJ= {:.4f}".format(1.25 * (1 - (1 - 3.2 * (1 / c1 ** 2)) ** 0.5)))

    except:
        print("BAD INPUT")