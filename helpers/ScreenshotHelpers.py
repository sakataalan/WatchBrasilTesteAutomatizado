import re
import uuid
import os

def make_screenshot_dir(scenario):
    path = resolve_path(scenario)
    return f'{path}/{uuid.uuid4()}.png'

def resolve_folder(scenario):
    return re.findall(r'".*"', scenario)[0].replace('"', '').rstrip()

def resolve_path(scenario):
    path = f'evidences/{resolve_folder(scenario)}'
    if not os.path.exists(path):
        os.makedirs(path)
    return path