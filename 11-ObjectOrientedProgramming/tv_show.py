# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
    myTV = TV()

   # object usage
    myTV.turn_on()
    myTV.show_status()
    myTV.turn_off()

if __name__ == "__main__":
   main() 
