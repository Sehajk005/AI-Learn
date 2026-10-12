import requests
class IRCTC:
    
    def __init__(self):
        
        user_input = input("""How would you like to procede?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule
              """)

        if user_input == "1":
            self.train_status()
        elif user_input == "2":
            self.pnr()
        elif user_input == "3":
            self.train_schedule()
        else:
            print("Invalid input. Please try again.")
        
        def train_status(self):
            pass
        
        def pnr(self):
            pass
        
        def train_schedule(self):
            train_num = input("Enter train number: ")
            self.fetch_data(train_num)
            
        def fetch_data(self, train_num):
            data = requests.get(f"http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/{train_num}/")
            
            data = data.json()
            
            for i in data['Route']:
                print(i['StationName'], "|", i['ArrivalTime'], "|", i['DepartureTime'], "|", i['Distance'])

obj = IRCTC()                
            
            