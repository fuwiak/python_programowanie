from github import Github

#dir, help


# token = "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"
#
# g = Github(token)
# user = g.get_user("fuwiak")
#
# for repo in user.get_repos():
#     print(repo)


#paramiko, netmiko, postgres

import requests

URL = 'https://www.tekstowo.pl/piosenki_artysty,bracia_figo_fagot.html'

page = requests.get(URL) #jak wylaczyc ssl

