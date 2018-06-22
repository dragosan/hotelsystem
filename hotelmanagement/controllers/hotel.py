
class Hotel:
    
    hotels=[]
    hotels_in_city=[]
    def __init__(self,number,hotel_name, city,total_rooms,empty_rooms):

        """ create an object of class Hotel and add it to the class variable list hotels"""
        self.number=number
        self.hotel_name=hotel_name
        self.city=city
        self.total_rooms=total_rooms
        self.empty_rooms=empty_rooms

        #Hotel.hotels.append([self.number,self.hotel_name,self.city,self.total_rooms,self.empty_rooms])
        Hotel.hotels.append(self)
        Hotel.hotels_in_city.append([self.hotel_name,self.city])


    @classmethod
    def list_hotels(cls):
        # search for city in hotels and print hotel name, total number of rooms if found
        #info=''
        #for hotel in Hotel.hotels:

            #info+="----------------------------\nhotel name : "+hotel[1]+"\nCity : "+hotel[2]+"\nnumber of rooms : "+str(hotel[4])+"\n----------------------------"
                                    
        return cls.hotels
    @classmethod
    def list_hotels_in_city(cls,city):
        # search for city in hotels and print hotel name, total number of rooms if found
        lst=[]
        #info='hotels in city of '+city+' : '

        for hotel in cls.hotels_in_city:
            if(hotel[1]==city):
                lst.append(hotel[0])
                #info+="\nhotel name : "+hotel[0]+"\n" """
        return lst
        


    def find_hotel(self):
        for hotel in Hotel.hotels:
            if(hotel[1]==self.hotel_name):
                return True
        else:
            return False


    def delete_hotel(self):
        for hotel in Hotel.hotels:
            if self.hotel_name in hotel:
                Hotel.hotels.remove(hotel)



    def display_name(self):
        return self.hotel_name

        


