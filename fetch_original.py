import shutil as fs
import requests as req
import py7zr as sz
import auto_configs as conf
import os, json, wget

API_URL = 'https://api.github.com/repos/be5invis/Sarasa-Gothic/releases/latest'

def get_latest():
    response = req.get(API_URL)
    details = json.loads(response.content)

    version = details['tag_name'][1:]
    name = 'Sarasa-TTF-' + version + '.7z'

    assets = details['assets']
    for asset in assets:
        if (asset['name'] == name):
            return asset['browser_download_url']

def clear_dir(directory):
    if (os.path.exists(directory)):
        fs.rmtree(directory)
    os.makedirs(directory)

def download(url):
    filename = url.split('/')[-1]
    path = conf.DOWNLOAD_DIR + '/' + filename
    
    wget.download(url, path)
    
    return path

def unzip(path):
    with sz.SevenZipFile(path, mode = 'r') as zip_file:
        zip_file.extractall(path = conf.DOWNLOAD_DIR)