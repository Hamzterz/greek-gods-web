import json
import requests


def str_get_wiki_summary(str_search):
    dc_wiki_request = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(str_search)).json()
    str_wiki_summary = dc_wiki_request['extract']

    return str_wiki_summary
