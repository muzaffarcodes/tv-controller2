# Pult uchun Class
import time
import random
class Pult():
    def __init__(self,on_off='Off',volume=0,channel_list=['BBC','Netflix'],channel='Netflix'):
        print("Controller is working, bruuh...")
        self.tv_position = on_off
        self.tv_volume = volume
        self.channel_list = channel_list
        self.channel = channel
    def __str__(self):
        return "Controller Position: {}".format(self.tv_position)
    # Volume 
    def volumeUp_Down(self):
        while True:
            second = 5
            char = input("+ | - : ")
            if(char == '+'):
                if(self.tv_volume < 5):
                    self.tv_volume += 1
                    print("Volume+ : {}".format(self.tv_volume))
                    second = 5
                    continue
            elif(char == "-"):
                if(self.tv_volume > 0):
                    self.tv_volume -= 1
                    print("Volume- : {}".format(self.tv_volume))
                    second = 5
                    continue
            else:
                print("Volume Updating ended...")
                break
            for i in range(5):
                time.sleep(1)
                second -= 1
                print("Sabr...")
            if(second <= 0):
                print("...:...")
                break
    def tv_power(self):
        if(self.tv_position == "ON"):
            print("TV is switching off...")
            self.tv_position = "Off"
        else:
            print("TV is switching ON...")
            self.tv_position = "ON"
    def random_channel(self):
        random_channel = random.randint(0,len(self.channel_list)-1)
        self.channel = self.channel_list[random_channel]
    def add_channel(self,new_Channel):
        self.channel_list.append(new_Channel)
        print("New Channel Added Successfully!!!")
      
