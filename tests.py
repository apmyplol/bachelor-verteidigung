from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide

config.write_to_movie = False
config.renderer = "opengl"

import_template("afa_template")

cite_temp = TexTemplate(tex_compiler="latexmk")
cite_temp.add_to_preamble(
    r"""
    \usepackage[style=apa, backend=biber]{biblatex}
    \addbibresource{refs.bib}
    """
)
d_color = "#531196"

def update_list(group, self, currind, color_update=GREY):
        self.play(group[currind].animate.set_color(color_update), group[currind+1].animate.set_color(BLACK))


#:'<,'>yank t | let @t = substitute(@t, '\n', '\r', 'g') | execute '! kitten @ send-text --match "title:ipythonn" ' . shellescape(@t, 1)
#:'<,'>yank t | let @t = substitute(@t, '\n', '\r', 'g') | execute '! kitten @ send-text --match "title:ipythonn" ' . shellescape(@t, 1)
#:'<,'>yank t | call system('kitten @ send-text --match "title:ipythonn" --stdin', @t)
class Cite(Tex):
    def __init__(self, *args, font_size=10, **kwargs) -> None:
        super().__init__(*args, tex_template=cite_temp, font_size=font_size, **kwargs)

class Test(Scene):
    def construct(self):
        curve_svg = SVGMobject("./images/2_homothm_curve.svg", use_svg_cache=False)
        self.embed()
        # self.play(Write(set_svg), Write(curve_svg))
