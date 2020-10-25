#!/usr/bin/env python


scriptName = "printComments"
scriptVersion = "0.1"


from argparse import ArgumentParser as argparseArgumentParser, SUPPRESS as argparseSUPPRESS
import library


def returnArgumentParser():
    argumentParser = argparseArgumentParser(add_help = False, description = "Locks posts created between two dates.")
    required = argumentParser.add_argument_group('required arguments')
    required.add_argument("-i", "--clientId", required = True, help = "https://www.reddit.com/prefs/apps")
    required.add_argument("-s", "--clientSecret", required = True, help = "https://www.reddit.com/prefs/apps")
    required.add_argument("-u", "--userName", required = True, help = "The name of your Reddit account.")
    required.add_argument("-r", "--subredditName", required = True, help = "e.g.: AskReddit")
    required.add_argument("-t", "--timespan", nargs = 2, required = True, metavar = "DATE", help = 'e.g.: -t "2020-01-13 13:31" "2020-01-14 13:31"')
    required.add_argument("-d", "--delta", type = int, required = True, help = 'The difference between post creation date and comment creation date or comment edit date. Needed to determine if a comment is "new" in relation to its post. E.g. 7 days (60*60*24*7): 604800')
    optional = argumentParser.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help', action = 'help', default = argparseSUPPRESS, help='show this help message and exit')
    return argumentParser


def printNewCommentUrls(post, deltaS):
    postDate = post.created_utc
    postUrl = None # *1 only set in case it's needed (- to minimize requests)

    for comment in post.comments.list():
        commentDate = comment.edited # either False or unix timestamp (e.g. 1603469757.0)

        if not commentDate:
            commentDate = comment.created_utc

        if commentDate - postDate > deltaS:
            if not postUrl: # *1
                postUrl = post.url
                
            print(postUrl + comment.id)
  

if __name__ == "__main__":
    argumentParser = returnArgumentParser()
    arguments = argumentParser.parse_args()
    api = library.returnPsawPushshiftApi(
        arguments.clientId,
        arguments.clientSecret,
        library.returnUserAgent(scriptName, scriptVersion, arguments.userName)
    )
    timestamps = sorted(map(library.returnUtcS, arguments.timespan))

    for post in api.search_submissions(
        after = timestamps[0],
        before = timestamps[-1],
        subreddit = arguments.subredditName
    ):
        printNewCommentUrls(post, arguments.delta)

