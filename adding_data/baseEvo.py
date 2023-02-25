import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# base form será a primeira evolução do pokemon
# idependente de ser uma baby form de uma geração futura

df = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\pokemon.csv')

# INCLUDING END


def between(first, last=0):
    if last == 0:
        last = first
    return df['#'].loc[((df['#'] >= first) & (df['#'] <= last))].index


bt = between

# First generation
df.loc[bt(1, 3), 'Base Form'] = 'Bulbasaur'
df.loc[bt(4, 6), 'Base Form'] = 'Charmander'
df.loc[bt(7, 9), 'Base Form'] = 'Squirtle'
df.loc[bt(10, 12), 'Base Form'] = 'Caterpie'
df.loc[bt(13, 15), 'Base Form'] = 'Weedle'
df.loc[bt(16, 18), 'Base Form'] = 'Pidgey'
df.loc[bt(19, 20), 'Base Form'] = 'Rattata'
df.loc[bt(21, 22), 'Base Form'] = 'Spearow'
df.loc[bt(23, 24), 'Base Form'] = 'Ekans'
df.loc[bt(25, 26), 'Base Form'] = 'Pichu'
df.loc[bt(27, 28), 'Base Form'] = 'Sandshrew'
df.loc[bt(29, 31), 'Base Form'] = 'Nidoran♀'
df.loc[bt(32, 34), 'Base Form'] = 'Nidoran♂'
df.loc[bt(35, 36), 'Base Form'] = 'Cleffa'
df.loc[bt(37, 38), 'Base Form'] = 'Vulpix'
df.loc[bt(39, 40), 'Base Form'] = 'Igglybuff'
df.loc[bt(41, 42), 'Base Form'] = 'Zubat'
df.loc[bt(43, 45), 'Base Form'] = 'Oddish'
df.loc[bt(46, 47), 'Base Form'] = 'Paras'
df.loc[bt(48, 49), 'Base Form'] = 'Venonat'
df.loc[bt(50, 51), 'Base Form'] = 'Diglett'
df.loc[bt(52, 53), 'Base Form'] = 'Meowth'
df.loc[bt(54, 55), 'Base Form'] = 'Psyduck'
df.loc[bt(56, 57), 'Base Form'] = 'Mankey'
df.loc[bt(58, 59), 'Base Form'] = 'Growlithe'
df.loc[bt(60, 62), 'Base Form'] = 'Poliwag'
df.loc[bt(63, 65), 'Base Form'] = 'Abra'
df.loc[bt(66, 68), 'Base Form'] = 'Machop'
df.loc[bt(69, 71), 'Base Form'] = 'Bellsprout'
df.loc[bt(72, 73), 'Base Form'] = 'Tentacool'
df.loc[bt(74, 76), 'Base Form'] = 'Geodude'
df.loc[bt(77, 78), 'Base Form'] = 'Ponyta'
df.loc[bt(79, 80), 'Base Form'] = 'Slowpoke'
df.loc[bt(81, 82), 'Base Form'] = 'Magnemite'
df.loc[bt(83, 83), 'Base Form'] = 'Farfetch\'d'
df.loc[bt(84, 85), 'Base Form'] = 'Doduo'
df.loc[bt(86, 87), 'Base Form'] = 'Seel'
df.loc[bt(88, 89), 'Base Form'] = 'Grimer'
df.loc[bt(90, 91), 'Base Form'] = 'Shellder'
df.loc[bt(92, 94), 'Base Form'] = 'Gastly'
df.loc[bt(95, 95), 'Base Form'] = 'Onix'
df.loc[bt(96, 97), 'Base Form'] = 'Drowzee'
df.loc[bt(98, 99), 'Base Form'] = 'Krabby'
df.loc[bt(100, 101), 'Base Form'] = 'Voltorb'
df.loc[bt(102, 103), 'Base Form'] = 'Exeggcute'
df.loc[bt(104, 105), 'Base Form'] = 'Cubone'
df.loc[bt(106, 107), 'Base Form'] = 'Tyrogue'
df.loc[bt(108, 108), 'Base Form'] = 'Lickitung'
df.loc[bt(109, 110), 'Base Form'] = 'Koffing'
df.loc[bt(111, 112), 'Base Form'] = 'Rhyhorn'
df.loc[bt(113, 113), 'Base Form'] = 'Happiny'
df.loc[bt(114, 114), 'Base Form'] = 'Tangela'
df.loc[bt(115, 115), 'Base Form'] = 'Kangaskhan'
df.loc[bt(116, 117), 'Base Form'] = 'Horsea'
df.loc[bt(118, 119), 'Base Form'] = 'Goldeen'
df.loc[bt(120, 121), 'Base Form'] = 'Staryu'
df.loc[bt(122, 122), 'Base Form'] = 'Mime Jr.'
df.loc[bt(123, 123), 'Base Form'] = 'Scyther'
df.loc[bt(124, 124), 'Base Form'] = 'Smoochum'
df.loc[bt(125, 125), 'Base Form'] = 'Elekid'
df.loc[bt(126, 126), 'Base Form'] = 'Magby'
df.loc[bt(127, 127), 'Base Form'] = 'Pinsir'
df.loc[bt(128, 128), 'Base Form'] = 'Taurus'
df.loc[bt(129, 130), 'Base Form'] = 'Magikarp'
df.loc[bt(131, 131), 'Base Form'] = 'Lapras'
df.loc[bt(132, 132), 'Base Form'] = 'Ditto'
df.loc[bt(133, 136), 'Base Form'] = 'Eevee'
df.loc[bt(137, 137), 'Base Form'] = 'Porygon'
df.loc[bt(138, 139), 'Base Form'] = 'Omanyte'
df.loc[bt(140, 141), 'Base Form'] = 'Kabuto'
df.loc[bt(142, 142), 'Base Form'] = 'Aerodactyl'
df.loc[bt(143, 143), 'Base Form'] = 'Munchlax'
df.loc[bt(147, 149), 'Base Form'] = 'Dratini'
df.loc[bt(151), 'Base Form'] = 'Mew'


# Second Generation
df.loc[bt(152, 154), 'Base Form'] = 'Chikorita'
df.loc[bt(155, 157), 'Base Form'] = 'Cyndaquil'
df.loc[bt(158, 160), 'Base Form'] = 'Totodile'
df.loc[bt(161, 162), 'Base Form'] = 'Furret'
df.loc[bt(163, 164), 'Base Form'] = 'Hoothoot'
df.loc[bt(165, 166), 'Base Form'] = 'Ledyba'
df.loc[bt(167, 168), 'Base Form'] = 'Spinarak'
df.loc[bt(169, 169), 'Base Form'] = 'Zubat'
df.loc[bt(170, 171), 'Base Form'] = 'Chinchou'
df.loc[bt(172, 172), 'Base Form'] = 'Pichu'
df.loc[bt(173, 173), 'Base Form'] = 'Cleffa'
df.loc[bt(174, 174), 'Base Form'] = 'Igglybuff'
df.loc[bt(175, 176), 'Base Form'] = 'Togepi'
df.loc[bt(177, 178), 'Base Form'] = 'Natu'
df.loc[bt(179, 181), 'Base Form'] = 'Mareep'
df.loc[bt(182, 182), 'Base Form'] = 'Oddish'
df.loc[bt(183, 184), 'Base Form'] = 'Azurill'
df.loc[bt(185, 185), 'Base Form'] = 'Bonsly'
df.loc[bt(186, 186), 'Base Form'] = 'Poliwag'
df.loc[bt(187, 189), 'Base Form'] = 'Hoppip'
df.loc[bt(190, 190), 'Base Form'] = 'Aipom'
df.loc[bt(191, 192), 'Base Form'] = 'Sunkern'
df.loc[bt(193, 193), 'Base Form'] = 'Yanma'
df.loc[bt(194, 195), 'Base Form'] = 'Wooper'
df.loc[bt(196, 197), 'Base Form'] = 'Eevee'
df.loc[bt(198), 'Base Form'] = 'Murkrow'
df.loc[bt(199, 199), 'Base Form'] = 'Slowpoke'
df.loc[bt(200, 200), 'Base Form'] = 'Misdreavus'
df.loc[bt(201, 201), 'Base Form'] = 'Unown'
df.loc[bt(202, 202), 'Base Form'] = 'Wynaut'
df.loc[bt(203, 203), 'Base Form'] = 'Girafarig'
df.loc[bt(204, 205), 'Base Form'] = 'Pineco'
df.loc[bt(206, 206), 'Base Form'] = 'Dunsparce'
df.loc[bt(207, 207), 'Base Form'] = 'Gligar'
df.loc[bt(208, 208), 'Base Form'] = 'Onix'
df.loc[bt(209, 210), 'Base Form'] = 'Snubbull'
df.loc[bt(211, 211), 'Base Form'] = 'Qwilfish'
df.loc[bt(212, 212), 'Base Form'] = 'Scizor'
df.loc[bt(213, 213), 'Base Form'] = 'Shuckle'
df.loc[bt(214, 214), 'Base Form'] = 'Heracross'
df.loc[bt(215, 215), 'Base Form'] = 'Sneasel'
df.loc[bt(216, 217), 'Base Form'] = 'Teddiursa'
df.loc[bt(218, 219), 'Base Form'] = 'Slugma'
df.loc[bt(220, 221), 'Base Form'] = 'Swinub'
df.loc[bt(222, 222), 'Base Form'] = 'Corsola'
df.loc[bt(223, 224), 'Base Form'] = 'Remoraid'
df.loc[bt(225, 225), 'Base Form'] = 'Delibird'
df.loc[bt(226, 226), 'Base Form'] = 'Mantyke'
df.loc[bt(227, 227), 'Base Form'] = 'Skarmory'
df.loc[bt(228, 229), 'Base Form'] = 'Houndour'
df.loc[bt(230, 230), 'Base Form'] = 'Horsea'
df.loc[bt(231, 232), 'Base Form'] = 'Phanpy'
df.loc[bt(233, 233), 'Base Form'] = 'Porygon'
df.loc[bt(234, 234), 'Base Form'] = 'Stantler'
df.loc[bt(235, 235), 'Base Form'] = 'Smeargle'
df.loc[bt(236, 236), 'Base Form'] = 'Tyrogue'
df.loc[bt(237, 237), 'Base Form'] = 'Tyrogue'
df.loc[bt(238, 238), 'Base Form'] = 'Smoochum'
df.loc[bt(239, 239), 'Base Form'] = 'Elekid'
df.loc[bt(240, 240), 'Base Form'] = 'Magby'
df.loc[bt(241, 241), 'Base Form'] = 'Miltank'
df.loc[bt(242, 242), 'Base Form'] = 'Happiny'
df.loc[bt(246, 248), 'Base Form'] = 'Larvitar'
df.loc[bt(251), 'Base Form'] = 'Celebi'


# Third Generation

df.loc[bt(252, 254), 'Base Form'] = 'Treecko'
df.loc[bt(255, 257), 'Base Form'] = 'Torchic'
df.loc[bt(258, 260), 'Base Form'] = 'Mudkip'
df.loc[bt(261, 262), 'Base Form'] = 'Poochyena'
df.loc[bt(263, 264), 'Base Form'] = 'Zigzagoon'
df.loc[bt(265, 269), 'Base Form'] = 'Wurple'
df.loc[bt(270, 272), 'Base Form'] = 'Lotad'
df.loc[bt(273, 275), 'Base Form'] = 'Seedot'
df.loc[bt(276, 277), 'Base Form'] = 'Taillow'
df.loc[bt(278, 279), 'Base Form'] = 'Wingull'
df.loc[bt(280, 282), 'Base Form'] = 'Ralts'
df.loc[bt(283, 284), 'Base Form'] = 'Surskit'
df.loc[bt(285, 286), 'Base Form'] = 'Shroomish'
df.loc[bt(287, 289), 'Base Form'] = 'Slakoth'
df.loc[bt(290, 292), 'Base Form'] = 'nincada'
df.loc[bt(293, 295), 'Base Form'] = 'Whismur'
df.loc[bt(296, 297), 'Base Form'] = 'Makuhita'
df.loc[bt(298, 298), 'Base Form'] = 'Azurill'
df.loc[bt(299, 299), 'Base Form'] = 'Nosepass'
df.loc[bt(300, 301), 'Base Form'] = 'Skitty'
df.loc[bt(302, 302), 'Base Form'] = 'Sableye'
df.loc[bt(303, 303), 'Base Form'] = 'Mawile'
df.loc[bt(304, 306), 'Base Form'] = 'Aron'
df.loc[bt(307, 308), 'Base Form'] = 'Meditite'
df.loc[bt(309, 310), 'Base Form'] = 'Electrike'
df.loc[bt(311, 311), 'Base Form'] = 'Plusle'
df.loc[bt(312, 312), 'Base Form'] = 'Minun'
df.loc[bt(313, 313), 'Base Form'] = 'Volbeat'
df.loc[bt(314, 314), 'Base Form'] = 'Illumise'
df.loc[bt(315, 315), 'Base Form'] = 'Budew'
df.loc[bt(316, 317), 'Base Form'] = 'Gulpin'
df.loc[bt(318, 319), 'Base Form'] = 'Carvanha'
df.loc[bt(320, 321), 'Base Form'] = 'Wailmer'
df.loc[bt(322, 323), 'Base Form'] = 'Numel'
df.loc[bt(324, 325), 'Base Form'] = 'Torkoal'
df.loc[bt(325, 326), 'Base Form'] = 'Spoink'
df.loc[bt(327, 327), 'Base Form'] = 'Spinda'
df.loc[bt(328, 330), 'Base Form'] = 'Trapinch'
df.loc[bt(331, 332), 'Base Form'] = 'Cacnea'
df.loc[bt(333, 334), 'Base Form'] = 'Swablu'
df.loc[bt(335, 335), 'Base Form'] = 'Zangoose'
df.loc[bt(336, 336), 'Base Form'] = 'Seviper'
df.loc[bt(337, 337), 'Base Form'] = 'Lunatone'
df.loc[bt(338, 338), 'Base Form'] = 'Solrock'
df.loc[bt(339, 340), 'Base Form'] = 'Barboach'
df.loc[bt(341, 342), 'Base Form'] = 'Corphish'
df.loc[bt(343, 344), 'Base Form'] = 'Baltoy'
df.loc[bt(345, 346), 'Base Form'] = 'Lileep'
df.loc[bt(347, 348), 'Base Form'] = 'Anorith'
df.loc[bt(349, 350), 'Base Form'] = 'Feebas'
df.loc[bt(351, 351), 'Base Form'] = 'Castform'
df.loc[bt(352), 'Base Form'] = 'Kecleon'
df.loc[bt(353, 354), 'Base Form'] = 'Shuppet'
df.loc[bt(355, 356), 'Base Form'] = 'Duskull'
df.loc[bt(357), 'Base Form'] = 'Tropius'
df.loc[bt(358), 'Base Form'] = 'Chimecho'
df.loc[bt(359), 'Base Form'] = 'Absol'
df.loc[bt(360), 'Base Form'] = 'Wynaut'
df.loc[bt(361, 362), 'Base Form'] = 'Snorunt'
df.loc[bt(363, 365), 'Base Form'] = 'Spheal'
df.loc[bt(366, 368), 'Base Form'] = 'Clamperl'
df.loc[bt(369), 'Base Form'] = 'Relicanth'
df.loc[bt(370), 'Base Form'] = 'Luvdisc'
df.loc[bt(371, 373), 'Base Form'] = 'Bagon'
df.loc[bt(374, 376), 'Base Form'] = 'Beldum'


# Forth Generation

df.loc[bt(387, 389), 'Base Form'] = 'Turtwig'
df.loc[bt(390, 392), 'Base Form'] = 'Chimchar'
df.loc[bt(393, 395), 'Base Form'] = 'Piplup'
df.loc[bt(396, 398), 'Base Form'] = 'Starly'
df.loc[bt(399, 400), 'Base Form'] = 'Bidoof'
df.loc[bt(401, 402), 'Base Form'] = 'Kricketot'
df.loc[bt(403, 405), 'Base Form'] = 'Shinx'
df.loc[bt(406, 407), 'Base Form'] = 'Budew'
df.loc[bt(408, 409), 'Base Form'] = 'Cranidos'
df.loc[bt(410, 411), 'Base Form'] = 'Shieldon'
df.loc[bt(412, 414), 'Base Form'] = 'Burmy'
df.loc[bt(415, 416), 'Base Form'] = 'Combee'
df.loc[bt(417), 'Base Form'] = 'Pachirisu'
df.loc[bt(418, 419), 'Base Form'] = 'Buizel'
df.loc[bt(420, 421), 'Base Form'] = 'Cherubi'
df.loc[bt(422, 423), 'Base Form'] = 'Shellos'
df.loc[bt(424), 'Base Form'] = 'Aipom'
df.loc[bt(425, 426), 'Base Form'] = 'Drifloon'
df.loc[bt(427, 428), 'Base Form'] = 'Buneary'
df.loc[bt(429), 'Base Form'] = 'Misdreavus'
df.loc[bt(430), 'Base Form'] = 'Murkrow'
df.loc[bt(431, 432), 'Base Form'] = 'Glameow'
df.loc[bt(433), 'Base Form'] = 'Chingling'
df.loc[bt(434, 435), 'Base Form'] = 'Stunky'
df.loc[bt(436, 437), 'Base Form'] = 'Bronzor'
df.loc[bt(438), 'Base Form'] = 'Bonsly'
df.loc[bt(439), 'Base Form'] = 'Mime Jr.'
df.loc[bt(440), 'Base Form'] = 'Happiny'
df.loc[bt(441), 'Base Form'] = 'Chatot'
df.loc[bt(442), 'Base Form'] = 'Spiritomb'
df.loc[bt(443, 445), 'Base Form'] = 'Gible'
df.loc[bt(446), 'Base Form'] = 'Munchlax'
df.loc[bt(447, 448), 'Base Form'] = 'Riolu'
df.loc[bt(449, 450), 'Base Form'] = 'Hippopotas'
df.loc[bt(451, 452), 'Base Form'] = 'Skorupi'
df.loc[bt(453, 454), 'Base Form'] = 'Croagunk'
df.loc[bt(455), 'Base Form'] = 'Carnivine'
df.loc[bt(456, 457), 'Base Form'] = 'Finneon'
df.loc[bt(458), 'Base Form'] = 'Mantyke'
df.loc[bt(459, 460), 'Base Form'] = 'Snover'
df.loc[bt(461), 'Base Form'] = 'Sneasel'
df.loc[bt(462), 'Base Form'] = 'Magnemite'
df.loc[bt(463), 'Base Form'] = 'Lickitung'
df.loc[bt(464), 'Base Form'] = 'Rhyhorn'
df.loc[bt(465), 'Base Form'] = 'Tangela'
df.loc[bt(466), 'Base Form'] = 'Elekid'
df.loc[bt(467), 'Base Form'] = 'Magby'
df.loc[bt(468), 'Base Form'] = 'Togepi'
df.loc[bt(469), 'Base Form'] = 'Yanma'
df.loc[bt(470, 471), 'Base Form'] = 'Eevee'
df.loc[bt(472), 'Base Form'] = 'Gligar'
df.loc[bt(473), 'Base Form'] = 'Swinub'
df.loc[bt(474), 'Base Form'] = 'Porygon'
df.loc[bt(475), 'Base Form'] = 'Ralts'
df.loc[bt(476), 'Base Form'] = 'Nosepass'
df.loc[bt(477), 'Base Form'] = 'Duskull'
df.loc[bt(478), 'Base Form'] = 'Snorunt'
df.loc[bt(479), 'Base Form'] = 'Rotom'
df.loc[bt(489), 'Base Form'] = 'Phione'

# Fifth Generation
df.loc[bt(495, 497), 'Base Form'] = 'Snivy'
df.loc[bt(498, 500), 'Base Form'] = 'Tepig'
df.loc[bt(501, 503), 'Base Form'] = 'Oshawott'
df.loc[bt(504, 505), 'Base Form'] = 'Patrat'
df.loc[bt(506, 508), 'Base Form'] = 'Lillipup'
df.loc[bt(509, 510), 'Base Form'] = 'Purrloin'
df.loc[bt(511, 512), 'Base Form'] = 'Pansage'
df.loc[bt(513, 514), 'Base Form'] = 'Pansear'
df.loc[bt(515, 516), 'Base Form'] = 'Panpour'
df.loc[bt(517, 518), 'Base Form'] = 'Munna'
df.loc[bt(519, 521), 'Base Form'] = 'Pidove'
df.loc[bt(522, 523), 'Base Form'] = 'Blitzle'
df.loc[bt(524, 526), 'Base Form'] = 'Roggenrola'
df.loc[bt(527, 528), 'Base Form'] = 'Woobat'
df.loc[bt(529, 530), 'Base Form'] = 'Drilbur'
df.loc[bt(531), 'Base Form'] = 'Audino'
df.loc[bt(532, 534), 'Base Form'] = 'Timburr'
df.loc[bt(535, 537), 'Base Form'] = 'Tympole'
df.loc[bt(538), 'Base Form'] = 'Throh'
df.loc[bt(539), 'Base Form'] = 'Sawk'
df.loc[bt(540, 542), 'Base Form'] = 'Sewaddle'
df.loc[bt(543, 545), 'Base Form'] = 'Venipede'
df.loc[bt(546, 547), 'Base Form'] = 'Cottonee'
df.loc[bt(548, 549), 'Base Form'] = 'Petilil'
df.loc[bt(550), 'Base Form'] = 'Basculin'
df.loc[bt(551, 553), 'Base Form'] = 'Sandile'
df.loc[bt(554, 555), 'Base Form'] = 'Darumaka'
df.loc[bt(556), 'Base Form'] = 'Maractus'
df.loc[bt(557, 558), 'Base Form'] = 'Dwebble'
df.loc[bt(559, 560), 'Base Form'] = 'Scraggy'
df.loc[bt(561), 'Base Form'] = 'Sigilyph'
df.loc[bt(562, 563), 'Base Form'] = 'Yamask'
df.loc[bt(564, 565), 'Base Form'] = 'Tirtouga'
df.loc[bt(566, 567), 'Base Form'] = 'Archen'
df.loc[bt(568, 569), 'Base Form'] = 'Trubbish'
df.loc[bt(570, 571), 'Base Form'] = 'Zorua'
df.loc[bt(572, 573), 'Base Form'] = 'Minccino'
df.loc[bt(574, 576), 'Base Form'] = 'Gothita'
df.loc[bt(577, 579), 'Base Form'] = 'Solosis'
df.loc[bt(580, 581), 'Base Form'] = 'Ducklett'
df.loc[bt(582, 584), 'Base Form'] = 'Vanillite'
df.loc[bt(585, 586), 'Base Form'] = 'Deerling'
df.loc[bt(587), 'Base Form'] = 'Emolga'
df.loc[bt(588, 589), 'Base Form'] = 'Karrablast'
df.loc[bt(590, 591), 'Base Form'] = 'Foongus'
df.loc[bt(592, 593), 'Base Form'] = 'Frillish'
df.loc[bt(594), 'Base Form'] = 'Alomomola'
df.loc[bt(595, 596), 'Base Form'] = 'Joltik'
df.loc[bt(597, 598), 'Base Form'] = 'Ferroseed'
df.loc[bt(599, 601), 'Base Form'] = 'Klink'
df.loc[bt(602, 604), 'Base Form'] = 'Tynamo'
df.loc[bt(605, 606), 'Base Form'] = 'Elgyem'
df.loc[bt(607, 609), 'Base Form'] = 'Litwick'
df.loc[bt(610, 612), 'Base Form'] = 'Axew'
df.loc[bt(613, 614), 'Base Form'] = 'Cubchoo'
df.loc[bt(615), 'Base Form'] = 'Cryogonal'
df.loc[bt(616, 617), 'Base Form'] = 'Shelmet'
df.loc[bt(618), 'Base Form'] = 'Stunfisk'
df.loc[bt(619, 620), 'Base Form'] = 'Mienfoo'
df.loc[bt(621), 'Base Form'] = 'Druddigon'
df.loc[bt(622, 623), 'Base Form'] = 'Golett'
df.loc[bt(624, 625), 'Base Form'] = 'Pawniard'
df.loc[bt(626), 'Base Form'] = 'Bouffalant'
df.loc[bt(627, 628), 'Base Form'] = 'Rufflet'
df.loc[bt(629, 630), 'Base Form'] = 'Vullaby'
df.loc[bt(631), 'Base Form'] = 'Heatmor'
df.loc[bt(632), 'Base Form'] = 'Durant'
df.loc[bt(633, 635), 'Base Form'] = 'Deino'
df.loc[bt(636, 637), 'Base Form'] = 'Larvesta'
df.loc[bt(647), 'Base Form'] = 'Keldeo'
df.loc[bt(648), 'Base Form'] = 'Meloetta'
df.loc[bt(649), 'Base Form'] = 'Genesect'

# gen six
df.loc[bt(650, 652), 'Base Form'] = 'Chespin'
df.loc[bt(653, 655), 'Base Form'] = 'Fennekin'
df.loc[bt(656, 658), 'Base Form'] = 'Froakie'
df.loc[bt(659, 660), 'Base Form'] = 'Bunnelby'
df.loc[bt(661, 663), 'Base Form'] = 'Fletchling'
df.loc[bt(664, 666), 'Base Form'] = 'Scatterbug'
df.loc[bt(667, 668), 'Base Form'] = 'Litleo'
df.loc[bt(669, 671), 'Base Form'] = 'Flabébé'
df.loc[bt(672, 673), 'Base Form'] = 'Skiddo'
df.loc[bt(674, 675), 'Base Form'] = 'Pancham'
df.loc[bt(676), 'Base Form'] = 'Furfrou'
df.loc[bt(677, 678), 'Base Form'] = 'Espurr'
df.loc[bt(679, 681), 'Base Form'] = 'Honedge'
df.loc[bt(682, 683), 'Base Form'] = 'Spritzee'
df.loc[bt(684, 685), 'Base Form'] = 'Swirlix'
df.loc[bt(686, 687), 'Base Form'] = 'Inkay'
df.loc[bt(688, 689), 'Base Form'] = 'Binacle'
df.loc[bt(690, 691), 'Base Form'] = 'Skrelp'
df.loc[bt(692, 693), 'Base Form'] = 'Clauncher'
df.loc[bt(694, 695), 'Base Form'] = 'Helioptile'
df.loc[bt(696, 697), 'Base Form'] = 'Tyrunt'
df.loc[bt(698, 699), 'Base Form'] = 'Amaura'
df.loc[bt(700), 'Base Form'] = 'Eevee'
df.loc[bt(701), 'Base Form'] = 'Hawlucha'
df.loc[bt(702), 'Base Form'] = 'Dedenne'
df.loc[bt(703), 'Base Form'] = 'Carbink'
df.loc[bt(704, 706), 'Base Form'] = 'Goomy'
df.loc[bt(707), 'Base Form'] = 'Klefki'
df.loc[bt(708, 709), 'Base Form'] = 'Phantump'
df.loc[bt(710, 711), 'Base Form'] = 'Pumpkaboo'
df.loc[bt(712, 713), 'Base Form'] = 'Bergmite'
df.loc[bt(714, 715), 'Base Form'] = 'Noibat'


# df.loc[bt(, ), 'Base Form'] = ''

# legendaries doesn't evolve
a = df.loc[df['Legendary'] == True].copy()
a['Base Form'] = a['Name']
df.loc.__setitem__((a['Name'].index, 'Base Form'), a['Base Form'])

print(df.head(50))


if __name__ == '__main__':
    save = input('save?')
    if save == 'save':
        ac = pd.read_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv')
        ac['Base Form'] = df['Base Form']
        ac.to_csv('C:\\Users\\guilh\\Desktop\\Programação\\Pokemon\\added_cols.csv', index=False)