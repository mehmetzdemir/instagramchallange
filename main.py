import requests
from api import InstagramAPI
from io import BytesIO
from PIL import Image



api = InstagramAPI("insta_photography_challange", "Mehmet123")
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

def sort_tag_result():
    result = get_tag('travel')  # son elemanin id si ile tekrar istek at.
    infos = []

    for i in result["ranked_items"]:
        info = {"username": i["user"]["username"], "full_name": i["user"]["full_name"],
                "pic_url": i["user"]["profile_pic_url"], "like_count": i["like_count"]}
        infos.append(info)
    infos = sorted(infos, key=lambda k: k['like_count'], reverse=True)

    return infos

def champion_post():
    infos = sort_tag_result()
    response = requests.get(infos[0]["pic_url"], stream=True)
    image = BytesIO(response.content)

    api.uploadPhoto(image)


if __name__ == '__main__':
    champion_post()
    # 1. get images from instagram
    # 2. sort tags by like
    # 3. post photo to instagram

