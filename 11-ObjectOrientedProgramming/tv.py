# tv.py file
# class definition
class TV:
   def __init__(self):
      self.is_on = False
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def show_status(self):
       if self.is_on == False:
            status = "TV is off"
       elif self.is_on == False:
            status = "TV is on"
       return status

        