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
#:'<,'>yank t | call system('kitten @ send-text --match "title:ipythonn" --stdin', @t)

class Homogeneity(Scene):
    def construct(self):
        # self.next_section(skip_animations=True)
        top = initTop(self, "Homogeneity Theorem", 3)
        self.add(top)

        int_subtr = Tex("intradimenional subtractivity: ").shift(LEFT)
        intr_subtr_f = MathTex(r"\metr{\ve{x}}{\ve{z}} = F(|x_1 - z_1|, \dots, |x_n - z_n|)").next_to(int_subtr, RIGHT)
        #NOTE: ad model yields translation invariance and important for arbitrary small delta balls
        self.play(Write(VGroup(intr_subtr_f, int_subtr)))

        text_admod = Tex(r"AD Model $\Rightarrow$").next_to(int_subtr, LEFT*0.5)
        self.play(Write(text_admod))

        self.play(VGroup(int_subtr, intr_subtr_f, text_admod).animate.shift(2*UP))

        thm = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        thm_0 = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r" with $\ve{0} \in S$",
                  r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        homo_eq = MathTex(r"\metric(",r"\ve{0},",r"t\ve{z})=t\metric(", r"\ve{0},",r"\ve{z})").next_to(thm, DOWN)
        homo_eq_0 = MathTex(r"\metric(",r"t\ve{z})=t\metric(", r"\ve{z})").move_to(homo_eq)
        thm_rect = SurroundingRectangle(VGroup(thm, homo_eq), color=d_color, buff=MED_LARGE_BUFF*0.6)
        self.play(Write(VGroup(thm,thm_rect, homo_eq)))

        self.play(TransformMatchingTex(thm, thm_0))
        self.play(TransformMatchingTex(homo_eq, homo_eq_0))


        thm_group = VGroup(thm_0, thm_rect, homo_eq_0)



        thm_stat_short1 = Tex(r"$S$ open, convex\\$\metr{\ve{x}}{\ve{z}}=F(\dots|x_i-z_i|\dots)$", font_size=20)
        thm_stat_short2 = Tex(r"$F$ cont. \& increasing\\$\metric$ metric w/ add. segments", font_size=20).next_to(thm_stat_short1, RIGHT)
        thm_res_short = Tex(r"$\Rightarrow$ homogeneous", font_size=20).next_to(thm_stat_short2, RIGHT*0.5)

        thm_short = VGroup(thm_stat_short1, thm_stat_short2, thm_res_short).next_to(top[-1].tit, RIGHT).to_edge(RIGHT)

        self.play(Write(thm_short, shift=UP))
        self.play(FadeOut(VGroup(text_admod, int_subtr, intr_subtr_f, thm_group)), run_time=0.5)

        steps = BulletedList(r"$\metric$ distance to set", 
                     r"$\frac 1m \metro{\ve{z}} \leq \metro{\frac 1m \ve{z}}$",
                     r"$\frac 1m \metro{\ve{z}} \geq \metro{\frac 1m \ve{z}}$",
                     r"$\frac km \metro{\ve{z}} = \metro{\frac km \ve{z}}$",
                     r"$t \metro{\ve{z}} = \metro{t \ve{z}}$",
                     font_size=30, buff=MED_SMALL_BUFF)

        self.play(Write(steps))
        self.play(steps.animate.scale(0.7).next_to(self.top, DOWN).to_edge(LEFT).set_color(GREY))
        self.play(steps[0].animate.set_color(BLACK))

        ### Proof part 0 
        set_svg = SVGMobject("./images/2_homothm0.svg", use_svg_cache=False).scale(2.1).shift(DR + DOWN*0.8)
        curve_svg = SVGMobject("./images/2_homothm_curve.svg", use_svg_cache=False).scale(0.8).shift(DR+LEFT*0.5+DOWN*0.8)
        # 0 : z
        # 1-4: points
        # 5: curve
        # curve_svg[0]
        p0 = LabeledDot(MathTex(r"\ve{0}", font_size=18, color=WHITE)).move_to(curve_svg[1])
        p1 = LabeledDot(MathTex(r"\ve{z}", font_size=18, color=WHITE)).move_to(curve_svg[0])
        lineOZ = Line(p0.get_center(), p1.get_center(), stroke_width=2)
        self.play(Write(set_svg), Write(lineOZ), Write(p0), Write(p1))



        
        sq = Square(side_length=1.9).move_to(curve_svg[1])
        #ANIM: point along line until proportion 0.1
        self.play(Write(sq))

        #NOTE: prove that this is possible
        cir = Circle(color=GREY).surround(sq, buffer_factor=0.68)
        self.play(Write(cir))

        #NOTE: try to measure in delta
        self.play(FadeOut(sq))
        
        #ANIM: point along line until proportion 0.1
        prop = 0.1
        predot = Dot(lineOZ.point_from_proportion(prop), color=GREY, fill_color=GREY)
        self.play(Write(predot), cir.animate.scale(0.8))

        ### Proof part 1
        self.play(update_list(steps, 0, h_1))

        #FIX: color is not grey...
        ldots = VGroup([Dot(lineOZ.point_from_proportion(i), color=GREY, fill_color=GREY) for i in np.arange(0.1, 1, 0.1)])
        self.add(ldots[0])
        self.remove(predot)


        self.play(Write(ldots[1]))
        self.play(Write(ldots[2:]))

        tr_ineq = MathTex(r"\metro{\ve{z}} \leq m\metro{\frac 1m \ve{z}}").next_to(lineOZ, UP)
        self.play(Write(tr_ineq))


        lineOZd = DashedLine(curve_svg[1], curve_svg[0], stroke_width=2)
        self.play(FadeOut(VGroup(tr_ineq, ldots)), ReplacementTransform(lineOZ, lineOZd))


        #
        # ### Proof part 2
        self.play(update_list(steps, 1, h_1))
        
        self.play(Write(curve_svg[5]))
        cdots = VGroup([Dot(curve_svg[5].point_from_proportion(i)) for i in np.arange(0.1, 1, 0.1)])

        self.play(Write(cdots))


        vecs = VGroup(Arrow(start=p0, end=cdots[0], color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3),
                      [Arrow(start=cdots[i], end=cdots[i+1], color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3) for i in range(0, len(cdots)-1)],
                      Arrow(start=cdots[-1], end=p1, color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3)
                      )

        self.play(Write(vecs), run_time=0.7)

        scaled_vecs = vecs.copy().scale(0.1, about_point=p0.get_center()).set_color(h_1)
        self.play(ReplacementTransform(vecs.copy(), scaled_vecs))

        sca_vec = Arrow(start=p0, end=predot.get_center(), color=h_1, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3)

        self.play(ReplacementTransform(scaled_vecs, sca_vec))

        self.play(cir.animate.set_color(h_1))

        eq1 = MathTex(r"= \sum_{i=1}^{m} \frac 1m")
        ga = Arrow(start=ORIGIN, end=UR, color=h_1, buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=3).scale(0.2).next_to(eq1, LEFT*0.5)
        ba = Arrow(start=ORIGIN, end=UR, color=h_2, buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=3).scale(0.2).next_to(eq1, RIGHT*0.5)

        konv_komb = VGroup(eq1, ga, ba).next_to(self.top, DOWN*0.5)

        ga2 = ga.copy()
        tex_in = MathTex(r"\in").next_to(ga2, RIGHT*0.5)
        gc = Circle(color=h_1).scale(0.1).next_to(tex_in, RIGHT*0.5)
        tex_conv = Tex(r" if $\metric$ balls are convex").next_to(gc, RIGHT*0.5)
        konv_ball = VGroup(ga2, tex_in, gc, tex_conv).next_to(konv_komb, DOWN)


        self.play(Write(konv_komb))

        self.play(Write(konv_ball))

        
        self.play(FadeOut(VGroup(konv_komb, konv_ball, sca_vec, vecs, cdots, cir, curve_svg[5])))

        self.next_section(skip_animations=False)

        # ### Proof part 3
        self.play(update_list(steps, 2, h_1))

        br1 = BraceLabel(VGroup(p0, ldots[0]),r"=\frac 1m \metro{z}",brace_direction=UP, font_size=20)
        self.play(Write(br1), Write(ldots[0]))

        self.play(Write(ldots[1].set_color(BLACK)), Write(ldots[2:]))

        br2 = BraceLabel(VGroup(p0, ldots[1]),r"\leq \frac 2m \metro{z}", brace_direction=UP,  font_size=20)


        #TODO: braces intersect fix, , brace_config={"sharpness":0.1} doesnt work I think
        br3 = BraceLabel(VGroup(ldots[1], p1), r"\leq \frac{m-2}{m} \metro{z}", font_size=20)
        br4 = BraceLabel(VGroup(p0, ldots[1]), r"\geq \frac 2m \metro{z}", font_size=20)

        self.play(ReplacementTransform(br1, br2))

        self.play(Write(br3))
        self.play(Write(br4))

        self.play(FadeOut(br3), br2.animate.set_color(h_1), br4.animate.set_color(h_1))

        # ### Proof part 4
        self.play(update_list(steps, 3, h_1))

        self.play(FadeOut(VGroup(br2, br4, set_svg, ldots, lineOZd, p0, p1)))


        
        approx = Tex(r"$\metro{\frac km \ve{z}} = \frac km \metro{\ve{z}}$ for arbitrary large $k$ and $m$").shift(UP)
        approx2 = Tex(r"$\metric$ continuous").next_to(approx, DOWN)
        approx3 = Tex(r"$t \in \mathbb{R}$ as limit of rational numbers").next_to(approx2, DOWN)

        self.play(Write(approx))
        self.play(Write(approx2))
        self.play(Write(approx3))
        # ### Proof finished
        self.play(steps[4].animate.set_color(h_1))

        # self.play(FadeOut(VGroup(approx, approx2)))
