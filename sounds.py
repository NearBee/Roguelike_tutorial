import pygame

pygame.mixer.init()

# Define audio channels
background_music_channel = pygame.mixer.Channel(0)
sound_effects_channel = pygame.mixer.Channel(1)

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


def menu_music() -> None:
    background_music_channel.play(menu_music_track, loops=-1, fade_ms=1500)
    background_music_channel.set_volume(0.5)


def menu_music_fadeout() -> None:
    background_music_channel.fadeout(1000)


def background_music() -> None:
    background_music_channel.play(background_music_track, loops=-1)
    background_music_channel.set_volume(0.5)


def death_jingle() -> None:
    background_music_channel.fadeout(500)
    background_music_channel.play(death_music_track, fade_ms=1000)


def hit_sound() -> None:
    sound_effects_channel.play(hit_sound_effect)


def stairs_sound_effect() -> None:
    sound_effects_channel.play(stairs_sound_loop)


def fireball_sound() -> None:
    sound_effects_channel.play(fireball_sound_effect)


def lightning_sound() -> None:
    sound_effects_channel.play(lightning_sound_effect)


def confusion_sound() -> None:
    sound_effects_channel.play(confusion_sound_effect)


def level_up_sound_effect() -> None:
    sound_effects_channel.play(level_up_sound)


# TODO: Clean up this entire file, possibly instead of just listing each variable then plugging it in, turn some sound variables into dicts.
