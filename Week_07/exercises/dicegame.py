import time
    import random

    # Trials
    for i in range(1, 100, 1):
        
        # Generates a random number from 1 and 6
        no = random.randint(1,6)
        
        if no == 1:
            print("┌─────────┐")
            print("│         │")
            print("│    ●    │")
            print("│         │")
            print("└─────────┘")
        if no == 2:
            print("┌─────────┐")
            print("│  ●      │")
            print("│         │")
            print("│      ●  │")
            print("└─────────┘")
        if no == 3:
            print("┌─────────┐")
            print("│  ●      │")
            print("│    ●    │")
            print("│      ●  │")
            print("└─────────┘")
        if no == 4:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│         │")
            print("│  ●   ●  │")
            print("└─────────┘")
        if no == 5:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│    ●    │")
            print("│  ●   ●  │")
            print("└─────────┘")
        if no == 6:
            print("┌─────────┐")
            print("│  ●   ●  │")
            print("│  ●   ●  │")
            print("│  ●   ●  │")
            print("└─────────┘")

        # Wait until the next trial
        time.sleep(0.25)
