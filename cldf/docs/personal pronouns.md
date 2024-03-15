**Authors**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI), [Marine Vuillermet](Contributor#cldf:MV), [Balthasar Bickel](Contributor#cldf:BB)

**Acknowledgements**: [Kellen Parker Van Dam](Contributor#cldf:KPVD), [Anna Graff](Contributor#cldf:AG), [Nora Muheim](Contributor#cldf:NJM)

[TOC]

## What?
This survey looks at specific contrasts within the personal pronoun paradigm, such as the presence vs. absence of an inclusive-exclusive opposition, of a minimal-augmented system, and of a number distinction for specific persons. This set of features is based on the typologies of [Cysouw (2003)](Source#cldf:cysouw2003paradigmatic) and [Bickel and Nichos (2005)](Source#cldf:bickel2005inclusive). We have combined these approaches with the aim of capturing patterns with areal potential across personal pronoun paradigms.

Cysouw’s monograph surveys any paradigm linked to person (independent pronouns, indexation affixes, and possessive affixes) and ends up with a very fine-grained typology of about one hundred types, among which only about a dozen turn out to be common ([Cysouw 2003](Source#cldf:cysouw2003paradigmatic)). [Bickel and Nichos](Source#cldf:bickel2005inclusive)’s [2005](Source#cldf:bickel2005inclusive) survey focuses on inclusive-exclusive oppositions found in any person paradigm, i.e. independent pronouns, indexation affixes, and possessive affixes.

Our approach prioritizes the paradigm of personal pronouns, as [Cysouw (2003: 311-315)](Source#cldf:cysouw2003paradigmatic) states that pronouns tend to have more oppositions than indexation and possessive paradigms (see the [How?](#how) section for our criteria and the way we proceed for languages without personal pronouns). Cysouw categorizes person paradigms as wholes, but we have chosen to extract quasi-independent dimensions that reveal common elements across Cysouw’s types. We believe that such elements can be points of convergence and mutual reinforcement in cases of prolonged multilingualism and linguistic area formation. [Cysouw (2003: 249-250, 268, 291-293)](Source#cldf:cysouw2003paradigmatic) provides cognitive maps between different paradigm types based on attested cases of diachronic change. While our aim is different, paradigms that are close in Cysouw’s cognitive map tend to be close according to our coding scheme as well, as we would expect.

## Why?
Aspects of personal pronoun paradigms have been observed to exhibit various areal tendencies.

[Bickel and Nichos (2005)](Source#cldf:bickel2005inclusive) found that the inclusive/exclusive distinction is
- more often present in the Circum-Pacific area (47%) than in the rest of the world (21%),
- more often present in Meso & South America (54%) than in North America (29%),
- much less frequent in Europe and North Asia (17%) than in the rest of the world (43%).

They also found a distributional difference between “Belhare” (1sg and 1excl are morphologically related) and “Chechen” (1sg and 1excl are morphologically unrelated) linguistic types ([Bickel and Nichos 2005](Source#cldf:bickel2005inclusive): 51). The two types are fairly evenly distributed within the Americas, but the Belhare type is the most frequent type elsewhere. Finally, they found that Minimal-Augmented systems occur most frequently in Australia (30%), followed by the Circum-Pacific area (10%); such a system is rare in the rest of the world (1%).

According to [Cysouw (2003)](Source#cldf:cysouw2003paradigmatic), certain types show areal distributions, for example:
- the Sinhalese type (no inclusive/exclusive distinction, no 3sg vs. 3pl) is common in North America and in the languages of Papua New Guinea (but with zero marked 3rd person);
- the Maranao type (minimal-augmented, with number distinction throughout the 4 persons) occurs in non-Pama-Nyungan languages from Australia, in a few Papuan languages, in a few languages in North America (mostly in West California and Oregon), and in Nivkh \[gily1242\];
- the Kwakiutl type (inclusive/exclusive distinction, singular vs. plural opposition only in the 1st person) is attested throughout the world, but interestingly, never widespread within a linguistic family.

Last but not least, according to [Krasnoukhova (2022)](Source#cldf:krasnoukhova2022number), a number of South American languages have all plural pronominal forms derived regularly with a plural marker, while she notes that suppletive plural pronominal forms are more common in the 1st person plural and least common in the 3rd person plural.

## How?
We consider pronouns to be elements that cannot co-occur with a noun phrase indexing the same referent. If a language has several pronoun series, we document pronouns:
- in assertive, intransitive main clauses;
- which encode the S argument of active verbs (e.g. ‘to run’), which is typically subject-like, in cases of split intransitivity;
- which keep track of topic rather than focus on or emphasize a referent (as in Nanti \[nant1250\], see [the example in Ppron-05](#yes-nanti-nant1250-arawakan-peru)).
- which refer to humans, in cases of differences depending on animacy, as it is the prototypical use of pronouns.

In languages where no personal pronouns are attested, we consider the indexation of intransitive verbs in assertive main clauses instead. While [Cysouw (2003)](Source#cldf:cysouw2003paradigmatic) only considered the person slot (if different from number) for indexation, we don’t restrict ourselves to a single slot. Our goal is to detect areal features and we believe that obligatory number distinction could be such a feature, regardless of the way it is marked within a paradigm (e.g. through a person-number stem or through separate person and number affixes). So, if person indexation is unspecified for number, but number marking is obligatory elsewhere for the subject of an intransitive verb, then we consider the paradigm of indexation to display number distinction. However, if the number marking is optional, i.e. if the same form can be used for both singular (or minimal) and plural (or augmented) reference, then we consider that there is no number distinction, as is the case in Nanti \[nant1250\] (see [the example in Ppron-05](#yes-nanti-nant1250-arawakan-peru)).

Special cases arise for languages in which a dual number or dual forms exist. Those are addressed below, as needed for each feature, in special “Dual notes” sections and examples.

## Features (preliminary)
The features in this feature set are categorized into preliminary, main, and derived ones. The main role of the preliminary features is to establish which paradigm has been coded for the main features. They also distinguish the few languages without personal pronouns (Ppron-001), and evaluate our assumption that pronouns encode the most distinctions available in any person paradigm (Ppron-002 and Pron.003).

### [](ParameterTable#cldf:Ppron-001)
&emsp;**{ yes | no }**

Personal pronouns are a person paradigm that cannot co-occur with a noun phrase that refers to the same argument. If the language has one, then this paradigm is used to code for the main features of this feature set. If it does not have any, then indexation of active intransitive verbs is used instead.

#### yes: Kwak’wala \[kwak1269\] (Wakashan; Canada)
Kwak’wala pronouns are enclitics (see Table 1) and they cannot co-occur with a noun phrase having the same referent [Littell (2016)](Source#cldf:littell2016kwakwala:558).

Table 1: Kwak’wala pronominal enclitics.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=ən</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=ənuʔx̌ʷ </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=ənʔs </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=s</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6"><br><br><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=k </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(proximal visible)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=gaʔ </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(proximal invisible)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=ux̌ </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(medial visible)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=uʔ </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(medial invisible)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=iq </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(distal visible)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">=iʔ </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(distal invisible)</span></td>
  </tr>
</tbody>
</table>

#### no: Karok \[karo1304\] (isolate; United States)
There are two pronouns mentioned in [Garrett et al (2020: 13-15)](Source#cldf:garrett2020karok) *váa* and *uum*, which are transitioning into copulas. When used as pronouns they both refer to third person, but in their more copular function they may be used with other persons too. [Bright (1957)](Source#cldf:bright1957karok) does not mention free pronouns at all. We consider the indexing paradigm of Karok for all the main features of this feature set.

### [](ParameterTable#cldf:Ppron-002)
&emsp;**{ yes-auto | yes | no }**

**Note**: This feature was added after most data had been collected and was partially filled without going back to the original sources.

**yes-auto**: If no explicit remarks existed (in the remarks field for other features) about an additional distinction present in a person paradigm of the language, then we assumed that the chosen paradigm encodes all distinctions.
**yes**: The assumption above has been checked with the original sources.
**no**: The additional distinction and when/where it appears is indicated in the remarks.

#### no: Seri \[seri1257\] (isolate; Mexico)
In Seri, independent pronouns can be used for both singular and plural referents, while indexation distinguishes between singular and plural in first and second person (see Table 2, [Marlett 2009](Source#cldf:marlett2009seri): 539-540, 31). The paradigm selected for the main features is that of independent pronouns, but the additional number distinction in the indexation paradigm is explained in the remarks field of this feature.

Table 2: Independent (simple) pronouns and verbal indexation in Seri ([Marlett 2009](Source#cldf:marlett2009seri): 539-540, 31). 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">number</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">pronouns</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">indexation</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></td>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">he</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ʔ- ~ ʔp-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ʔa-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></td>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">me</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">m-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ma-</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3 (human)</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular and plural</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ee</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">∅-</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Ppron-003)
&emsp;**{ NA | yes | no }**

**Note**: Similarly to Ppron-002, this feature was added later. It targets the encoding of clusivity in other person paradigms of the language, beyond the one selected for the main features below (usually the paradigm of personal pronouns). The aim was to track the encoding of clusivity in a language irrespective of paradigm, which corresponds to derived feature [Ppron-01a](#12). For a definition of clusivity see [Ppron-01](#3).

#### yes: Highland Popoluca \[high1276\] (Mixe-Zoque; Mexico)
The Highland Popoluca pronoun paradigm consists of three forms, one for each person (see Table 3), while the indexing paradigm of intransitive verbs consists of four forms, with an additional inclusive person (1+2) (see Table 4). The language has no plural marker for any of the grammatical persons. 

Table 3: Pronouns in Highland Popoluca ([de Jong Boudreault 2009](Source#cldf:boudreault2009popoluca:155): 155) 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">form</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ʔɨch</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mich</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">jeʔ</span></td>
  </tr>
</tbody>
</table>

Table 4: Absolutive indexation (proclitics) in Highland Popoluca ([de Jong Boudreault 2009](Source#cldf:boudreault2009popoluca): 396).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">form</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1excl</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ʔa=</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1incl</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ta=</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mi=</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">∅=</span></td>
  </tr>
</tbody>
</table>

## Features (main)
### [](ParameterTable#cldf:Ppron-01)
&emsp;**{ NA | yes | no }**

For the 1st person plural pronouns, there are three possible contexts that can be distinguished in the world's languages ([Cysouw 2003](Source#cldf:cysouw2003paradigmatic)): 1+2, 1+3, and 1+2+3. The one excluding the addressee (1+3) is exclusive, while the ones including the addressee (1+2 and 1+2+3) are inclusive. It is rare for languages to distinguish between the two inclusive contexts. Therefore we commonly use the terms clusivity or inclusive-exclusive distinction to refer to the distinction of 1+2(+3) and 1+3.

---

**Dual note**: In some grammars, forms that are actually inclusive (1+2(+3)) may be erroneously referred to or described as “dual”, since their most common reference is the minimal inclusive group (1+2) which consists of two people. In such cases, it is usually telling that there is no other dual form in the language (i.e. there are no dual forms for 2nd or 3rd person). However, it is possible although rare that languages do have a real dual form only in the 1st person. In such cases this dual 1st person form is attested in both 1+2 and 1+3 contexts, as long as only two people are involved. Therefore, when a single “dual” form is described in the grammar, one needs to carefully search for examples to establish if it is really a dual form or if it is in fact an inclusive form. There are two possible diagnostic contexts: 
- 1+3 with only two people: If the “dual” form in question is a real dual it will be used in this context, while an inclusive will not.
- 1+2+3: If the “dual” form in question is a real dual it will not be used in this context, while an inclusive will.

Another possible (but very rare) complication is that the language distinguishes inclusive from exclusive in one number (e.g. dual) and not in the other (e.g. plural), as is the case in Hanis \[coos1249\] (Coosan; United States). In such a case, we take into account the number that exhibits the most distinctions and all subsequent features that presuppose an inclusive/exclusive distinction refer to this number.

---

#### NA: Pirahã \[pira1253\] (isolate; Brazil)
The clusivity distinction is not applicable in Pirahã, since the independent pronouns for 1st and 2nd person only encode singular (see Table 5) and there is no pronoun for 1st and 2nd person plural. [Everett (1986: 281-282)](Source#cldf:everett1986piraha) mentions two ways to express 'we'[^1]: either with conjunction (example 1) or with the associative/comitative (example 2). 

Table 5: Independent pronouns in Pirahã ([Everett 1986](Source#cldf:everett1986piraha)).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0x09{background-color:#9b9b9b;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ti</span></td>
    <td class="tg-0x09"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">gíxai</span></td>
    <td class="tg-0x09"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">hiapióxio</span></td>
  </tr>
</tbody>
</table>

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(1)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ti</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">gíxai</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">pí-o</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ahá-p-i-í</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">also-OBL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">go-IMPERF-PROX-COMPLETE-CERT</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">'You and I will go (i.e. we will go).'</span></td>
  </tr>
</tbody>
</table>

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(2)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ti</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">gíxai</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xigí-o</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xopaohoa-i-baí</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ASSOC-OBL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">work-PROX-INTENS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">'I work a lot with you.' or 'we work a lot together.'</span></td>
  </tr>
</tbody>
</table>

#### yes: Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia, Peru)
Table 6 below shows that Ese Ejja has the independent pronouns ekwana, used when the speaker excludes the addressee, and eseya, used when they include them. 

Table 6: Independent pronouns in Ese Ejja (adapted from [Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 348).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e=ya</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e=kwana </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ese=ya </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mi=ya</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mi=kiana</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">o=ya</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Ppron-02)
&emsp;**{ NA | yes | no }**

#### NA: Pirahã \[pira1253\] (isolate; Brazil)
As seen in Table 5 [above](#na-pirahã-pira1253-isolate-brazil), the independent pronouns of Pirahã for 1st person encode only singular number. 

#### yes: Jaqaru \[jaqa1244\] (Aymaran; Peru)
Jaqaru has number-indifferent pronouns, as can be seen in Table 7. 

Table 7: Jaqaru independent pronouns ([Hardman 2000](Source#cldf:hardman2000jaqaru)).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">form</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1 (+3)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">na</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1+2 (+3)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">jiwsa</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2 (+3)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">juma</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3 (+3)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">upa</span></td>
  </tr>
</tbody>
</table>

#### no: Kwak’wala \[kwak1269\] (Wakashan; Canada)
As can be seen in Table 1 in the [Kwak’wala example](#yes-kwakwala-kwak1269-wakashan-canada) in Ppron-001, there are distinct forms for 1sg and 1pl exclusive, namely *=ən* and *=ənuʔx̌ʷ* respectively ([Littell 2016](Source#cldf:littell2016kwakwala:558)).

### [](ParameterTable#cldf:Ppron-03)
&emsp;**{ NA | yes | no }**
 
&lt;NA&gt; encompasses cases with an incl-excl distinction, as well as cases like Pirahã (see Ppron-02 example [above](#na-pirahã-pira1253-isolate-brazil)).

This feature differs only from the previous one (Ppron-02) in the assignment of states for two rare paradigm types (named Sierra Popoluca and Salt-Yui in [Cysouw 2003](Source#cldf:cysouw2003paradigmatic)). The Sierra Popoluca type is a minimal paradigm with no augmented and has 4 persons: 1 (+3), 1 + 2 (+3), 2 (+3), 3 (+3). The Salt-Yui type is a unified-we paradigm with no plural and has 3 persons: 1 (+2, +3), 2 (+3), 3 (+3). Both paradigm types share that their pronouns are number-indifferent (and thus share the same state in Ppron-02). In Ppron-03, the Salt-Yui type is contrasted with the unified-we type.

#### yes: Seri \[seri1257\] (isolate; Mexico)
As seen in Table 2 [above](#no-seri-seri1257-isolate-mexico), Seri has number-indifferent pronouns ([Marlett 2009](Source#cldf:marlett2009seri): 539-540, 31).

#### no: Daga \[daga1275\] (Dagan; Papua New Guinea)
Daga pronouns are shown in Table 8. The forms for 1sg and 1pl are distinct, ne vs nu ([Murane 1974](Source#cldf:murane1974daga): 34).

Table 8: Daga pronouns

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#333;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#333;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#333;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">ne</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">nu</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#333;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">ge</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">e</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#333;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">me</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#333;background-color:transparent">mu</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Ppron-04)
&emsp;**{ NA | inclusive | exclusive | unified we | no }**

#### no: Cavineña \[cavi1250\] (Pano-Tacanan; Bolivia)
Neither *yatse* '1du' nor *ekwana* '1pl' seem related to the endonym Cavineña, whose origin is unknown ([Guillaume 2008](Source#cldf:guillaume2008cavinena): 1). It might originate from “Caviña”, the name of one of the two moieties in the neighboring sister language Araona. 

#### inclusive: Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia, Peru)
Ese Ejja \[eseʔeχa\] is an endonym and it resembles the form *ese(a)* '1incl'. A possible etymology is from *ese(a)'dejja* \[eseɖeχa\] 'we people', where the dental implosive is realized as a glottal stop: ese'dejja &gt; Ese Ejja ([Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 45-46).

### [](ParameterTable#cldf:Ppron-05)
&emsp;**{ NA | yes | no }**

In the literature, languages in which 1incl and 1excl forms have equally many number distinctions are known as '**minimal(-augmented)**' systems ([Cysouw 2003](Source#cldf:cysouw2003paradigmatic)). In other words, such systems consider 1+2 as a grammatical person just like 1st, 2nd or 3rd person: they have 4 grammatical persons in the minimal number. The augmented number refers to adding at least one 3rd person to these four grammatical persons. Tables 7 and 8 summarize this conceptualization: in Table 9 the augmented number is derived from the minimal with an “augmentizer” affix, while in Table 10 the minimal and augmented forms are not morphologically related.

Table 9: Schematic Minimal-Augmented system with the augmented forms derived from minimal forms. 

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Minimal (basic unit)</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Augmented (basic unit + 3)</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a-AUGM</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1+2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b-AUGM</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c-AUGM</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">d</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">d-AUGM</span></td>
  </tr>
</tbody>
</table>

Table 10: Schematic Minimal-Augmented system with no morphological relationship between the two numbers

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Minimal (basic unit)</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Augmented (basic unit + 3)</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">e</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1+2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">f</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">g</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">d</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">h</span></td>
  </tr>
</tbody>
</table>

---

**Dual note**: There are cases where the 1incl is described as dual, while no other person has a dual, only a plural. In such cases it is fairly straightforward that the system is better described as minimal-augmented with no dual present whatsoever. However, there are even cases where there is a dual for all persons (and for 1incl), but this 1incl form does not pattern morphologically with the other duals and seems more in line with the singular forms. We categorize such cases as minimal-augmented too (see Umpila [below](#yes-umpila-umpi1239-pama-nyungan-australia)). 

Finally, there are a few cases where 1incl has a dual and a plural, 1excl has a singular and a plural, while the other persons have dual and plural. Here it seems that the 1excl is the exception, while dual exists as a category in the language, and the system should not be categorized as minimal-augmented.

---

#### yes: Nanti \[nant1250\] (Arawakan; Peru)
Pronouns in Nanti, as described in [Michael (2008)](Source#cldf:michael2008nanti), look like a singular-plural system with a special 1st inclusive form (see Table 11). 

Table 11: Topic pronouns in Nanti (adapted from [Michael 2008](Source#cldf:michael2008nanti): 372).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">naro</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">narohegi </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">harohegi </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">biro</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">birohegi</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3 </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">iriro </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(masc.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">irirohegi </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(masc.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">iroro </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(non-masc.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">irorohegi </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(non-masc.)</span></td>
  </tr>
</tbody>
</table>

However, [Michael (2020)](Source#cldf:michael2020nantipc) confirms that the plural marker *-hegi* is optional, even for the first person inclusive *haro*. Therefore, the topic pronoun system can be reanalyzed as in (10b), since we do not consider optional plural marking. Since the 1st inclusive form can occur without the plural marker, it can be analyzed as a separate person, and the system of independent topic pronouns in Nanti is thus a minimal system (without an augmented number). This reanalysis of the topic pronouns is also mirrored by Nanti’s focus pronouns, which lack number differentiation altogether.

Table 12: Nanti topic pronouns reanalyzed

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">form</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">naro</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1+2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">haro</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">biro</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">iriro </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(masc.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">iroro </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(non-masc.)</span></td>
  </tr>
</tbody>
</table>

#### yes: Umpila \[umpi1239\] (Pama-Nyungan; Australia)
The independent pronouns of Umpila can be analyzed as having singular, plural and dual number as in Table 13 below (adapted from [Cysouw 2003](Source#cldf:cysouw2003paradigmatic)).

Table 13: Independent pronouns of Umpila.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dual</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋayu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋana</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> (excl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋana</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> (excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋambula </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋali </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋanu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋuʔula</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋuʔula</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nhulu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">bula</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">bula</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span></td>
  </tr>
</tbody>
</table>

However, the 1incl dual is the only dual form not derived from the corresponding plural form with the addition of *-baʔamu*. The system could be better reanalyzed as minimal-augmented with a dual additional number as shown in Table 14 below. Such systems are referred to as partial-unit-augmented in [Cysouw (2003)](Source#cldf:cysouw2003paradigmatic).

Table 14: Reanalyzed independent pronouns of Umpila.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">minimal</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">augmented</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dual</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1+2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋali</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋambula</span></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋayu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋana</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋana</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋanu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋuʔula</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋuʔula</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nhulu</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">bula</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">bula</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-baʔamu</span></td>
  </tr>
</tbody>
</table>

#### no: Lavukaleve \[lavu1241\] (isolate; Solomon Islands)
The personal pronouns of Lavukaleve can be seen in Table 15 below. The dual and plural 1incl forms have the same morphological relationship as the 1excl dual and plural forms, the dual has an additional *-l* suffix. There is thus no indication that 1incl is a basic unit in the person system, as is the case for Umpila [above](#yes-umpila-umpi1239-pama-nyungan-australia).

Table 15: Personal pronouns of Lavukaleve ([Terrill 2003](Source#cldf:terrill2003lavukaleve): 170).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dual</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ngai</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e-l </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">me </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">me-l </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">inu</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">imi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">imi-l</span></td>
  </tr>
</tbody>
</table>

#### no: Ngarinyin \[ngar1284\] (Worrorran; Australia)
There is no evidence that the inclusive *ŋarun* in Ngarinyin represents a separate basic grammatical person: rather than having a distinct plural (or rather augmented form), the inclusive is available for both minimal and augmented configurations: 1+2 *and* 1+2+3.

Table 16 Personal pronouns in Ngarinyin ([Rumsey 1978](Source#cldf:rumsey1978ungarinjin)).

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">njarun </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ŋarun </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">njaŋan</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nurun</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="4"><br><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">djiri </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(masc.)</span></td>
    <td class="tg-0lax" rowspan="4"><br><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">biri</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:italic">njindi</span> (fem.)</td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:italic">mindi </span>(m-class neut.)</td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-style:italic">di </span>(w2-class neut.)</td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Ppron-06)
&emsp;**{ NA | 1excl/pl = 1sg + pl | 1excl/pl includes 1sg | no relation }**

For this feature, we have aligned the first person exclusive (in languages with a clusivity distinction) with the first person plural (in languages that lack that distinction) in order to generate cross-linguistic comparisons. This decision was made following the observation that in many languages with a clusivity distinction the 1st person singular and the 1st person exclusive share morphological material ([Cysouw 2003](Source#cldf:cysouw2003paradigmatic); [Bickel and Nichos 2005](Source#cldf:bickel2005inclusive)). The &lt;**1excl/pl = 1sg + pl**&gt; state means that the exclusive or plural is derived from the first person with a plural marker, while the &lt;**1excl/pl includes 1sg**&gt; state means that the 1sg morpheme is included in the plural or exclusive form, but without anything that can be interpreted as a plural marker. In order for a morpheme to be considered a plural marker, it should manifest itself as a plural marker in at least another instance outside the 1st person (e.g. for other personal pronouns or nouns). &lt;NA&gt; is used only in cases where there is neither 1st person exclusive nor 1st person plural.

---

**Dual note**: The essence of this feature is the sharing of morphology across 1st persons, irrespective of number. If this is the case, then we would expect a dual number to follow this pattern. Therefore, in case the language has a dual and a plural number and the pattern is not consistent (e.g. 1excl dual includes 1sg, but 1excl plural doesn’t), we code the language as &lt;?&gt; for this feature (see Garrwa below).

---

#### 1excl/pl = 1sg + pl: Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia, Peru)
The Ese Ejja personal pronoun system has a plural morpheme used for both 1st and 2nd person, *-kwana~-kiana* (see Table 17). When applied to the 2nd person it yields 2nd person plural, but when applied to 1st person it yields 1st person exclusive:

Table 17: Ese Ejja personal pronouns (adapted from [Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 342)

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e(ya)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">e</span><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">kwana </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ese(ya) </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mi(ya)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">mi</span><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">kiana</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">o(ya)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ona</span></td>
  </tr>
</tbody>
</table>

#### 1excl/pl includes 1sg: Karitiâna \[kari1311\] (Tupian; Brazil)
In Karitiâna, the 1excl form contains the 1sg form, as can be seen in Table 18, but without a plural marker. Instead, the plural morpheme *-jxa* is used to derive the inclusive.

Table 18: Karitiâna pronouns

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">yn</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">yta </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">y</span><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">jxa </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">an</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">a</span><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">jxa</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">i</span></td>
  </tr>
</tbody>
</table>

#### no relation: Ngarinyin \[ngar1284\] (Worrorran; Australia)
As can be seen in Table 16 [above](#no-ngarinyin-ngar1284-worrorran-australia), there is no morphological relationship between the 1sg form *ŋin* and the 1excl form *njarun*.

#### ?: Garrwa \[gara1269\] (Garrwan; Australia)
The nominative stem of Garrwa pronouns can be seen in Table 19 ([Mushin 2012](Source#cldf:mushin2012garrwa:85): 85). The 1st singular pronoun *nga-yu* (the root is *nga-* according to the source) is partially included in the 1excl dual form *ngali(ya)*, while the 1excl plural form *nurru* seems morphologically unrelated. Since dual and plural follow different patterns here, we code this language as &lt;?&gt; following the Dual note above.

Table 19: nominative stem of Garrwa pronouns ([Mushin 2012](Source#cldf:mushin2012garrwa:85): 85)

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">singular</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dual </span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plural</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1</span></td>
    <td class="tg-0lax" rowspan="2"><br><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nga-yu</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ngali(ya) </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nurru </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(excl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nungka(la) </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ngambala </span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(incl.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ni-nji</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nimbala</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">narri</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nyulu</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">bula</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">yalu</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:Ppron-07)
&emsp;**{ NA | 1incl = 1sg + pl | 1incl includes 1sg | no relation }**

Like the relationship between 1st person singular and exclusive (or unified we), there can also be a relationship between 1st person singular and 1st person inclusive, although [Krasnoukhova (2022)](Source#cldf:krasnoukhova2022number) observes that the inclusive is not morphologically derived in most languages. If a language has no clusivity marking, this feature is coded as &lt;NA&gt;.

Note that this feature is not applicable for minimal-augmented systems.[^2] 

---

**Dual note**: As for Ppron-06, in case the language has a dual and a plural number and the pattern is not consistent (e.g. 1incl dual includes 1sg, but 1incl plural doesn’t), the language  is coded as &lt;?&gt;.

---

#### 1incl = 1sg + pl: Karitiâna \[kari1311\] (Tupian; Brazil)
As indicated in Table 18 [above](#1exclpl-includes-1sg-karitiâna-kari1311-tupian-brazil), the 1st person inclusive in Karitiâna is made up of the 1sg and a plural morpheme.

#### 1incl includes 1sg: Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia and Peru)
As shown in Table 6 [above](#yes-ese-ejja-esee1248-pano-tacanan-bolivia-peru), Ese Ejja demonstrates a morphological relationship between 1incl and 1sg, but without plural marking. The *-se* component of the 1incl *ese* is likely from an old dual morpheme, which has a cognate *(a)tse* in Cavineña ([Guillaume 2008](Source#cldf:guillaume2008cavinena): 78).

#### no relation: Ngarinyin \[ngar1284\] (Worrorran; Australia)
As can be seen in Table 16 [above](#no-ngarinyin-ngar1284-worrorran-australia), there is no morphological relationship between the 1sg form *ŋin* and the 1incl form *ŋarun*.

### [](ParameterTable#cldf:Ppron-08)
&emsp;**{ NA | yes | no }**

#### yes: Kwak’wala \[kwak1269\] (Wakashan; Canada)
Kwak’wala has a series of pronominal enclitics (see Table 1 [above](#yes-kwakwala-kwak1269-wakashan-canada)). The pronominal subject enclitics have a number distinction only for the 1st person.

#### yes: Nanti \[nant1250\] (Arawakan; Peru)
As shown in Table 11 [above](#yes-nanti-nant1250-arawakan-peru), the plural (or better augmentive) marking of Nanti topic pronouns is optional. Therefore the form for 2nd person minimal can also be used for 2nd person augmented contexts.

#### no: Karitiâna \[kari1311\] (Tupian; Brazil)
As indicated in Table 18 [above](#1exclpl-includes-1sg-karitiâna-kari1311-tupian-brazil), the 2sg form *an* in Karitiâna is distinct from the 2pl *ajxa*.

### [](ParameterTable#cldf:Ppron-09)
&emsp;**{ NA | yes | no }**

There are many cases where there are not any 3rd person pronouns and it is noted that demonstratives are used instead (see [Bhat 2004](Source#cldf:bhat2004pronouns), [Bhat 2013](Source#cldf:bhat2013wals)). In such cases, this feature is coded based on whether these demonstratives have an obligatory number distinction. 

---

**Dual note**: If the language has both a 3rd dual and a plural, the comparison is always between 3sg and 3pl.

---

#### yes: Ese Ejja \[esee1248\] (Pano-Tacanan; Bolivia and Peru)
As can be seen in Table 6 [above](#yes-ese-ejja-esee1248-pano-tacanan-bolivia-peru), in the independent pronoun paradigm, Ese Ejja has a single form *oya* for 3rd person, no matter whether the referent is singular or plural, while 1st and 2nd have a dedicated plural form.

## Derived Features
### [](ParameterTable#cldf:Ppron-01a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-01 is &lt;NA&gt; AND Ppron-003 is &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-01 is &lt;yes&gt; </span>OR Ppron-003 is &lt;yes&gt;</td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-01 is &lt;no&gt; AND Ppron-003 is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This feature unites all languages that have an inclusive-exclusive distinction in pronouns and/or indexation.

### [](ParameterTable#cldf:Ppron-04a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-04 is &lt;ΝΑ&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-04 is &lt;inclusive&gt; OR &lt;unified we&gt; OR &lt;exclusive&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-04 is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

There was no attested case of an endonym being related to the 1st person exclusive form. This derived feature groups languages with an endonym that is related to the 1st inclusive or unified-we form (for languages with no inclusive-exclusive distinction).

### [](ParameterTable#cldf:Ppron-06a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;1excl or pl is 1sg plus pl&gt;  OR &lt;1excl or pl includes 1sg&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;no relation&gt;</span></td>
  </tr>
</tbody>
</table>

This feature groups all languages that have shared morphology between 1st person singular and 1st person exclusive (or unified we when there is no inclusive-exclusive distinction).

### [](ParameterTable#cldf:Ppron-06b)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;NA&gt; OR &lt;no relation&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;1excl or pl is 1sg plus pl&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-06 is &lt;1excl or pl includes 1sg&gt;</span></td>
  </tr>
</tbody>
</table>
	
This feature separates the languages with a &lt;yes&gt; state from the previous feature (Ppron-06a) in the ones that have pluralizing morphology and the ones who do not.
 
### [](ParameterTable#cldf:Ppron-07a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;1incl is 1sg plus pl&gt; OR &lt;1incl includes 1sg&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;no relation&gt;</span></td>
  </tr>
</tbody>
</table>
	
This feature groups all languages that have shared morphology between 1st person singular and 1st person inclusive.

### [](ParameterTable#cldf:Ppron-07b)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;NA&gt; OR &lt;no relation&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;1incl is 1sg plus pl&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-07 is &lt;1incl includes 1sg&gt;</span></td>
  </tr>
</tbody>
</table>
	
This feature separates the languages with a &lt;yes&gt; state from the previous feature (Ppron-07a) into the ones which have pluralizing morphology and the ones which do not.

### [](ParameterTable#cldf:Ppron-08a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-02 is &lt;yes&gt; OR &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-02 is &lt;no&gt; AND Ppron-08 is &lt;yes&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-02 is &lt;no&gt; AND Ppron-08 is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>
	
Since it is vanishingly rare to have a number distinction in 2nd and 3rd person if there is no such distinction in the 1st person ([Corbett 2000](Source#cldf:corbett2000number): 62-65), this feature conditions Ppron-08 on Ppron-02. This way Ppron-08a and Ppron-02 are independent.

### [](ParameterTable#cldf:Ppron-09a)
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-09 is &lt;NA&gt; OR </span>Ppron-08a is &lt;yes&gt; OR &lt;NA&gt;</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-09 is &lt;yes&gt; AND Ppron-08a is &lt;no&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Ppron-09 is &lt;no&gt; AND Ppron-08a is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

For the same reasons as for Ppron-08a, this feature conditions Ppron-09 on Ppron-08a, i.e. on the language having a number distinction in the 2nd person. In the case of English \[stan1293\], the most famous language which lacks a number distinction in the 2nd person but maintains it in the 3rd, this apparent lack of 2nd person number marking arguably belies an underlying distinction, as evidenced by multiple varieties of English “fixing” this problem with new second person plural forms (*you guys*, *y’all*, *youse*, *yins*, etc).

## Results
As expected, the vast majority of languages in our sample do have personal pronouns, with the exception of 9 North American languages and Hattic \[hatt1246\], an extinct isolate of present-day Turkey (Ppron-001). Also, most languages make the same or more person and number distinctions in their pronominal paradigms than in indexing, confirming the observations of [Cysouw (2003)](Source#cldf:cysouw2003paradigmatic) (Ppron-002). Interestingly, of the 24 languages in our sample that make more distinctions in the indexing paradigm, 18 are from North America.

As far as clusivity is concerned, the results from our sample also largely confirm the observations of [Bickel and Nichos (2005)](Source#cldf:bickel2005inclusive), with Australia and South America having the highest prevalence of clusivity distinction (96% and 54% respectively) (Ppron-01a). Among systems with a clusivity distinction, Australia and South America also have the highest prevalence of Minimal(-Augmented) systems (30% and 22% respectively, or 29% and 12% of all languages in the macroarea), with Papunesia following (20% of languages with clusivity distinctions, or 7% of all languages in the macroarea) (Ppron-05). Within South America, such systems are more common in the Andean region and in a group of mostly Cariban languages in the north.

Some morphological relationship between 1sg and 1pl exclusive (or unified we) (Ppron-06a) is more common globally than a morphological relationship between 1sg and 1pl inclusive (Ppron-07a) (38% vs 26%), and any relationship between 1sg and an inclusive or exclusive plural is vanishingly rare in Papunesia. Among the languages with a morphological relationship between 1sg and 1pl exclusive (or unified we), which include the “Belhare” type of [Bickel and Nichos (2005)](Source#cldf:bickel2005inclusive), the vast majority derive their 1pl with a plural marker, except for a cluster in western Amazonia, where this is not the case (Ppron-06b). 

Finally, in terms of number distinctions, the Americas stand out as having many more cases of no number distinction for 3rd person compared with the rest of the world. This pattern is similar for no number distinctions for the 2nd person (especially for North America) and even the 1st person, although this is overall much rarer.

## Contributions
**Conceptualization**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI), [Marine Vuillermet](Contributor#cldf:MV), [Balthasar Bickel](Contributor#cldf:BB)

**Data collection**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Kellen Parker Van Dam](Contributor#cldf:KPVD), [Anna Graff](Contributor#cldf:AG), [David Inman](Contributor#cldf:DI), [Nora Muheim](Contributor#cldf:NJM), [Marine Vuillermet](Contributor#cldf:MV)

**Supervision of data collection**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Kellen Parker Van Dam](Contributor#cldf:KPVD), [David Inman](Contributor#cldf:DI), [Marine Vuillermet](Contributor#cldf:MV)

## References
[References](Source?cited_only#cldf:__all__)

[^1]: Examining all examples in several souces on Pirahã (\citealt{everett1986piraha, sheldon1988piraha, everett1993piraha}) didn’t uncover any case where the 1st person pronoun was used and then interpreted/translated as “we” (1+3). Also, no cases of “I and him” or “I with him” were found.
[^2]: Making Ppron-07 applicable to minimal-augmented systems is not trivial, as it is not clear what forms should be compared. We considered three options: (i) Ppron-07 is not applicable for minimal-augmented systems, the option we ultimately chose, (ii) the forms compared are 1 (minimal exclusive) and 1+2 (minimal inclusive), (iii) the forms compared are 1+2 (minimal inclusive) and 1+2+3 (augmented inclusive). Option (ii) is appealing for comparing the “same” forms as in a singular-plural system. However, the conceptualization of 1+2(+3) (1st plural inclusive) is arguably different from 1+2 (minimal inclusive), since the last one is a basic person of the system. Option (iii) retains the symmetry of the plural/augmented relationship between the two forms being compared, but loses the connection to the arguably more basic 1 (sg or minimal exclusive) form. Thus, we opt for Option (i), the most conservative in a sense, since it remains agnostic.
