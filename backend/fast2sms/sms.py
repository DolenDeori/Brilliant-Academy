url = "https://www.fast2sms.com/dev/bulkV2"

def send_it(message , number):
    my_data = {
    # Your default Sender ID
    'sender_id': '<senderID>', 

    # Put your message here!
    'message': message, 

    'language': 'english',
    'route': 'dlt',
    "flash" :"0",
    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': number
    }

    # create a dictionary
    headers = {
        'authorization': '',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    return my_data , headers
