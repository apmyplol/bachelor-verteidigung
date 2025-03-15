from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from afa_functions import *



config.write_to_movie = False
# config.renderer = "opengl"




class Intro(Slide):
    def construct(self):
        # self.next_section(skip_animations=True)
        title = Title_Presentation(title= "Representational Measurement of Similarity: The Additive-Difference Model, Revisited",
                                    affiliation= "TU Darmstadt",
                                    author= "Arthur Liske")
        self.add(title)

        points = BulletedList(r"Representational Measurement",
                 r"Representation of Similarity",
                 r"Unique Representation Theorem",
                 r"Homogeneity Theorem",
                 r"Discussion",
                buff=MED_SMALL_BUFF)

        self.wipe(title, points)
        
        initTop(self, "Representaional Measurement")

        self.play(Transform(points, self.top[0:5]))



class test(Scene):
    def construct(self):

        self.embed()
