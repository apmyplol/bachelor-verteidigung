from manim import *
from beanim import *
from afa_template import *
from typing import Union as uni, Tuple

cite_temp = TexTemplate(tex_compiler="latexmk")
cite_temp.add_to_preamble(
    r"""
    \usepackage[style=apa, backend=biber]{biblatex}
    \addbibresource{refs.bib}
    """
)

def initTop(self, title, num):
    tit = Title_Section(title, color=h_2).shift(DOWN*0.4)
    ind_stat = Tex(r"Repr. Measurement", font_size = 20, color=GREY).next_to(tit, UP).to_edge(LEFT)
    ind_sim_repr = Tex(r"Representation of\\Similarity", font_size = 20, color=GREY).next_to(ind_stat, RIGHT*2)
    ind_pr = Tex(r"Unique Repr.\\Theorem", font_size = 20, color=GREY).next_to(ind_sim_repr, RIGHT*2)

    ind_hthm = Tex(r"Homogeneity\\Theorem", font_size = 20, color=GREY).next_to(ind_pr, RIGHT*2) 
    ind_refs = Tex(r"References", font_size=20, color=GREY).next_to(ind_hthm, RIGHT*2)

    #tuda logo
    tuda_logo_svg = SVGMobject("./images/tuda_logo_RGB.svg", use_svg_cache=False)
    tuda_logo = tuda_logo_svg[1:].to_corner(UR)
    tuda_logo.scale(0.4, about_point=tuda_logo.get_corner(UR)).shift(UR*0.45)

    top = VGroup(ind_stat, ind_sim_repr, ind_pr, ind_hthm, ind_refs, tuda_logo, tit)
    top[num].set_color(BLACK)

    self.top = top
    return top


def update_list(group: uni[VGroup, BulletedList], currind: int, color_update: ManimColor =GREY) -> Tuple[Animation, Animation]:
        return group[currind].animate.set_color(color_update), group[currind+1].animate.set_color(BLACK)




class Cite(Tex):
    def __init__(self, *args, font_size=12, color=b_color, **kwargs) -> None:
        super().__init__(*args, tex_template=cite_temp, font_size=font_size, color=color, **kwargs)


