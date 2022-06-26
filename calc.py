data = []

def get_input():
    
    global x
    print("\ntype the number one by one and press any letter to start computing\n")

    while True:
        try:
            n = int(input('enter a number: '))
            data.append(n)
           
        except:
            print("\ncalculating.....")
            x = len(data)
            print(data)
            break

def calculate():
    q1, q2, q3 = 1, 2, 3

#quartile 1 (Q1) 
    q = float(q1*(x+1))
    n_int = int(q / 4)
    n_float = float(q / 4)
#indexes
    n1 = float(data[n_int-1])
    n2 = float(data[n_int])
    z1 = n1 - n2
    dec = n_int - n_float
    q1 = n1 + (z1 * dec)
    print (q1)

#quartile 2 (Q2)
    q = float(q2*(x+1))
    n_int = int(q / 4)
    n_float = float(q / 4)
#indexes
    n1 = float(data[n_int-1])
    n2 = float(data[n_int])
    z1 = n1 - n2
    dec = n_int - n_float
    q2 = n1 + (z1 * dec)
    print (q2)

#quartile 3 (Q3)    
    q = float(q3*(x+1))
    n_int = int(q / 4)
    n_float = float(q / 4)
#indexes
    n1 = float(data[n_int-1])
    n2 = float(data[n_int])
    z1 = n1 - n2
    dec = n_int - n_float
    q3 = n1 + (z1 * dec)
    print (q3)

get_input()
calculate()


