import os

cmd = 'mode 30,40'
os.system(cmd)

while True:

    try:
        c1 = float(input("\n\n\nINPUT C1 Value: "))
        if c1 <= 2.92:
            print("This C1 Value is small. Make sure it satisfies your minimum C1 according to fy:")
            print("""
fy = 500 \n>> C1_min = 2.92
fy = 420 \n>> C1_min = 2.86
fy = 400 \n>> C1_min = 2.83
fy = 350 \n>> C1_min = 2.75
fy = 240 \n>> C1_min = 2.65
            
            """)
        try:
            r = 1/c1**2
            c_d = 1.25 * (1 - (1 - 4.48*r) ** 0.5)
            j = (1-0.4*c_d)/1.15

            print("\nR= {:.4f}".format(r))
            print("\nc/d= {:.4f}".format(c_d))

            if j > 0.826:
                j = 0.826
                print("\nc/d is less than code minimum!")
            print("\nJ= {:.4f}".format(j))
        except: print("\nC1 value too small!")

    except: print("BAD INPUT")