class Phone:
      def __init__(self,volume,brightness):
            self.turned_on = True
            self.volume = volume
            self.brightness = brightness

      def turn_on(self):
            self.turned_on = True
      def turn_off(self):
            self.turned_on = False
      def display_info(self):
            print(f"Phone is turned on: {self.turned_on}")
            print(f"Phone volume: {self.volume}")
            print(f"Phone brightness: {self.brightness}")


def main():
    my_phone = Phone(30,100)
    
    my_phone.turn_on
    my_phone.display_info()
    my_phone.turn_off
    print("Turning off..")
    
if __name__ =="__main__":
    main()





    

