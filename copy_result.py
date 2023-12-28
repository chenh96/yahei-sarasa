import shutil
import auto_configs as conf

def copy_result():
    shutil.copy(conf.DOWNLOAD_DIR + '/msyh.ttc', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/msyhbd.ttc', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/msyhl.ttc', conf.RESULT_DIR)

    shutil.copy(conf.DOWNLOAD_DIR + '/simsun.ttc', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/simsunb.ttf', conf.RESULT_DIR)
    
    shutil.copy(conf.DOWNLOAD_DIR + '/SarasaMonoSC-Regular.ttf', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/SarasaMonoSC-Bold.ttf', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/SarasaMonoSC-Italic.ttf', conf.RESULT_DIR)
    shutil.copy(conf.DOWNLOAD_DIR + '/SarasaMonoSC-BoldItalic.ttf', conf.RESULT_DIR)