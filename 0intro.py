from enum import unique
from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from afa_functions import *



config.write_to_movie = True
# config.renderer = "opengl"

#NOTE: in the beginning say the goals of this presentation: provide overview of the topics and the proofs
# That definitions are not 100% precise and focus on intuition


class Intro(Scene):
    def ns(self, *args, **kwargs):
        if isinstance(self, Slide):
            self.next_slide(*args, **kwargs)

    def wp(self, p1, p2):
        if isinstance(self, Slide):
            self.wipe(p1, p2)
        else:
            self.play(Unwrite(p1), Write(p2))
            

    def construct(self):
        self.next_section(skip_animations=True)
        self.wait_time_between_slides = 0.1


        self.start_and_content()

        part2 = self.emp_and_num_struct_thms()

        part3 = self.mental_representations(part2)

        part4 = self.ps_and_metric(part3)

        part5 = self.ad_model_seg_add(part4)
    


    
    def start_and_content(self):
        title = Title_Presentation(title= "Representational Measurement of Similarity: The Additive-Difference Model, Revisited",
                                    affiliation= "TU Darmstadt",
                                    author= "Arthur Liske")
        self.add(title)
        self.wait(1)
        self.ns()

        points = BulletedList(r"Representational Measurement",
                 r"Representation of Similarity",
                 r"Unique Representation Theorem",
                 r"Homogeneity Theorem",
                 r"Discussion",
                buff=MED_SMALL_BUFF)

        self.wp(title, points)
        self.ns()

        
        top = initTop(self, "Representational Measurement", 0)

        self.play(ReplacementTransform(points, top[0:5]))
        self.add(top[-1])
        self.ns()

        self.top = top


    def emp_and_num_struct_thms(self):
        # Write measurement definition
        mes_def = Tex(r"Loosely speaking, measurement is the quantification of observations.")
        self.play(Write(mes_def), run_time=1)
        self.ns()

        # Example with weather
        sun = SVGMobject("./images/emoji_sun.svg", use_svg_cache=False)
        sunny_cloud = SVGMobject("./images/emoji_sunny_cloud.svg", use_svg_cache=False).next_to(sun)
        cloud = SVGMobject("./images/emoji_cloud.svg", use_svg_cache=False).next_to(sunny_cloud)
        snow_cloud = SVGMobject("./images/emoji_snow_cloud.svg", use_svg_cache=False).next_to(cloud)
        weather = VGroup(sun, sunny_cloud, cloud, snow_cloud).scale(0.3).arrange(DOWN).to_edge(LEFT).shift(RIGHT*2.5+DOWN)
        self.play(Write(weather), mes_def.animate.next_to(self.top, DOWN*0.5), run_time=1)
        self.ns()


        # add Celsius degrees to example with arrows
        cels = VGroup(MathTex(r"30^\circ C"),
                    MathTex(r"17^\circ C"),
                    MathTex(r"9^\circ C"),
                    MathTex(r"-2^\circ C"),
                     ).scale(1.3).arrange(DOWN, buff=MED_LARGE_BUFF*1.2).to_edge(RIGHT).shift(LEFT*2.5+DOWN)
        arrs = VGroup([DashedVMobject(CurvedArrow(weather[i].get_center()+RIGHT*0.5, cels[i].get_center() + LEFT*0.6, angle=-TAU/8, tip_length=0.2), dashed_ratio=0.7) for i in range(0, 4)])
        self.play(Write(cels), Write(arrs))
        self.ns()


        # Empirical structure and numerical structure
        weather_box = SurroundingRectangle(weather, color=d_color)
        emp = Tex(r"Empirical\\Structure").next_to(weather_box, DOWN)
        cels_box = SurroundingRectangle(cels, color=d_color)
        num = Tex(r"Numerical\\Structure").next_to(cels_box, DOWN)
        #Empirical
        self.play(Write(VGroup(weather_box, emp)))
        self.ns()
        #Numerical
        self.play(Write(VGroup(cels_box, num)))
        self.ns()


        # Hmomorphism delta 
        func = MathTex(r"\metric").scale(1.5).next_to(arrs, UP)
        self.play(Write(func))
        self.ns()

        # Show the homomorphism property
        # sun <= clouds <=> f(sun) <= f(clouds)
        sun_1 = weather[0].copy().scale(0.5)
        ssim = MathTex(r"\quad \succsim ~")
        cl_1 = weather[2].copy().scale(0.5)
        midtex = MathTex(r"~ \iff \metric(")
        sun_2 = sun_1.copy()
        midtex2 = MathTex(r") \geq \metric(")
        cl_2 = cl_1.copy()
        endtex = MathTex(r")")
        homo_gr1 = VGroup(sun_1, ssim, cl_1).arrange(RIGHT,buff=0.1)
        homo_gr2 = VGroup(midtex, sun_2, midtex2, cl_2, endtex).arrange(RIGHT, buff=0)
        homo_gr = VGroup(homo_gr1,homo_gr2).arrange(RIGHT, buff=0.2).next_to(arrs, DOWN)
        self.play(ReplacementTransform(VGroup(weather[0], weather[2], cels[0], cels[2], arrs[0], arrs[2]).copy(),homo_gr))
        self.ns()


        # Change box sizes to add existence & repr theorem
        weather_box.add_updater(lambda rect: rect. become(SurroundingRectangle(weather, color=d_color)))
        cels_box.add_updater(lambda rect: rect.become(SurroundingRectangle(cels, color=d_color)))
        emp.add_updater(lambda emp: emp.next_to(weather_box, DOWN))
        num.add_updater(lambda num: num.next_to(cels_box, DOWN))
        # Homomorphism arrow
        fat_dash = CurvedArrow(weather.get_center()+RIGHT, cels.get_center() + 1.16*LEFT, angle=-TAU/8, tip_length=0.4, stroke_width=4)
        # Animate everything
        self.play(weather.animate.arrange_in_grid(rows=2), cels.animate.arrange_in_grid(rows=2), ReplacementTransform(arrs, fat_dash), func.animate.next_to(fat_dash, UP).shift(LEFT*2))
        dp = MathTex(r":").next_to(func, RIGHT*0.3)
        self.play(homo_gr.animate.next_to(dp, RIGHT*0.5), Write(dp))
        self.ns()

        
        # Existence Theorem
        existThm2 = Tex(r"Proves existence of homomorphism $\metric$").next_to(homo_gr, UP*2)
        existThm = Tex(r"Existence/Representation Theorem:", color=d_color).scale(1.2).next_to(existThm2, UP)
        self.play(FadeIn(VGroup(existThm2, existThm)))
        self.ns()


        # Uniqueness Theorem example d'
        fat_dash_dot = DashedVMobject(CurvedArrow(weather.get_center()+RIGHT, cels.get_center() + 1.16*LEFT, angle=TAU/8, tip_length=0.3, stroke_width=4)).shift(DOWN*0.5)
        dels = MathTex(r"\metric'").scale(1.5).next_to(fat_dash_dot, DOWN)
        self.play(Write(fat_dash_dot), Write(dels), run_time=0.6)
        self.ns()
        # Uniqueness Theorem
        uniqueThm = Tex(r"Uniqueness Theorem:", color=d_color).scale(1.2).next_to(dels, DOWN)
        uniqueThm2 = Tex(r"Proves ``how many'' such homomorphisms exist").next_to(uniqueThm, DOWN)
        self.play(FadeIn(VGroup(uniqueThm, uniqueThm2)))
        self.ns()
        
        #return old objects for wipe
        return VGroup(uniqueThm, uniqueThm2, fat_dash_dot, dels, fat_dash, existThm, existThm2, weather, cels, emp, num, weather_box, cels_box, dp, mes_def, homo_gr, func)

    def mental_representations(self, prev_part):
        #Transition to next part
        s1 = Tex(r"CogSci and Psychology are interested in mental representations:").shift(UP*2)
        s2 = Tex(r"How external reality is modelled in the mind.").next_to(s1, DOWN)
        self.wp(prev_part, VGroup(s1, s2))
        self.play(*update_list(self.top, 0))
        self.ns()

        # Dimensional and categorical representation
        dim = Tex("Dimensions").scale(1.4).next_to(s2, DL*1.7).shift(DOWN*0.5)
        cate = Tex("Categorizations").scale(1.4).next_to(s2, DR*1.7).shift(DOWN*0.5)
        self.play(FadeIn(VGroup(dim, cate)))
        self.ns()


        #ANIM: maybe animate colors
        # dot = Dot(fill_color="#e65639")
        #
        # dot_colors = hex_to_rgb(dot.color)
        #
        # r_dot = Dot(fill_color=rgb_to_color([dot_colors[0], 0.0, 0.0]))
        # g_dot = Dot(fill_color=rgb_to_color([0.0, dot_colors[1], 0.0]))
        # b_dot = Dot(fill_color=rgb_to_color([0.0, 0.0, dot_colors[2]]))


        # Dimensional examples
        dim_ex = BulletedList("Color: RGB, HSV",
                              "Speech: pitch, loudness, speech rate").next_to(dim, DOWN)
        self.play(Write(dim_ex), run_time=1)
        # dots=VGroup(dot, r_dot, g_dot, b_dot).arrange(RIGHT).next_to(dim_ex[0], RIGHT)
        # self.add(dots)
        self.ns()

        # Categorical examples
        cat_ex = BulletedList("Color: light, dark, warm, cold",
                              "Faces: happy, angry, sad").next_to(cate, DOWN)
        self.play(Write(cat_ex), run_time=1)
        self.ns()

        #return objects on screen
        return VGroup(cat_ex, dim_ex, cate, dim, s1, s2)

    def ps_and_metric(self, prev_part):
        # Transition to next part
        # Next section, introducing similarity measurement
        c1 = MathTex(r"\bullet", r"\succsim", r"\bullet").scale(1.5)
        c2 = MathTex("(", r"\bullet", "," , r"\bullet", r") \succsim (", r"\bullet", ",", r"\bullet", ")").scale(1.5).next_to(c1, DOWN)
        ques = Tex("?", color=RED).scale(1.5)
        c1[0].set_color(GREEN)
        c1[2].set_color(d_color)
        c2[1].set_color(ORANGE)
        c2[3].set_color(GREEN)
        c2[5].set_color("#eab4fa")
        c2[7].set_color(d_color)
        self.wp(prev_part, c1)
        self.ns()

        # Not possible to directly compare two colors
        self.play(Transform(c1[1], ques))
        self.ns()
        
        # But pairs are comparable wrt. similarity
        self.play(Write(c2))
        self.ns()

        # Restructure
        self.play(FadeOut(c1))
        self.play(c2.animate.next_to(self.top, DOWN))
        self.ns()


        # Introduce Proximity Structure and Metric
        prox_st = Tex("Proximity Structure", color=d_color).scale(1.5).to_edge(LEFT).shift(RIGHT+DOWN*0.5)
        metric = Tex("Metric", color=d_color).scale(1.5).to_edge(RIGHT).shift(LEFT*2+DOWN*0.5)
        self.play(Write(VGroup(prox_st, metric)), run_time=1)
        self.ns()


        # Metric def
        met_def0 = Tex(r"$\metric$ is a metric on $X$ iff for all $x, y, z \in X$:")
        met_def1 = BulletedList(r"$\metr{x}{x} = 0$ and $\metr{x}{y} > 0$ if $x \neq y$",
                                r"$\metr{x}{y} = \metr{y}{x}$",
                                r"$\metr{x}{y} + \metr{y}{z} \geq \metr{x}{z}$"
                                ,buff=MED_SMALL_BUFF)
        met_def = VGroup(met_def0, met_def1).arrange(DOWN).next_to(metric, DOWN)
        self.play(FadeIn(met_def))
        self.ns()

        #PS def
        ps_def0 = Tex(r"$\langle \ps{A}, \succsim \rangle$ is a PS iff for all $\ps{a}, \ps{b} \in \ps{A}:$")
        ps_def1 = BulletedList(r"$\succsim$ is connected and transitive",
                               r"$(\ps{a}, \ps{b}) \succsim (\ps{a}, \ps{a})$ for $\ps{a} \neq \ps{b}$",
                               r"$(\ps{a}, \ps{a}) \sim (\ps{b}, \ps{b})$ (minimality)",
                               r"$(\ps{a}, \ps{b}) \sim (\ps{b}, \ps{a})$ (symmetry)",
                               buff=MED_SMALL_BUFF)
        ps_def = VGroup(ps_def0, ps_def1).arrange(DOWN).next_to(prox_st, DOWN)
        self.play(FadeIn(ps_def))
        self.ns()


        # Introduce Homomorphism
        homo_tex = Tex(r"$\metric$ homomorphism:").scale(1.2).next_to(self.top, DOWN)
        d1 = MathTex(r"\iff \metric", "(", r"\bullet", "," , r"\bullet", r") \geq \metric (", r"\bullet", ",", r"\bullet", ")").scale(1.5)
        d1[2].set_color(ORANGE)
        d1[4].set_color(GREEN)
        d1[6].set_color("#eab4fa")
        d1[8].set_color(d_color)
        homo_ex = VGroup(c2, d1).arrange(RIGHT).scale(0.7).next_to(homo_tex, DOWN)
        # And its equation
        homo_eq = MathTex(r"""
                            (\ps{a}, \ps{b}) \succsim (\ps{c}, \ps{d})
                            \iff
                            \delta(\ps{a}, \ps{b}) \geq \delta(\ps{c}, \ps{d})
        """).scale(1.2).next_to(homo_ex, DOWN)
        self.play(FadeIn(VGroup(homo_ex, homo_tex)), Write(homo_eq))
        self.ns()

        return [metric, VGroup(homo_eq, homo_ex, homo_tex, met_def, ps_def, prox_st)]


    def ad_model_seg_add(self, prev_part):
        # Animate metric -> mink metric, transition from prev part
        mink_metr = Tex("Minkowski Metric: ")
        mink_eq = MathTex(r"\metric", "_p", "(", r"\ve{x}", ",", r"\ve{y}", r")= \left( \sum_{i=1}^{n} |", "x_i",  "-", "y_i", r"|^p \right)^{1/p}").next_to(mink_metr, RIGHT)
        mink = VGroup(mink_metr, mink_eq).arrange(RIGHT).next_to(self.top, DOWN)
        self.play(ReplacementTransform(prev_part[0], mink), FadeOut(prev_part[1]))
        self.ns()



        # AD Model
        # sep = Line(ORIGIN, DOWN*5, color=h_3)
        # self.add(sep)
        ad_m = Tex("AD Model", color=d_color).scale(1.3).shift(LEFT*3.5+UP*0.5)
        seg_add = Tex("Segmental Additivity", color=d_color).scale(1.3).shift(RIGHT*3.5+UP*0.5)
        self.play(Write(VGroup(ad_m, seg_add)), run_time=1)
        self.ns()

        # Segmental Additivity
        ad_m_func = MathTex(r"\left(",
                            r"\sum", "_{i=1}", "^n",
                            "|", "x", "_i", "-", "y", "_i", "|", "^p",
                            r"\right)", "^{1/p}").next_to(ad_m, DOWN)
        self.play(FadeIn(ad_m_func), run_time=0.5)
        self.ns()

        # Transition from equation to steps
        ad_dec = VGroup(ad_m_func[5:7], ad_m_func[8:10]).copy()
        ad_diff = VGroup(ad_m_func[4:12]).copy()
        ad_sum = VGroup(ad_m_func[1:4]).copy()
        ad_t_back = VGroup(ad_m_func[-1]).copy()
        ad_steps = BulletedList(
            r"Decompose $\ve{x}$ and $\ve{y}$ into $(x_1, \dots x_n)$ and $(y_1, \dots, y_n)$",
            r"Coordinatewise differences $|x_i - y_i|$ and apply $F(x)$",
            r"Sum up the transformed differences",
            r"Transform the sum with $F^{-1}$",
            buff=MED_SMALL_BUFF
            ).scale(0.85).next_to(ad_m_func, DOWN)
        
        # Decomp
        self.play(Indicate(ad_dec))
        self.play(ReplacementTransform(ad_dec, ad_steps[0]))
        self.ns()

        # Intradim subtr.
        self.play(Indicate(ad_diff))
        self.play(ReplacementTransform(ad_diff, ad_steps[1]))
        self.ns()
        
        #Additivity
        self.play(Indicate(ad_sum))
        self.play(ReplacementTransform(ad_sum, ad_steps[2]))
        self.ns()

        # Back transform
        self.play(Indicate(ad_t_back))
        self.play(ReplacementTransform(ad_t_back, ad_steps[3]))
        self.ns()


        # AD Model
        ad_m1 = MathTex(r"G" ,r"\left( \sum_{i=1}^n", "F_i", r"(|", "x_i", "-", "y_i", r"|) \right)").scale(0.8).next_to(ad_steps, DOWN)
        self.play(Write(ad_m1))
        self.ns()

        # Reposition ad model
        self.play(FadeOut(VGroup(ad_steps, ad_m_func)))
        self.ns()

        # add ad Model condition
        ad_cond1 = MathTex("F_i", ",", "G", r": \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}")
        ad_cond2 = Tex("increasing")
        ad_conds = VGroup(ad_cond1, ad_cond2).arrange(RIGHT, MED_SMALL_BUFF).scale(0.9)
        # ad_conds = BulletedList(r"$F_i, G: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$", "(strictly) increasing", buff=MED_SMALL_BUFF).scale(0.9)
        ad_defs = VGroup(ad_m1, ad_conds).arrange(DOWN).next_to(ad_m, DOWN)
        self.play(FadeIn(ad_defs))
        self.ns()


        # Segmental additivity
        # Add axes
        ax = Axes(
            x_range = [0, 5],
            y_range = [0, 5],
            x_length=3,
            y_length=3,
            # axis_config = {"include_numbers": True},
            tips = False
        ).next_to(seg_add, DOWN)
        self.play(Write(ax))
        self.ns()

        # add Two dots
        px = Dot(ax.c2p(4, 0), fill_color=d_color)
        pz = Dot(ax.c2p(1, 3), fill_color=h_2)
        self.play(Write(VGroup(px, pz)))
        self.ns()

        # line between dots
        pline = DashedLine(start = px, end = pz, color=GREY)
        pline_ndash = Line(start=px, end=pz)
        self.play(Write(pline), run_time=0.6)
        self.ns()

        # third point on line moving & additivity equation
        py = Dot(fill_color=h_1).scale(0.7).move_to(px)
        seg_add_ex = MathTex(
            r"\metric_{p}(", r"\bullet", ",", r"\bullet", ")", "+",
            r"\metric_{p}(", r"\bullet", ",", r"\bullet", ")", "=",
            r"\metric_{p}(", r"\bullet", ",", r"\bullet", ")"
        ).next_to(ax, DOWN)
        seg_add_ex[1].set_color(h_2)
        seg_add_ex[3].set_color(h_1)
        seg_add_ex[7].set_color(seg_add_ex[3].get_color())
        seg_add_ex[9].set_color(d_color)
        seg_add_ex[13].set_color(seg_add_ex[1].get_color()) 
        seg_add_ex[15].set_color(seg_add_ex[9].get_color()) 
        self.play(Write(seg_add_ex), MoveAlongPath(py, pline_ndash), run_time=1.5)
        self.ns()


        # Seg add definition
        seg_add_def0 = Tex(r"$\langle X, \metric\rangle$", r"metric space with add. segments", r"iff $\forall x, z \in X$:", arg_separator=" ")
        seg_add_def1 = BulletedList(
            r"$\exists$ curve with finite length connecting $x$ and $z$",
            r"$\forall$ $y$ on that curve, the distances are additive:"
        ,buff=MED_SMALL_BUFF)
        seg_add_def3 = MathTex(
            r"\metr{x}{y} + \metr{y}{z} = \metr{x}{z}"
        )
        seg_add_def = VGroup(seg_add_def0, seg_add_def1, seg_add_def3).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(seg_add, DOWN).scale(0.9)
        self.play(ReplacementTransform(seg_add_ex, seg_add_def[2]), ReplacementTransform(VGroup(ax, px, pz, pline, py), seg_add_def[0:2]))
        self.ns()


        # AD structure yields AD Model with phi_i
        ad_s1 = Tex("AD Structure", color=d_color).scale(1.3).next_to(ad_defs, DOWN).to_edge(DOWN)
        ad_arr = Arrow(color=d_color, stroke_width=10,start=ORIGIN, end=UP*1.5, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=25).next_to(ad_s1, UP)
        ad_m_ps = MathTex(r"\metr{\ps{a}}{\ps{b}}=", "G" ,r"\left( \sum_{i=1}^n", "F_i", r"(|", r"\varphi_i(\ps{a}_i)", "-", r"\varphi_i(\ps{b}_i)", r"|) \right)").scale(0.9).move_to(ad_m1)
        ad_met_cond0 = MathTex(r"\varphi_i: \ps{A}_i \rightarrow \mathbb{R}").scale(0.9).next_to(ad_cond1, DOWN)
        # Arrow and AD Structure
        self.play(Write(VGroup(ad_s1, ad_arr)))
        self.ns()
        #  yields ad model with phi_i
        self.play(TransformMatchingTex(ad_m1, ad_m_ps), Write(ad_met_cond0))
        self.ns()


        # ad model becomes metric
        ad_metr1 = MathTex(r"\metr{\ps{a}}{\ps{b}}=",r"F^{-1}" ,r"\left( \sum_{i=1}^n", "F", r"(|", r"\varphi_i(\ps{a}_i)", "-", r"\varphi_i(\ps{b}_i)", r"|) \right)").move_to(ad_m_ps)
        ad_met_cond1 = MathTex("F", ",", "F^{-1}", r": \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}")
        ad_met_cond2 = Tex("increasing", r"\& cont.", arg_separator=" ")
        VGroup(ad_met_cond1, ad_met_cond2).arrange(RIGHT).next_to(ad_metr1, DOWN)
        ad_s = Tex("AD Structure", r"\& $\metric$ metric$^*$", color=d_color, arg_separator=" ").scale(1.2).move_to(ad_s1)
        # Transform ad structure -> + metric
        self.play(TransformMatchingTex(ad_s1, ad_s))
        self.ns()
        # transform F_i and G into F^{-1} and F, add continuity and F(0)=0
        self.play(TransformMatchingTex(ad_m_ps, ad_metr1))
        self.play(TransformMatchingTex(ad_cond1, ad_met_cond1), TransformMatchingTex(ad_cond2, ad_met_cond2),ad_met_cond0.animate.shift(LEFT*0.6))
        self.ns()



        # Seg add PS yields Metr. space with add segments
        # Segmental additive PS
        seg_add_ps1 = Tex("Segmentally Additive PS", color=d_color).scale(1.2).next_to(seg_add_def, DOWN).to_edge(DOWN)
        seg_arr = Arrow(color=d_color, stroke_width=10, start=ORIGIN, end=UP*1.5, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=25).next_to(seg_add_ps1, UP)
        seg_add_def0 = Tex(r"$\langle \ps{A}, \metric\rangle$", r"metric space with add. segments", arg_separator=" ").move_to(seg_add_def[0])
        seg_arr = Arrow(color=d_color, stroke_width=10, start=ORIGIN, end=UP*1.5, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=25).next_to(seg_add_ps1, UP)

        # Fade out old def, make A seg add metric space, add seg add. ps
        self.play(FadeOut(seg_add_def[1:]))
        self.play(TransformMatchingTex(seg_add_def[0], seg_add_def0))
        self.play(Write(VGroup(seg_add_ps1, seg_arr)))
        self.ns()

        # seg add metric spaces becomes complete
        seg_add_def1 = Tex(r"$\langle \ps{A}, \metric\rangle$", "complete", r"metric space\\ with add. segments", arg_separator=" ").move_to(seg_add_def[0])
        seg_add_ps = Tex(r"Complete", "Segmentally Additive PS", color=d_color, arg_separator=" ").scale(1.2).next_to(seg_add_def, DOWN).to_edge(DOWN)
        self.play(TransformMatchingTex(seg_add_def0, seg_add_def1), TransformMatchingTex(seg_add_ps1, seg_add_ps))
        self.ns()

        # Combining both things
        plus = MathTex(r"\oplus", color=YELLOW_E).scale(2).shift(UP*0.5+LEFT*0.5)
        arr_up = Arrow(color=YELLOW_E, stroke_width=10, start=plus.get_center(), end=plus.get_center()+UP, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=25)
        seg_line = Line(plus.get_edge_center(RIGHT), seg_add.get_edge_center(LEFT)+0.1*LEFT, stroke_width=10, color=YELLOW_E)
        ad_line = Line(ad_m.get_edge_center(RIGHT)+0.1*RIGHT, plus.get_edge_center(LEFT), stroke_width=10, color=YELLOW_E)
        thm_transition = VGroup(plus, arr_up, ad_line, seg_line)
        # Add combination lines and plus
        self.play(Write(thm_transition))
        self.ns()
        
        # Mink becomes mink on prox struct
        mink_eq1 = MathTex(r"\metric", "(", r"\ps{a}", ",", r"\ps{b}", r")= \left( \sum_{i=1}^{n} |", r"\varphi_i(\ps{a}_i)",  "-", r"\varphi_i(\ps{b}_i)", r"|^p \right)^{1/p}").move_to(mink_eq)
        mink_metr1 = Tex(r"$\metric$ Homomorphism: ").next_to(mink_eq1, LEFT*0.8)
        self.play(TransformMatchingTex(mink_metr, mink_metr1), TransformMatchingTex(mink_eq, mink_eq1), thm_transition.animate.set_color(GREEN))
        return VGroup(mink_metr1, seg_line, ad_line, arr_up, plus, seg_add_ps, seg_arr, ad_s, ad_arr, seg_add, ad_m)

class test(Scene):
    def construct(self):
        top = initTop(self, "Representation of Similarity", 1)
        self.add(top)



        metric = Tex("Metric", color=d_color).scale(1.5).to_edge(RIGHT).shift(LEFT*2+DOWN*0.5)
        self.add(metric)
        self.embed()



