Feature set adapted from [Maddieson (2013)](Source#cldf:maddieson2013wals6).

**Authors**: [David Inman](Contributor#cldf:DI)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Anna Graff](Contributor#cldf:AG)

[TOC]

## What?
The presence or absence in a language of a **phonemic distinction between velar and uvular consonants**.

## Why?
The presence of a velar/uvular distinction has been claimed to be a property of certain linguistic areas: particularly the Pacific Northwest ([Campbell 1997](Source#cldf:campbell1997america), [Beck 2000](Source#cldf:beck2000nwcoast)) and Southern California and possibly California generally ([Campbell 1997](Source#cldf:campbell1997america)). This feature appears to be shared with Siberia ([Maddieson 2013](Source#cldf:maddieson2013wals6)), as well as the southern part of South America, more specifically the Andean core described by michaeletal2014andean. Outside of this region, uvulars are concentrated in the Caucasus and parts of Africa.

This survey differs from [Maddieson (2013)](Source#cldf:maddieson2013wals6) by looking at phonemic contrastiveness rather than just whether uvular stops and continuants are present. This definition excludes languages like French, which have a single uvular fricative /ʁ/ that functions as a rhotic, but does not contrast with a velar. As in other phonological feature sets, we exclude sounds that occur only in recent loanwords.

## How?
Some of the data for this feature set were obtained directly from the PHOIBLE database version 2.0 ([Phoible](Source#cldf:phoible), accessed January 27, 2020). A custom R script was written to process it. For each language, inventories were checked for the presence of velar and uvular stops and velar and uvular fricatives. If a pair of velar and uvular stops was found which differed from each other only by manner of articulation (and not by manner and airstream mechanism, e.g. voicing differences), then VelUv-01 was coded as &lt;yes&gt;. Similarly, if a pair of velar and uvular fricatives was found which differed from each other only by manner of articulation, then VelUv-02 was coded as &lt;yes&gt;. Otherwise, the features were coded as &lt;no&gt;. Afterwards, 19 languages were checked against grammars for accuracy, which yielded an acceptable error rate. Other discrepancies found in the data or cases where more recent sources have become available were corrected opportunistically while coding for other features. Such corrections are marked by “contra-PHOIBLE” in the remark field of the database.

Automatically extracted data are marked with “auto” in remarks. The remaining data were coded by hand from available phonological and phonetic descriptions.

## Features
### [](ParameterTable#cldf:VelUv-01)
&emsp;**{ yes | no }**

#### yes: Kalaallisut \[kala1399\] (Eskimo-Aleut; Greenland)
Kalaallisut has both /q/ and /k/ phonemes, alongside /t/ and /p/ making up the language’s stop series ([Aagesen 1987](Source#cldf:aagesen1987greenlandic): 2).

#### yes: Pilagá \[pila1245\] (Guaicuruan; Argentina, Paraguay)
Pilagá distinguishes voiceless /k/ from /q/ ([Vidal 2001](Source#cldf:vidal2001pilaga): 30). The language possesses a voiced /g/ without a uvular counterpart /ɢ/, but the distinction is present for at least one series of stops.

### [](ParameterTable#cldf:VelUv-02)
&emsp;**{ yes | no }**

#### yes: Kalaallisut \[kala1399\] (Eskimo-Aleut; Greenland)
In addition to /q/ and /k/, Kalaallisut also has a contrast between voiced /ʁ/ (orthographic &lt;r&gt;) and /ɣ/ (orthographic &lt;g&gt;). Though the language lacks voiceless continuants, a velar-uvular distinction is present among its voiced fricatives ([Aagesen 1987](Source#cldf:aagesen1987greenlandic): 2). 

#### no: Pilagá \[pila1245\] (Guaicuruan; Argentina, Paraguay)
Though it distinguishes velar and uvular voiceless stops, Pilagá lacks any such distinction in its continuants ([Vidal 2001](Source#cldf:vidal2001pilaga): 30).

## Derived features
### [](ParameterTable#cldf:VelUv-01a)
&emsp;**{ yes | no }**

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-km2t{border-color:#ffffff;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-km2t">yes</th>
    <th class="tg-zv4m">if VelUv-01 is &lt;yes&gt; OR VelUv-02 is &lt;yes&gt;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-km2t">no</td>
    <td class="tg-zv4m">if VelUv-01 is &lt;no&gt; AND VelUv-02 is &lt;no&gt;</td>
  </tr>
</tbody>
</table>

This derived feature groups together all languages which have any distinction between velar and uvular places of articulation, regardless of the manner of articulation.

### [](ParameterTable#cldf:VelUv-02a)
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
    <th class="tg-1wig">NA</th>
    <th class="tg-0lax">if VelUv-01 is &lt;no&gt;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax">if VelUv-01 is &lt;yes&gt; AND VelUv-02 is &lt;yes&gt;</td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax">if VelUv-01 is &lt;yes&gt; AND VelUv-02 is &lt;no&gt;</td>
  </tr>
</tbody>
</table>

This derived feature conditions VelUv-02 on VelUv-01, since it is rare for languages to have a distinction between velar and uvular continuants if they lack the distinction among plosives. This conditioning removes a hidden (linguistic) dependence between VelUv-01 and VelUv-02, which is useful for algorithms that assume independence between variables, but at the cost of rendering &lt;NA&gt; the few languages which maintain the distinction only among continuants.

## Results
As noticed by previous scholars ([Campbell 1997](Source#cldf:campbell1997america): 332-352; [Beck 2000](Source#cldf:beck2000nwcoast); [Maddieson 2013](Source#cldf:maddieson2013wals6); [Michael et al 2014](Source#cldf:michaeletal2014andean)), the presence of a velar-uvular distinction in plosives (VelUv-01) is highly geographically constrained, occurring for the most part along the North American west coast, the southern South American coast (roughly from the southern half of Peru to the Southern Cone), Northeast Asia, and the Caucasus. Isolated examples of uvular contrasts occur elsewhere, some of which is constrained by family (Mayan and Totonacan languages in Central America), and some of which may be areal or contact-driven, but for which our sample lacks sufficient density to say (namely, the Indian isolates of Burushaski \[buru1296\] and Kusunda \[kusu1250\]). The presence of a velar-uvular distinction in continuants (VelUv-02) is attested almost entirely in a subset of the languages which have the distinction among plosives.

## Contributions
**Conceptualization**: [David Inman](Contributor#cldf:DI)

**Data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Anna Graff](Contributor#cldf:AG)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Kellen Parker van Dam](Contributor#cldf:KPVD), [Marine Vuillermet](Contributor#cldf:MV)

**Computer code**: [David Inman](Contributor#cldf:DI)

## References
[References](Source?cited_only#cldf:__all__)
