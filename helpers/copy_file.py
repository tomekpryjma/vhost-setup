import shutil

def copy_file(original_name, target):
    try:
        return shutil.copy(original_name, target)

    except Exception as err:
        print("FATAL ERROR whilst copying file: {0}".format(err))