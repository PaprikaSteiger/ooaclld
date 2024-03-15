**Author**: [Shelece Easterday](Contributor#cldf:SE)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [David Inman](Contributor#cldf:DI)

[TOC]

## What?
**Syllable structure properties** of a language, including consonant phonotactics and vowel reductive patterns:
- Maximal onset and coda (or word-initial and word-final) structures in number of consonants, and their sums;
- Restrictions on the shape of maximal biconsonantal onsets;
- Restrictions on the sonority of simple codas;
- Categorical syllable complexity.

The syllable patterns considered here include only **native phonotactic patterns**, and exclude patterns that occur solely in recent loans (i.e., from imperial and globalizing languages).

The syllable patterns considered here only include **invariant patterns**, not those which occur in variation with other forms as a result of vowel reduction. Thus the initial \[pʰtʰ\] in most American pronunciations of *potato* would not count as a canonical onset here, as there is a variant with an intervening reduced vowel that is considered standard and grammatical, even though it is less frequent in speech.

The coding here is **blind to morphology**; that is, we consider the largest onset/coda patterns in a language regardless of whether they occur within morphemes or only as a result of a morphological process. E.g., the largest codas in English are 4 consonants (*texts* /tɛ**kst-s**/); we don’t care that such patterns only occur within the context of inflection.

The syllable complexity categories used here are from Easterday ([2017](Source#cldf:easterday2017highly), [2019](Source#cldf:easterday2019highly)), which take Maddieson’s holistic definitions as a starting point. As laid out in his WALS chapter, [Maddieson (2013)](Source#cldf:maddieson2013wals12) divides languages into three categories according to the size and shape of their maximal canonical syllable patterns. The maximal canonical syllable pattern incorporates the largest (in number of consonants) onset and coda in the language. For example, the maximal canonical syllable pattern in English is (C)(C)(C)V(C)(C)(C)(C): in this language, up to three consonants may occur in the onset (e.g., *spring*, /spɹ/) and up to four consonants may occur in the coda (e.g., *texts*, /ksts/). Most often, a language’s largest onsets and codas can be found in word-initial and word-final position, respectively.[^1] Maddieson’s typology also considers cross-linguistically important sonority sequencing properties for languages whose maximal onsets are biconsonantal: among these, languages whose biconsonantal onsets are limited to C+glide and/or C+liquid shapes are considered to have less complex syllable structure than those which have more permissive sonority sequencing for biconsonantal onsets (e.g., C+stop or C+nasal in addition to C+glide shapes). On the basis of the structural properties of the maximal canonical syllable pattern, [Maddieson (2013)](Source#cldf:maddieson2013wals12) classifies languages into the categories below:

- **Simple**: simple onsets, no codas;
- **Moderately Complex**: biconsonantal onsets of C+liquid or glide, and/or simple codas;

And a third category, **Complex**, which includes any patterns larger or more complex than the **Moderately Complex** category above. Thus maximal biconsonantal coda ranging from /rd/ to /ksts/ and even larger, or a maximal onset ranging from /st/ to /vzgl/ or larger would cause a language to be classified as **Complex**. Because this is such a heterogeneous group of patterns, Easterday ([2017](Source#cldf:easterday2017highly), [2019](Source#cldf:easterday2019highly)) proposed another categorical division in order to isolate more extreme cases of syllable complexity in the world’s languages. This involves the introduction of a fourth category, **Highly Complex**, resulting in a more restricted definition of Maddieson’s **Complex** category:

- **Complex**: patterns with larger or more permissive sequencing properties than the Moderately Complex category and smaller or less permissive sequencing properties than the Highly Complex category;
- **Highly Complex**: onset (or word-initial) and/or coda (or word-final) patterns of three obstruents, or of four or more consonants of any kind.

Under these definitions, English would be classified as **Highly Complex** due to its maximal codas, which include up to four consonants. Note that maximal onsets in English, all of which are of the shape /s/+stop+liquid/glide, are not enough on their own to classify English as **Highly Complex**: the maximal onsets are up to three consonants in length, but do not meet the crucial sonority sequencing requirements (three obstruents in a sequence) for inclusion in the category.

## Why?
Syllable structure complexity is not evenly distributed geographically. [Maddieson (2013)](Source#cldf:maddieson2013wals12) notes that languages with complex syllable structure are predominantly found in the northern two-thirds of the northern hemisphere, while languages with simple syllable structure are distributed closely around the equator. It’s been proposed that there are ecological factors behind these distributions ([Maddieson and Coupé 2015](Source#cldf:maddieson2015human), [Munroe et al 2000](Source#cldf:munroe2000rhythmicity), [Ember and Ember 1999](Source#cldf:ember1999cross) inter alia).

High syllable complexity has been described as a prominent areal feature of the Caucasus ([Chirikba 2008](Source#cldf:chirikba2008problem)) and the Pacific Northwest ([Thompson and Kinkade 1990](Source#cldf:thompsonkinkade1990pnw)). Highly Complex syllable structure is particularly areally concentrated, found in very high concentrations in the Pacific Northwest, the Caucasus, and Western Europe; smaller concentrations can be found in Northeast Asia, Patagonia, the Atlas Mountains, northern Papua New Guinea, and the Sonoran Desert, among a few other scattered regions (Easterday [2017](Source#cldf:easterday2017highly), [2019](Source#cldf:easterday2019highly)). Easterday speculates that these areal concentrations could reflect rhythmic transfer of vowel reductive patterns in situations of intense bi/multilingualism.

Syllable complexity has been found to be positively correlated with vowel reduction rates in Easterday ([2017](Source#cldf:easterday2017highly), [2019](Source#cldf:easterday2019highly)) and in speech rhythm typologies ([Auer 1993](Source#cldf:auer1993rhythm)). Syllable complexity has also been correlated or associated with a variety of other phonological and morphological properties, most notably and consistently with consonant phoneme inventory size ([Maddieson 2013](Source#cldf:maddieson2013wals12)); see Chapter 8 of [Easterday (2019)](Source#cldf:easterday2019highly) for a summary of these correlations.

## Features
### [](ParameterTable#cldf:Syll-01)
&emsp;**{ \_number\_ }**

The ‘word-initial pattern’ specification is for cases in which the largest word-marginal patterns include syllabic obstruents (rare; see Tehuelche example).

#### 1: Urarina \[urar1246\] (isolate; Peru)
Onsets are maximally one consonant in this language ([Olawsky 2006](Source#cldf:olawsky2006urarina): 75-76). CCV syllables sometimes occur in Spanish loanwords in the speech of bilinguals, but even these are usually split up by epenthesis.

#### 1: Karok \[karo1304\] (isolate; United States)
Onsets are maximally one consonant in this language ([Bright 1957](Source#cldf:bright1957karok): 11).

#### 2: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Onsets are maximally two consonants in this language. Biconsonantal onsets are always of shape C + glide (/w/ or /j/) ([Vallejos Yopán Yopán 2010](Source#cldf:vallejos2010grammar): 112-115).

#### 2: Pech \[pech1241\] (Chibchan; Honduras)
This language has onsets of up to two consonants and are always of C/ɾ/ shape ([Holt 1999](Source#cldf:holt1999pech): 20-21).

#### 2: Lakota \[lako1247\] (Siouan; United States)
Onsets may be up to two consonants in length; biconsonantal onsets include stop+stop, stop+fricative, fricative+stop, stop+voiced continuant, and sequences of voiced continuants ([Rood and Taylor 1996](Source#cldf:rood1996sketch): 446-447, [Mirzayan 2010](Source#cldf:mirzayan2010lakota): 39, [Ingham 2003](Source#cldf:ingham2003lakota): 5).

#### 3: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
This language has onsets of up to three consonants, including patterns such as /psk/, /nsp/, and /nkh/ ([LeSourd 1993](Source#cldf:lesourd1993passamaquoddy): 58-61, 121-160).

#### 1: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Onsets are maximally one consonant in this language ([Kim 2003](Source#cldf:kim2003theoretical): 161-166, [Stonham 1999](Source#cldf:stonham1999tsishaath): 47-55).

#### 3: Tehuelche \[tehu1242\] (Chonan; Argentina)
This language is analyzed by Fernandez Fernández Garay as having syllabic obstruents in grammatical affixes. While the largest onsets within syllables are two consonants, affixation processes can result in larger word-initial sequences of obstruents like **kʃ.x**aw (&lt; kʃ-xaw with-lend; [Fernández Garay 1998](Source#cldf:garay1998tehuelche): 95).

### [](ParameterTable#cldf:Syll-02)
&emsp;**{ \_number\_ }**

The ‘word-final pattern’ specification is for cases in which the largest word-marginal patterns include syllabic obstruents (rare; see Tehuelche example).

#### 0: Urarina \[urar1246\] (isolate; Peru)
Coda consonants do not occur in this language ([Olawsky 2006](Source#cldf:olawsky2006urarina): 75-76).

#### 1: Karok \[karo1304\] (isolate; United States)
Codas are maximally one consonant in this language ([Bright 1957](Source#cldf:bright1957karok): 11).

#### 1: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Codas are maximally one consonant ([Vallejos Yopán 2010](Source#cldf:vallejos2010grammar): 112-115).

#### 2: Pech \[pech1241\] (Chibchan; Honduras)
This language has codas of up to two consonants. Biconsonantal codas are of shape /ɾ/C, and only occur word-medially ([Holt 1999](Source#cldf:holt1999pech): 20-21).

#### 1: Lakota \[lako1247\] (Siouan; United States)
Codas are maximally one consonant ([Rood and Taylor 1996](Source#cldf:rood1996sketch): 446-447, [Mirzayan 2010](Source#cldf:mirzayan2010lakota): 39, [Ingham 2003](Source#cldf:ingham2003lakota): 5).

#### 3: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
This language has codas of up to three consonants, usually of the form C/s/C: e.g., /nsk/, /wsk/, and /pskʷ/ ([LeSourd 1993](Source#cldf:lesourd1993passamaquoddy): 58-61, 121-160).

#### 4: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Codas are maximally four consonants, and include patterns like /mtqʃ/, /ħsqħ/, and /nkqħ/ ([Stonham 1999](Source#cldf:stonham1999tsishaath): 48).

#### 4: Tehuelche \[tehu1242\] (Chonan; Argentina)
This language is analyzed by Fernandez Fernández Garay as having syllabic obstruents in grammatical affixes. While the largest codas within syllables are three consonants, affixation processes can result in larger word-final sequences of up to four obstruents like maː.le**ʃp.ʃ.k’** (&lt; maː.leʃp-ʃ-k' ‘they steal’; [Fernández Garay 2006](Source#cldf:garay2006textos): 63). There are even larger word-final patterns, as in kt͡ʃa**ʔʃpʃk’n** ‘it is being washed’ (6 word-final consonants; [Fernández Garay 2006](Source#cldf:garay2006textos): 13), but the nasal may be syllabic in this example (the authors don’t specify).

### [](ParameterTable#cldf:Syll-03)
&emsp;**{ \_number\_ }**

Here the same eight languages as above are used. Maximal word-initial and word-final patterns are used instead of maximal onset and coda for Tehuelche.

#### 1: Urarina \[urar1246\] (isolate; Peru)
Onset (1) + Coda (0) = 1

#### 2: Karok \[karo1304\] (isolate; United States)
Onset (1) + Coda (1) = 2

#### 3: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Onset (2) + Coda (1) = 3

#### 4: Pech \[pech1241\] (Chibchan; Honduras)
Onset (2) + Coda (2) = 4

#### 3: Lakota \[lako1247\] (Siouan; United States)
Onset (2) + Coda(1) = 3

#### 6: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
Onset (3) + Coda (3) = 6

#### 5: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Onset (1) + Coda (4) = 5

#### 7: Tehuelche \[tehu1242\] (Chonan; Argentina)
Onset (3) + Coda (4) = 7

### [](ParameterTable#cldf:Syll-04)
&emsp;**{ S | MC | C | HC }**

**S** = Simple
**MC** = Moderately Complex
**C** = Complex
**HC** = Highly Complex

- **Simple**: maximal structure has simple onsets and no codas 
- **Moderately Complex**: maximal structure has at most biconsonantal onsets of C+liquid or glide, and at most simple codas.
- **Complex**: maximal structure has patterns larger than the Moderately Complex category and smaller than the Highly Complex category
- **Highly Complex**: language has maximal onset (or word-initial) or maximal coda (or word-final) patterns of three or more obstruents, or of four or more consonants of any kind.

This categorization is a holistic measure which considers the sizes and shapes of maximal onsets and maximal codas. Here I illustrate with the same eight languages from above.

#### S: Urarina (isolate; Peru)
This language has onsets of only one consonant, and no codas. Its canonical (C)V patterns put it in the Simple category.

#### MC: Karok \[karo1304\] (isolate; United States)
Karok has onsets of only one consonant and codas of only one consonant, putting it in the Moderately Complex category.

#### MC: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Cocama has biconsonantal onsets, but they are of the shape C+glide. Together with its coda patterns, which allow only a single consonant, this puts the language in the Moderately Complex category.

#### C: Pech \[pech1241\] (Chibchan; Honduras)
Like Cocama (Tupian), Pech has biconsonantal onsets which would normally be characterized as Moderately Complex. However, the language also has biconsonantal codas, which puts it in the Complex category.

#### C: Lakota \[lako1247\] (Siouan; United States)
Like Pech and Cocama, Lakota has biconsonantal onsets; however, these include shapes such as stop+stop, fricative+stop, and so on. Coda patterns are simple and consist of one consonant. The onset patterns of this language put it in the Complex category.

#### HC: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
This language has maximal onsets and codas of three consonants. However, these clusters include sequences of three obstruents, which put this language into the Highly Complex category.

#### HC: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
This language has only simple onsets, but codas of up to four consonants in length. Clusters of four consonants of any kind puts a language into the Highly Complex category.

#### HC: Tehuelche \[tehu1242\] (Chonan; Argentina)
This language has syllabic obstruents which participate in the largest word-marginal sequences of consonants observed in the language. The maximal word-marginal obstruent cluster in this language is three for word-initial patterns and four for word-final patterns. This puts the language into the Highly Complex category.

### [](ParameterTable#cldf:Syll-05)
&emsp;**{ C | CG | CCplus }**

Here C = any consonant; G = glide (non-lateral approximant) or liquid (tap, flap, trill, lateral approximant).

#### C: Urarina \[urar1246\] (isolate; Peru)
Onsets are maximally one consonant in this language ([Olawsky 2006](Source#cldf:olawsky2006urarina): 75-76).

#### C: Karok \[karo1304\] (isolate; United States)
Onsets are maximally one consonant in this language ([Bright 1957](Source#cldf:bright1957karok): 11).

#### CG: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Onsets are maximally two consonants in this language. Biconsonantal onsets are always of shape C + glide (/w/ or /j/) ([Vallejos Yopán 2010](Source#cldf:vallejos2010grammar): 112-115).

#### CG: Pech \[pech1241\] (Chibchan; Honduras)
This language has onsets of up to two consonants and are always of C/ɾ/ shape ([Holt 1999](Source#cldf:holt1999pech): 20-21).

#### CCplus: Lakota \[lako1247\] (Siouan; United States)
Onsets may be up to two consonants in length; biconsonantal onsets include stop+stop, stop+fricative, fricative+stop, stop+voiced continuant, and sequences of voiced continuants ([Rood and Taylor 1996](Source#cldf:rood1996sketch): 446-447, [Mirzayan 2010](Source#cldf:mirzayan2010lakota): 39, [Ingham 2003](Source#cldf:ingham2003lakota): 5).

#### CCplus: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
This language has onsets of up to three consonants, including patterns such as /psk/, /nsp/, and /nkh/ ([LeSourd 1993](Source#cldf:lesourd1993passamaquoddy): 58-61, 121-160).

#### C: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Onsets are maximally one consonant in this language ([Kim 2003](Source#cldf:kim2003theoretical): 161-166, [Stonham 1999](Source#cldf:stonham1999tsishaath): 47-55).

#### CCplus: Tehuelche \[tehu1242\] (Chonan; Argentina)
Maximal onsets within syllables are two consonants, affixation processes can result in larger word-initial sequences of obstruents (&lt; kʃ-xaw with-lend; [Fernández Garay 1998](Source#cldf:garay1998tehuelche): 95).

### [](ParameterTable#cldf:Syll-06)
&emsp;**{ nocoda | sonorant | simple | complex }**

**nocoda** = language does not have codas

**sonorant** = language has only simple codas and these are restricted to sonorants (= glide (central approximant), lateral approximant, tap, trill, nasal)

**simple** = language has only simple codas but these include non-sonorant consonants

**complex** = language has complex codas

#### nocoda: Urarina \[urar1246\] (isolate; Peru)
Coda consonants do not occur in this language ([Olawsky 2006](Source#cldf:olawsky2006urarina): 75-76).

#### simple: Karok \[karo1304\] (isolate; United States)
Codas are maximally one consonant in this language, and all consonants may occur in that position ([Bright 1957](Source#cldf:bright1957karok): 11).

#### sonorant: Cocama-Cocamilla \[coca1259\] (Tupian; Peru, Colombia, Brazil)
Codas are maximally one consonant and only /w j n/ occur ([Vallejos Yopán 2010](Source#cldf:vallejos2010grammar): 112-115).

#### complex: Pech \[pech1241\] (Chibchan; Honduras)
This language has codas of up to two consonants ([Holt 1999](Source#cldf:holt1999pech): 20-21).

#### simple: Lakota \[lako1247\] (Siouan; United States)
Codas are maximally one consonant; limited to /s ʃ h l b g/ word-internally and /n m/ word-finally ([Rood and Taylor 1996](Source#cldf:rood1996sketch): 446-447, [Mirzayan 2010](Source#cldf:mirzayan2010lakota): 39, [Ingham 2003](Source#cldf:ingham2003lakota): 5).

#### complex: Malecite-Passamaquoddy \[male1292\] (Algic; United States, Canada)
This language has codas of up to three consonants ([LeSourd 1993](Source#cldf:lesourd1993passamaquoddy): 58-61, 121-160).

#### complex: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Codas are maximally four consonants ([Stonham 1999](Source#cldf:stonham1999tsishaath): 48).

#### complex: Tehuelche \[tehu1242\] (Chonan; Argentina)
Maximal codas within syllables are three consonants, affixation processes can result in larger word-final sequences of up to four obstruents ([Fernández Garay 2006](Source#cldf:garay2006textos): 63).

## Results
In this survey, the scale for maximal onset/word-initial patterns (Syll-01) is 1-8 consonants, while the scale for maximal coda/word-final patterns (Syll-02) is 0-5 consonants, which is consistent with a strong crosslinguistic tendency for onsets to be more complex than codas (Maddieson 2013, Easterday 2017, 2019). The reverse trend in the region of Australia is particularly prominent in the current survey when comparing the maps for Syll-01 and Syll-02.

Echoing the results of earlier surveys (Maddieson 2013 and Easterday 2017, 2019), high syllable complexity, measured here as the sum of the size of maximal onset and coda patterns (Syll-03) is concentrated in several hotspots, including the northwest coast of North America, the Caucasus region, and some more localized areas of Northeast Asia, Mesoamerica, and Patagonia. Regions of low syllable complexity can be found in the Amazon region of South America and in island Oceania. A more holistic characterization of syllable complexity which considers both the size and shape of maximal onset and coda patterns yields the same pattern (Syll-04).

The geographic patterning of the purportedly crosslinguistically preferred maximal onset shape C+glide or C+liquid (Syll-05) is neither globally dominant nor regionally concentrated in this survey. While high syllable complexity as measured by Syll-03 and Syll-04 is concentrated on the northwest coast of North America, complex coda patterns (Syll-06) and patterns in which complex onsets are relatively unrestricted in their sonority profile and/or may be larger than two consonants (Syll-05) are widespread throughout the entire continent of North America. 

Languages with maximal onsets of one consonant (Syll-05) are widely dispersed around the globe, but languages which have no codas or only sonorant codas (Syll-06) are concentrated around the equatorial zone in very much the same areas where languages with Simple syllable structure (Syll-04) are found.

## Contributions
**Conceptualization**: [Shelece Easterday](Contributor#cldf:SE), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [David Inman](Contributor#cldf:DI)

**Data collection**: [Shelece Easterday](Contributor#cldf:SE)

## References
[References](Source?cited_only#cldf:__all__)

[^1]: An areal exception to this trend can be found in Australia, in which the size and structure of codas is more restricted word-finally than word-internally [Flack (2009)](Source#cldf:flack2009constraints). 