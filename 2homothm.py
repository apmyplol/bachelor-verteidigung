from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide

config.write_to_movie = True
# config.renderer = "opengl"

import_template("afa_template")
#TODO: create tex template for citation that uses latexmk and everythign else with default latex

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

class Homogeneity(Scene):
    def construct(self):
        self.next_section(skip_animations=True)
        self.initTop()

        int_subtr = Tex("intradimenional subtractivity: ").shift(LEFT)
        self.add(int_subtr)
        intr_subtr_f = MathTex(r"\metr{\ve{x}}{\ve{z}} = F(|x_1 - z_1|, \dots, |x_n - z_n|)").next_to(int_subtr, RIGHT)
        self.add(intr_subtr_f)
        #NOTE: ad model yields translation invariance and important for arbitrary small delta balls

        text_admod = Tex(r"AD Model $\Rightarrow$").next_to(int_subtr, LEFT*0.5)
        self.add(text_admod)

        VGroup(int_subtr, intr_subtr_f, text_admod).shift(2*UP)

        thm = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        thm_0 = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r" with $\ve{0} \in S$",
                  r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        homo_eq = MathTex(r"\metric(",r"\ve{0},",r"t\ve{z})=t\metric(", r"\ve{0},",r"\ve{z})").next_to(thm, DOWN)
        homo_eq_0 = MathTex(r"\metric(",r"t\ve{z})=t\metric(", r"\ve{z})").move_to(homo_eq)
        thm_rect = SurroundingRectangle(VGroup(thm, homo_eq), color=d_color, buff=MED_LARGE_BUFF*0.6)
        self.add(thm, thm_rect, homo_eq)

        self.play(TransformMatchingTex(thm, thm_0))
        self.play(TransformMatchingTex(homo_eq, homo_eq_0))


        thm_group = VGroup(thm_0, thm_rect, homo_eq_0)



        thm_stat_short1 = Tex(r"$S$ open, convex\\$\metr{\ve{x}}{\ve{z}}=F(\dots|x_i-z_i|\dots)$", font_size=20)
        thm_stat_short2 = Tex(r"$F$ cont. \& increasing\\$\metric$ metric w/ add. segments", font_size=20).next_to(thm_stat_short1, RIGHT)
        thm_res_short = Tex(r"$\Rightarrow$ homogeneous", font_size=20).next_to(thm_stat_short2, RIGHT*0.5)

        thm_short = VGroup(thm_stat_short1, thm_stat_short2, thm_res_short).next_to(self.top[0].tit, RIGHT).to_edge(RIGHT)

        self.play(Write(thm_short, shift=UP))
        self.play(FadeOut(VGroup(text_admod, int_subtr, intr_subtr_f, thm_group)), run_time=0.5)

        steps = BulletedList(r"$\metric$ distance to set", 
                     r"$\frac 1m \metro{\ve{z}} \leq \metro{\frac 1m \ve{z}}$",
                     r"$\frac 1m \metro{\ve{z}} \geq \metro{\frac 1m \ve{z}}$",
                     r"$\frac km \metro{\ve{z}} \geq \metro{\frac km \ve{z}}$",
                     r"$\metric$ continuous"
                     , font_size=30, buff=MED_SMALL_BUFF)

        self.play(Write(steps))
        self.play(steps.animate.scale(0.7).next_to(self.top, DOWN).to_edge(LEFT).set_color(GREY))
        self.play(steps[0].animate.set_color(BLACK))
        self.next_section(skip_animations=False)

        ### Proof part 0 
        set_svg = SVGMobject("./images/2_homothm0.svg", use_svg_cache=False).scale(2).shift(DR)
        curve_svg = SVGMobject("./images/2_homothm_curve.svg", use_svg_cache=False)
        # 0 : z
        # 1-4: points
        # 5: curve
        # curve_svg[0]
        self.play(Write(set_svg), Write(curve_svg))

        # self.play(set_svg.animate.set_color(PURPLE))

        ### Proof part 1
        # update_list(steps, self, 0, GREEN)
        #
        #
        # ### Proof part 2
        # update_list(steps, self, 1, GREEN)
        #
        # ### Proof part 3
        # update_list(steps, self, 2, GREEN)
        #
        #
        # ### Proof part 4
        # update_list(steps, self, 3, GREEN)
        #
        #
        # ### Proof finished
        # self.play(steps[4].animate.set_color(GREEN))


    def initTop(self):
        tit = Title_Section("Homogeneity Theorem", color=PURPLE).shift(DOWN*0.4)
        ind_stat = Tex("Unique Repr.\\\\Theorem", font_size = 20, color=GREY).next_to(tit, 0.5*UP).to_edge(LEFT)
        ind_pr = Tex("Proof Idea", font_size = 20, color=GREY).next_to(ind_stat, RIGHT*2)

        ind_hthm = Tex("Homogeneity\\\\Theorem", font_size = 20, color=GREY).next_to(ind_pr, RIGHT*2) 
        ind_disc = Tex("Discussion", font_size=20, color=GREY).next_to(ind_hthm, RIGHT*2)
        top = VGroup(tit, ind_stat, ind_pr, ind_hthm, ind_disc)
        self.add(top)
        self.top = top
