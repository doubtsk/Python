import os
import shutil
os.chdir("image")
imagelist = os.listdir()
os.makedirs("good_photo", exist_ok=True)
os.makedirs("bad_photo", exist_ok=True)
for photopath in imagelist:
    if os.path.getsize(photopath) < 30000:
        shutil.move(photopath, './bad_photo/'+photopath)
    if os.path.getsize(photopath) > 10000:
        shutil.move(photopath, './good_photo/'+photopath)
