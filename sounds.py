import pygame

pygame.mixer.init()
menu_music_track = pygame.mixer.Sound("WavSounds/Dash_runner.wav")
background_music_track = pygame.mixer.Sound("WavSounds/8_bit_adventures.wav")
death_music_track = pygame.mixer.Sound("WavSounds/death_jingle.wav")
hit_sound_effect = pygame.mixer.Sound("WavSounds/hit_sound.wav")
fireball_sound_effect = pygame.mixer.Sound("WavSounds/sfx_exp_fireball.wav")
lightning_sound_effect = pygame.mixer.Sound(
    "WavSounds/sfx_weapon_singleshot_lightning.wav"
)
confusion_sound_effect = pygame.mixer.Sound("WavSounds/sfx_sound_bling.wav")
stairs_sound_loop = pygame.mixer.Sound("WavSounds/sfx_movement_stairs3loop.wav")
level_up_sound = pygame.mixer.Sound("WavSounds/sfx_sounds_levelup.wav")


def menu_music():
    pygame.mixer.Sound.play(menu_music_track, loops=-1)
    pygame.mixer.Sound.set_volume(menu_music_track, 0.1)


def menu_music_fadeout():
    pygame.mixer.Sound.fadeout(menu_music_track, 1000)


def background_music():
    pygame.mixer.Sound.play(background_music_track, loops=-1, fade_ms=3500)
    pygame.mixer.Sound.set_volume(background_music_track, 0.1)


def death_jingle():
    pygame.mixer.Sound.stop(background_music_track)
    pygame.mixer.Sound.play(death_music_track)
    pygame.mixer.Sound.set_volume(death_music_track, 0.2)


def hit_sound():
    pygame.mixer.Sound.play(hit_sound_effect)
    pygame.mixer.Sound.set_volume(hit_sound_effect, 0.1)


def stairs_sound_effect():
    pygame.mixer.Sound.play(stairs_sound_loop)
    pygame.mixer.Sound.set_volume(stairs_sound_loop, 0.2)


def fireball_sound():
    pygame.mixer.Sound.play(fireball_sound_effect)
    pygame.mixer.Sound.set_volume(fireball_sound_effect, 0.1)


def lightning_sound():
    pygame.mixer.Sound.play(lightning_sound_effect)
    pygame.mixer.Sound.set_volume(lightning_sound_effect, 0.1)


def confusion_sound():
    pygame.mixer.Sound.play(confusion_sound_effect)
    pygame.mixer.Sound.set_volume(confusion_sound_effect, 0.1)


def level_up_sound_effect():
    pygame.mixer.Sound.play(level_up_sound)
    pygame.mixer.Sound.set_volume(level_up_sound, 0.2)


# TODO: Clean up this entire file, possibly instead of just listing each variable then plugging it in, turn some sound variables into dicts.
