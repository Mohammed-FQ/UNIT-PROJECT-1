from random import choice, randint

from asciimatics.effects import Mirage, Print, Snow, Stars
from asciimatics.exceptions import StopApplication, ResizeScreenError
from asciimatics.particles import PalmFirework, RingFirework, SerpentFirework, StarFirework
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def any_key(_event):
    """Exit current scene as soon as any key is pressed."""
    raise StopApplication("User requested exit from scene.")


def play_effects(screen, effects):
    """Play a single effect scene until any key is pressed."""
    try:
        screen.play([Scene(effects, -1)], stop_on_resize=True, unhandled_input=any_key)
    except ResizeScreenError:
        pass
def open_and_play(build_effects):
    """Open a screen, render scene effects, and always close the screen."""
    screen = Screen.open()
    try:
        effects = build_effects(screen)
        play_effects(screen, effects)
    except StopApplication:
        raise StopApplication("User requested exit from scene.")
    finally:
        screen.close()


def centered_print(screen, text, font, y, colour):
    renderer = FigletText(text, font=font)
    x = max(0, (screen.width - renderer.max_width) // 2)
    return Print(screen, renderer, y, x=x, colour=colour)


def build_victory_effects(screen):
    effects = [
        Stars(screen, (screen.width + screen.height) // 4),
        centered_print(screen, "PYTHON SLAYER", "small", max(1, screen.height // 2 -32), Screen.COLOUR_CYAN),
        centered_print(screen, "VICTORY!", "big", max(1, screen.height // 2), Screen.COLOUR_GREEN),
        Mirage(screen, FigletText("Press any key to continue", font="small"), max(1, screen.height // 2 + 20), Screen.COLOUR_GREEN),
    ]

    fireworks = [
        (PalmFirework, 25, 30),
        (PalmFirework, 25, 30),
        (StarFirework, 25, 35),
        (StarFirework, 25, 35),
        (StarFirework, 25, 35),
        (RingFirework, 20, 30),
        (SerpentFirework, 30, 35),
    ]

    for _ in range(20):
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(
                screen,
                randint(0, screen.width),
                randint(screen.height // 8, screen.height * 3 // 4),
                randint(start, stop),
                start_frame=randint(0, 250),
            ),
        )

    return effects


def build_defeat_effects(screen):
    return [
        Snow(screen),
        centered_print(screen, "PYTHON SLAYER", "small", max(1, screen.height // 2 - 32), Screen.COLOUR_CYAN),
        centered_print(screen, "YOU DIED...", "big", max(1, screen.height // 2), Screen.COLOUR_RED),
        Mirage(screen, FigletText("Press any key to continue", font="small"), max(1, screen.height // 2 + 20), Screen.COLOUR_RED),
    ]


def victory():
    open_and_play(build_victory_effects)


def defeat():
    open_and_play(build_defeat_effects)