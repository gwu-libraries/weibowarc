#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibowarc import Weibowarc
import logging
import time
import os

"""
You will need to have these environment variables set to run these tests:
* API_KEY
* API_SECRET
* REDIRECT_URL
* ACCESS_TOKEN
"""

api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')
redirect_uri = os.environ.get('REDIRECT_URL')
access_token = os.environ.get('ACCESS_TOKEN')

weibotest = Weibowarc(api_key, api_secret, redirect_uri, access_token)

logging.basicConfig(filename="test.log", level=logging.INFO)


def test_get_friendship():
    count = 0
    for weibo in weibotest.search_friendships():
        assert weibo[u'mid']
        # testing the retweeted
        if u'retweeted_status' in weibo and weibo[u'retweeted_status'] is not None:
            assert weibo[u'retweeted_status'][u'mid']
        count += 1
        if count == 100:
            break

    assert count == 100


def test_since_id():
    count = 0
    for weibo in weibotest.search_friendships():
        mid = weibo[u'mid']
        count += 1
        if count == 10:
            break

    assert mid
    time.sleep(5)

    count = 0
    for weibo in weibotest.search_friendships(since_id=mid):
        print 'new_id [%s], pre_id [%s]' % (weibo[u'mid'], mid)
        assert weibo[u'mid'] > mid
        count += 1
        if count == 9:
            break


def test_max_id():
    for weibo in weibotest.search_friendships():
        mid = weibo[u'mid']
        break
    assert mid
    time.sleep(5)

    count = 0
    for weibo in weibotest.search_friendships(max_id=mid):
        count += 1
        assert weibo[u'mid'] <= mid
        if count > 100:
            break


def test_max_and_since_ids():
    max_id = since_id = None
    count = 0
    for weibo in weibotest.search_friendships():
        count += 1
        if not max_id:
            max_id = weibo[u'mid']
        since_id = weibo[u'mid']
        if count == 50:
            break
    count = 0
    for weibo in weibotest.search_friendships(max_id=max_id, since_id=since_id):
        count += 1
        assert weibo[u'mid'] <= max_id
        assert weibo[u'mid'] > since_id


def test_page():
    # pages are 100 weibo post but total we can get 150
    count = 0
    for weibo in weibotest.search_friendships():
        count += 1
        if count == 150:
            break
    assert count == 150


def test_friends_list_all():
    count = 0
    for weibo in weibotest.search_friends_list():
        if weibo[u'screen_name']:
            count += 1

    assert count >= 0


def test_error_code():
    friendships_url = "statuses/user_timeline"
    params = {
            'count': 100,
            'page': 1,
            'uid': 5789331626
        }
    try:
        weibotest.get(friendships_url, **params)
    except Exception, e:
        error_code = ''.join(e)[0:5]
        assert error_code == '21335'

# test_error_code()
# test_get_friendship()
# test_since_id()
# test_max_and_since_ids()
# test_friends_list_all()
