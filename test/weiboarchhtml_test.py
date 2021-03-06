#!/usr/bin/env python
# -*- coding: utf-8 -*-
from weibowarchtml import WeibowarcHtml

USERNAME = ''
PASSWORD = ''

WeiboHtmlTest = WeibowarcHtml(username=USERNAME, password=PASSWORD)


def get_list_test():
    count = 0
    for followers in WeiboHtmlTest.get_follower_list():
        print followers
        count += 1
    print count
    assert count == 6


def search_keyword():
    count = 0
    for followers in WeiboHtmlTest.search_word(key_word=u'郭德纲', max_page_num=10):
        print followers


def follow_test():
    users_id = []
    WeiboHtmlTest.follow_users(uids=users_id)


def unfollow_test():
    users_id = []
    WeiboHtmlTest.unfollow_users(uids=users_id)

follow_test()
#unfollow_test()