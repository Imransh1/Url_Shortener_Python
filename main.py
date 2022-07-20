import requests
import webbrowser
from key import headers
short_url = input("Please Enter link to shorten: ")

def shortener():
    try:
        url = "https://url-shortener-service.p.rapidapi.com/shorten"
        payload = f"url={short_url}"
        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        url_data = res['result_url']
        return url_data
    except:
        x = 1
        return x
def redirect():
    rcd_data = shortener()
    if rcd_data == 1:
        print('Error Occured: Please enter a valid url')
    else:
        redirect_menu = int(input("""
            Operation Successful!

            1. Press 1 to Open Url In Browser: 
            2. Press 2 to Show shortened url 
            3. Press 3 to Exit
        \n"""))
        if redirect_menu == 1:
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(rcd_data)
        elif redirect_menu == 2:
            print(shortener())
        elif redirect_menu == 3:
            print('\nThank you for using Url shortener.')
            exit()
        else:
            print('Please choose correct option')
            redirect()

shortener()
redirect()
