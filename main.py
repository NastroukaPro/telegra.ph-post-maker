import requests
import json

print('Hello and welcome!')
while True:
    print('Do you have a account at telegra.ph?')
    haveacccount = input("Enter Yes/No:")

    if haveacccount == 'Yes' or haveacccount == 'Y' or  haveacccount =='yes':
        token = input("Please enter the account token:")
        break

    elif haveacccount == 'No' or haveacccount == 'n' or  haveacccount == 'no':
        newusername = input("Please enter your desaired username:")

        print('The short name is displayed to the you above the "Edit/Publish"')
        print("button on Telegra.ph, other users don't see this name.")

        newshortname = input("Please enter your desaired short name username:")

        serverreply = requests.get(f'https://api.telegra.ph/createAccount?short_name={newshortname}_name={newusername}')

        parsedserverreply = json.loads(serverreply.text)

        dpsr = parsedserverreply["result"]

        token = dpsr["access_token"]

        break

    else:
        print('You have enterted unpredicked answer,')
        print('psease try again.')


Pagetitle = input('Enter the title for the page:')

print('Enter the content of the page:')
pageconten = input('')

pageserverresponse = requests.get(f'https://api.telegra.ph/createPage?access_token={token}&title={Pagetitle}&content=[{pageconten}]')

print(pageserverresponse.text)