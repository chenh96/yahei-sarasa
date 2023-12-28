import shutil
import auto_configs as conf


def copy_result():
    shutil.copy(conf.TEMP_DIR + '/msyh.ttc', conf.RESULT_DIR)
    shutil.copy(conf.TEMP_DIR + '/msyhbd.ttc', conf.RESULT_DIR)
    shutil.copy(conf.TEMP_DIR + '/msyhl.ttc', conf.RESULT_DIR)

    shutil.copy(conf.TEMP_DIR + '/simsun.ttc', conf.RESULT_DIR)
    shutil.copy(conf.TEMP_DIR + '/simsunb.ttf', conf.RESULT_DIR)

    for file in conf.OTHER_COPY:
        shutil.copy(conf.TEMP_DIR + '/' + file, conf.RESULT_DIR)
