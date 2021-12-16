from github import Github


token = "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"

g = Github(token)
user = g.get_user("fuwiak")

for repo in user.get_repos():
    print(repo)