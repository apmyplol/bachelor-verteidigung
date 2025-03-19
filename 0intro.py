from enum import unique
from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from svgelements import tostring
from afa_functions import *
import refs


config.write_to_movie = True
# config.renderer = "opengl"

#NOTE: in the beginning say the goals of this presentation: provide overview of the topics and the proofs
# That definitions are not 100% precise and focus on intuition


class Intro(Slide):
    def ns(self, *args, **kwargs):
        if isinstance(self, Slide):
            self.next_slide(*args, **kwargs)

    def wp(self, p1, p2):
        if isinstance(self, Slide):
            return self.wipe(p1, p2, return_animation=True)
        else:
            return [Unwrite(p1), Write(p2)]
            
    def update_title(self, title : Title_Section, new_title : str):
        new_t = Title_Section(new_title, color=h_2).move_to(title)
        old_t = title.tit
        title.tit = new_t.tit
        return self.wp(old_t, new_t.tit)

    def update_refs(self, ind: int) -> Animation:
        return self.wp(refs.refs[ind], refs.refs[ind+1].next_to(self.top[-2], LEFT))
        

    def construct(self):
        # self.next_section(skip_animations=True)
        self.wait_time_between_slides = 0.1

        self.start_and_content()

        part2 = self.emp_and_num_struct_thms()

        part3 = self.mental_representations(part2)

        part4 = self.ps_and_metric(part3)

        part5 = self.ad_model_seg_add(part4)

        part6 = self.unique_repr_thm(part5)
        
        self.homogen_thm(part6)

    


    
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

        self.play(self.wp(title, points))
        self.ns()

        
        top = initTop(self, "Representational Measurement", 0)

        self.play(ReplacementTransform(points, top[0:-2]), Write(top[-2:]), self.update_refs(0), run_time=1)
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
        self.play(Write(VGroup(weather_box, emp)),run_time=1)
        self.ns()
        #Numerical
        self.play(Write(VGroup(cels_box, num)),run_time=1)
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
        self.play(weather.animate.arrange_in_grid(rows=2), cels.animate.arrange_in_grid(rows=2), ReplacementTransform(arrs, fat_dash), func.animate.next_to(fat_dash, UP).shift(LEFT*2),)
        dp = MathTex(r":").next_to(func, RIGHT*0.3)
        self.play(homo_gr.animate.next_to(dp, RIGHT*0.5), Write(dp),run_time=1)
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
        self.play(self.wp(prev_part, VGroup(s1, s2)), *update_list(self.top, 0), self.update_title(self.top[-1], "Representation of Similarity"), self.update_refs(1))
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
        #ZI:_refs: FM2 and 
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
        self.play(self.wp(prev_part, c1), self.update_refs(2))
        self.ns()

        # Not possible to directly compare two colors
        self.play(Transform(c1[1], ques))
        self.ns()
        
        # But pairs are comparable wrt. similarity
        self.play(Write(c2))
        self.ns()

        # Restructure
        self.play(FadeOut(c1), c2.animate.next_to(self.top, DOWN), run_time=1)
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
        #ZI: similarity thing and FM2 chapters
        # Animate metric -> mink metric, transition from prev part
        mink_metr = Tex("Minkowski Metric: ")
        mink_eq = MathTex(r"\metric", "_p", "(", r"\ve{x}", ",", r"\ve{y}", r")= \left( \sum_{i=1}^{n} |", "x_i",  "-", "y_i", r"|^p \right)^{1/p}").next_to(mink_metr, RIGHT)
        mink = VGroup(mink_metr, mink_eq).arrange(RIGHT).next_to(self.top, DOWN)
        self.play(ReplacementTransform(prev_part[0], mink), FadeOut(prev_part[1]), self.update_refs(3))
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
        self.play(ReplacementTransform(ad_dec, ad_steps[0]), run_time=1)
        self.ns()

        # Intradim subtr.
        self.play(Indicate(ad_diff))
        self.play(ReplacementTransform(ad_diff, ad_steps[1]), run_time=1)
        self.ns()
        
        #Additivity
        self.play(Indicate(ad_sum))
        self.play(ReplacementTransform(ad_sum, ad_steps[2]), run_time=1)
        self.ns()

        # Back transform
        self.play(Indicate(ad_t_back))
        self.play(ReplacementTransform(ad_t_back, ad_steps[3]), run_time=1)
        self.ns()


        # AD Model
        ad_m1 = MathTex(r"G" ,r"\left( \sum_{i=1}^n", "F_i", r"(|", "x_i", "-", "y_i", r"|) \right)").scale(0.8).next_to(ad_steps, DOWN)
        self.play(Write(ad_m1), run_time=1)
        self.ns()

        # Reposition ad model
        self.play(FadeOut(VGroup(ad_steps, ad_m_func)),
                  ad_m1.animate.next_to(ad_m, DOWN), run_time=1)
        self.ns()

        # add ad Model condition
        ad_cond1 = MathTex("F_i", ",", "G", ":", r"\mathbb{R}_{\geq 0}", r"\rightarrow \mathbb{R}_{\geq 0}")
        ad_cond1[4].set_color(YELLOW_E)
        ad_cond2 = Tex("increasing")
        ad_conds = VGroup(ad_cond1, ad_cond2).arrange(RIGHT, MED_SMALL_BUFF).scale(0.9).next_to(ad_m1, DOWN)
        # ad_conds = BulletedList(r"$F_i, G: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$", "(strictly) increasing", buff=MED_SMALL_BUFF).scale(0.9)
        ad_defs = VGroup(ad_m1, ad_conds)
        self.play(FadeIn(ad_conds))
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
        self.ns()

        # add Two dots
        px = Dot(ax.c2p(4, 0), fill_color=d_color)
        pz = Dot(ax.c2p(1, 3), fill_color=h_2)
        self.play(Write(VGroup(ax, px, pz)), run_time=1)
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
        self.play(Write(VGroup(py, seg_add_ex)), run_time=1)
        self.ns()

        self.play(MoveAlongPath(py, pline_ndash))
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
        self.play(ReplacementTransform(seg_add_ex, seg_add_def[2]), ReplacementTransform(VGroup(ax, px, pz, pline, py), seg_add_def[0:2]), run_time=1)
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
        ad_met_cond1 = MathTex("F", ":", r"[0, \Omega]", r"\rightarrow \mathbb{R}_{\geq 0}")
        ad_met_cond1[2].set_color(YELLOW_E)
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
        self.play(
            Write(VGroup(seg_add_ps1, seg_arr)),
            FadeOut(seg_add_def[1:]),
            TransformMatchingTex(seg_add_def[0], seg_add_def0), run_time=1.5)
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
        return VGroup(VGroup(ad_metr1, ad_met_cond0, ad_met_cond1, ad_met_cond2 ,seg_add_def1), VGroup(mink_metr1, mink_eq1, seg_line, ad_line, arr_up, plus, seg_add_ps, seg_arr, ad_s, ad_arr, seg_add, ad_m))


    def unique_repr_thm(self, prev_part):
        ad_metr1 = prev_part[0][0].copy()
        ad_met_cond0 = prev_part[0][1].copy()
        ad_met_cond1 = prev_part[0][2].copy()
        ad_met_cond2 = prev_part[0][3].copy()
        seg_add_def1 = prev_part[0][4].copy()

        ad_met_cond0.scale(1.2)
        ad_metr1.scale(0.8)
        
        #ZI: FM2 thm page, uniqueness of quasi arithm means ref
        # move conditions
        conds = VGroup(ad_metr1, ad_met_cond0, ad_met_cond1, ad_met_cond2, seg_add_def1).arrange(DOWN, buff=MED_SMALL_BUFF).center().shift(LEFT*3)
        self.play(self.wp(prev_part, conds), *update_list(self.top, 1), self.update_title(self.top[-1], "Unique Representation Theorem"), self.update_refs(4))
        # self.play(ReplacementTransform(prev_part[0], conds), FadeOut(prev_part[1]), )
        self.ns()

        # Fade In the result we want to prove
        long_arr = MathTex(r"\Longrightarrow").scale(2).next_to(conds)
        f_res = MathTex(r"F(x) = \alpha x ^ p\\ p \geq 0").next_to(long_arr)
        self.play(FadeIn(VGroup(long_arr, f_res)))
        self.ns()

        # Add Theorem that we use and rectangle
        thm = Tex(r"""
		\begin{thm*}[Uniqueness of Homogeneous Quasi-Arithmetic Means]
			Suppose that $\phi$ is continuous and strictly increasing in the open interval $(0,\infty)$ and that
			\begin{equation*}
				\phi^{-1} \left( \sum_{i=1}^{N} w_i \phi(t x_i) \right) = t \phi^{-1} \left( \sum_{i=1}^{N} w_i \phi(x_i) \right) 
			\end{equation*}
			for all positive $\ve{x}, \ve{w}, t$ and all $N \in \mathbb{N}$ such that $\sum_{i=1}^{n} w_i = 1$. If $\phi > 0$ then $\phi(x) = \alpha x^p + \beta$ and $\alpha, \beta, p \in \mathbb{R}, p > 0$.
		\end{thm*}
        """).scale(0.8).to_edge(DOWN)
        thm_rect = SurroundingRectangle(thm, color=d_color)
        # Shift other stuff and add theorem
        self.play(conds.animate.scale(0.8).shift(UL+LEFT), f_res.animate.shift(UP).to_edge(RIGHT))
        sarr1 = MathTex(r"\Rightarrow").scale(2).next_to(conds)
        sarr2 = MathTex(r"\Rightarrow").scale(2).next_to(f_res, LEFT)
        self.play(ReplacementTransform(long_arr, VGroup(sarr1, sarr2)),FadeIn(VGroup(thm, thm_rect)))
        self.ns()

        # Add center part with function we want to derive
        to_prove_func = MathTex(r"F^{-1} \left( \sum_{i=1}^{N} w_i F(t x_i) \right) = t F^{-1} \left( \sum_{i=1}^{N} w_i F(x_i) \right)").scale(0.8)
        to_prove_conds = MathTex(r"\forall N \in \mathbb{N}\\", r"\forall t, x_i, w_i > 0")
        to_prove = VGroup(to_prove_func, to_prove_conds).arrange(DOWN, buff=MED_SMALL_BUFF).next_to(sarr1).shift(RIGHT*0.5)
        to_prove_box = SurroundingRectangle(to_prove, color=YELLOW_E)
        self.play(Write(VGroup(to_prove, to_prove_box)), run_time=1)
        self.ns()


        l_sep = Line(LEFT, RIGHT).shift(DOWN*0.5)
        l_sep.width = config["frame_width"]
        proof_steps_h = Tex("Proof Steps", color=d_color).next_to(l_sep, DOWN).scale(1.4)
        self.play(ReplacementTransform(VGroup(thm, thm_rect), VGroup(l_sep, proof_steps_h)))
        self.ns()

        # self.next_section(skip_animations=False)

        # Add text for the proof steps and arrange them with circled numbers
        n_text = [Tex(r"Homogeneity Thm.:\\$\rightarrow$ homog. for $t \in [0, 1]$"),
                  Tex(r"Extend $F$ to $\mathbb{R}_{\geq 0} \rightarrow \tilde F$"),
                  Tex(r"$\tilde F$ cont., monot. \& homog. $\forall t > 0 $"),
                  Tex(r"Increase summands $n \rightarrow N \in \mathbb{N}$"),
                  Tex(r"Incorporate weights $w_i$"),
                  Tex(r"$\tilde F = F$ for all $x \in \mathbb{R}_{\geq 0}$")]
        nums = VGroup()
        for i in range(1, 7):
            n = MathTex(str(i), color=d_color)
            c = Circle(color=d_color).surround(n, buffer_factor=1.5)
            t = n_text[i-1]
            nums += VGroup(VGroup(n, c), t).arrange(RIGHT, buff=MED_SMALL_BUFF)
        # Arrange downwards, add items 2-4 to center, 1 to left and 5 to right
        nums.arrange(DOWN, aligned_edge=LEFT)
        nums_center = VGroup(nums[1:5]).next_to(proof_steps_h, DOWN)
        nums[0].next_to(nums_center, LEFT).to_edge(LEFT)
        nums[-1].next_to(nums_center, RIGHT).to_edge(RIGHT)

        # add everything
        for i in range(0, 6):
            self.play(Write(nums[i]), run_time=1.0)
            self.ns()

        #return visible objects for next method
        return VGroup(nums, proof_steps_h, l_sep, to_prove, to_prove_box, f_res, conds, sarr1, sarr2)


    def homogen_thm(self, prev_part):
        #ZI: intradim sub, homogen thm page in FM2
        # Transition from before
        self.play(self.wp(prev_part, VGroup()), *update_list(self.top, 2), self.update_title(self.top[-1], "Homogeneity Theorem"), self.update_refs(5))
        self.ns()

        # Introduce intradim subr
        int_subtr = Tex("intradimenional subtractivity: ")
        intr_subtr_f = MathTex(r"\metr{\ve{x}}{\ve{z}} = F(|x_1 - z_1|, \dots, |x_n - z_n|)")
        int_f = VGroup(int_subtr, intr_subtr_f).arrange(RIGHT).center()
        self.play(Write(int_f), run_time=1)
        self.ns()

        # AD Models implies itradim subractivity
        text_admod = Tex(r"AD Model $\Rightarrow$").next_to(int_f, LEFT*0.5)
        self.play(Write(text_admod), run_time=1)
        self.ns()


        # Add Homogeneity THeorem statement
        thm = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        thm_0 = Tex(r"Let $S$ be an open convex subset of $n$-dimensional Euclidean space", r" with $\ve{0} \in S$",
                  r". Let $\metric$ be a metric on $S$ that satisfies intradimensional subtractivity with respect to a continuous function $F: \mathbb{R}_{\geq 0}^n \rightarrow \mathbb{R}_{\geq 0}$. If $\langle S, \metric \rangle$ is a metric space with additive segments, then $\metric$ is homogeneous, i.e., for any $\ve{z} \in S$ and $t \in [0,1]$")
        homo_eq = MathTex(r"\metric(",r"\ve{0},",r"t\ve{z})=t\metric(", r"\ve{0},",r"\ve{z})").next_to(thm, DOWN)
        homo_eq_0 = MathTex(r"\metric(",r"t\ve{z})=t\metric(", r"\ve{z})").move_to(homo_eq)
        thm_rect = SurroundingRectangle(VGroup(thm, homo_eq), color=d_color, buff=MED_LARGE_BUFF*0.6)
        self.play(FadeIn(VGroup(thm,thm_rect, homo_eq)), VGroup(int_subtr, intr_subtr_f, text_admod).animate.center().shift(2*UP), run_time=1)
        self.ns()


        # Transform delta notation with translation invariance
        thm_group = VGroup(thm_0, thm_rect, homo_eq_0)
        self.play(TransformMatchingTex(thm, thm_0), TransformMatchingTex(homo_eq, homo_eq_0))
        self.ns()


        # Short version of Theorem on top
        thm_stat_short1 = Tex(r"$S$ open, convex\\$\metr{\ve{x}}{\ve{z}}=F(\dots|x_i-z_i|\dots)$", font_size=20)
        thm_stat_short2 = Tex(r"$F$ cont. \& increasing\\$\metric$ metric w/ add. segments", font_size=20).next_to(thm_stat_short1, RIGHT)
        thm_res_short = Tex(r"$\Rightarrow$ homogeneous", font_size=20).next_to(thm_stat_short2, RIGHT*0.5)
        thm_short = VGroup(thm_stat_short1, thm_stat_short2, thm_res_short).next_to(self.top[-1].tit, RIGHT).to_edge(RIGHT)
        self.play(Write(thm_short, shift=UP), run_time=1)
        self.ns()

        # Fade out everything
        self.play(FadeOut(VGroup(text_admod, int_subtr, intr_subtr_f, thm_group)), run_time=0.5)
        self.ns()


        # Add proof steps
        steps = BulletedList(r"$\metric$ distance to set", 
                     r"$\frac 1m \metro{\ve{z}} \leq \metro{\frac 1m \ve{z}}$",
                     r"$\frac 1m \metro{\ve{z}} \geq \metro{\frac 1m \ve{z}}$",
                     r"$\frac km \metro{\ve{z}} = \metro{\frac km \ve{z}}$",
                     r"$t \metro{\ve{z}} = \metro{t \ve{z}}$",
                     font_size=30, buff=MED_SMALL_BUFF)

        self.play(FadeIn(steps), run_time=0.7)
        self.ns()

        # Animate steps to TR
        self.play(steps.animate.scale(0.7).next_to(self.top, DOWN).to_edge(LEFT).set_color(GREY), run_time=0.7)
        self.ns()
        
        # Start with the first step
        ### Proof part 0 
        # Add svg objects: Set and two pionts adn line between these points
        set_svg = SVGMobject("./images/2_homothm0.svg", use_svg_cache=False).scale(2.1).shift(DR + DOWN*0.8)
        curve_svg = SVGMobject("./images/2_homothm_curve.svg", use_svg_cache=False).scale(0.8).shift(DR+LEFT*0.5+DOWN*0.8)
        # 0 : z
        # 1-4: points
        # 5: curve
        # curve_svg[0]
        p0 = LabeledDot(MathTex(r"\ve{0}", font_size=18, color=WHITE), fill_color=d_color).move_to(curve_svg[1])
        p1 = LabeledDot(MathTex(r"\ve{z}", font_size=18, color=WHITE), fill_color=d_color).move_to(curve_svg[0])
        lineOZ = Line(p0.get_center(), p1.get_center(), stroke_width=2)
        self.play(steps[0].animate.set_color(BLACK),
                  Write(set_svg), Write(lineOZ), Write(p0), Write(p1), run_time=1)
        self.ns()



        # Add inf metric square
        sq = Square(side_length=1.9).move_to(curve_svg[1])
        self.play(Write(sq))
        self.ns()


        # Add metric ball inside square with radius line
        cir = Circle(color=GREY).surround(sq, buffer_factor=0.68)
        cir_l = LabeledLine(MathTex("r", font_size=16), start=p0.get_corner(UL)+DR*0.1, end=cir.point_at_angle(3*PI/4), stroke_width=2)
        cir_l.add_updater(lambda lab: lab.put_start_and_end_on(start=p0.get_corner(UL)+DR*0.1, end=cir.point_at_angle(3*PI/4)))
        self.play(Write(cir), Write(cir_l))
        self.ns()

        # Add condition for choice of m and dot
        m_cond = Tex(r"$m$ such that $\frac 1m \metro{\ve{z}} < r$").next_to(set_svg, UP)
        prop = 0.1
        predot = Dot(lineOZ.point_from_proportion(prop), color=GREY, fill_color=GREY)
        self.play(Write(predot), Write(m_cond), run_time=0.7)
        self.ns()

        # Fade out the Square, decrease circle radius
        self.play(cir.animate.scale(0.8),
                  ReplacementTransform(cir_l.label, Label(label=MathTex(r"\frac{\metro{\ve{z}}}{m}", font_size=10), box_config={"color":WHITE, "buff": 0}, frame_config={"buff":0, "stroke_width":0}).move_to(cir_l.label.get_center()+DR*0.1)))
        self.ns()


        ### Proof part 1
        self.play(FadeOut(VGroup(sq, m_cond)), update_list(steps, 0, h_1))
        self.ns()

        # Add second dot on line
        ldots = VGroup([Dot(lineOZ.point_from_proportion(i), color=GREY, fill_color=GREY) for i in np.arange(0.1, 1, 0.1)])
        self.add(ldots[0])
        self.remove(predot)
        self.play(Write(ldots[1]))
        self.ns()

        # Add all other dots on line
        self.play(Write(ldots[2:]))
        self.ns()

        # Triangle inequality m times
        tr_ineq = MathTex(r"\metro{\ve{z}} \leq m\metro{\frac 1m \ve{z}}").next_to(lineOZ, UP)
        self.play(Write(tr_ineq))
        self.ns()


        # Make line dashed, transition to next part
        lineOZd = DashedLine(curve_svg[1], curve_svg[0], stroke_width=2)
        self.play(FadeOut(VGroup(tr_ineq, ldots)),
                  ReplacementTransform(lineOZ, lineOZd),
                  update_list(steps, 1, h_1),
                  run_time=1)
        self.ns()

        # ### Proof part 2
        # Write curve 
        self.play(Write(curve_svg[5]))
        self.ns()

        # equally space points on curve
        cdots = VGroup([Dot(curve_svg[5].point_from_proportion(i)) for i in np.arange(0.1, 1, 0.1)])
        self.play(Write(cdots))
        self.ns()

        # Vectors for consecutive points on curve
        vecs = VGroup(Arrow(start=p0, end=cdots[0], color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3),
                      [Arrow(start=cdots[i], end=cdots[i+1], color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3) for i in range(0, len(cdots)-1)],
                      Arrow(start=cdots[-1], end=p1, color=h_2, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3)
                      )
        self.play(Write(vecs), run_time=0.7)
        self.ns()

        # scaled vectors my 1/m
        scaled_vecs = vecs.copy().scale(0.1, about_point=p0.get_center()).set_color(h_1)
        self.play(ReplacementTransform(vecs.copy(), scaled_vecs))
        self.ns()

        # Transform vector sum to one vector
        # and Change circle color to green to indicate connection
        sca_vec = Arrow(start=p0, end=predot.get_center(), color=h_1, buff=0, max_tip_length_to_length_ratio=0.2, stroke_width=3)
        self.play(ReplacementTransform(scaled_vecs, sca_vec),
                  cir.animate.set_color(h_1),
                  run_time=1)
        self.ns()


        # Add convex comb equation
        eq1 = MathTex(r"= \sum_{i=1}^{m} \frac 1m")
        ga = Arrow(start=ORIGIN, end=UR, color=h_1, buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=3).scale(0.2).next_to(eq1, LEFT*0.5)
        ba = Arrow(start=ORIGIN, end=UR, color=h_2, buff=0, max_tip_length_to_length_ratio=0.1, stroke_width=3).scale(0.2).next_to(eq1, RIGHT*0.5)
        konv_komb = VGroup(eq1, ga, ba).next_to(self.top, DOWN*0.5)
        self.play(Write(konv_komb), run_time=0.7)
        self.ns()

        # convexity of balls
        ga2 = ga.copy()
        tex_in = MathTex(r"\in").next_to(ga2, RIGHT*0.5)
        gc = Circle(color=h_1).scale(0.1).next_to(tex_in, RIGHT*0.5)
        tex_conv = Tex(r" if $\metric$ balls are convex").next_to(gc, RIGHT*0.5)
        konv_ball = VGroup(ga2, tex_in, gc, tex_conv).next_to(konv_komb, DOWN)
        self.play(Write(konv_ball), run_time=0.7)
        self.ns()

        # Fade out, transition to next slide
        self.play(FadeOut(VGroup(konv_komb, konv_ball, sca_vec, vecs, cdots, cir, cir_l, curve_svg[5])),
                update_list(steps, 2, h_1))
        self.ns()


        # ### Proof part 3
        # Brace to indicate 1/m homogeneity
        br1 = BraceLabel(VGroup(p0, ldots[0]),r"=\frac 1m \metro{z}",brace_direction=UP, font_size=20)
        self.play(Write(br1), Write(ldots[0]))
        self.ns()

        # indicate that we want toe distance to the second point
        self.play(Write(ldots[1].set_color(BLACK)), Write(ldots[2:]))
        self.ns()

        # Change to 2/m brace with triangle ineq
        br2 = BraceLabel(VGroup(p0, ldots[1]),r"\leq \frac 2m \metro{z}", brace_direction=UP,  font_size=20)
        self.play(ReplacementTransform(br1, br2))
        self.ns()


        # Braces from below, double triangle inequality
        br3 = BraceLabel(VGroup(ldots[1], p1), r"\leq \frac{m-2}{m} \metro{z}", font_size=20)
        br4 = BraceLabel(VGroup(p0, ldots[1]), r"\geq \frac 2m \metro{z}", font_size=20)
        # m-2/m
        self.play(Write(br3))
        self.ns()
        
        #reverse 2/m
        self.play(Write(br4))
        self.ns()

        # Transition next part
        self.play(FadeOut(br3), br2.animate.set_color(h_1), br4.animate.set_color(h_1))
        self.ns()

        # Fade Out everything
        # ### Proof part 4
        self.play(update_list(steps, 3, h_1), FadeOut(VGroup(br2, br4, set_svg, ldots, lineOZd, p0, p1)))
        self.ns()

        
        # Text: approximate with rationals
        approx = Tex(r"$\metro{\frac km \ve{z}} = \frac km \metro{\ve{z}}$ for arbitrary large $k$ and $m$").shift(UP)
        approx2 = Tex(r"$\metric$ continuous").next_to(approx, DOWN)
        approx3 = Tex(r"$t \in \mathbb{R}$ as limit of rational numbers").next_to(approx2, DOWN)
        self.play(Write(VGroup(approx, approx2, approx3)))
        self.ns()

        # ### Proof finished
        self.play(steps[4].animate.set_color(h_1))
        self.ns()


        self.play(
                self.wp(VGroup(approx, approx2, approx3, steps, thm_short), refs.refs[-1]),
                *update_list(self.top, 3), self.update_title(self.top[-1], "References"),
            self.update_refs(6)
        )
        self.wait(1)

class test(Scene):
    def construct(self):
        top = initTop(self, "Representation of Similarity", 1)
        self.add(top)
        self.embed()

        tuda_logo_svg = SVGMobject("./images/tuda_logo_RGB.svg", use_svg_cache=False)
        tuda_logo = tuda_logo_svg[1:].to_corner(UR)
        tuda_logo.scale(0.6, about_point=tuda_logo.get_corner(UR)).shift(UR*0.45)

        self.add(tuda_logo)

