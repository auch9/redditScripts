# redditScripts

## Installation

### Linux (Arch)
```shell
sudo pacman -S python python-pip
pip install -U pip praw psaw
```

### Windows 
- Download and execute https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
- **Tick "Add Python 3.9 to PATH"!**
- Open a command prompt and type:
```
python -m pip install -U pip praw psaw
```

### Create a Reddit client id and client secret
- go to https://www.reddit.com/prefs/apps and click "create an app..."
- enter some name, select "script", and enter http://localhost:8080 into the "redirect uri" field
- click "create app" - the client id is the string below "personal use script" 

## Running the scripts
- Click the green button named "Code" above and select "Download ZIP". 
- Extract the archive 
- Open a command prompt and change to the directory you extracted the archive to
- Example: For all posts created between October 13 and 14 (1:59 pm), print the URLs of comments that are one week (604800 seconds) newer than the posts they're in:
```
python printComments.py -i "<client id>" -s "<client secret>" -u "<reddit account name>" -r "<subreddit name>" -t "2020-10-13 13:59" "2020-10-14 13:59" -d 604800

```
- Example: Lock all posts created between October 13 and 14: 
```
python lockPosts.py -i "<client id>" -s "<client secret>" -u "<reddit account name>" -p "<reddit account password>" -r "<subreddit name>" -t "2020-10-13 13:59" "2020-10-14 13:59"

```
