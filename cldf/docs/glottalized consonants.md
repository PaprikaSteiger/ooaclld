Feature set adapted from [Maddieson (2013)](Source#cldf:maddieson2013wals7).

**Authors**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Anna Graff](Contributor#cldf:AG)

[TOC]

## What?
The presence or absence in a language of **phonemic glottalized consonants**. For the purposes of this survey, our greatest interest was the presence of **glottalized obstruents** and **glottalized resonants**. However, we encoded for finer distinctions which can be later subsumed into these two categories. We definitionally excluded phonemes that occur solely in recent loanwords.

## Why?
The presence of coarticulated glottal closure or ejectives in a language has been determined in prior work to be highly correlated with geographic location, notably in [Maddieson (2013)](Source#cldf:maddieson2013wals7). Maddieson shows that ejectives are extremely common in the Americas compared to the rest of the world, especially along the Andes, in Mesoamerica, and along the North American west coast. Outside of the Americas they cluster in northeast Africa and the Caucasus. There is no similar claim of geographical patterning of implosives in the Americas (although there is in Africa and Southeast Asia). 

Prior to the typology of [Maddieson (2013)](Source#cldf:maddieson2013wals7), glottalized consonants have been noticed as an areal feature in the Pacific Northwest ([Jacobs 1954](Source#cldf:jacobs1954areal), [Haas 1969](Source#cldf:haas1969prehistory), [Beck 2000](Source#cldf:beck2000nwcoast)) and the Pueblo area ([Bereznak 1995](Source#cldf:bereznak1995pueblo), [Campbell 1997](Source#cldf:campbell1997america)). [Campbell (2012)](Source#cldf:campbell2012southamerica) reports “glottalized (ejective) stops and affricates, and often also glottalized sonorants (liquids, nasals, glides) \[...\] in a good number of SA languages'' though it is less common in Amazonia. [Michael et al (2014)](Source#cldf:michaeletal2014andean) use statistical methods to explore phonological areality in the Circum-Andes region, and find ejective stops to be a significant feature in the consonantal profile of Andean languages.

## How?
Though it is possible to differentiate types of glottalization, e.g., whether the articulation of a glottalized stop is an ejective or a pre- or post-glottalized plosive, for the purposes of generating a strong areal feature we considered any presence of phonemic glottalization, regardless of its phonetic realization.

One reason for this is that in some languages with glottalized consonants, the type of glottalization is less important than the presence of a phonemic feature \[+glottal\]. For example, many Mayan languages have a glottalic series which is ejective dorsally and often coronally (/q’/, /k’/, /t’/) but implosive bilabially (i.e. /ɓ/ where a /p’/ might otherwise be expected). Other variations of this pattern occur in the family, and the phonemic alternations of the glottalized series in Mayan are well-studied (e.g., [Campbell 1973](Source#cldf:campbell1973glottalic), [Pinkerton 1986](Source#cldf:pinkerton1986quichean), [Russell 1997](Source#cldf:russell1997mam), [Burnett-Deas 2009](Source#cldf:burnett2009mayan), [Shosted 2009](Source#cldf:shosted2009mayan)). As another example, Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada) has both glottalized obstruents and resonants in a mostly symmetric consonant chart. While the typical articulation of glottalized plosives is ejective, glottalized resonants range from full glottal closure to creaky phonation ([Werle 2010](Source#cldf:werle2010wakashan)). Once again, the glottalic series, in this case for resonants instead of obstruents, is in some sense characterized by an abstract \[+glottal\] feature with more than one phonetic realization.

Therefore we chose to include glottalization of all types under the same umbrella, including implosives. However, for an implosive stop to count as a glottalized consonant for our purposes, the implosiveness had to be significant and contrastive: i.e., simple laryngeal lowering, as has been measured for voiced stops in languages like English \[stan1293\] and French \[stan1290\] (Indo-European; ([Clements and Osu 2008](Source#cldf:clementsosu2008implosives): 305-309)), is insufficient on its own. However, a language that has a series of plain voiceless stops contrasting with strongly implosive stops, such as Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia, Peru; ([Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 187f), does meet our criteria.

Some of the data for this feature set were obtained directly from the PHOIBLE database version 2.0 ([Phoible](Source#cldf:phoible), accessed January 27, 2020). A custom R script was written to process it. For Glot-01, a list of all possible glottalized plosives was compiled (complete pre- and post-glottalization, ejectivization, implosivization, and creaky voice), and each available inventory was checked for the presence of at least one of these segments. If a glottalized segment was found, Glot-01 was coded as &lt;yes&gt;, and otherwise as &lt;no&gt;. If the segment was implosive, this information was added to the remarks. The same procedure was repeated for Glot-02 (with a list of all possible glottalized affricates), Glot-03 (with a list of all possible glottalized fricatives), Glot-04 (glottalized nasals), Glot-05 (glottalized liquids), and Glot-06 (glottalized glides). Automatically extracted data are marked with “auto” in remarks. 

Afterwards, 19 automatically extracted languages were checked against grammars for accuracy, which yielded an acceptable error rate. Other discrepancies found in the data or cases where more recent sources have become available were corrected opportunistically while coding for other features. Such corrections are marked by “contra-PHOIBLE” in the remark field of the database.

## Features
### [](ParameterTable#cldf:Glot-01)
&emsp;**{ yes | no }**

Ejectives count as glottalized consonants, as do pre- or post-glottalized consonants and strongly and contrastively implosive stops.

“Laryngealized” consonants are considered as well if they induce glottal closure or require creak on the following vowel. An example of this kind of laryngealization can be seen in Achumawi \[achu1247\] (Palaihnihan; United States; [Nevin 1998](Source#cldf:nevin1998phonology): 53):

> “The most prominent cue distinguishing the laryngealized stops from the plain and aspirated stops is laryngealization of adjacent vowels (creaky voice) \[...\] During the stop phase, creaky voice ceases, and the glottis usually closes.”

### [](ParameterTable#cldf:Glot-02)
&emsp;**{ yes | no }**

The same criteria for glottalized plosives apply to glottalized affricates: They may be ejective, have coarticulated glottal closure or creak, or be implosively articulated.

### [](ParameterTable#cldf:Glot-03)
&emsp;**{ yes | no }**

There are a small number of languages which have a distinction between plain fricatives and ejective ones, such as Tlingit \[tlin1245\] (Athabaskan-Eyak-Tlingit; Canada, United States; [Maddieson et al 2001](Source#cldf:maddiesonetal2001tlingit), [Crippen 2019](Source#cldf:crippen2019tlingit): 789f), which contrasts phonemes such as /x/ vs /x’/, and /s/ vs /s’/. This is distinct from glottalized affricates such as /ts/ vs /ts’/ or /kx/ vs /kx’/. We did not encounter descriptions of glottalized fricatives that were non-ejective.

### [](ParameterTable#cldf:Glot-04)
&emsp;**{ yes | no }**

There are many ways that a glottalic distinction for nasal phonemes can be described: as pre- or post-articulation, such as /m/ vs /ˀm/ or  /n/ vs /nˀ/, as individual but phonemically distinct segments,  such as /m/ vs /ʔm/, as phonemic creak such as /n̰/ or /m̰/, and sometimes given simply as orthographic m̓, n̓. If the segment is described as creaky, we require that the creak be a property introduced by the nasal, and not an autosegmental or vocalic property.

### [](ParameterTable#cldf:Glot-05)
&emsp;**{ yes | no }**

The same considerations applied to glottalized nasal segments are applied to glottalized liquids.

### [](ParameterTable#cldf:Glot-06)
&emsp;**{ yes | no }**

The same considerations applied to glottalized nasal and glottalized liquid segments are applied to glottalized glides.

## Derived features

### [](ParameterTable#cldf:Glot-01q)
&emsp;**{ yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax">if Glot-01 is &lt;yes&gt; or Glot-02 is &lt;yes&gt; or Glot-03 is &lt;yes&gt;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax">if Glot-01 is &lt;no&gt; AND Glot-02 is &lt;no&gt; AND Glot-03 is &lt;no&gt;</td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Glot-04a)
&emsp;**{ yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04 is &lt;yes&gt; OR Glot-05 is &lt;yes&gt; OR Glot-06 is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04 is &lt;no&gt; AND Glot-05 is &lt;no&gt; AND Glot-06 is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Glot-04b)
&emsp;**{ NA | yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if (Glot-04 is &lt;yes&gt; OR Glot-05 is &lt;yes&gt; OR Glot-06 is &lt;yes&gt;) AND Glot-01a is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04 is &lt;no&gt; AND Glot-05 is &lt;no&gt; AND Glot-06 is &lt;no&gt; AND Glot-01a is &lt;yes&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">NA</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-01a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Glot-03a)
&emsp;**{ NA | yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-01a is &lt;yes&gt; and Glot-03 is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-01a is &lt;yes&gt; and Glot-03 is &lt;no&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">NA</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-01a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This derived feature is identical to Glot-03 except that all the languages without any glottalized obstruents at all are coded as &lt;NA&gt;. This is done to maintain statistical independence between Glot-01a and Glot-03a.

### [](ParameterTable#cldf:Glot-04c)
&emsp;**{ NA | yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-04 is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-04 is &lt;no&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">NA</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This derived feature is identical to Glot-04 except that all the languages without any glottalized resonants at all are coded as &lt;NA&gt;. This is done to maintain statistical independence between Glot-04a and Glot-04b.

### [](ParameterTable#cldf:Glot-05a) 
&emsp;**{ NA | yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-05 is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-05 is &lt;no&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">NA</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This derived feature is identical to Glot-05 except that all the languages without any glottalized resonants at all are coded as &lt;NA&gt;. This is done to maintain statistical independence between Glot-04a and Glot-05a.

### [](ParameterTable#cldf:Glot-06a)
&emsp;**{ NA | yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-1wig{font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-1wig">yes</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-06 is &lt;yes&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;yes&gt; and Glot-06 is &lt;no&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">NA</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Glot-04a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This derived feature is identical to Glot-06 except that all the languages without any glottalized resonants at all are coded as &lt;NA&gt;. This is done to maintain statistical independence between Glot-04a and Glot-06a.

## Automatic Extraction from PHOIBLE
Some of the states of this feature set were obtained  directly from data present in the PHOIBLE database. The entire PHOIBLE database was downloaded (version 2.0, downloaded January 27, 2020), and an R script was written to process it searching for glottalized consonants. For every language in our sample, the set of inventories was searched for orthographic glottalizations of all varieties (for example, for the bilabial series, /pʼ/, /pˀ/, /ˀp/, /ɓ/, /ɓ̥/), and if such a phoneme contrasted with a non-glottalized phoneme (/p/, /b/), the relevant feature was coded as &lt;yes&gt;. If there was no such contrast, it was coded as &lt;no&gt;.

After this extraction, 19 automatically coded languages were checked against grammars for accuracy, for both this feature and other derived phonological features. In this review, fewer than 5% of errors were found, so the other extracted values were accepted. Any further errors were corrected opportunistically when coding for other features, and corrections were entered with the remark “contra-PHOIBLE”.

## Results
Glottalized plosives (Glot-01) are overwhelmingly found in North America, along the west coast, in the North American Pueblos, in parts of the North American Southeast, and in Central America (excluding Mixe-Zoquean and Otomanguean languages, and many of their close neighbors). Outside of North America, they are found in the Caucasus and much of the East African Rift Valley, and in some languages in South America without a clear areal pattern. Glottalized affricates (Glot-02) and fricatives (Glot-03) largely occur in a subset of these languages, with glottalized fricatives being very rare. Nearly all glottalized resonants (Glot-04, Glot-05, and Glot-06) occur in a subset of the languages which have glottalized plosives, and almost all of them are in North America.

## Contributions
**Conceptualization**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD)

**Data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Anna Graff](Contributor#cldf:AG)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Marine Vuillermet](Contributor#cldf:MV)

**Computer code**: [David Inman](Contributor#cldf:DI)

## References
[References](Source?cited_only#cldf:__all__)
