import os
import sys
import subprocess

if(len(sys.argv) == 2): 
    path = sys.argv[1]
    is_list = "0"
    remove_file = "0"
if(len(sys.argv) == 3): 
    path = sys.argv[1]
    is_list = sys.argv[2]
    remove_file = "0"
if(len(sys.argv) == 4): 
    path = sys.argv[1]
    is_list = sys.argv[2]
    remove_file = sys.argv[3]

if(is_list == "0"):
    os.system("you-get '%s'"%path)
else:
    os.system("you-get '%s' -l"%path)

for root, dirs, files in os.walk("."):
    for file in files: 
        is_video = file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".flv")
        if is_video :
            print(os.path.join(root, file)) 
            name = os.path.splitext(file)[0]
            print(name)
            os.system('ffmpeg -i "%s" -vn -ab 320k "%s.mp3"' % (file,name))

if(remove_file == "0"):
    print("It's all done")
else:
    os.system("rm -f *.mp4")
    os.system("rm -f *.flv")
    os.system("rm -f *.str")
    os.system("rm -f *.xml")
    print("Videos and subtitles are removed")