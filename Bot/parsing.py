import json



#pullrequest:created
author = request["actor"]
prTitle = request["pullrequest"]["title"]
prDescription = request["pullrequest"]["description"]
sourceBranch = request["pullrequest"]["source"]["branch"]["name"]
destBranch= request["pullrequest"]["destination"]["branch"]["name"]

prMessage = "Pull request {} created by {} from {} to {}. \nDescription: {}".format(prTitle, author, sourceBranch, destBranch, prDescription)


#repo:push
repo = request["Repository"]["name"]
branch = request["push"]["changes"]["new"]["name-of-branch"]
message = request["push"]["changes"]["new"]["name-of-branch"]["target"]["message"]
author = request["push"]["changes"]["new"]["target"]["author"]["user"]["display_name"]
message = request["push"]["changes"]["new"]["name-of-branch"]["target"]["parents"]["html"]["ref"]

pushMessage = "Push made on {} repo on {} branch by {}. \nMessage: {}".format(repo, branch, author, message)

