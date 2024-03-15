**Authors**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Selma Hardegger](Contributor#cldf:SH), [Nora Muheim](Contributor#cldf:NJM)

[TOC]

## What?
This feature set looks at the distinctions made among coronally-articulated consonants in a language. As in other phonological features, we definitionally exclude patterns that occur solely in recent loans.

This feature set targets the **primary articulation** of coronal consonants (including sibilants), i.e. distinctions in the place of articulation of consonants made with the tongue tip (apical or subapical articulation). This includes all varieties of coronal stops (/t/-like sounds), sibilant fricatives and affricates, and retroflex consonants. On the other hand, it definitionally excludes lamino-palatal consonants like /c, ʝ/, articulated with the blade of the tongue, and also excludes phonemic distinctions made by coarticulation. If two phonemes are distinguished by additional secondary coarticulation, then we consider only the single place of articulation made coronally. The pharyngeal coarticulation distinguishing /s/ and /sˤ/ in Arabic (س and ص), would therefore only be considered with respect to the single place of articulation of the /s/. The same reasoning extends to palatalization as well.

## Why?
The presence of retroflex consonants has been claimed as a distinctive property of at least two North American linguistic areas: California ([Haas 1976](Source#cldf:haas1976california)) and the American Southeast ([Rankin 1988](Source#cldf:rankin1988quapaw), [Nicklas 1994](Source#cldf:nicklas1994southeast)). This analysis of retroflexion has later been challenged, as it is unclear if many of the languages have a distinction between dental/alveolar and retroflex consonants, or between dental and alveolar or postalveolar (but not necessarily retroflex) consonants ([Dart 1993](Source#cldf:dart1993tohono), [Mithun 2001](Source#cldf:mithun2001languages)). This suggests that the areal phonological feature may be the number of place distinctions among coronal consonants, rather than strictly phonetic retroflexion.

It is also unclear if the observations of these scholars describe phonological properties of two separate areas (California and the Southeast), potentially with slightly different properties, or if it is part of a broader area that extends west-to-east from California to the southeast.

To investigate these possibilities, this feature set is split into two sections. Features 1-3 target the number of phonemic place distinctions for coronal plosives, and for sibilant affricates and fricatives, regardless of the specific articulatory points of each place. Features 4-8 ask about specific places of articulation.

## How?
Some of the data for this feature set was obtained directly from the PHOIBLE database version 2.0 ([Phoible](Source#cldf:phoible), accessed January 27, 2020), using a custom R script. This was only done for features relating to retroflex consonants and the interdental fricative. For Cor-04, a list of retroflex plosives was compiled and inventories searched for matching phonemes, and for Cor-07, Cor-08, and Cor-09 a list of retroflex sibilants. Languages in which a matching phoneme was found were coded as &lt;yes&gt; to the appropriate question, and otherwise as &lt;no&gt;. For Cor-06, a list of interdental phonemes was compiled, and inventories searched for matches against this list. Because the other questions were coded manually, every value from PHOIBLE was checked against information in available phonological resources. In cases where these sources contradicted data from PHOIBLE, “contra-PHOIBLE” was entered into the remarks.

## Features
### [](ParameterTable#cldf:Cor-01)
&emsp;**{ 1 | 2 | 3 }**

Coronal plosives are phonemic consonants produced with the tongue tip, or informally “/t/-like” consonants. We did not find any language with more than 3 places of articulation.

For this feature we did not consider the phonetic realization of the different coronal phonemes (e.g. if they are described as retroflex or not), but instead the number of distinctions present. The range of possible phonemes is typically /t̪-t-ʈ/, although there are differences in the transcription systems used, with many systems using a &lt;ṭ&gt;, which indicates either an alveolar or retroflex articulation.

As an example of possible contrasts, Hindi \[hind1269\] (Indo-European; Bengladesh, Bhutan, India, Nepal; [Koul 2009](Source#cldf:koul2009hindi)) has a distinction between dental and retroflex places of articulation (/t̪, ʈ/), Nihali \[niha1238\] (isolate; India; [Nagaraja 2014](Source#cldf:nagaraja2014nihali)) has a distinction between alveolar and retroflex places of articulation (/d, ɖ/), and Thayore \[thay1249\] (Pama-Nyungan; Australia; [Gaby 2006](Source#cldf:gaby2006kuuk)) has a distinction between dental and alveolar places of articulation (/t̪, t/). Though each of these three languages has different pairs of phonemes, all of them have 2 places of articulation in contrast. On the other hand, Tiwi \[1244\] (isolate; Australia; [McGregor 1990](Source#cldf:mcgregor1990functional)) has a distinction between dental, alveolar, and retroflex articulations (t̪, t, ʈ), which gives it 3 places of articulation among coronal plosives.

There were some languages with a place of articulation distinction that was coupled with a voicing distinction, such as Wapishana \[wapi1243\] (Arawakan; Brazil, Guyana), which has a distinction between voiceless /t/ and voiced /ɖ/ ([Gomes dos Santos 2006](Source#cldf:gomes2006wapixana)). We still considered such cases as having two places of articulation, so long as the place of articulation distinction was described as a primary component of the phonemic distinction, either more than or equal with voicing. If a grammar carefully noted subtle place distinctions, but that two phonemes contrasted primarily by voicing, this was excluded definitionally, as was a case where a place of articulation only occurred as a clear case of cross-phonemic assimilation.[^1]

If a language was described as having a “palatal” stop, we took care to confirm that this was a real palatal stop (made with the tongue body, as in /c/) and not a shorthand for an affricate (e.g. coronal affricate /tʃ/, made with the tongue tip). True palatals, such as those present in Nihali (isolate) ([Nagaraja 2014](Source#cldf:nagaraja2014nihali): 131) did not count as a coronal place of articulation, while affricates such as /tʃ/, /tɕ/, and so on were considered in the following feature, Cor-02.

### [](ParameterTable#cldf:Cor-02)
&emsp;**{ 0 | 1 | 2 | 3 | 4 }**

This feature concerns the number of distinct sibilant affricates in a language, all of which fall within the range of /t̪s̪-ts-tʃ-ʈʂ-tɕ/. Only a maximum of a 4-way distinction was found.

Affricates stand phonetically in-between plosives and fricatives, and as such we expected languages *a priori* to either have the same number of distinctions in plosives and affricates, or the same number of distinctions in affricates and fricatives, or to simply lack affricates. However, we found for a number of languages that affricates behaved somewhat independently, whether by having fewer distinctions among sibilant affricates than among either plosives or sibilant fricatives, as in Southern Sierra Miwok \[sout2985\] (Miwok-Costanoan; United States; [Broadbent 1964](Source#cldf:broadbent1964miwok)), and Southeast Pomo \[sout2984\] (Pomoan; United States; [Moshinsky 1970](Source#cldf:moshinsky1970pomo)), or by having more distinctions among sibilant affricates than either plosives or sibilant fricatives, as in Abkhaz \[abkh1244\] (Abkhaz-Adyge; Georgia, Russia, Turkey; [Hewitt 2010](Source#cldf:hewitt2010abkhaz)) and Jaqaru \[jaqa1244\] (Aymaran; Peru; [Hardman 2000](Source#cldf:hardman2000jaqaru), [Zúñiga 2020](Source#cldf:zuniga2020pc)). This finding *a posteriori* justifies the treatment of affricates as a distinct category.

### [](ParameterTable#cldf:Cor-03)
&emsp;**{ 0 | 1 | 2 | 3 }**

This feature concerns the number of distinct sibilants in a language, all of which fall within the range /s̪-s-ʃ-ʂ-ɕ/. As with Cor-02, the “coronal-ness” of the phonemes is of secondary importance to their status as sibilants. And as with both Cor-01 and Cor-02, the feature is focused on the number of distinctions and not what the actual phonetic realizations are: A grammar describing only a distinction between &lt;s&gt; and &lt;ṣ&gt;, with no clear description of the latter, would have a state of 2, just as much as a language with a clearer articulatory description of two phonemes as /s/ and /ɕ/, as is the case for Lango \[lang1324\] (Nilotic; Uganda; [Noonan 1992](Source#cldf:noonan1992lango)).

### [](ParameterTable#cldf:Cor-04)
&emsp;**{ yes | no }**

Unlike Cor-01-Cor-03, this feature does not consider whether the retroflex is contrastive with another coronal (although we did not find a phonemic retroflex stop that did not contrast with a non-retroflex coronal). If *any* stop is described in the grammar as retroflex, the state was &lt;yes&gt;.

### [](ParameterTable#cldf:Cor-05)
&emsp;**{ yes |no }**

In the same way that retroflexion has been claimed to be an areal phenomenon, we believe it may be possible for the other extreme of coronal articulation (dentality) to be areal.

As with Cor-04, it does not matter for the purposes of this feature if the dental stop is contrastive with another coronal, and unlike Cor-04, this is fairly common. As an example, Modern Standard Spanish would be coded as a &lt;yes&gt;, even though the dental /t̪/ does not contrast with a non-dental /t/.

### [](ParameterTable#cldf:Cor-06)
&emsp;**{ yes | no }**

This feature is partially a companion to Cor-05. In the same way that we ask for retroflexion in both plosives (Cor-04) and fricatives (Cor-07), we ask for dentality in both plosives and fricatives. It is important that the dental fricative θ or ð be phonemic and not merely an allophone. For instance, Latin American Spanish would be coded as a &lt;no&gt; since ð appears only as an allophone of /d/, but Castillian Spanish would be coded as a &lt;yes&gt;, since θ appears as its own phoneme (*casar* vs *cazar*).

### [](ParameterTable#cldf:Cor-07)
&emsp;**{ yes | no }**

We have not asked about retroflex affricates because there were only two languages in our sample that had retroflex affricates but not retroflex fricatives.

### [](ParameterTable#cldf:Cor-08)
&emsp;**{ NA | yes | no }**

### [](ParameterTable#cldf:Cor-09)
&emsp;**{ NA | yes | no }**

Coding for the presence of a voiced /ʐ/ as distinct and separate from voiceless /ʂ/ (when a voicing distinction was not considered for other segments) arose from encountering this phoneme more frequently than expected in our Amazonian sample, and wanting to capture this, if it was an areal phenomenon. A possible mechanism for the development of /ʐ/ (separately form /ʂ/) is the spirantization of a rhotic.

## Results
The presence of more than one place of articulation for coronal consonants (Cor-01) is for the most part geographically constrained, occurring with the most frequency in Australia, the Indian subcontinent, and in California and the American Southwest. Several languages in South America also have more than one place of coronal articulation, but their distribution is highly scattered. The presence of retroflex plosives (Cor-04) occurs only in a subset of the languages with more than one coronal plosive, as we found no language with a retroflex phoneme that lacked a non-retroflex one.

The number of places of articulation for sibilant affricates (Cor-02) and fricatives (Cor-03) are somewhat correlated, with Australia and parts of the Amazon lacking sibilants altogether. Most languages have only one or two places of articulation for sibilants, making three-way (or more) distinctions rare, though noticeably more common along the South American west coast. The presence of retroflex sibilants (Cor-07) largely occurs in languages with more than one sibilant fricative, and shows a highly local geographic distribution, present in the American Southwest, parts of southern Central America, and Northern Peru. As with coronal contrast distinctions, retroflex sibilants occur more frequently in South America than in other regions, but with a highly scattered distribution. Voiceless retroflex sibilants (Cor-08) are much more common than voiced ones (Cor-09). 

The presence of dental stops (Cor-05) shows some degree of geographic clustering, for example in California, northern Central America, and the northwest Australian coast. The presence of interdental fricatives (Cor-06) is rare and shows no clear geographic clustering.

## Contributions
**Conceptualization**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD)

**Data collection**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Nora Muheim](Contributor#cldf:NJM), [Selma Hardegger](Contributor#cldf:SH)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP)

**Computer code**: [David Inman](Contributor#cldf:DI) 

## References
[References](Source?cited_only#cldf:__all__)

[^1]: An example of the latter case would be something like assimilation between /t/ and /ɹ/ resulting in \[ɖ\], when the language otherwise does not have retroflex stops. Such cases were not tracked.
