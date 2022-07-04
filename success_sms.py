# import required module
import requests
import json

# mention url
url = "https://www.fast2sms.com/dev/bulkV2"
  
  
# create a dictionary
my_data = {
     # Your default Sender ID
    'sender_id': 'FSTSMS', 
    
     # Put your message here!
    'message': 'Dear Customer,\n Your bank locker was accessed. If you did not do it please contact your bank.', 
    
    'language': 'english',
    'route': 'v3',
    
    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': {7234086699, 7456090902, 8127410947}   
}
  
# create a dictionary
headers = {
"authorization":"YF67Xsq1BKufv3zgpMyPDwb8Z4WOxJr0tInCVTmRSo9eQHAckEDg3qKi54mrRZ8tosFuecTUvVIYQAl6",
"Content-Type":"application/x-www-form-urlencoded",
'Cache-Control': "no-cache"

}


# make a post request
response = requests.request("POST",
                            url = url,
                            data = my_data,
                            headers = headers)


#returned_msg = json.loads(response.text)
  
# print the send message
print(response.text)