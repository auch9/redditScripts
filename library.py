from datetime import datetime as datetimeDatetime, timezone as datetimeTimezone
from platform import system as platformSystem
from praw import Reddit as prawReddit
from psaw import PushshiftAPI as psawPushshiftApi


def returnUtcS(localDateString):
    return int(datetimeDatetime.strptime(localDateString, "%Y-%m-%d %H:%M").astimezone(datetimeTimezone.utc).timestamp())


def returnUserAgent(scriptName, scriptVersion, userName):
    return platformSystem() + ":local.script." + scriptName + ":" + scriptVersion + " (by u/" + userName + ")"


def returnPsawPushshiftApi(clientId, clientSecret, userAgent, userName = None, password = None):
    if userName and password:
        return psawPushshiftApi(prawReddit(
            client_id = clientId,
            client_secret = clientSecret,
            user_agent = userAgent,
            username = userName,
            password = password
        ))
    
    return psawPushshiftApi(prawReddit(
        client_id = clientId,
        client_secret = clientSecret,
        user_agent = userAgent
    ))

