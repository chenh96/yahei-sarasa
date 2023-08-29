import os, shutil

DOWNLOAD_DIR = '/home/chenh/font'
RESULT_DIR = DOWNLOAD_DIR + '/result'

def copy_result():
    os.makedirs(RESULT_DIR)

    shutil.copy(DOWNLOAD_DIR + '/msyh.ttc', RESULT_DIR)
    shutil.copy(DOWNLOAD_DIR + '/msyhbd.ttc', RESULT_DIR)
    shutil.copy(DOWNLOAD_DIR + '/msyhl.ttc', RESULT_DIR)
    
    shutil.copy(DOWNLOAD_DIR + '/sarasa-mono-sc-regular.ttf', RESULT_DIR)
    shutil.copy(DOWNLOAD_DIR + '/sarasa-mono-sc-bold.ttf', RESULT_DIR)
    shutil.copy(DOWNLOAD_DIR + '/sarasa-mono-sc-italic.ttf', RESULT_DIR)
    shutil.copy(DOWNLOAD_DIR + '/sarasa-mono-sc-bolditalic.ttf', RESULT_DIR)


