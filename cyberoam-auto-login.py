import requests
import sys

### ONE TIME SETUP ###
### Enter User Id (Roll Number)
user = 
### Enter Password
password = ""


url = "http://172.16.73.12:8090/httpclient.html"

# messages
success = "<?xml version='1.0' ?><requestresponse><status><![CDATA[LIVE]]></status><message><![CDATA[You have successfully logged in]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n"
dataexceed="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[Your data transfer has been exceeded, Please contact the administrator]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n"
maxlogin="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[You have reached Maximum Login Limit.]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse>\n"

def connect():
    values = {
        'mode': '191',
        'username': user,
        'password': password
    }
    r = requests.post(url, data=values)
    r = r.text
    flag = False
    # print(r)

    if(r == success):
        print("User: " + str(user) + " Logged In Successfully!!!")
    elif(r == dataexceed):
        print("User: " + str(user) + " Data Exceeded!!!")
    elif(r == maxlogin):
        print("User: " + str(user) + " Max Login!!!")
    else:
        print("User: " + str(user) + " Check Details!!!")

def logout():
    values = {
        'mode': '193',
        'username': user
    }
    r  = requests.post(url, data=values)
    print("Logged Out Successfully")

if __name__ == "__main__":
    command = sys.argv[1]
    if(command == 'login'):
        connect()
    if(command == 'logout'):
        logout()