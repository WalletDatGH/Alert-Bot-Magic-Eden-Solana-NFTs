import http.client
import json
import time
import tkinter 
import threading
import requests

class MyTkApp(threading.Thread):     
    def __init__(self): 
        threading.Thread.__init__(self) 

        self.start() 
    def callback(self): 
        self.root.quit() 

    def run(self): 
        self.root=tkinter.Tk() 
        self.root.protocol("WM_DELETE_WINDOW", self.callback) 
        self.s = tkinter.StringVar()  
        l = tkinter.Label(self.root,textvariable=self.s) 
        l.pack() 
        self.root.geometry("500x200")
        self.root.title("NFTs Magic Eden Alert")
        self.root.iconbitmap('ico.ico')
        self.root.mainloop()

app = MyTkApp()

num = 0

while 1 > num:
    try:
        collection = "Your collection Name, y00ts FOR EXAMPLE"
        conn = http.client.HTTPSConnection("api-mainnet.magiceden.dev")
        payload = ''
        headers = {}
        conn.request("GET", "/v2/collections/" + collection + "/stats", payload, headers)
        res = conn.getresponse()
        data = res.read()
        jsondata = json.loads(data.decode("utf-8"))
        floorPrice = jsondata["floorPrice"]
        floorPSOL = floorPrice / 1000000000
        WantedPrice = 10
        
        
        if WantedPrice < floorPSOL:
            app.s.set('Price has dropped: ' + str(floorPSOL)) 
            botAPI = "Your API of BOT FATHER TELEGRAM"
            chatID = "CHAT ID, you can get here = https://api.telegram.org/botAPIKEY/getUpdates CHANGE API KEY FOR YOUR KEY"
            photo = "Link of your collection image"
            
            requests.post('https://api.telegram.org/bot' + botAPI + '/sendPhoto', data={'chat_id': chatID, 'photo': photo, 'parse_mode' : 'HTML'})
            
            chat1 = 'Your ' + collection + ' collection has dropped the price. Now cost ' + str(floorPSOL)
            requests.post('https://api.telegram.org/bot' + botAPI + '/sendMessage', data={'chat_id': chatID, 'text': chat1, 'parse_mode' : 'HTML'})
            
            num = 2
        else:
            app.s.set('Checking... Price: ' + str(floorPSOL))     
    except:
        app.s.set("Tried to stop, close the program to stop it.")
        pass
    
    time.sleep(0.5)

app.s.set("You must have the notification on your mobile, you can close this program.")
