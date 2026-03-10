from Game.RunnerGame import RunnerGame
from Game.Stories import Story1, Story2, Story3
from Game.Ultils.main_menu import menu

story_modules = {
    "Story1": Story1.Story,
    "Story2": Story2.Story,
    "Story3": Story3.Story
}

RunnerGame(menu, story_modules)