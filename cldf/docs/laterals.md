Feature set adapted and extended from [Maddieson 2013](Source#cldf:maddieson2013wals8).

**Authors**: [David Inman](contributors.csv#cldf:DI), [Kellen Parker Van Dam](contributors.csv#cldf:KPVD)

**Acknowledgements**: [Natalia Chousou-Polydouri](contributors.csv#cldf:NCP), [Marine Vuillermet](contributors.csv#cldf:MV), [Anna Graff](contributors.csv#cldf:AG)


**Conceptualization**: [David Inman](contributors.csv#cldf:DI), [Kellen Parker Van Dam](contributors.csv#cldf:KPVD)

**Data collection**: [David Inman](contributors.csv#cldf:DI), [Kellen Parker Van Dam](contributors.csv#cldf:KPVD), [Natalia Chousou-Polydouri](contributors.csv#cldf:NCP), [Marine Vuillermet](contributors.csv#cldf:MV), [Anna Graff](contributors.csv#cldf:AG), [Selma Hardegger](contributors.csv#cldf:SH)

**Supervision of data collection**: [David Inman](contributors.csv#cldf:DI), [Kellen Parker Van Dam](contributors.csv#cldf:KPVD), [Marine Vuillermet](contributors.csv#cldf:MV)

**Computer code**: [David Inman](contributors.csv#cldf:DI)

[TOC]

## What?
The presence or absence in a language of phonemically distinctive lateral consonants. For the purposes of this survey, our interest is the presence of phonemic 
Voiced alveolar (lateral) approximant /l/, and allophonic \[l\] when it alternates with another phoneme;

- Voiceless alveolar (lateral) approximant /l̥/; 
- Voiceless alveolar (lateral) fricative/ɬ/;
- Voiceless alveolar (lateral) affricate/tɬ/;
- Ejective alveolar (lateral) affricate /tɬ’/;
- Palatal (lateral) approximant /ʎ/.

The survey does not distinguish between two very close places of articulation, namely alveolar and apico-dental, as they rarely stand in phonemic opposition. We also exclude phonemes that occur solely in recent loans.

## Why?
The presence or absence of laterals and lateral obstruents is claimed to cluster in geographic regions. [Maddieson 2013](Source#cldf:maddieson2013wals8) notes a cluster of /l/-less languages in northern South America (and New Guinea), and the presence of lateral obstruents in northern and western North America (as well as in the Caucasus and around Lake Chad).

[Maddieson 2013](Source#cldf:maddieson2013wals8) focuses on obstruent vs sonorant laterals. However, the precise type of obstruent is claimed as distinctive in other work, namely /tɬ’/ in the Pacific Northwest, even when a language lacks /tɬ/ ([Sherzer 1976](Source#cldf:sherzer1976northamerica); [Thompson and Kinkade 1990](Source#cldf:thompsonkinkade1990pnw); [Beck 2000](Source#cldf:beck2000nwcoast)). The voiced lateral affricate /dɮ/ is not included in this survey, as [Maddieson 2013](Source#cldf:maddieson2013wals8) only finds one language (Tigak; Austronesian; Papua New Guinea) that has a voiced /dɮ/ without a corresponding voiceless /tɬ/.

/ɬ/ as a feature is common in North America in Maddieson’s survey, and has also been claimed to be prominent in the North American Southeast ([Haas 1969](Source#cldf:haas1969prehistory); [Campbell 1997](Source#cldf:campbell1997america)), and in the Southern Andean core ([Michael et al 2014: 33](Source#cldf:michaeletal2014andean)). It’s unclear whether these represent truly distinct areas, or if a high frequency of the /ɬ/ phoneme is part of a broader American west coast pattern.

/ʎ/ stands among the distinctive core phonological features for the Southern Andean core ([Michael et al 2014](Source#cldf:michaeletal2014andean)).

## How?
Some of the data for this feature set were obtained directly from the PHOIBLE database version 2.0 ([PHOIBLE](Source#cldf:phoible), accessed January 27, 2020). A custom R script was written to process it. For Lat.01, which considers the allophones of the segment [l], all languages in PHOIBLE that had an inventory without an /l/ phoneme or \[l\] allophone were coded as <no>, and the remainder that did have a lateral liquid present somewhere were marked to be reviewed by hand. The presence or absence of /ɬ/, /tɬ/, /tɬ’/, and /ʎ/ (Lat.03, Lat.04, Lat.05, Lat.06) were extracted and encoded by the binary presence or absence of the relevant segment. Afterwards, 19 extracted languages were checked against grammars for accuracy, which yielded an acceptable error rate. Other discrepancies found in the data or cases where more recent sources have become available were corrected opportunistically while coding for other features. Such corrections are marked by “contra-PHOIBLE” in the remark field of the database.

The remaining data were coded by hand from available phonological and phonetic descriptions.

## Features

### [Lat.01 Does the language have a lateral approximant phoneme /l/ or an allophone \[l\] and if so, with what other allophones does this /l/ or \[l\] alternate?](ParameterTable#cldf:Lat-01)
  **{ laterals or glides | rhotic | n or d | n or d and rhotic | no }**

The first state <laterals or glides> includes all languages that only have an /l/ as its own phoneme without variation, or that have an /l/ which alternates with other laterals (ʎ, lʲ, ɫ, ɬ, and so on) or glides (w, j, etc). The reason for these allophones being lumped together is that we believe buccalization of /l/ is common for phonetic reasons, as are alternations with other laterals (\[ɬ\] after an aspirated stop, etc). This is the expected state for most languages that are described as having an /l/ in their inventory.

The second state <rhotic> includes all languages that have an \[l\] alternating with some kind of rhotic consonant. We expect the rhotics an /l/ alternates with to mostly be \[ɾ\], \[ɹ\], and \[r\].

The third state <n or d>  includes all languages that alternate an \[l\] with an \[n\], a \[d\], or both. The sounds \[n\] and \[d\] are lumped together here because we believe that the mechanism for the two alternations is similar, and some languages allow all 3 allophones (see Ese Ejja). However, which allophone or allophones are present should be noted in the remarks (n, d, both).

The fourth state <n or d and rhotic> is a combination of the two previous states, as we found a few languages where there is allophony between all these segments (Kotiria, Tutelo, Cayubaba).

The final state <no> includes all languages that have no /l/ phoneme at all, and not even an \[l\] as an allophone.

In the case where the language only has a lateral flap, as is the case in Cavineña [cavi1250] (Pano-Tacanan; Bolivia), Western Keres [west2632] (Keresan; United States), and Tohono O’odham [toho1245] (Uto-Aztecan; Mexico, United States), this feature was coded as a ?. This is because it could pattern areally both as a non-lateral (non-continuous, as a flap), or as a lateral (since it is laterally articulated).

#### laterals or glides: Lillooet \[lill1248\] (Salishan; Canada)
St’at’imcets or Lillooet contains a phonemic /l/ which does not appear to alternate with other phonemes, as in words like lóləm’ ‘jealous in love’ ([Eijk 1997: 2, 11](Source#cldf:eijk1997lillooet)

#### laterals or glides: Cherokee \[cher1273\] (Iroquoian; United States)
Cherokee contains a phonemic /l/, as in words like aaliíyo ‘sock’ ([Montgomery-Anderson 2008](Source#cldf:montgomeryanderson2008cherokee): 33, 41).

#### n or d: Ese Ejja \[esee1248\] (Pano-Tacanan; Peru, Bolivia)
Ese Ejja has a \[d\]/\[n\]/\[l\] phonemic alternation [Vuillermet 2012: 165](Source#cldf:vuillermet2012eseejja). \[l\] is only heard in the speech of older people, with the other allophones being more common in other speakers (Vuillermet, p.c.).

#### rhotic: Cocama-Cocamilla \[coca1259\] (Tupian; Peru)
Cocama-Cocamilla has a phoneme that alternates between \[l\] and \[ɾ\] with completely free variation [Vallejos 2016: 47](Source#cldf:vallejos2016kukama). According to Vallejos, it is possible that this developed from an older system that had just /l/.

#### no: Nuuchahnulth \[nuuc1236\] (Wakashan; Canada)
Nuuchahnulth contains no \[l\] sound, despite having /ɬ/, /t͡ɬ/, and /t͡ɬ’/ [Nakayama 2001: 7](Source#cldf:nakayama2001nuuchahnulth). This is even visible in loanwords, where a borrowed /l/ becomes /n/, as in taana, ultimately from English ‘dollar’ (Inman, p.c.).

#### ?: Western Keres \[west2632\] (Keresan; United States)
Western Keres contains a lateral flap [Valiquette 1990: 14](Source#cldf:valiquette1990keres), described as “something of a combination of a Spanish flapped /r/ and a lateral.”

#### no: Nanti \[nant1250\] (Arawakan; Peru)
Nanti only has a flap /ɾ/ as a liquid, and no /l/ [Michael 1008: 221](Source#cldf:michael2008nanti).

### Lat.02 Does the language have a phonemic voiceless lateral approximant /l̥/?
  **{ yes | no }**

/l̥/ signifies a voiceless non-fricative approximant. This differs from Lat.03 /ɬ/, which is a fricative non-approximant lateral.

This feature was actually added after coding was completed for the other features because we discovered that a few languages had a /l̥/, which seemed to behave in a phonologically similar way to /ɬ/, so we wanted to track it as a potentially informative lateral. We first reviewed the PHOIBLE database to check the cooccurrences of /l̥/ with other lateral segments. Of 2,186 languages in the database, only one, Wakhi, was claimed to have a voiceless /l̥/ without /l/, citing [Paxalina 1975](Source#cldf:paxalina1975wakhi). However, another grammar ([Lorimer 1958](Source#cldf:lorimer1958wakhi)) notes an /l/ with, potentially, an allophone [l̥]: “I occasionally recorded an l which I marked as abnormal. I think that in most cases it may have been a voiceless l” ([Lorimer 1958: 53-54](Source#cldf:lorimer1958wakhi)). Because this state (/l̥/ without /l/) seems to be vanishingly rare if not impossible, we automatically coded a <no> to Lat.02 for all languages that lack an /l/ or an \[l]\ (<no> to Lat.01), with the remark “auto”.

We also noted that there are zero inventories in PHOIBLE that showed both a phonemic /l̥/ and /ɬ/. Therefore, we again automatically coded the state <no> to Lat.02 if the language possesses a /ɬ/ (i.e., <yes> to Lat.03), with the remark "auto". This reduced the number of languages coded by hand after the rest of the features set had been completed.

### Lat.03 Does the language have a phonemic lateral fricative /ɬ/?
  **{ yes | no }**

A phoneme that has \[ɬ\] as a prominent allophone (perhaps alternating with \[θ\]) should be counted as a phonemic /ɬ/, by analogy with Lat.01. However, \[ɬ\] is not considered as a phoneme for this feature if it is in allophonic distribution with \[l\].

#### yes: Nuuchahnulth \[nuuc1236\] (Wakashan; Canada)
Nuuchahnulth has a phonemic /ɬ/ as in the first sound in łiw̓aḥak ‘cloudy’ and the last sound in ƛuł ‘good’ (Inman, personal knowledge).

#### no: Pipil \[pipi1250\] (Uto-Aztecan; El Salvador, Honduras)
Pipil has an \[ɬ\] alternating  with the main allophone \[l\]. Historically \[ɬ\] was a word final variant of /l/ but it is now present in more contexts. Still, \[l\] is the main realization and thus considered the phoneme ([Campbell 1985](Source#cldf:campbell1985pipil)).

### Lat.04 Does the language have a phonemic alveolar lateral affricate /tɬ/?
  **{ yes | no }**

#### yes: Nuuchahnulth \[nuuc1236\] (Wakashan; Canada)
Nuuchahnulth has a phonemic /t͡ɬ/ as in the first sound in ƛaʔuu ‘other’ and the last sound in haw̓iiqƛ ‘hungry’ (Inman, p.c.).

#### yes: Cherokee \[cher1273\] (Iroquoian; United States)
An underlying /t͡ɬ/ in Cherokee has shifted to \[ɬ\] in the Oklahoma variety. This is an ongoing change. Phonetically, the language appears to have merged this phoneme with /ɬ/, however according to [Montgomery-Anderson 2008](Source#cldf:montgomeryanderson2008cherokee),

\[the phonemes'\] separate identity as distinctive sounds is established through their behavior relative to vowel deletion and metathesis. (p.39)

Therefore it is clear that underlyingly, Oklahoma Cherokee retains these as two separate phonemes despite cases showing an apparent phonetic merger.

#### no: Hupa \[hupa1240\] (Athabaskan-Eyak-Tlingit; United States)
Though Hupa has both an /l/ and a /ɬ/, it does not have a /t͡ɬ/ ([Golla 1970](Source#cldf:golla1970hupa)).

### Lat.05 Does the language have a phonemic alveolar lateral ejective affricate /tɬ’/?
  **{ yes | no }**

#### yes: Nuuchahnulth \[nuuc1236\] (Wakashan; Canada)
Nuuchahnulth has a phonemic /t͡ɬ’/ as in the difference between ƛuł ‘good’ and ƛ̓ułšiƛ ‘touch, feel’ (Inman, p.c.).

#### no: Cherokee \[cher1273\] (Iroquoian; United States)
Cherokee has no ejective series and lacks /t͡ɬ’/ ([Montgomery-Anderson 2008](Source#cldf:montgomeryanderson2008cherokee): 33).

### Lat.06 Does the language have a phonemic palatal lateral approximant /ʎ/?
  **{ yes | no }**

NOTE: While the IPA symbol for the palatal lateral is \[ʎ\], this is not always given in grammars. In some grammars, and particularly in Australia, the symbol <ȴ> is used for an alveo-palatal lateral. In other grammars, the symbols <lʸ> or <lʲ> or <l’> indicate a “palatalized” lateral.

There is an articulatory distinction between a lateral with a palatal off-glide (realized phonetically at the beginning of the following vowel) and a lateral with palatal articulation. However, we do not think this distinction will be significant areally: i.e., if a language has an alveolar lateral with an off-glide /lʲ/, and a language has a true palatal lateral /ʎ/, from an areal perspective, we think these phonemes are mutually reinforcing. There is also an analytical issue, as different linguists may approach the same set of facts with some coming to the analysis of an /lʲ/ phoneme and others of a /ʎ/. The same arguments can be extended to /ȴ/. For the purposes of this feature set, then, we consider all palatal or palatalized laterals to share the same state, <yes>. However, it is important that this sound be a unitary phoneme: i.e., treated by the phonology of the language as a single phoneme, and not the juxtaposition of /l/ + /j/.

#### yes: Northern Yukaghir \[nort2745\] (Yukaghir; Russia)
Northern Yukaghir has an palatalized lateral, Romanized as l’, which contrasts with a non-palatalized lateral, Romanized as l ([Schmalz 2013: 30](Source#cldf:schmalz2013yukaghir)).

#### no: Cherokee \[cher1273\] (Iroquoian; United States)
Despite its other lateral phonemes, Cherokee lacks a palatal lateral ([Montgomery-Anderson 2008](Source#cldf:montgomeryanderson2008cherokee): 33).
Derived features
Derived features offer different views of the same data included in the base features. Often, this is done to group together some states of multi-state features, to capture specific similarities. In other cases, derived features are designed so that they are independent from other features used in the same computational analyses that assume feature independence, e.g. the Bayesian software sBayes, which detects areal signal ([Ranacher et al 2021](Source#ranacher2021sbayes)).

### Lat.01a Does the language have an allophonic \[l\]?
  **{ yes | no }**
	
	yes	if Lat.01 is <laterals or glides> OR <rhotic> OR <n or d> OR <n or d and rhotic>
	no 	if Lat.01 is <no>
	?	if Lat.01 is <?>

This derived feature groups together all languages with some kind of lateral articulation against those without any.

### Lat.01b Does the language have a phonemic /l/ which only alternates with other laterals or glides?
  **{ yes | no }**
	
yes	if Lat.01 is <laterals or glides>
no	if Lat.01 is <rhotic> OR <n or d> OR <n or d and rhotic> OR <no>
? 	if Lat.01 is <?>

This derived feature groups languages with a lateral that is only a lateral against everything else.

### Lat.01c If the language has an allophonic \[l\], what does this allophone alternate with?
  **{ laterals or glides | rhotic | n or d | NA }**

laterals or glides	if Lat.01 is <laterals or glides>
rhotic 			if Lat.01 is <rhotic>
n or d	 		if Lat.01 is <n or d>
NA 			if Lat.01 is <no>
? 			if Lat.01 is <n or d and rhotic> OR <?>
	

This derived feature conceptually pairs with Lat.01a, and expresses all the possible allophones of the phonemic \[l\], if there was one.

### Lat.02a Does the language have a phonemic voiceless lateral continuant?
  **{ yes | no }**
	
yes 	if Lat.02 is <yes> (l̥) OR if Lat.03 is <yes> (ɬ)
no 	if Lat.02 is <no> AND Lat.03 is <no>
? 	if Lat.02 is <?> OR if Lat.03 is <?>

This derived feature groups together languages with /l̥/ and /ɬ/ phonemes, on the observation that they are perceptually difficult to distinguish and on the belief that they fulfill the same phonological function.

### Lat.02b If yes to Lat.02a, which voiceless lateral continuant does the language have?
  **{ l̥ | ɬ | NA }**

l̥ 	if Lat.02 is <yes>
ɬ 	if Lat.03 is <yes>
NA 	if Lat.02a is <no>

This derived feature recovers the phonetic details of which voiceless lateral a language has.

###nLat.04a Does the language have either a phonemic /tɬ/ or /tɬ’/?
  **{ yes | no }**

yes	if Lat.04 is <yes> OR Lat.05 is <yes>
no	if Lat.04 is <no> AND Lat.05 is <no>
? 	if Lat.04 is <?> AND Lat.05 is not <yes> OR if Lat.05 is <?> AND Lat.04 is not <yes>

This derived feature asks if there is any phonemic lateral affricate. Many languages of the Pacific Northwest have the ejective affricate, but not the plain one.

### Lat.04b If yes to Lat.04a, does the language have a phonemic /tɬ/?
  **{ yes | no | NA }**

	yes	if Lat.04 is <yes> AND Lat.04a is <yes>
	no	if Lat.04 is <no> AND Lat.04a is <yes>
NA	if Lat.04a is <no>
	?	if Lat.04a is <?>

This derived feature conditions the presence of /tɬ/ on the presence of any lateral affricate.

### Lat.05a If yes to Lat.05a, Does the language have /tɬ’/?
  **{ yes | no | NA }** 

	yes 	if Lat.05 is <yes> AND Lat.04a is <yes>
	no 	if Lat.05 is <no> AND Lat.04a is <yes>
NA 	if Lat.04a is <no>
?	if Lat.05 is <?>

This derived feature conditions the presence of /tɬ’/ on the presence of any lateral affricate.

## Results
Following the observations of [Maddieson 2013](Source#cldf:maddieson2013wals8), the Greater Amazon is overwhelmingly characterized by an absence of /l/ phonemes altogether (Lat.01). The presence of an /l～ɾ/ phoneme is most common in Papunesia and parts of Southern and Central America, however even in these regions it is a minority pattern. As expected, the Pacific Northwest of North America is characterized by /tɬ/ and /tɬ’/ phonemes (Lat.04, Lat.05), while the presence of /ɬ/ is somewhat more widespread, characterizing the Pacific Northwest, but also the North American Pueblos, the American Southeast, and the Gran Chaco. The presence of a phonemic voiceless /l̥/ (Lat.02) is extremely rare, without apparent areal patterns. The palatal lateral /ʎ/ (Lat.06) is characteristic of the west coast of South America and the northwest coast of Australia. Our sample is not dense enough to demonstrate it, but the Eurasian sample suggests that palatal lateral phonemes are also especially present in northern Eurasia.


## References

[References](Source?cited_only#cldf:__all__)

