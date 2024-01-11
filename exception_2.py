#write a python program that prompts the user to input an integer and raises a valueError exception if the input is not a valid integer
def exp_program(value):
    try: 
      a=int(input(value))
    except ValueError:
       print("Error : Invalid input,input a valid integer")

exp_program("abc")