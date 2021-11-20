while True:

    try:
        c1 = float(input("\n\nINPUT C1 Value: "))
        try:
            r = 1/c1**2
            c_d = 1.25 * (1 - (1 - 4.48*r) ** 0.5)
            j = (1-0.4*c_d)/1.15

            print("\nR= {:.4f}".format(r))
            print("\nc/d= {:.4f}".format(c_d))

            if j > 0.826: j = 0.826
            print("\nJ= {:.4f}".format(j))
        except: print("\nC1 value too small!")

    except: print("BAD INPUT")