import os
import sys
import subprocess
import ffmpy
import argparse
import shutil

is_list = "0"
remove_file = "0"

parser = argparse.ArgumentParser()
parser.description='Auto download playlist and encode them to mp3'
parser.add_argument("-u","--url", help="the url of the video or playlist",type=str)
parser.add_argument("-l","--list", default="0", help="0 for video, 1 for list",type=str)
parser.add_argument("-r","--remove_dist", default="0", help="0 for no, 1 for yes",type=str)
args = parser.parse_args()

path = args.url
is_list = args.list
remove_file = args.remove_dist

# if(len(sys.argv) == 2): 
#     path = sys.argv[1]
# if(len(sys.argv) == 3): 
#     path = sys.argv[1]
#     is_list = sys.argv[2]
# if(len(sys.argv) == 4): 
#     path = sys.argv[1]
#     is_list = sys.argv[2]
#     remove_file = sys.argv[3]

video_dir = "./video/"
audio_dir = "./audio/"

if(is_list == "0"):
    cmd = ["you-get", path, "-o", video_dir]
else:
    cmd = ["you-get", path, "-l", "-o", video_dir]

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding="utf-8")
while True:  
    line = p.stdout.readline() 
    is_progress = line.find("┤", 0, len(line))
    is_complete = line.find("100", 0, len(line))
    if(is_progress == -1):
        print(line,end='\r')
    else:
        if(is_complete == -1):
            print(line.strip('\n'),end='\r') 
        else:
            print(line,end='\r')
    if not line:
        break

for root, dirs, files in os.walk(video_dir):
    for file in files: 
        is_video = file.endswith(".mp4") or file.endswith(".webm") or file.endswith(".flv")
        if is_video :
            print(root)
            print(file)
            name = os.path.splitext(file)[0]
            folder = os.path.exists(audio_dir)
            if not folder:
                os.mkdir(audio_dir)
            ff = ffmpy.FFmpeg(
                inputs={root+file: None},
                outputs={audio_dir + name + ".mp3": '-vn -ab 320k'}
            )
            audio = os.path.exists(audio_dir + name + ".mp3")
            if not audio:
                ff.run()
            else:
                print(name + ".mp3" + " is exists")

if(remove_file == "0"):
    print("It's all done")
else:
    shutil.rmtree(video_dir, True)
    print("Videos and subtitles are removed")