import os
import shutil

directories_list = ["Music", "Videos", "Pictures", "PDFs", "DWGs", "EXEs", "Archives", "Excel", "Word", "Uncategorized"]
music_list = [".ogg", ".mp3", ".ogg"]
pictures_list = [".jpg", ".gif", ".png"]
videos_list = [".mp4", ".webm", ".avi"]
excel_list = [".xls", ".xlsx"]
doc_list = [".doc"]
archive_list = [".zip", ".rar"]
dwg_list = [".dwg", ".dwl"]
pdf_list = [".pdf"]
exe_list = [".exe"]

directory = 'C:\\Users\\hsimov\\Downloads'
os.chdir(directory)

for dir in directories_list:
    if os.path.exists(dir):
        continue
    else:
        os.mkdir(dir)

files_and_dirs = os.listdir(directory)

file_list = []
for file in files_and_dirs:
    split = os.path.splitext(file)
    if split[1] == "":
        continue
    else:
        file_list.append(file)

file_list.sort()

for file in file_list:
    split = os.path.splitext(file)

    if split[-1] in pictures_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Pictures\\{file}"
        shutil.move(src, dest)
    elif split[-1] in music_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Music\\{file}"
        shutil.move(src, dest)
    elif split[-1] in dwg_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\DWGs\\{file}"
        shutil.move(src, dest)
    elif split[-1] in pdf_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\PDFs\\{file}"
        shutil.move(src, dest)
    elif split[-1] in videos_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Videos\\{file}"
        shutil.move(src, dest)
    elif split[-1] in exe_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\EXEs\\{file}"
        shutil.move(src, dest)
    elif split[-1] in archive_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Archives\\{file}"
        shutil.move(src, dest)
    elif split[-1] in excel_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Excel\\{file}"
        shutil.move(src, dest)
    elif split[-1] in doc_list:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Word\\{file}"
        shutil.move(src, dest)
    else:
        src = f"{directory}\\{file}"
        dest = f"{directory}\\Uncategorized\\{file}"
        shutil.move(src, dest)




