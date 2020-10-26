import os


_ASSETS_URL_PREFIX = os.getenv('ASSETS_URL_PREFIX')
"""
ex.) https://bucket_name.s3-region.amazonaws.com/oracle-follower/assets
"""


def get_image(image_key: str, extension: str = '.png') -> str:
    """
    :param image_key: 関数内で小文字に変換します。ex) hero/hero_anticipation.jpg
    :param extension:
    :return: url ex.) https://bucket_name.s3-region.amazonaws.com/oracle-follower/assets/images/hero/hero_anticipation.jpg
    """
    if '.' in image_key:
        # image_keyが拡張子つきなら、extensionはこの関数は付与しない
        return f'{_ASSETS_URL_PREFIX}/images/{image_key.lower()}'
    return f'{_ASSETS_URL_PREFIX}/images/{image_key.lower()}{extension}'
