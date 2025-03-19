from afa_functions import *

finalrefs = Cite(r"""
\nocite{foundations1}
\nocite{foundations2}
\nocite{TheorieDesMessens}
\nocite{handbookMeans}
\printbibliography
""").scale(2).shift(DOWN)

ref11 = Cite(r"\parencite[pp. 8-12]{foundations1}")
ref12 = Cite(r"\parencite[pp. 14-27]{TheorieDesMessens}")
ref1 = VGroup(ref11, ref12).arrange(DOWN, buff=SMALL_BUFF)

ref2 = Cite(r"\parencite[p. 160]{foundations2}")

ref3 = Cite(r"\parencite[p. 161]{foundations2}")

ref41 = Cite(r"\parencite[Chapters 14.2-14.4]{foundations2}")
ref42 = Cite(r"\parencite{tversky1970dimensional}")
ref4 = VGroup(ref41, ref42).arrange(DOWN, buff=SMALL_BUFF)

ref51 = Cite(r"\parencite[p. 187]{foundations2}")
ref52 = Cite(r"\parencite[p. 272]{handbookMeans}")
ref5 = VGroup(ref51, ref52).arrange(DOWN, buff=SMALL_BUFF)

ref6 = Cite(r"\parencite[pp. 194-196]{foundations2}")

# add empty vgroup for first slide animation
refs = [VGroup(), ref1, ref2, ref3, ref4, ref5, ref6, VGroup(), finalrefs]
