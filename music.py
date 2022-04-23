import pygame

pygame.mixer.init()
menu_music_track = pygame.mixer.Sound("mp3_wav_samples/Dash_runner.wav")
background_music_track = pygame.mixer.Sound("mp3_wav_samples/8_bit_adventures.wav")


def menu_music():
    pygame.mixer.Sound.play(menu_music_track, loops=-1)
    pygame.mixer.Sound.set_volume(menu_music_track, 0.2)


def menu_music_fadeout():
    pygame.mixer.Sound.fadeout(menu_music_track, 1000)


def background_music():
    pygame.mixer.Sound.play(background_music_track, loops=-1, fade_ms=3500)
    pygame.mixer.Sound.set_volume(background_music_track, 0.2)
