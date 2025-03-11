from manim import *
from beanim import *
from manim_slides import Slide

import_template("afa_template")

class Title_Slide(Slide):
    def construct(self):
        self.add(Title_Presentation(title= "Representational Measurement of Similarity: The Additive-Difference Model, Revisited",
                                    affiliation= "TU Darmstadt",
                                    author= "Arthur Liske"))

        ref1= Ref(the_dictionary="./refs.txt", the_ref="tv").to_corner(UR)
        self.play(Write(ref1))
        # ref1 = Ref(
        #     the_dictionary="example_refeq/dictionaries/test_ref.txt", the_ref="RS1"
        # ).to_corner(UR)

        self.wait(5)
