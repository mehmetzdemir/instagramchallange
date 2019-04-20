from api import InstagramAPI


api = InstagramAPI("<username>", "<password>")
api.login()


def get_tag(tag, max_id=''):
    """
    Get items for the tag.
    :param tag: hashtags name
    :param max_id: latest post's id
    :return: list of posts as json
    """
    api.getHashtagFeed(tag, maxid=max_id)
    return api.LastJson


if __name__ == '__main__':
    # 1. get images from instagram
    result = get_tag('travel')
    # 2. sort tags by like
    # 3. post photo to instagram
    # import code
    # code.interact(local=locals())
