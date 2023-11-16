import requests
import json
import webbrowser

print('Hello and welcome!')
while True:
    print('Do you have a account at telegra.ph?')
    haveacccount = input("Enter Yes/No:")

    if haveacccount == 'Yes' or haveacccount == 'Y' or  haveacccount =='yes':
        token = input("Please enter the account token:")

        jsaccname = requests.get(f'https://api.telegra.ph/getAccountInfo?access_token={token}&fields=["author_name"]')
        djsaccname = json.loads(jsaccname.text)
        tjsaccname = djsaccname['result']

        accname = tjsaccname['author_name']


        break

    elif haveacccount == 'No' or haveacccount == 'n' or  haveacccount == 'no':
        newusername = input("Please enter your desaired username:")


        newusername.replace(" ", "+")
        accname = newusername

        print('The short name is displayed to the you above the "Edit/Publish"')
        print("button on Telegra.ph, other users don't see this name.")

        newshortname = input("Please enter your desaired short name username:")

        newshortname.replace(" ", "+")

        serverreply = requests.get(f'https://api.telegra.ph/createAccount?short_name={newshortname}_name={newusername}')

        parsedserverreply = json.loads(serverreply.text)

        dpsr = parsedserverreply["result"]

        token = dpsr["access_token"]

        break

    else:
        print('You have enterted unpredicked answer,')
        print('psease try again.')


Pagetitle = input('Enter the title for the page:')
Pagetitle.replace(" ", "+")

print('Enter the content of the page:')
pageconten = input('')
pageconten.replace(" ", "+")

pagetemp1= '{"tag":"p","children":["'
pagetemp2 = '"]}'

pagetemp = (pagetemp1 + pageconten) + pagetemp2

pageserverresponse = requests.get(f'https://api.telegra.ph/createPage?access_token={token}&title={Pagetitle}&content=[{pagetemp}]&author_name={accname}')
print(pageserverresponse.text)
jsweblink = json.loads(pageserverresponse.text)
djsweblink = jsweblink["result"]
weblink = djsweblink["url"]

print ('Your webpage is created and it will open in a moment.')
print('link:')
print(weblink)

webbrowser.open(weblink)