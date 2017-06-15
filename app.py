from github import Github
from getpass import getpass

try:
    prompt = raw_input
except NameError:
    prompt =input

user ='rblack42'
password = ''

while not password:
    password= getpass('Password for{0}: '.format(user))

g = Github(user,password)

for repo in g.get_user().organizations():
    print(repo.name)
