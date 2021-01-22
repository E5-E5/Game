from moviepy.editor import VideoFileClip
import pygame
def get_clip(video_title, start=(0,0), seconds=10):
    video = VideoFileClip(video_title)

    end = (start[0], start[1]+seconds)
    clip = video.subclip(start, end)

    return clip

pygame.display.set_caption('My video!')

clip = get_clip('C:/Users/USER/Desktop/piton/RABOTI/Игра/Maze - 15891.mp4')
clip.preview()

pygame.quit()