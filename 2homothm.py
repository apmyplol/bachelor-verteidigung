from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from numpy import size
from afa_functions import *

config.write_to_movie = True
# config.renderer = "opengl"

#:'<,'>yank t | let @t = substitute(@t, '\n', '\r', 'g') | execute '! kitten @ send-text --match "title:ipythonn" ' . shellescape(@t, 1)
#:'<,'>yank t | let @t = substitute(@t, '\n', '\r', 'g') | execute '! kitten @ send-text --match "title:ipythonn" ' . shellescape(@t, 1)
#:yank t | call system('kitten @ send-text --match "title:ipythonn" --stdin', @t)

class Homogeneity(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1

        # top = initTop(self, "Homogeneity Theorem", 3)
        # self.add(top)
        # Update top
        self.next_slide()


