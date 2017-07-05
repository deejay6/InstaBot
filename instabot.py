import requests
from termcolor import colored
from access_token import ACCESS_TOKEN
from user_detail import User, user_list
BASE_URL = 'https://api.instagram.com/v1/'

# Function retrieve owner's information


def self_info():
    print "Displaying Own Information"
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    try:
        owner_info = requests.get(request_url).json()
        if owner_info['meta']['code'] == 200:  # HTTP 200 means transmission is OK
            if len(owner_info['data']):
                print colored("Username: ", "red"), '%s' % colored(owner_info['data']['username'], "blue")
                print colored('Number of followers: ', "red"), '%s' % colored(owner_info['data']['counts']['followed_by'], "blue")
                print colored('Number of people you are following: ', "red"), '%s' % colored(owner_info['data']['counts']['follows'],
                                                                                             "blue")
                print colored('Number of posts: ', "red"), '%s' % colored(owner_info['data']['counts']['media'], "blue")
                print owner_info
            else:
                print 'User does not exist!'
        else:
            print 'Status code other than 200 received!'
    except:
        print "Something Wrong with the url"

# Function to add user using username and generate corresponding user id


def add_user():
    username = raw_input("Enter Username: ")
    try:
        request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (username, ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        user_info = requests.get(request_url).json()
        if user_info['meta']['code'] == 200:
            if len(user_info['data']):
                id = user_info['data'][0]['id']
                print id
                print user_info
                user_list.append(User(username, id))
        else:
            print "Status code not 200!"
    except:
        print "Url request exception occurred!"


def fetch_user_details():
    index = select_user()
    id = user_list[index].id
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    try:
        user_info = requests.get(request_url).json()
        if user_info['meta']['code'] == 200:  # HTTP 200 means transmission is OK
            if len(user_info['data']):
                print colored("Username: ", "red"), '%s' % colored(user_info['data']['username'], "blue")
                print colored("Bio: ", "red"), '%s' % colored(user_info['data']['bio'], "blue")
                print colored('Number of followers: ', "red"), '%s' % colored(user_info['data']['counts']['followed_by'], "blue")
                print colored('Number of people you are following: ', "red"), '%s' % colored(user_info['data']['counts']['follows'],
                                                                                             "blue")
                print colored('Number of posts: ', "red"), '%s' % colored(user_info['data']['counts']['media'], "blue")
                print user_info
            else:
                print 'User does not exist!'
        else:
            print 'Status code other than 200 received!'
    except:
        print "Something Wrong with the url"


def select_user():
    if not user_list:
        print 'Add Users Please'
    else:
        index = 1
        for i in range(0, len(user_list)):
            print '%d %s' % (index, user_list[i].name)
            index = index + 1
        while True:
            choice = raw_input("Enter Your Choice: ")
            try:
                choice = int(choice)
                break
            except:
                print colored("Enter Valid Choice", "red")
        choice = int(choice)
        return choice-1

self_info()
add_user()
fetch_user_details()