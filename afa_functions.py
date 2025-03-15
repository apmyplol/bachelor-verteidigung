from manim import *
from beanim import *
from afa_template import *

cite_temp = TexTemplate(tex_compiler="latexmk")
cite_temp.add_to_preamble(
    r"""
    \usepackage[style=apa, backend=biber]{biblatex}
    \addbibresource{refs.bib}
    """
)

def initTop(self, title):
    tit = Title_Section(title, color=h_2).shift(DOWN*0.4)
    ind_stat = Tex("Repr. Measurement \\&\\\\Similarity", font_size = 20, color=GREY).next_to(tit, 0.5*UP).to_edge(LEFT)
    ind_pr = Tex("Unique Repr.\\\\Theorem", font_size = 20, color=GREY).next_to(ind_stat, RIGHT*2)

    ind_hthm = Tex("Homogeneity\\\\Theorem", font_size = 20, color=GREY).next_to(ind_pr, RIGHT*2) 
    ind_disc = Tex("Discussion", font_size=20, color=GREY).next_to(ind_hthm, RIGHT*2)
    top = VGroup(tit, ind_stat, ind_pr, ind_hthm, ind_disc)
    self.add(top)
    self.top = top


def update_list(group, self, currind, color_update=GREY):
        self.play(group[currind].animate.set_color(color_update), group[currind+1].animate.set_color(BLACK))


class Cite(Tex):
    def __init__(self, *args, font_size=10, **kwargs) -> None:
        super().__init__(*args, tex_template=cite_temp, font_size=font_size, **kwargs)


