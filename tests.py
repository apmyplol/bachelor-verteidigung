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
        # 0 : z
        # 1-4: points
        # 5: curve
        # curve_svg[0]
        set_svg = SVGMobject("./images/2_homothm0.svg", use_svg_cache=False).scale(2).shift(DR)

        curve_svg = SVGMobject("./images/2_homothm_curve.svg", use_svg_cache=False).scale(0.8).shift(DR+LEFT*0.5)

        p0 = LabeledDot(MathTex(r"\ve{0}", font_size=20)).move_to(curve_svg[1])
        p1 = LabeledDot(MathTex(r"\ve{z}", font_size=20)).move_to(curve_svg[0])
 

        self.add(set_svg, p0, p1)
        self.add(curve_svg[5])
        self.embed()

        lineOZ = Line(p0, p1, stroke_width=2)
        # lineOZd = DashedLine(curve_svg[1], curve_svg[0], stroke_width=2)
        self.add(lineOZ)
        
        sq = Square(side_length=1.8).move_to(curve_svg[1])
        self.add(sq)

        cir = Circle().surround(sq, buffer_factor=0.65)
        self.add(cir)
        
        prop = 0.1
        #ANIM: point along line until proportion 0.1
        predot = Dot(lineOZ.point_from_proportion(prop))
        self.add(predot)

        dots = VGroup(p0, [Dot(curve_svg[5].point_from_proportion(i)) for i in np.arange(0.1, 1, 0.1)], p1)
        self.add(dots)

        # self.remove(predot)


        vecs = VGroup([Arrow(start=dots[i], end=dots[i+1], color=PURPLE, buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=3) for i in range(0, len(dots)-1)])
        self.add(vecs)

        scaled_vecs = vecs.copy().scale(0.1, about_point=dots[0].get_center())
