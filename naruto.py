from moviepy.editor import VideoFileClip, clips_array

import argparse
import os

parser = argparse.ArgumentParser(description='Clips together two mp4 videos')
parser.add_argument('video1', help='name of first videoclip')
parser.add_argument('video2', help='name of second videoclip')
parser.add_argument('target', help='name of desired name of concatination')

args = parser.parse_args()


def main():
    if not os.path.isfile(args.video1) or not os.path.isfile(args.video2):
        print("Video files does not exists")
        return
    
    clip1 = VideoFileClip(args.video1)
    clip2 = VideoFileClip(args.video2)
    final_clip = clips_array([[clip1, clip2]])
    if clip1.duration > clip2.duration:
        final_clip.audio = clip1.audio
    else:
        final_clip.audio = clip2.audio
    print("Creating your video...")
    final_clip.write_videofile(args.target, verbose=False, logger=None)


if __name__ == "__main__":
    main()
