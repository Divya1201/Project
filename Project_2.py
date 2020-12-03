# creating a file of physics formulas
print("""
       ___ _           _         ___                  _         
 | _ \ |_ _  _ __(_)__ ___ | __|__ _ _ _ __ _  _| |__ _ ___
 |  _/ ' \ || (_-< / _(_-< | _/ _ \ '_| '  \ || | / _` (_-<
 |_| |_||_\_, /__/_\__/__/ |_|\___/_| |_|_|_\_,_|_\__,_/__/
          |__/                                           """)
another = 'Yes'
while another == 'Yes':
    print("What do you want to calculate:\n 1)Speed\n2)Acceleration\n3)Force\n4)Power\n5)Resistance\n6)Heat")
    num = int(input("Give the number before formula u want to calculate:  "))
    if num == 1:
        print("""You select:\n
        _____                     _ 
        /  ___|                   | |
        \ `--. _ __   ___  ___  __| |
         `--. | '_ \ / _ \/ _ \/ _` |
        /\__/ | |_) |  __|  __| (_| |
        \____/| .__/ \___|\___|\__,_|
              | |                    
              |_|                    """)
        distance = float(input("Give distance(in m): "))
        time = float(input("Give time(in sec): "))
        speed = distance / time
        print(f"Speed calculated is {speed} m/sec")
    elif num == 2:
        print("""You select:\n
              ___               _                _   _             
         / _ \             | |              | | (_)            
        / /_\ \ ___ ___ ___| | ___ _ __ __ _| |_ _  ___  _ __  
        |  _  |/ __/ __/ _ | |/ _ | '__/ _` | __| |/ _ \| '_ \ 
        | | | | (_| (_|  __| |  __| | | (_| | |_| | (_) | | | |
        \_| |_/\___\___\___|_|\___|_|  \__,_|\__|_|\___/|_| |_|

                                                               """)
        velocity = float(input("Give velocity(in m/s): "))
        time = float(input("Give time(in s): "))
        acc = velocity / time
        print(f"Acceleration calculated is {acc} m/s2")
    elif num == 3:
        print("""You select:\n
            ______                 
        |  ___|                
        | |_ ___  _ __ ___ ___ 
        |  _/ _ \| '__/ __/ _ \
        | || (_) | | | (_|  __/
        \_| \___/|_|  \___\___|""")
        mass = float(input("Give mass(in kg): "))
        acc = float(input("Give acceleraton(in m/s2): "))
        force = mass * acc
        print(f"Calculated force is {force} N")
    elif num == 4:
        print("""You select:\n
            ______                      
        | ___ \                     
        | |_/ _____      _____ _ __ 
        |  __/ _ \ \ /\ / / _ | '__|
        | | | (_) \ V  V |  __| |   
        \_|  \___/ \_/\_/ \___|_|   
                                    """)
        work = float(input("Give work done(in J): "))
        time = float(input("Give time(in s): "))
        power = work / time
        print(f"Power calculated is {power} watt")
    elif num == 5:
        print("""You select:\n
                     ______         _     _                       
        | ___ \       (_)   | |                      
        | |_/ /___ ___ _ ___| |_ __ _ _ __   ___ ___ 
        |    // _ / __| / __| __/ _` | '_ \ / __/ _ \
        | |\ |  __\__ | \__ | || (_| | | | | (_|  __/
        \_| \_\___|___|_|___/\__\__,_|_| |_|\___\___|
                                                      """)
        voltage = float(input("Give voltage applied(in V): "))
        current = float(input("Give current(in ampere): "))
        r = voltage / current
        print(f"Resistance calculated is {r} ohms")
    else:
        print("""You select:\n 
             _   _            _   
        | | | |          | |  
        | |_| | ___  __ _| |_ 
        |  _  |/ _ \/ _` | __|
        | | | |  __| (_| | |_ 
        \_| |_/\___|\__,_|\__|
                              """)
        current = float(input("Give current(in ampere): "))
        resistance = float(input("Give resistance(in ohms): "))
        time = float(input("Give time(in s): "))
        heat = (current ** 2) * resistance * time
        print(f"Calculated heat is {heat} J")
    another = input("Do You want to calculate another formula(Yes/No): ")
    if another == 'No':
        print("Thanks")
        break