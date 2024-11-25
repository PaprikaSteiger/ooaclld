**Authors**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI), [Balthasar Bickel](Contributor#cldf:BB)

**Acknowledgements**: [Thomas Huber](Contributor#cldf:TH), [André Müller](Contributor#cldf:AM), [Marine Vuillermet](Contributor#cldf:MV)

[TOC]

## What?
This feature set catalogs different lexical classes of nominal possession (henceforth, **noun possession classes**) and the constructions available to them. These classes are defined by their lexically-restricted access to particular constructions of nominal possession (i.e., constructions which form a noun phrase) and unpossession (i.e., the possibility for nouns to be expressed without a possessor, and how that is done). This includes the commonly-described alienable and inalienable noun classes, as well as nonpossessible nouns, but also possession classes that are not semantically coherent. A complete account of the scope of this feature is given in [Chousou-Polydouri et al (2023)](Source#cldf:chousoupolydouri2023multivariate), for which a summary is presented here.

This feature set strictly focuses on categorical possession classes and noun phrases which are headed by the (un)possessed noun. This excludes possession that is (i) statistically-differentiated (i.e., one set of nouns is *more likely* to be attested in a certain set of constructions), or (ii) expressed via predicative possession, possessor raising, or other constructions which yield a verb-headed phrase (rather than a noun-headed one). Because it is focused on *constructions*, this feature set also does not count the number of classifiers in a language. A set of nouns that all take different possessive classifiers are categorized and encoded as having access to a single classifier construction, rather than to separate constructions for each individual classifier.

This feature set is focused on possession constructions where the possessor is expressed by an overt noun, rather than by a pronominal element only. The main reason for this decision is for comparison. The locus of possessive marking — whether it is on the head (possessed) noun, the dependent (possessor) noun, or both — can be difficult to determine under pronominal possession, especially if the pronoun encliticizes onto the head noun, or if the pronominal element is dedicated to expressing possession (and there is no clear genitive marker indicating locus of marking). Given the importance of locus in typological research ([Nichols 1986](Source#cldf:nichols1986marking)), the encoding of this feature has prioritized constructions with nominal possessors over pronominal possessors. Pronominal constructions have only been encoded when they are necessary for distinguishing between noun possession classes, or if they were the only constructions presented in available sources.

## Why?
[Bugaeva et al (2021)](Source#cldf:bugaevanicholsbickel2021possession) claim that non-possessible nouns, that is nouns which must have their possession expressed through an appositive construction, are an American and Oceanic phenomenon, and similarly [Bickel and Nichols (2013)](Source#cldf:bickelnichols2013wals) cite obligatory possession as a particularly American feature. [Campbell (1997: Chapter 9)](Source#cldf:campbell1997america) cites an alienable/inalienable distinction as diagnostic for several American areas (the Northwest Coast, the Plains, and Mesoamerica). The anecdotal experience of many members of the ATLAs team also suggested to us that possession strategies were a good candidate for areal features within the region.

## How?
Unlike most of the other feature sets in ATLAs, all the features in this feature set are derived from an underlying database of possession. The scope and structure of this database, as well as the intermediate computational steps performed to derive the present features are described in detail in [Chousou-Polydouri et al (2023)](Source#cldf:chousoupolydouri2023multivariate).  Below we provide a brief summary.

Data about possession for every language were encoded into two data tables: One which catalogs possession classes (the Possession Class Table), and one which catalogs constructions (the Construction Table). These tables are available in CLDF format on the [ATLAs GitHub repository](https://github.com/davidainman/atlas-data/cldf-possession/). Note that a variety of different derived features can be extracted from the full data.

The Possession Class Table lists all the possession classes in the language. Every language has at least one possession class (the default class), which in the minimal case is the entire set of the language’s nouns. Further possession classes exist only if a lexically-defined set of nouns can be found which has access to a different combination of possession and unpossession constructions than the default class.

Once the set of possession classes in the language is determined, the class is given a name and entered into the Possession Class Table. The semantic categories (see Table 1) of members of the possession class are also listed in this table according to a semantic ontology (see Table 2)

<div class="datainset">
Table 1: Semantic categories (expanded from <a class="Source" href="../sources/chousoupolydouri2023multivariate">Chousou-Polydouri et al 2023</a>). 
<table class="fulltable"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">animals</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">animals, wild or domesticated</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">wild_animals</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">wild animals only</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body parts in a broad sense, possibly including mental faculties, feelings, name, etc., as well as (some) body functions, excreta, footprints, etc.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body_internal</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">internal body parts only</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">humans</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">human or higher animate (divine or supernatural beings, etc.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> kin relations</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kin related by blood (not marriage)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin_above_ego</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">parents and grandparents</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin_below_ego</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">siblings, children, grandchildren</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">non_blood_kin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kin related through marriage</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nuclear_kin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">only parents, siblings, and children</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nature_inanimate</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">rocks, mountains, celestial objects, etc.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">celestial</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">sun, moon, stars, etc.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">relation</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">relational nouns, such as teacher, master, birthplace</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">owner</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘master’, ‘owner’, etc.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">place_relation</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">native land, village, etc.<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">part</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">the part in part-whole relations; spatial relations nouns, locatives, etc.; subsetting terms like ‘group’, ‘part’, etc.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plant_part</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plant parts (root, leaf, branch, etc.)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plants</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">whole plants and types of plants</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">intimate_property</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">furniture, tools, weapons, clothes, ornaments</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">clothing</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">clothing items and ornaments</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">tools</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">tools and weapons</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">names</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">person and place names</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">food</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plants and animals used as food, processed food</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mass_noun</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">all uncountable nouns<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mixed</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a lexically specified class with no semantic cohesion</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">default</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">the default set of nouns, membership in which is determined once all other semantic categories are subtracted</span></td>
  </tr>
</tbody></table>
</div>

<div class="datainset">
Table 2: Semantic ontology relating the different semantic categories. DD stands for deduced category, a semantic category that was not attested in our sample (expanded from <a class="Source" href="../sources/chousoupolydouri2023multivariate">Chousou-Polydouri et al 2023</a>).
<table class="fulltable"><thead>
  <tr>
    <td class="tg-0lax" rowspan="22"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">default</span></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_default</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body_internal</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_body_external</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kin</span></td>
    <td class="tg-0lax" rowspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin</span></td>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nuclear_kin</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin_below_ego</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">blood_kin_above_ego</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_non_nuclear_blood_kin</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">non_blood_kin</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">part</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plant_part</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_other_part</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nature</span></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plants</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nature_inanimate</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">celestial</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_non_celestial</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">animals</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">wild_animals</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_domestic_animals</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">humans</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2" rowspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">relation</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">owner</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">place_relation</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DD_other_relation</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2" rowspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">intimate_property</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">clothing</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">tools</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">food</span></td>
  </tr>
  <tr>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">names</span></td>
  </tr></thead></table>
</div>

All possession constructions in the language are entered into the Constructions Table, and each construction is associated with at least one possession class that has access to it. Each construction falls into one of three categorical types: possession constructions, unpossession constructions, and suppletive constructions (see section Suppletion constructions and suppletive classes below).

Possession constructions are given a Construction Type, which is a schematic representation that combines locus/type of marking and agreement properties. Locus/type can be PSSR (marking on the possessor noun), PSSD (marking on the possessed noun), JUXT (no marking on either noun), CLASS (the possessed noun is not syntactically possessed at all, but a classifier is possessed in its stead), and CLAUSE (the possessed noun is always the syntactic argument of a verb expressing possession: direct nominal possession is impossible). Agreement is schematized with brackets, follows the locus on which agreement occurs (PSSR or PSSD), and gives the element that the morphology agrees with (e.g., PSSR\[AGR:PSSD\] indicates a locus of marking on the possessor noun which morphologically agrees with the possessed noun). In the case of complex constructions with multiple morphemes, these elements can be combined with “+”. For example, PSSD + PSSD\[AGR:PSSR\] indicates two morphemes, both on the possessed noun, one of which only marks possession, and another which agrees with the possessor. PSSR + PSSD\[AGR:PSSR\] indicates a construction with one morpheme on the possessor noun (which does not express agreement) and one morpheme on the possessed noun (which agrees with the possessor).

Unpossession constructions are all given the Construction Type UNPOSSESSION, with a free-form shape explaining what the unpossession construction is. If no unpossession constructions are present for a given class, it is assumed that member nouns can appear unpossessed without any special morphology.

The Possession Class Table and Construction Table are analyzed jointly using R scripts to generate intermediate levels of structure, classify possession classes semantically, and finally to the language-wide features presented below. All R code is available in the [ATLAs Github repository](https://github.com/davidainman/atlas-data/cldf-possession/).

### Suppletion constructions and suppletive classes
Suppletion constructions were not included in [Chousou-Polydouri et al (2023)](Source#cldf:chousoupolydouri2023multivariate). This type of construction indicates that the shape of the nominal stem changes between possessed and unpossessed, and are assigned the Construction Type SUPPLETION. This is not formally a construction in the way that possession and unpossession are, but rather sets of lexical pairs, for which one member always appears unpossessed and the other always appears possessed.

In fact, SUPPLETION covers a wide range of phenomena which were not possible to accurately represent within our database. On one end of the range, one encounters cases of irregular stem changes in a small group of nouns, with the etymological relationship between the two stems being obvious. On the other end, one has two completely different stems that are usually treated as different nouns in the grammar. Both types are exemplified by nouns in Wari’, which when affixed with a possession marker, undergo unpredictable stem changes. Some of these changes preserve a clear relationship between the possessed and unpossessed forms, such as in the pairs *toc/tocoxi* ‘eye/our eye’, *at/araxi’* ‘bone/our bone’, *catat/caraxixi’* ‘breast/our breast’. Other pairs though do not preserve any clear relationship, as in *topac/capijaxi’* ‘mouth/our mouth’, and *jat/xixi’* ‘teeth/our teeth’ ([Everett and Kern 1997](Source#cldf:everett1997wari): 436-440). Arguably, one could categorize one of these nouns as obligatorily possessed, and the other as unpossessible, but they would share the same meaning (if we don’t consider possessibility part of the noun’s meaning). Categorizing all intermediate cases of SUPPLETION in these two extremes proved impossible, and instead we opted for grouping them under a special class (SUPPLETIVE) and a special construction type (SUPPLETION). Details of the lexical class membership and which proper constructions this class has access to are given in the remarks fields of the tables. 

Because suppletion in the database is a special case which neither forms a coherent possession class nor a coherent kind of construction, when extracting the derived questions for this feature set (see below), suppletion only contributes to NounPoss-22, the presence of suppletive pairs as such.

## Features
We have derived many features on possession from the underlying database, as the typology of possession is highly multivariate and many views can be taken of it. The features are thus broken into conceptual groups. [NounPoss-01](#nounposs-01-how-many-morphosyntactically-distinct-possession-classes-are-there) is about the overall number of possession classes in a language, and [NounPoss-02](#nounposs-02-what-are-the-semantic-types-of-the-possession-classes), [03](#nounposs-03-how-many-conceptually-inalienable-possession-classes-are-there), [04](#nounposs-04-how-many-conceptually-non-possessible-possession-classes-are-there), [05](#nounposs-05-how-many-mixed-possession-classes-are-there) primarily concern the semantic categorization of possession classes. [NounPoss-06](#nounposs-06-what-are-the-semantic-categories-included-in-conceptually-inalienable-classes) and [07](#nounposs-07-what-are-the-semantic-categories-included-in-conceptually-non-possessible-classes) concern the gross semantic categories present in possession classes. [NounPoss-08](#nounposs-08-what-are-the-nominal-possession-constructions-used-for-the-default-possession-class), [09](#nounposs-09-what-are-the-nominal-possession-constructions-used-for-conceptually-inalienable-classes-if-present), [10](#nounposs-10-what-are-the-nominal-possession-constructions-used-for-conceptually-non-possessible-classes-if-present), [11](#nounposs-11-if-there-is-a-conceptually-inalienable-possession-class-what-are-its-unpossession-constructions) concern the possession and unpossession constructions that are used per noun class semantic type. [NounPoss-12](#nounposs-12-is-there-a-juxt-possession-construction-and-if-so-for-which-conceptual-classes), [13](#nounposs-13-is-there-a-pssr-possession-construction-and-if-so-for-which-conceptual-classes), [14](#nounposs-14-is-there-a-pssd-possession-construction-and-if-so-for-which-conceptual-classes), [15](#nounposs-15-is-there-a-pssr-and-pssd-possession-construction-and-if-so-for-which-conceptual-classes), [16](#nounposs-16-is-there-a-clause-possession-construction-and-if-so-for-which-conceptual-classes), [17](#nounposs-17-is-there-a-class-possession-construction-and-if-so-for-which-conceptual-classes), [18](#nounposs-18-if-any-head-marking-construction-is-used-pssd-or-pssr-and-pssd-does-the-possessed-noun-contain-any-agreement-with-the-possessor), [19](#nounposs-19-if-any-head-marking-is-present-pssd-or-pssr-and-pssd-is-there-any-morpheme-which-only-marks-the-possessed-noun-without-agreeing-with-the-possessor), [20](#nounposs-20-does-possession-ever-involve-stem-suppletion) primarily concern the presence of different types of constructions. [NounPoss-21](#nounposs-21-how-many-possession-classes-of-optionally-possessed-nouns-in-terms-of-valence-are-there), [22](#nounposs-22-how-many-possession-classes-of-obligatorily-possessed-nouns-in-terms-of-valence-are-there), [23](#nounposs-23-if-there-is-at-least-one-obligatorily-possessed-class-can-it-be-unpossessed-via-a-dedicated-non-person-marker), [24](#nounposs-24-how-many-possession-classes-of-non-possessible-nouns-in-terms-of-valence-are-there), [25](#nounposs-25-what-is-the-valency-of-the-default-class), [26](#nounposs-26-if-there-are-conceptually-inalienable-classes-what-are-their-valencies), [27](#nounposs-27-if-there-are-conceptually-non-possessible-classes-what-are-their-valencies), [28](#nounposs-28-if-there-are-mixed-classes-what-are-their-valencies) concern the valence of different classes.

### [](ParameterTable#cldf:NounPoss-01)
&emsp;**{ \_number\_ }**

#### 1: North Junín Quechua \[nort2980\] (Quechuan; Peru)

Nominal possession in North Junín Quechua is expressed by affixing a genitive case marker to the possessor and affixing the person-number information of the possessor to the possessed noun. There is no distinction made among types of possessed nouns.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(1)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">čay</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">warmi-pa</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">wayi-</span><span style="color:#000;background-color:transparent">ṅ-maṅ</span></th>
    <th class="tg-0lax">ĉa-ru-ṅ</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">that</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">woman-GEN</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">house-3-ALL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">arrive-PERF-3</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘He arrived at that woman’s house.’ (<a class="Source" href="../sources/adelaar1977northjuninquechua">Adelaar 1977</a>: 204, glossing added)</span></td>
  </tr>
</tbody></table>

#### 4: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr there are seven noun possession classes, summarized in Table 3 below. All classes are possessed with the same paradigm of possessive prefixes that agree in number and gender with the possessor (some persons have an additional suffix as well), except the non-possessible2 class, whose members cannot be possessed at all and include inanimate natural elements (e.g. ‘thunder’). Plants and animals (non-possessible1 class) are also non-possessible in terms of valence, but they can be possessed through the use of classifiers, which enter into the possessive construction in their stead. The nouns of the inalienable class are obligatorily possessed and they need additional morphology to be unpossessed. Finally, there are four classes of alienable nouns that can occur unpossessed without any additional morphology. Nouns of the alienable-invariant class are possessed through the same possession construction as the inalienable nouns, but they do not require a special unpossession construction. The alienable-a class is the largest class and also contains loanwords, leading us to consider this as the default class, and has an additional *-a* suffix on the possessed noun. The alienable-n class has a different suffix *-n* on the possessed noun. Finally the alienable-suppletive class is a relatively large and heterogeneous class of nouns that undergo a number of largely idiosyncratic changes to their stem when they are possessed. These changes range from mid-syllable deletion, vowel changes and metathesis to even more intrusive changes that render the root almost unrecognizable. All alienable classes are mixed classes, since their members do not show semantic coherence.

<div class="datainset">
Table 3: Noun possession classes of Palikúr (<a class="Source" href="../sources/launey2003palikur">Launey 2003</a>: 71-79).
<table class="fulltable"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Noun Possession Class</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Possession constructions</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Unpossession constructions</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Comments</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">inalienable</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-PSSD</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">i/∅ - N - t/ti</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">body; kin; intimate_property; relation</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">non-possessible1</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-CLASS PSSD</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">N</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plants; animals</span><br><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">various classifiers (prey, food, pet, cultivated)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">non-possessible2</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">NULL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">N</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nature_inanimate</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">alienable-invariant</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-PSSD</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">N</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mixed</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">alienable-a</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-PSSD-a</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">N</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">default (largest class, contains loanwords)</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">alienable-n</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-PSSD-n/ni</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">N</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mixed</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">alienable-suppletive</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PSSR poss-PSSD.form</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">UNPOSS.form</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">largely idiosyncratic stem changes</span></td>
  </tr>
</tbody></table>
</div>

### [](ParameterTable#cldf:NounPoss-02)
&emsp;**{ ; separated list of \[ default:\_frequency\_, conceptually inalienable:\_frequency\_, conceptually non-possessible:\_frequency\_, mixed:\_frequency\_ \] }**

Noun possession classes are categorized into broad semantic types according to the finer semantic categories they contain, as explained in [Chousou-Polydouri et al (2023)](Source#cldf:chousoupolydouri2023multivariate).

#### default:1 North Junín Quechua \[nort2980\] (Quechuan; Peru)

With only one possession class, North Junín Quechua has only the default semantic class.

#### default:1; conceptually inalienable:1; conceptually non-possessible:2; mixed:2 Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr contains a conceptually inalienable class (class inalienable), which includes body parts, kinship terms, intimate property and relation nouns, two conceptually non-possessible classes (non\_possessible1 and non\_possessible2), which include animals and plants and other natural elements, and two conceptually mixed classes (alienable-invariant and alienable-n), as shown in Table 3 above.

### [](ParameterTable#cldf:NounPoss-03)
&emsp;**{ \_number\_ }**

#### 0: North Junín Quechua \[nort2980\] (Quechuan; Peru)

North Junín Quechua has only the default class, and no conceptually inalienable classes.

#### 1: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr has one conceptually inalienable class.

#### 2: Yucatec Maya \[yuca1254\] (Mayan; Mexico)

Yucatec Maya has two inalienable classes, which are divided between body part and part-whole terms on the one hand, and kinship and ownership nouns (e.g., ‘master’) on the other. Both of these inalienable classes may be possessed through a person-indexing prefix on the possessed noun followed by the suffix *-il*. However, they differ in their unpossession constructions: part relations and some kinship terms are unpossessed with the suffix *-tsil* (2) while other kinship terms and ownership relations may not appear without a possessor ([Lehmann 1998](Source#cldf:lehmann1998yucatecmaya): 53-56).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(2)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">u</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nohoch</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">suku’n</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">POSS.3</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">big</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">elder.brother</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘his senior brother’ (<a class="Source" href="../sources/lehmann1998yucatecmaya">Lehmann 1988</a>: 74)</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">le</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">suku’n-tsil-e’</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DEF</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">elder.brother-UNPOSS-D3</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘the older brother’ (<a class="Source" href="../sources/lehmann1998yucatecmaya">Lehmann 1988</a>: 74)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-04)
&emsp;**{ \_number\_ }**

#### 0: North Junín Quechua \[nort2980\] (Quechuan; Peru)

North Junín Quechua has only the default class, and no non-possessibles.

#### 2: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr has two conceptually non-possessible classes. The class of inanimate natural elements, such as ‘thunder’, cannot be possessed at all, while plants and animals are possessed according to the type of relation we have with them ([Launey 2003](Source#cldf:launey2003palikur): 79). Thus, different classifiers are used when a plant or an animal is used as food, as shown in example (3) ([Launey 2003](Source#cldf:launey2003palikur): 79), segmentation and glossing added. 

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(3)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nu-win-uh</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bukutru</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.POSS-game.CLASS-1SG.POSS<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">agouti</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘My agouti (that I hunted)’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nu-mana</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bukutru</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.POSS-food.CLASS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">agouti</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘My agouti (cooked, in my plate)’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">n-amutra</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">pilatnu</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.POSS-plant.CLASS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bananas</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘My bananas (that I cultivate)’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">d.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nu-mana</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">pilatnu</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.POSS-food.CLASS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bananas</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘My bananas (that I eat)’</span></td>
  </tr>
</tbody></table>

### [](ParameterTable#cldf:NounPoss-05)
&emsp;**{ \_number\_ }**

#### 2: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr has two mixed classes, alienable-invariable and alienable-n. Members of alienable-invariable can be possessed only with prefixation with the possessive paradigm, unlike the default alienable class which further requires a suffix *-a*. Members of the alienable-n class have a suffix *-n* when possessed, instead of the default suffix *-a*. In both classes, there is not a common semantic core for their members, hence their semantic categorization as mixed.

#### 1: Yucatec Maya \[yuca1254\] (Mayan; Mexico)

There is one possession class in Yucatec Maya whose membership is mixed, such that no semantic generalization can be made about them. These are called the “neutral” nouns by [Lehmann (1998: 49)](Source#cldf:lehmann1998yucatecmaya), and undergo tone lowering and vowel lengthening when possessed (4). The semantics of this class are highly diverse, including human artifacts like ‘hammock’, ‘wall’, and ‘dress’, the body part ‘tooth’, the flora ‘corn plant’ and ‘squash’, ‘sickness’, ‘shade’, and others. We have thus categorized this as a mixed class.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(4)</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kay</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">fish</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘fish’ (<a class="Source" href="../sources/bricker1998yucatecanmaya">Bricker et al 1998</a>: 360)</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">in</span></th>
    <th class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kàay</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">POSS.1SG</span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">fish</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘my fish’ (<a class="Source" href="../sources/bricker1998yucatecanmaya">Bricker et al 1998</a>: 360, glossing added)</span></td>
  </tr>
</tbody></table>

### [](ParameterTable#cldf:NounPoss-06)
&emsp;**{ NA | ; separated list of \[ body, kin, part, relation, intimate\_property \] }**

#### NA: North Junín Quechua \[nort2980\] (Quechuan; Peru)

North Junín Quechua has no inalienable classes.

#### body; kin; intimate\_property; relation: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr’s single inalienable class encompasses body, kin, intimate property, and relations (such as ‘servant’ and ‘leader’).

### [](ParameterTable#cldf:NounPoss-07) 
&emsp;**{ NA | ; separated list of \[ plants, nature\_inanimate, humans, animals, names \] }**

#### NA: North Junín Quechua \[nort2980\] (Quechuan; Peru)

North Junín Quechua has no non-possessible classes.

#### plants; animals; nature\_inanimate: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikur’s two non-possessible classes encompass plants, animals, and inanimate nature terms (such as ‘thunder’).

### [](ParameterTable#cldf:NounPoss-08)
&emsp;**{ ; list of \[ PSSR, PSSD, PSSR and PSSD, LINKER, JUXT, CLAUSE, CLASS, NULL \] }**

#### PSSR and PSSD: North Junín Quechua \[nort2980\] (Quechuan; Peru)

As seen in example (1) [above](#nounposs-01-how-many-morphosyntactically-distinct-possession-classes-are-there), the possession construction in North Junín Quechua is double-marked, both on the possessor (through a genitive morpheme) and on the possessed noun (through agreement with the possessor).

#### PSSD: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr’s default possession strategy includes two markers on the possessed noun: a (mostly) prefixal paradigm of possessive markers that agree in gender and number with the possessor, as well as an invariable suffix *-a*  (this suffix is analyzed as deriving a possessed form of the noun in the source; see example (5) with the French loan *lapot* ‘door’ and [Launey 2003](Source#cldf:launey2003palikur): 71-79).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(5)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">payt</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ga-lapot-a</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">house</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3sg.Ndef.POSS-door-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The house’s door’ (<a class="Source" href="../sources/launey2003palikur">Launey 2003</a>: 72)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-09)
&emsp;**{ NA | ; list of \[ PSSR, PSSD, PSSR and PSSD, LINKER, JUXT, CLAUSE, CLASS, NULL \] }**

#### PSSD: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, inalienable nouns are possessed with the addition of a (mostly) prefixal possessive paradigm, see example (6). 

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(6)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">José</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">gi-nag</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">miyovi</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">José</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3sg.M.poss-mother</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">died</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘José’s mother died’ (<a class="Source" href="../sources/launey2003palikur">Launey 2003</a>: 194)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-10)
&emsp;**{ NA | ; list of \[ PSSR, PSSD, PSSR and PSSD, LINKER, JUXT, CLAUSE, CLASS, NULL \] }**

#### CLASS; NULL: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, there are two conceptually non-possessible classes, as explained [above](#nounposs-04-how-many-conceptually-non-possessible-possession-classes-are-there). For the class of plants and animals, the possession construction makes use of a classifier which enters the standard possession construction instead of the possessed noun. For the class of inanimate natural elements, the possession construction is NULL, since they cannot be possessed at all ([Launey 2003](Source#cldf:launey2003palikur)).

### [](ParameterTable#cldf:NounPoss-11)
&emsp;**{ NA | ; separated list of \[ Noun, NULL, SPECIAL\_MARKER, ARTICLE, 1SG, 1PL, 1INCL, 3, 3SG, 3SG.N, 3SG.M, 3.INAN, 3.INDEF \] }**

#### SPECIAL\_MARKER: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, inalienable nouns (which contain mainly kinship terms and body parts) can be unpossessed with the derivation of a so-called absolute form by adding a prefix *i-* (with allomorph *∅-* in front of a vowel) and a suffix *-ti* (with allomorph *-t* after a vowel), as seen in Table 4.

<div class="datainset">
Table 4: Examples of possessed and unpossessed forms in Palikúr (<a class="Source" href="../sources/launey2003palikur">Launey 2003</a>: 78).
<table class="fulltable"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3sgM possessed form</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Absolute form</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Meaning</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">gi-dugas</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">i-dugas-ti</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">navel</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">g-aybu</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aybu-t</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">tooth, teeth</span></td>
  </tr>
</tbody></table>
</div>

#### 1INCL: Nanti \[nant1250\] (Arawakan; Peru)

Inalienable nouns in Nanti are unpossessed with the first person inclusive, which means that context alone distinguishes between the meanings of *a-gito* ‘our (incl) head’ vs. ‘a head’ ([Michael 2008](Source#cldf:michael2008nanti): 297-298).

### [](ParameterTable#cldf:NounPoss-12)
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### no: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr the possessed noun or a classifier is always marked. There is no juxtaposition construction.

#### default: Bulo Stieng \[bulo1242\] (Austroasiatic; Cambodia, Viet Nam)

In Bulo Stieng possession is expressed with juxtaposition with the possessed noun preceding the possessor, as in example (7).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(7)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">hej</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">gɔk</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">lɘw</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bok</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ɟun</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1sg</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">be.seated</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">on</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">head</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">deer</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="5"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I am sitting on the head of a deer.’ (<a class="Source" href="../sources/bon2014grammaire">Bon 2014</a>: 278)</span></td>
  </tr>
</tbody></table>

#### inalienable: Abun \[abun1252\] (isolate; Indonesia)

The juxtaposition construction in Abun is only available with body and part terms (8), which comprise the language’s sole inalienable class.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(8)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Ndar</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">sye</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ne</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">gwes</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">de-dari</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">fot.</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dog</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">big</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DET</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">leg</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">side-back</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">broken</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="6"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The big dog’s back leg is broken.’ (<a class="Source" href="../sources/berry1999abun">Berry and Berry 1999</a>: 77)</span></td>
  </tr>
</tbody></table>

### [](ParameterTable#cldf:NounPoss-13)
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### no: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

The possessor is always unmarked in Palikúr.

#### default: Nihali \[niha1238\] (isolate; India)

The default (and only) class in Nihali expresses construction through a marker on the possessor noun, *-na*, as in (9).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(9)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ra:ja-na</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a:wa:r</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">king-POS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">house</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘king’s house’ (<a class="Source" href="../sources/nagaraja2014nihali">Nagaraja 2014</a>: 34, glossing added)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-14) 
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### default; inalienable; mixed: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, all noun classes that can be directly possessed use constructions with marking on the possessed noun. All these constructions involve prefixation with the same possessive paradigm, and some involve further invariable possessive suffixes. Examples (5) [above](#nounposs-08-what-are-the-nominal-possession-constructions-used-for-the-default-possession-class) and (6) [above](#nounposs-09-what-are-the-nominal-possession-constructions-used-for-conceptually-inalienable-classes-if-present) show the constructions used for the default (possessive suffix *-a*) and the inalienable classes (no possessive suffix). Of the two mixed classes, the alienable-invariable class is possessed without any additional suffix, while the alienable-n class has an additional invariable *-n* suffix for possession.

### [](ParameterTable#cldf:NounPoss-15)
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### default: North Junín Quechua \[nort2980\] (Quechuan; Peru)

The default (and sole) possession class in North Junín Quechua is expressed through double marking on both the possessor and possessed nouns, as seen in (1) [above](#nounposs-01-how-many-morphosyntactically-distinct-possession-classes-are-there).

### [](ParameterTable#cldf:NounPoss-16)
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### default: Hokkaidu Ainu \[ainu1240\] (Ainu; Japan)

The default class of nouns in Hokkaidu Ainu is possessed through a clausal construction with the verb ‘have’, as in (10). Note that Hokkaidu Ainu also has an inalieanable class, which is possessed through a different construction.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(10)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ku=∅=kor</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kamuy</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.A=3.O=have</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">god</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘my god’ (<a class="Source" href="../sources/bugaeva2012southern">Bugaeva 2012</a>: 478)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-17) 
&emsp;**{ no | ; list of \[ default, inalienable, non-possessible, mixed \] }**

#### non-possessible: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, plants and animals are possessed with classifiers depending on the type of relationship (food, pet, etc), see [above](#nounposs-04-how-many-conceptually-non-possessible-possession-classes-are-there).

### [](ParameterTable#cldf:NounPoss-18)
&emsp;**{ NA | yes | no }**

#### yes: North Junín Quechua \[nort2980\] (Quechuan; Peru)

The North Junín Quechua possession construction includes person agreement on the possessed noun with the possessor, as seen in example (1) [above](#nounposs-01-how-many-morphosyntactically-distinct-possession-classes-are-there).

#### no: Rotokas \[roto1249\] (North Bougainville; Papua New Guinea)

Nominal possession in Rotokas is marked by an invariant morpheme *-aro* on the possessed noun which does not agree with the possessor, as in examples (11-12).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(11)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ragai</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kotoko-aro</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">PRO.1SG</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">leg-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘my leg’ (<a class="Source" href="../sources/robinson2011split">Robinson 2011</a>: 122)</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(12)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Siuparai</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aite-aro</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Siuparai</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">father-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘Siuparai’s father’ (<a class="Source" href="../sources/robinson2011split">Robinson 2011</a>: 122)</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:NounPoss-19) 
&emsp;**{ NA | yes | no }**

A &lt;yes&gt; is equivalent with the concept of construct state marking.

#### no: North Junín Quechua \[nort2980\] (Quechuan; Peru)

The only morpheme on the possessed noun agrees in person with the possessor (see example 1 [above](#nounposs-01-how-many-morphosyntactically-distinct-possession-classes-are-there)).

#### yes: Rotokas \[roto1249\] (North Bougainville; Papua New Guinea)

The only morpheme on the possessed noun indicating possession has no agreement with the possessor noun (see examples 11-12 [above](#nounposs-18-if-any-head-marking-construction-is-used-pssd-or-pssr-and-pssd-does-the-possessed-noun-contain-any-agreement-with-the-possessor)).

#### yes: Hokkaidu Ainu \[ainu1240\] (Ainu; Japan)

Though the default class in Hokkaido Ainu only has access to a classifier construction, the inalienable class behaves differently. Two morphemes mark possession on an inalienable noun, an A proclitic (also used on verbs) which agrees with the possessor, and an independent possessive marker *-hV/-V(hV)*. Note that the third person A proclitic is null, but we nevertheless consider it present, as it is paradigmatically opposed to the other persons (13-14).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(13)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ku=sapa-ha</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.A=head-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘my head’ (<a class="Source" href="../sources/bugaeva2012southern">Bugaeva 2012</a>: 478)</span></td>
  </tr>
</tbody>
</table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(14)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bear</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">∅=rus-i(hi)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bear</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3.A=fur-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘the bear(‘s) skin’ (<a class="Source" href="../sources/bugaeva2012southern">Bugaeva 2012</a>: 478)</span></td>
  </tr>
</tbody></table>

### [](ParameterTable#cldf:NounPoss-20)
&emsp;**{ yes | no }**

#### yes: Garifuna \[gari1256\] (Arawakan; Honduras, Guatemala, Nicaragua, Belize)

Some nouns in Garifuna undergo complete suppletion when they are possessed versus unpossessed. For example, *eréba* ‘cassava bread’ when possessed becomes *\*-bu* as in *nu-bu-te* ‘my cassava bread’. The possessed form cannot appear unpossessed, and likewise the unpossessed form cannot appear possessed ([Haurholm-Larsen 2016](Source#cldf:haurholm2016garifuna): 57-59).

#### no: North Junín Quechua \[nort2980\] (Quechuan; Peru)

There are no suppletive paradigms in North Junín Quechua.

### [](ParameterTable#cldf:NounPoss-21)
&emsp;**{ \_number\_ }**

#### 1: North Junín Quechua \[nort2980\] (Quechuan; Peru)

The only possession class in North Junín Quechua is the default class, which is optionally possessed.

#### 3: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

In Palikúr, there are three optionally possessed noun classes in terms of valence: the default class and two mixed classes of other alienable nouns.

### [](ParameterTable#cldf:NounPoss-22) 
&emsp;**{ \_number\_ }**

#### 0: North Junín Quechua \[nort2980\] (Quechuan; Peru)

There are no obligatorily possessed classes in North Junín Quechua.

#### 1: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Palikúr’s inalienable nouns are obligatorily possessed in terms of valence, as they require morphology to be unpossessed, see [above](#nounposs-11-if-there-is-a-conceptually-inalienable-possession-class-what-are-its-unpossession-constructions).

### [](ParameterTable#cldf:NounPoss-23)
&emsp;**{ NA | yes | no }**

#### NA: North Junín Quechua \[nort2980\] (Quechuan; Peru)

There are no obligatorily possessed classes in North Junín Quechua.

#### yes: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

As explained [above](nounposs-11-if-there-is-a-conceptually-inalienable-possession-class-what-are-its-unpossession-constructions), Palikúr inalienable nouns can be unpossessed by the addition of a prefix and a suffix. These morphemes are not related to any person markers.

#### no: Coahuilteco \[coah1252\] (isolate; United States)

Coahuilteco has an inalienable/alienable split among its nouns, and the inalienables are obligatorily possessed, that is they cannot occur without a possessor ([Troike 1996](Source#cldf:troike1996coahuilteco): 659-660).

### [](ParameterTable#cldf:NounPoss-24)
&emsp;**{ \_number\_ }**

#### 0: North Junín Quechua \[nort2980\] (Quechuan; Peru)

There are no non-possessible classes in North Junín Quechua.

#### 2: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

As explained [above](#nounposs-04-how-many-conceptually-non-possessible-possession-classes-are-there), Palikúr has two conceptually non-possessible classes and they both non-possessible in terms of valence. The nouns of the first one can only be possessed indirectly through a classifier construction, and the nouns of the second one cannot be possessed at all. 

### [](ParameterTable#cldf:NounPoss-25)
&emsp;**{ non-possessible | obligatorily possessed | optionally possessed }**

#### optionally possessed: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

The default class of nouns in Palikúr can be possessed through a construction with marking on the possessed noun, and can be unpossessed without any morphology. 

#### non-possessible: Hokkaido Ainu \[ainu1240\] (Ainu; Japan)

The default class in Hokkaido Ainu is possessed only through a classifier construction (see example 10 [above](#nounposs-16-is-there-a-clause-possession-construction-and-if-so-for-which-conceptual-classes)), which makes this class non-possessible.

### [](ParameterTable#cldf:NounPoss-26)
&emsp;**{ NA | ; separated list of \[ non-possessible:\_frequency\_, obligatorily possessed:\_frequency\_, optionally possessed:\_frequency\_ \] }**

#### obligatorily possessed: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

The inalienable class of nouns in Palikúr requires morphology to be unpossessed, see [above](#nounposs-11-if-there-is-a-conceptually-inalienable-possession-class-what-are-its-unpossession-constructions). 

#### optionally possessed: Hokkaido Ainu \[ainu1240\] (Ainu; Japan)

Hokkaido Ainu’s inalienable class is distinguished from the alienable class only by a different possession construction. Inalienable nouns can appear unpossessed, and thus the inalienable class has an optionally possessed valence ([Shibatani 1999](Source#cldf:shibatani1990japan): 14; [Bugaeva 2012](Source#cldf:bugaeva2012southern): 478).

### [](ParameterTable#cldf:NounPoss-27)
&emsp**{ NA | ; separated list of \[ non-possessible:\_frequency\_, obligatorily possessed:\_frequency\_, optionally possessed:\_frequency\_ \] }**

#### non-possessible:2: Palikúr \[pali1279\] (Arawakan; Brazil, French Guiana)

Both conceptually non-possessible classes in Palikúr are non-possessible in terms of valence, as they cannot be possessed with a direct construction (i.e., with morphological marking or juxtaposition).

#### optionally possessed:1: Tohono O’odham \[toho1245\] (Wakashan; Canada)

Tohono O’odham’s non-possessible class can be freely unpossessed or directly possessed through an affix on the possessed noun, making it optionally possessed ([Zepeda 1983](Source#cldf:zepeda1983papago): 75).

### [](ParameterTable#cldf:NounPoss-28) 
&emsp;**{ NA | ; separated list of \[ non-possessible:\_frequency\_, obligatorily possessed:\_frequency\_, optionally possessed:\_frequency\_ \] }**

#### optionally possessed:1: Yucatec Maya \[yuca1254\] (Mayan; Mexico)

Yucatec Maya has one conceptually mixed classes, the “neutral” nouns which are possessed directly, along with vowel lengthening. These nouns show no semantic coherence and can be freely unpossessed with no special construction or dedicated morphology, making them optionally possessed ([Lehmann 1998](Source#cldf:lehmann1998yucatecmaya): 49-51; [Bricker et al 1998](Source#cldf:bricker1998yucatecanmaya): 360-361).

## Derived Features
### [](ParameterTable#cldf:NounPoss-01a) 
&emsp;**{ 1 | 2 | 3-or-more }**

This feature groups the high level of diversity in NounPoss-01 (some languages have as many as 9 possession classes), making patterns more visible.

### [](ParameterTable#cldf:NounPoss-03a)
&emsp;**{ NA | yes | no }**

This feature unites all languages that have at least one inalienable class into the same category, dependent on the presence of at least two classes (as a single class by definition means that it is not conceptually inalienable).

### [](ParameterTable#cldf:NounPoss-03b)
&emsp;**{ NA | yes | no }**

There is an overwhelming tendency for obligatorily possessed classes to be conceptually inalienable, and this derived feature takes into consideration this strong dependency. Of 177 obligatorily possessed classes in our database, 169 are conceptually inalienable. Of the remaining classes, 17 are semantically mixed, and most of these co-occur with obligatorily possessed inalienable classes in the same language. Only 3 languages have obligatorily possessed default classes (Cahuilla, Pipil, and Tetelcingo Nahuatl; all Uto-Aztecan) and a further 2 have obligatorily possessed classes that combine both conceptually inalienable and non-possessible nouns (Rikbaktsa and Ticuna).

### [](ParameterTable#cldf:NounPoss-03c)
&emsp;**{ NA | yes | no }**

### [](ParameterTable#cldf:NounPoss-03d)
&emsp;**{ NA | yes | no }**

### [](ParameterTable#cldf:NounPoss-04a)
&emsp;**{ NA | yes | no }**

This feature unites all languages that have at least one non-possessible class into the same category, dependent on the presence of at least two classes (as a single class by definition means that it is not non-possessible).

### [](ParameterTable#cldf:NounPoss-04b)
&emsp;**{ NA | yes | no }**

It is rare that a non-possessible class in terms of valence is not conceptually non-possessible as well, and this derived feature takes into consideration that dependency. Of 70 non-possessible classes in our database, 50 are conceptually non-possessible, while the remaining 20 are either default (12), inalienable (5), mixed (2) or combine both conceptually inalienable and non-possessible nouns (1). 

### [](ParameterTable#cldf:NounPoss-08a)
&emsp;**{ NA | yes | no }**

This feature groups together the PSSR marking and PSSR and PSSD marking of the default class in NounPoss-08.

### [](ParameterTable#cldf:NounPoss-08b)
&emsp;**{ NA | yes | no }**

This feature groups together the PSSD marking and PSSR and PSSD marking of the default class in NounPoss-08.

### [](ParameterTable#cldf:NounPoss-12a)
&emsp;**{ no JUXT | default plus | only inalienables }**

This feature groups together the lists in NounPoss-15 to distinguish languages that have JUXT constructions only in inalienables from languages which use the construction elsewhere, and those that lack it altogether.

### [](ParameterTable#cldf:NounPoss-16a)
&emsp;**{ yes | no }**

### [](ParameterTable#cldf:NounPoss-17a)
&emsp;**{ none | default plus | only non-possessibles }**

### [](ParameterTable#cldf:NounPoss-20a)
&emsp;**{ NA | yes | no }**

This feature conditions NounPoss-22 according to the presence of more than one possession class. No language in our sample always expressed possession through suppletion (and we suspect this is impossible).

## Results
Possession typological features are indeed unevenly distributed according to area and even macroarea. The presence of large numbers of possession classes ([NounPoss-01](../parameters/NounPoss-01), [01a](../parameters/NounPoss-01a)) is highly skewed. Relatively more languages in the Americas have 3 or more possession classes, with the skew being more pronounced for 4, 5, and 6 or more possession classes. By comparison, the presence of two classes — almost always an alienable and an inalienable class ([NounPoss-03a](../parameters/NounPoss-03a)) — is widespread throughout the world, with no clear macroareal tendencies.

Within inalienable possession, the presence of a class dedicated to body parts without kinship ([NounPoss-03c](../parameters/NounPoss-03c)) or kinship without body parts ([NounPoss-03d](../parameters/NounPoss-03d)) is locally significant. Some larger regions show a strong skew, with most of Papunesia and much of our sparse African sample having an inalienable class of only kinship terms and none for body parts, while the presence of a class only for body parts but not kinship terms is typical of the Andean coast and the North American Piedmont. Both patterns are present in Australia.

Obligatorily possessed noun classes are almost exclusively conceptually inalienable ([NounPoss-03b](../parameters/NounPoss-03b), and compare [25](../parameters/NounPoss-25), [26](../parameters/NounPoss-26), [27](../parameters/NounPoss-27), [28](../parameters/NounPoss-28)). Despite the global presence of inalienable classes, obligatorily possessed noun classes are far more present in the Americas than elsewhere ([NounPoss-22](../parameters/NounPoss-22)), and dedicated (non-pronominal) unpossession markers are exclusively found in the Americas in our sample ([NounPoss-23](../parameters/NounPoss-23)).

Conceptually non-possessible classes are rare compared to inalienable classes ([NounPoss-04](../parameters/NounPoss-04), [04a](../parameters/NounPoss-04a)), and their presence is heavily skewed toward the Americas, where they appear most frequently in Central America and in the Amazon. It is very typical for such classes to be absolutely non-possessible by any construction, although classifier and direct constructions are sometimes used ([NounPoss-10](../parameters/NounPoss-10)).

The possession construction used for the default class ([NounPoss-08](../parameters/NounPoss-08), [08c](../parameters/NounPoss-08c)) sharply distinguishes large regions of the world, with marking on the possessed noun (PSSD) far more common in North America than anywhere else, a pattern which extends through Central America to the northern tip of South America. A narrow band of languages with a default PSSR construction can be seen among the inland North American West Coast languages, most members of which are part of the proposed Penutian family ([DeLancey and Golla](Source#cldf:delanceygolla1997penutian)). The typical locus of marking in Eurasia, Africa, Papunesia, and Australia is the possessor (PSSR), although the northern coast of Australia and Papunesia show more diversity than Eurasia and Africa. South America is split among geographic regions, with a coastal Andean region of PSSR and PSSD double marking, an Andean Highland region of PSSR marking, and a mixture of juxtaposition (JUXT) and PSSD marking in the Amazon.

The type of possession construction used for inalienable classes, if there are any, most typically echoes the type used for the default class ([NounPoss-09](../parameters/NounPoss-09)). Though a juxtaposition (JUXT) construction is often used only for inalienable classes, this most commonly occurs in regions where some languages make use of a JUXT construction for the default class as well ([NounPoss-12a](../parameters/NounPoss-12a)). Clausal possession constructions (CLAUSE) are rare and only attested in our sample in North America, Papunesia, and for Hokkaido Ainu \[ainu1240\] (Ainu; Japan) ([NounPoss-16](../parameters/NounPoss-16), [16a](../parameters/NounPoss-16a)). Classifier constructions (CLASS) are also rare, although they frequently target conceptually non-possessible classes ([NounPoss-17](../parameters/NounPoss-17), [17a](../parameters/NounPoss-17a)). Just as conceptually non-possessible classes are more common in the Americas, so are classifier (CLASS) constructions.

Suppletive possession in our sample only occurs in the Americas and Africa ([NounPoss-20](../parameters/NounPoss-20)). Within the Americas, suppletion is most common in Central America. Several languages of the Amazon also have suppletive possession, and although they do not form a clear geographic unit, many are Arawakan (Wayuu \[wayu1243\], Tariana \[tari1256\], Parecís \[pare1272\]) or Cariban (Ikpeng \[ikpe1245\], Kuikúro-Kalapálo \[kuik1246\], Trió \[trio1238\]).

## Contributions
**Conceptualization**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI), [Balthasar Bickel](Contributor#cldf:BB)

**Data collection**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI), [Thomas Huber](Contributor#cldf:TH), [André Müller](Contributor#cldf:AM), [Marine Vuillermet](Contributor#cldf:MV)

**Supervision of data collection**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [David Inman](Contributor#cldf:DI)

**Computer Code**: [David Inman](Contributor#cldf:DI)

## References
[References](Source?cited_only#cldf:__all__)

[^1]: The noun ‘house’ is commonly encountered as a member of the inalienable class, and it could be conceptually categorized as place\_rel or intimate\_property. We have categorized it on a language-by-language basis depending on what other nouns are present in the same possession class.

[^2]: The semantic category of mass nouns is the only one that is not included in our ontology, as it is a cross-cutting category.

[^3]: The accompanying suffix -uh for the 1st person singular is not always used, especially if the next word is the name of an animal.