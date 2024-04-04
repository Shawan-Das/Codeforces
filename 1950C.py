for _ in range(int(input())):
    form = input()
    hh, mm = map(int, form.split(':'))
    
    if hh == 0:
        time = f"12:{mm:02d} AM"
    elif hh == 12:
        time = f"{hh:02d}:{mm:02d} PM"
    elif hh < 12:
        time = f"{hh:02d}:{mm:02d} AM"
    else:
        time = f"{hh-12:02d}:{mm:02d} PM"
    
    print(time)
