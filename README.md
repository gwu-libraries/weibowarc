# weibowarc
The python library for archiving weibo friendship timeline.

##How to use
###Installing

```bash
git clone https://github.com/gwu-libraries/weibowarc.git
cd weibowarc
pip install -r requirements.txt
```

Also, it can be included as a dependency by adding the following to `requirements.txt`:

```bash
git+https://github.com/gwu-libraries/weibowarc.git@master#egg=weibowarc
```

###Reday to work
* Sign up for a Sina developer account at [Sina Development Platform](http://open.weibo.com/apps) to create a new app.
* Get the information about `API_KEY`, `API_SECRET`, `REDIRECT_URI`.
* How to get these information you can refer to the [API guide](https://www.cs.cmu.edu/~lingwang/weiboguide/).

###Get a token Authentication
* Get the authorize url
```python
    >>> from weibo import Client
    >>> c = Client(API_KEY, API_SECRET, REDIRECT_URI)
    >>> c.authorize_url
    'https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A%2F%2F&client_id=123456'
```    
* Open the authorize url in your local browser
* Login with your weibo account or click the '授权'(Authorized) button to get the code in the return URL marked as 'code='
* Set authorize code
```python
    >>> c.set_code('codecodecode')
```
* Get the `ACCESS_TOKEN`.
```python
    >>> c.token
    {u'access_token': u'abcd',u'remind_in': u'123456', u'uid': u'123456', u'expires_at': 1609785214}
```  

###Harvesting through [friends_timeline](http://open.weibo.com/wiki/2/statuses/friends_timeline)
Using the `API_KEY`, `API_SECRET`, `REDIRECT_URI`, `ACCESS_TOKEN` above to get the posts.

```bash
weibowarc.py -s --api_key apikey --api_secret apiscecret --redirect_uri uri --access_token accesstoken 
```  

It will return the nearest 150 weibo posts among all the followers of the current user.

#weibowarchtml
##How to use
To use the weibowarchtml, you need to give your `USERNAME`,`PASSWORD` with your sina account  

##Getting a full list of followers
Usually, It can call the [friends API](http://open.weibo.com/wiki/2/friendships/friends) to get the full list of following friends.However, the API calling only results 30% of them.
Currently, a full list of followers can get through the html parser analyzing the simple [mobile website](http://weibo.cn/) contents, since it hasn't decorated with css or javascript. 

```bash
weibowarchtml.py --followlist --username 'username' --password 'password'
```  

##Search key words
Since the same reason of limitation of API calling, searing key word also rely on parsing the search result pages, but we can't get the exact time of the post. 
It can return the user name and text of the weibo post.

```bash
weibowarchtml.py --search '郭德纲'  --username 'username' --password 'password'
```  

##Follow or Unfollow users
When you try to follow someone using the [friends create API](http://open.weibo.com/wiki/2/friendships/create), it won't work. What can do is parsing the html request for adding a friend. 

```bash
weibowarchtml.py --follow 12345 1234 123
```  
Simulating the request data in the http session is a solution for following the special uids, it's very similar for unfollowing users.However, it's not as efficient as calling API.
