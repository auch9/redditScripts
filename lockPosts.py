#!/usr/bin/env python


scriptName = "lockPosts"
scriptVersion = "0.1"


from argparse import ArgumentParser as argparseArgumentParser, SUPPRESS as argparseSUPPRESS
import library


def returnArgumentParser():
    argumentParser = argparseArgumentParser(add_help = False, description = "Locks posts created between two dates.")
    required = argumentParser.add_argument_group('required arguments')
    required.add_argument("-i", "--clientId", required = True, help = "https://www.reddit.com/prefs/apps")
    required.add_argument("-s", "--clientSecret", required = True, help = "https://www.reddit.com/prefs/apps")
    required.add_argument("-u", "--userName", required = True, help = "The name of your Reddit account.")
    required.add_argument("-p", "--password", required = True, help = "The password of your Reddit Account.")
    required.add_argument("-r", "--subredditName", required = True, help = "e.g.: AskReddit")
    required.add_argument("-t", "--timespan", nargs = 2, required = True, metavar = "DATE", help = 'e.g.: -t "2020-01-13 13:31" "2020-01-14 13:31"')
    optional = argumentParser.add_argument_group('optional arguments')
    optional.add_argument('-h', '--help', action = 'help', default = argparseSUPPRESS, help='show this help message and exit')
    return argumentParser


if __name__ == "__main__":
    argumentParser = returnArgumentParser()
    arguments = argumentParser.parse_args()
    userName = arguments.userName
    api = library.returnPsawPushshiftApi(
        arguments.clientId,
        arguments.clientSecret,
        library.returnUserAgent(scriptName, scriptVersion, userName),
        userName,
        arguments.password
    )
    timestamps = sorted(map(library.returnUtcS, arguments.timespan))

    for post in api.search_submissions(
        after = timestamps[0],
        before = timestamps[-1],
        subreddit = arguments.subredditName
    ):
        if post.locked or post.archived:
            continue

        post.mod.lock()

