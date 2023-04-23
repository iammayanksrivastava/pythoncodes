def ask_for_int():

    while True: 
        try: 
            result = int(input("Please provide a number: "))
        
        except: 
            print('That is not a number ! Try again')
            continue
        else: 
            print('Thank you for your input')
            break
        finally:
            print('I always run !! Ukhaad le')


ask_for_int()