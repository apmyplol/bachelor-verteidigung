from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide

config.write_to_movie = False
config.renderer = "opengl"

import_template("afa_template")
#TODO: create tex template for citation that uses latexmk and everythign else with default latex

cite_temp = TexTemplate(tex_compiler="latexmk")
cite_temp.add_to_preamble(
    r"""
    \usepackage[style=apa, backend=biber]{biblatex}
    \addbibresource{refs.bib}
    """
)

class Cite(Tex):
    def __init__(self, *args, font_size=10, **kwargs) -> None:
        super().__init__(*args, tex_template=cite_temp, font_size=font_size, **kwargs)


class Title_Slide(Slide):
    def construct(self):
        # self.next_section(skip_animations=True)
        self.add(Title_Presentation(title= "Representational Measurement of Similarity: The Additive-Difference Model, Revisited",
                                    affiliation= "TU Darmstadt",
                                    author= "Arthur Liske"))

        ref1= Ref(the_dictionary="./refs.txt", the_ref="tv").to_corner(UR)
        ref1 = MathTex(r"(\ps{a}, \ps{b}) \succsim (\ps{c}, \ps{d})")
        self.play(Write(ref1))
        ref2 = Cite(r"\parencite{mulholland}").next_to(ref1, DOWN)
        self.play(Write(ref2))
        ref3 = MathTex(r"\cball{\len}").next_to(ref2, DOWN)
        self.add(ref3)
        # self.interactive_embed()
        # ref1 = Ref(
        #     the_dictionary="example_refeq/dictionaries/test_ref.txt", the_ref="RS1"
        # ).to_corner(UR)


        # self.next_section(skip_animations=False)


        self.play(Write(Circle()))
