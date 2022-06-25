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
    """quartile 1"""
    q1, q2, q3 = 1, 2, 3
    
    q = q1*(x+1)
    q = float(q / 4)
    q = int(q)
    print(f"Q1 = {data[q-1:q]}")

    q = q2*(x+1)
    q = float(q / 4)
    q = int(q)
    print(f"Q2 = {data[q-1:q]}")
    
    q = q3*(x+1)
    q = float(q / 4)
    q = int(q)
    print(f"Q3 = {data[q-1:q]}")
    

get_input()
calculate()


