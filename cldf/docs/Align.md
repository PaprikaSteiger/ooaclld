**Authors**: [David Inman](Contributor#cldf:DI), [Alena Witzlack-Makarevich](Contributor#cldf:AWM), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Balthasar Bickel](Contributor#cldf:BB)

**Acknowledgments**: [Alexandra Nogina](Contributor#cldf:AN), [Tai Hong](Contributor#cldf:HT), [Anna Graff](Contributor#cldf:AG), [Melvin Steiger](Contributor#cldf:MS)

[TOC]

## What?
The concept of alignment refers to statements about which arguments are treated the same way in a language. Morphological alignment specifically targets the marking patterns of different arguments.[^1] In this feature set, we focus on the formal relationship between the A (more agent-like) and P (more patient-like) arguments of bivalent clauses and the S (sole) argument of monovalent clauses.
In the examples below, *Kim* is treated morphologically the same way in all three examples; this corresponds to a neutral alignment (S=A=P). On the other hand, the pronominal form *she* is used for S (1c) and A (1a) arguments, whereas the same pronoun has the form *her* in the P role in (1b). This corresponds to an accusative alignment (S=A≠P).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">A</span></th>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">P</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(1)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">She/Kim</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kissed</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">him.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">A</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">P</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">He</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kissed</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">her/Kim.</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">S</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c.</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">She/Kim</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ran away.</span></td>
    <td class="tg-0lax"></td>
  </tr>
</tbody></table>

In features targeting “exemplar” alignments ([Align-01](#align-01-what-are-the-exemplar-alignments-of-nouns), [04](#align-04-what-are-the-exemplar-alignments-of-pronouns), [07](#align-07-what-are-the-exemplar-alignments-of-indexing)), we use a definition of an **exemplar transitive clause**, adapted from [Birchall (2014: 24-25)](Source#cldf:birchall2014argument) (following [Lazard 2002: 252](Source#cldf:lazard2002transitivity)). Such clauses have the following properties:

1. they are main declarative active clauses;
2. they refer to a real event (i.e. not prospective or imagined);
3. they refer to a discrete event, i.e. perfective (and thus by default, past) or completive, not imperfective or conative or somehow incomplete;
4. the A argument is a human that voluntarily performs the event;
5. the A argument controls the event (i.e. the event is not non-intentional or uncontrolled);
6. the P argument is a well-individuated human entity;
7. the P is affected by the event.

We likewise extend this definition to **exemplar intransitive clauses**, which have the following properties:

1. they are main declarative active clauses;
2. they refer to a real event (i.e. not prospective or imagined);
3. they refer to a discrete event, i.e. perfective (and thus by default, past) or completive, not imperfective or conative or somehow incomplete;
4. the S argument is a human that voluntarily performs the event;
5. the S argument controls the event (i.e. the event is not non-intentional or uncontrolled).

These provide exemplar, prototypical clauses that can be compared cross-linguistically. We call the alignment between the arguments of the exemplar intransitive clause and the arguments of the exemplar transitive clause a language’s **exemplar alignment**. Many languages have different alignments even within the exemplar definition, specifically, when alignment splits are based on person and number. In such cases, we present all the alignments present, as well as indicate the majority alignment. This majority alignment is calculated on the basis of a simple majority vote of all available referential types for the language in question.

Further alignment statements can be made about the arguments of clauses that do not meet our exemplar definitions. There are many other ways according to which alignment can differ (by tense, predicate class, polarity, and other conditions). For this feature set, we are interested in all alignments present in main declarative active clauses, as we aim to capture any minority alignment patterns which may be of areal interest, such as a tense-based non-exemplar ergative alignment. These other alignment statements can be seen in features collecting “all” alignments ([Align-02](#align-02-what-are-all-the-alignments-of-nouns), [05](#align-05-what-are-all-the-alignments-of-pronouns), [07](#align-07-what-are-the-exemplar-alignments-of-indexing)). With respect to deviations from the exemplar, we have taken special care to include in our data two specific types of phenomena.

First, we are particularly interested in alignment statements which involve intransitive verbs with a sole argument that lacks control (e.g. ‘fall’, ‘vomit’, ‘wake up’,  etc.). Consequently, in addition to the exemplar, we have made sure to encode cases which correspond to what traditionally has been referred to as split-S systems or stative-active systems. This pattern is included if the S argument of a substantial number of intransitive predicates has a different marking pattern than the S argument of the exemplar declarative intransitive predicates and this S argument does not control the event (at least in case of the majority of the relevant intransitive predicates).

Second, we are interested in the presence of differential P marking by case (i.e. what is traditionally referred to as differential object marking or DOM). To capture this pattern we deviate from the exemplar default declarative transitive main clause and consider P arguments which are not well-individuated human entities. We are thus able to capture the presence of DOM in a language, across both exemplar and non-exemplar clauses.

Finally, we have here only considered alignment statements which minimally include grammatical information about person, i.e. excluding verbal morphemes that index only number. Such morphemes, along with their alignments, are presented in the [Monoexponential Verbal Plurals](MonPl) feature set.

## Why?
Morphological alignment has been studied as a prominent areal feature since at least [Nichols (1992)](Source#cldf:nichols1992linguistic), even if individual studies find no areal effect with respect to certain alignment features and certain areas (e.g. [Cathcart et al 2018](Source#cldf:cathcartetal2018areal)). Further areal patterns of case marking have been observed in dedicated studies. For instance, [Comrie (2013)](Source#cldf:wals98) observes the presence of the marked nominative pattern in Africa, both in some Afroasiatic languages and in Nilo-Saharan languages. DOM in flagging ([Align-03](#align-03-is-there-differential-object-marking-dom-for-nouns)) varies between different macroareas ([Bickel et al 2015](Source#cldf:bickeletal2015exploring)).

For indexing, [Siewierska (2013)](Source#cldf:siewierska2013verbal) observes a number of areal patterns: ergative indexing ([Align-10](#align-10-is-s-ever-marked-differently-from-a-in-indexing-if-there-is-indexing-in-the-language-ie-if-yes-to-align06)) is attested mainly in South America, Southeast Asia, and Mesoamerica, and it is absent in New Guinea, Australia and the Pacific; on the other hand, split-S patterns ([Align-11](#align-11-if-s-is-ever-marked-differently-than-a-in-indexing-or-flagging-ie-if-yes-to-either-align09-or-align10-is-there-a-difference-in-marking-according-to-an-activestative-distinction-among-monovalent-predicates-in-either-indexing-or-flagging) and [Align-12](#align-12-if-s-is-ever-marked-differently-than-a-in-indexing-or-flagging-ie-if-yes-to-either-align09-or-align10-are-s-arguments-of-one-predicate-class-coded-identically-to-a-arguments-of-the-default-transitive-class-and-s-arguments-of-another-predicate-class-coded-identically-to-p-arguments-of-the-default-transitive-class-split-s)) are not characteristic of any particular area or areas, but are characterized as primarily a New World phenomenon ([Nichols 1992](Source#cldf:nichols1992linguistic): 229). Areal diffusion of indexing ([Align-06](#align-06-is-there-indexing-in-the-language)) has been reported to result from contact between the non-Pama-Nyungan languages of Arnhem land and their Pama-Nyungan neighbors ([Blake 1990](Source#cldf:blake1990pronouns); [Siewierska 2004](Source#cldf:siewierska2004person): 276).

There have also been claims about the correlations between individual alignment-related features, e.g. about the correlation between stative-active systems ([Align-11](#align-11-if-s-is-ever-marked-differently-than-a-in-indexing-or-flagging-ie-if-yes-to-either-align09-or-align10-is-there-a-difference-in-marking-according-to-an-activestative-distinction-among-monovalent-predicates-in-either-indexing-or-flagging)) and the presence of head marking, which includes indexing ([Align-06](#align-06-is-there-indexing-in-the-language)), and between ergativity and dependent marking ([Nichols 1992](Source#cldf:nichols1992linguistic)). 

## How?
Unlike most of the other feature sets in ATLAs, all the features in this feature set are derived from an underlying database of alignment. The scope and structure of this database, as well as the intermediate computational steps performed to derive some of the features are described in detail in [Inman et al (2024)](Source#cldf:inman2024alignment). Below we provide a brief summary.

Argument marking data for every language were encoded from available resources (grammars, dedicated articles, and personal correspondence with experts) into two data tables: one which lists contexts or bundles of contexts (Context Table), and one which lists selectors, which are usually markers or marker paradigms (Selector Table). From these primary data tables, an aggregated table is derived which lists alignment statements for each referential type, such as a person-number combination or a noun class (references.csv). All these tables are available in the CLDF format on the [ATLAs GitHub repository](https://github.com/davidainman/atlas-data/tree/master/cldf-alignment/generic-cldf). Note that a variety of different derived features can be extracted from the data, and we are including only a selection in this feature set.

The Context Table lists all the available contexts in every language. Every language has at least three contexts for flagging (one for each role S, A, and P) and one context for indexation (in the case of indexation being absent). The full list of contexts for each language depends on the attested person and number distinctions, the presence of noun classes, the presence of co-argument sensitivity, etc. Each context is associated with only one selector and one argument. A selector that marks two roles at the same time will therefore be represented in  two contexts, one context per argument (i.e. one for A and one for P). In many cases, contexts require more information to be fully specified, such as which slot the selector appears in, TAM, predicate class or other conditions. All this information is encoded in the Context Table in appropriate fields.

The Selector Table lists all selectors of all languages, along with information about them being used for flagging or indexation, what features they index, and if they are phonologically overt or not. There are two special pseudo-selectors NO\_FLAGGING and ROLE\_NOT\_MARKED to indicate the complete absence of flagging and indexing respectively for one or more roles. 

In the derived Reference Table, each row represents a referential type and it may be further specified with appropriate conditions such as TAM, predicate class, etc. For each referential type, an alignment statement is calculated over all contexts that include this referential type as an argument. We also calculated alignment statements while ignoring local scenarios (i.e. scenarios involving only 1st and 2nd persons), since they are more prone to co-argument sensitivity and could obscure more general patterns present in the language ([Heath 1998](Source#cldf:heath1998pragmatic); [Bank 2017](Source#cldf:bank2017assessing); [DeLancey 2021](Source#cldf:delancey2021differential)).

Data from the three aforementioned tables are analyzed jointly using R scripts to generate the language-wide features presented below. All R code is available in the [ATLAs Github repository](https://github.com/davidainman/atlas-data).

## Features

The features are organized thematically in the following way: we begin with the alignment patterns for nouns ([Align-01](#align-01-what-are-the-exemplar-alignments-of-nouns), [02](#align-02-what-are-all-the-alignments-of-nouns), [03](#align-03-is-there-differential-object-marking-dom-for-nouns)), for pronouns ([Align-04](#align-04-what-are-the-exemplar-alignments-of-pronouns), [05](#align-05-what-are-all-the-alignments-of-pronouns)), and for indexing ([Align-06](#align-06-is-there-indexing-in-the-language), [07](#align-07-what-are-the-exemplar-alignments-of-indexing), [08](#align-08-what-are-all-the-alignments-of-indexing)). We then have a group of features targeting various types of ergativity in the wide sense of S≠A ([Align-09](#align-09-is-s-ever-marked-differently-from-a-in-flagging), [10](#align-10-is-s-ever-marked-differently-from-a-in-indexing-if-there-is-indexing-in-the-language-ie-if-yes-to-align06), [11](#align-11-if-s-is-ever-marked-differently-than-a-in-indexing-or-flagging-ie-if-yes-to-either-align09-or-align10-is-there-a-difference-in-marking-according-to-an-activestative-distinction-among-monovalent-predicates-in-either-indexing-or-flagging), [12](#align-12-if-s-is-ever-marked-differently-than-a-in-indexing-or-flagging-ie-if-yes-to-either-align09-or-align10-are-s-arguments-of-one-predicate-class-coded-identically-to-a-arguments-of-the-default-transitive-class-and-s-arguments-of-another-predicate-class-coded-identically-to-p-arguments-of-the-default-transitive-class-split-s)), and finally a group targeting various types of relationship between the A and P roles, including whether they are both indexed, the presence of co-argument sensitivity, and direct/inverse marking ([Align-13](#align-13-if-there-is-indexing-ie-if-yes-to-align06-can-both-a-and-p-be-indexed), [14](#align-14-if-both-a-and-p-can-be-indexed-ie-if-yes-to-align13-are-there-person-portmanteaus), [15](#align-15-is-there-any-coargument-sensitivity-that-is-not-exclusively-due-to-person-portmanteaus-and-if-so-where), [16](#align-16-if-co-argument-sensitivity-exists-in-indexing-and-it-is-not-only-due-to-portmanteaus-ie-indexing-or-both-to-align15-is-there-directinverse-marking-in-some-scenarios)).

Some features (e.g. [Align-01](#align-01-what-are-the-exemplar-alignments-of-nouns), [02](#align-02-what-are-all-the-alignments-of-nouns), [04](#align-04-what-are-the-exemplar-alignments-of-pronouns)) contain information about the proportion of an alignment type. This is calculated according to a simple voting procedure for each relevant referential type (e.g. 1sg, 2sg, 3sg.masc, 3sg.fem, 1pl, 2pl, 3pl for pronouns, or masc and fem for nouns). We include the common alignments of:

- **accusative** (S=A≠P)
- **ergative** (S=P≠A)
- **tripartite** (S≠A≠P)
- **horizontal** (S≠A=P)
- and neutral (S=A=P), distinguished into two types:
    - **no marking**, where there is no overt morphology
    - **overt neutral**, where there is identical overt morphology

Finally, we include the pseudo-alignment type **sensitive**, which indicates that there are further alignment patterns which depend on the referential type of the transitive co-argument, e.g. the alignment of the 1st person could be neutral when considering 1>3 scenarios, but ergative when considering 1>2 scenarios.

We illustrate the features below with data, however these features were not coded manually but derived algorithmically from the underlying data structure. For details about how this derivation functions, see [Inman et al (2024)](Source#cldf:inman2024alignment) and the [publicly available code](https://github.com/davidainman/atlas-data).

### [](ParameterTable#cldf:Align-01)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] }**

#### ergative:1: Shipibo-Conibo \[ship1254\] (Pano-Tacanan; Peru)
Shipibo-Conibo has an ergative marker which appears on all nouns marking the A role, as exemplified for the word ‘dog’ in the S (1a), A (1b) and P (1c) roles.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(1)</span></th>
    <th class="tg-0lax" colspan="5"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Shipibo-Conibo (<a class="Source" href="../sources/valenzuela2010ergativity">Valenzuela 2010</a>: 72)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Nawa-n</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ochíti-ra</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">jojo</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ik-ai</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mestizo-GEN</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dog:ABS-EVID</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ONOM.bark</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DO.I-INC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The mestizo’s dog is barking.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">E-a-ra</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nawa-n</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ochíti-nin</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">natex-ke</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1-ABS-EV</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mestizo-GEN</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dog-ERG</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">bite-CMPL</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The mestizo’s dog bit me.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">E-n-ra</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">nawa-n</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ochíti</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">jamá-ke</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1-ERG-EV</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mestizo-GEN</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dog:ABS</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kick-CMPL</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I kicked the mestizo’s dog.’</span></td>
  </tr>
</tbody></table>


#### accusative:1: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
In the exemplar condition of definite and animate objects, S and A roles are in the unmarked nominative case, while the P role is marked with the accusative (2).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(2)</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Mongolian (<a class="Source" href="../sources/janhunen2012mongolian">Janhunen 2012</a>: 206)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">en’</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mory-ii.g</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ab-sen</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">this</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">horse-ACC</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">buy-P.PRF</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I bought this horse.’</span></td>
  </tr>
</tbody></table>


#### ergative:1: Kalaallisut \[kala1399\] (Eskimo-Aleut; Greenland)
In the exemplar condition, Kalaallisut has an ergative alignment, with A roles being marked in the relative (or ergative) case while other roles are unmarked, as seen in (3).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(3)</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Kalaallisut (<a class="Source" href="../sources/fortescue1984kalaallisut">Fortescue 1984</a>: 210)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ilinniartitsisuq</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ani-pallag-puq</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">teacher</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">go.out-quickly-3SG.INDIC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The teacher came out quickly.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">umiarsu-up</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aataaq</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aallaa-vaa</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">uncle-my.REL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">harp.seal</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">shoot-3SG&gt;3SG.INDIC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘My uncle shot the harp seal.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">c.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">umiarsu-up</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Qaqurtuq</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aqqusaar-paa</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ship-REL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Qaqortoq</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">stop.by.at-3SG&gt;3SG.INDIC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘The ship stopped (en route) at Qaqartoq.’</span></td>
  </tr>
</tbody></table>


### [](ParameterTable#cldf:Align-02)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] }**

#### ergative:1: Shipibo-Conibo \[ship1254\] (Pano-Tacanan; Peru)
There are no other alignments for nouns in Shipibo-Conibo other than the ergative.

#### accusative:0.5; neutral:0.5: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
In the non-exemplar case of an indefinite (or non-specific or generic) object, the P role does not receive any case marking, generating a neutral alignment for indefinites (since nominative is also unmarked). Compare the indefinite (4) below with the definite (2) [above](#align-01-what-are-the-exemplar-alignments-of-nouns).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(4)</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Mongolian (<a class="Source" href="../sources/janhunen2012mongolian">Janhunen 2012</a>: 206)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">en’</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">mory</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ab-sen</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">this</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">horse</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">buy-P.PRF</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I bought a horse.’</span></td>
  </tr>
</tbody></table>

The two relevant types of nouns in Halh Mongolian, definite and indefinite, are thus split evenly between accusative and neutral alignments.

#### ergative:0.5; tripartite:0.5: Kalaallisut \[kala1399\] (Eskimo-Aleut; Greenland)
In the non-exemplar case of an indefinite object, the P role receives instrumental marking, as exemplified in (5).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(5)</span></th>
    <th class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Kalaallisut (<a class="Source" href="../sources/fortescue1984kalaallisut">Fortescue 1984</a>: 249)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">atuakka-nik</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">atuar-puq</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">book-INSTR.PL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">read-3SG.INDIC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘He read </span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">some</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> books.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">atuakka-t</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">atuar-puq</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">book-PL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">read-3SG&gt;3PL.INDIC</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘He read </span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">the</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> books.’</span></td>
  </tr>
</tbody></table>

The instrumental case means that indefinite nouns have a tripartite alignment: unmarked when in the S role, relative (ergative) in A role, and instrumental in P role. The two relevant types of nouns in Kalaallisut, definite and indefinite, are split between ergative and tripartite alignments.

### [](ParameterTable#cldf:Align-03)
&emsp;**{ yes | no }**

For this feature, we consider differential object marking (DOM) in the “wide” sense: it includes any situation where the P role is marked differently (for whatever reason, including a different referential type, TAM, or another condition, but excluding declension class-based allomorphy).

It is conceivable that this question could have an &lt;NA&gt; value for languages that have no marking on nouns in the S, A, and P roles. However, such languages share the property that all arguments (i.e. S, A, and P) are the same, and most languages have some way of marking at least some other roles and/or adjuncts differently (e.g. with an adposition or a locative). We have thus grouped languages with a neutral alignment for nouns with languages that lack DOM.

#### no: Shipibo-Conibo \[ship1254\] (Pano-Tacanan; Peru)
All nouns in Shipibo-Conibo receive ergative marking.

#### yes: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
Halh Mongolian has DOM according to the properties of the P role, as shown in example (4) [above](#align-02-what-are-all-the-alignments-of-nouns).

### [](ParameterTable#cldf:Align-04)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] }**

#### ergative:1: Shipibo-Conibo \[ship1254\] (Pano-Tacanan; Peru)
Pronouns in Shipibo-Conibo are consistently ergatively aligned, as is true for the language’s nouns ([Valenzuela 2003](Source#cldf:valenzuela2003shipibokonibo): 185-186).

#### accusative:1: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
Like nouns, pronouns in the P role under exemplar conditions receive the accusative case ([Janhunen 2012](Source#cldf:janhunen2012mongolian): 205-208).

#### accusative:0.5; tripartite: 0.5: Siuslaw \[sius1254\] (isolate; United States)
Siuslaw pronouns have three distinct cases: subjective, objective, and discriminative ([Frachtenberg 1922](Source#cldf:frachtenberg1922siuslaw): 575-576). The subjective case is used to mark both S and A roles, and the objective case strictly marks the P role. However, the so-called “discriminative” marks A roles, especially when, according to Frachtenberg, “the sentence absolutely requires that the subjectivity of action be indicated.” This is a type of miscellaneous condition which has no bearing on the definition of the exemplar transitive clause, and so there are two possible alignments present in the exemplar scenario for Siuslaw pronouns: the accusative alignment and the tripartite alignment.

### [](ParameterTable#cldf:Align-05)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] }**

#### accusative:1: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
Unlike nouns, pronouns in the P role are always in the accusative case, as the conditions that trigger nominative marking (indefiniteness) cannot apply to pronouns ([Janhunen 2012](Source#cldf:janhunen2012mongolian): 205-208).

#### accusative:0.5; tripartite: 0.5: Siuslaw \[sius1254\] (isolate; United States)
Because the conditions that alter the pronominal alignment of Siuslaw cross-cut the exemplar definition, the language has the same alignments and in the same proportion in both the exemplar condition and in all conditions.

### [](ParameterTable#cldf:Align-06)
&emsp;**{ yes | no }**

#### yes:  Creek \[cree1270\] (Muskogean; United States)
Creek has a complex method of indexing, explained in more detail [below](#align-07-what-are-the-exemplar-alignments-of-indexing) ([Kimball 2005](Source#cldf:kimball2005natchez): 407-414).

#### no: Bulo Stieng \[bulo1242\] (Austroasiatic; Cambodia, Viet Nam)
There is no marking of roles on the verb in Bulo Stieng ([Bon 2014](Source#cldf:bon2014grammaire): 321).

### [](ParameterTable#cldf:Align-07)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] | NA }**

#### accusative:1: Dukha \[dukh1234\] (Turkic; Mongolia)
The completive aspect in Dukha is marked on verbs with a suffix *-də*, followed by a possessive suffix indexing the subject (S or A role) of the clause (6) ([Ragagnin 2011](Source#cldf:ragagnin2011dukhan): 122).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(6)</span></th>
    <th class="tg-0lax" colspan="5"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Dukha (<a class="Source" href="../sources/ragagnin2011dukhan">Ranagnin 2011</a>: 155)</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Pis-ter</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">aʰt</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">suɣ-ar-ar</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">te-eš</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">gel-də-</span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">βəs</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">we-PL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">horse</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">water-V.DER-INTRA.VBN</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">say-CB</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">come-PST-</span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1PL</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="5"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘We came to water the horses.’</span></td>
  </tr>
</tbody></table>


Dukha has other alignments in non-completive aspects, discussed [below](#align-08-what-are-all-the-alignments-of-indexing).

#### accusative:0.8; no marking:0.2: Creek \[cree1270\] (Muskogean; United States)
Creek verbs have both agentive and patientive paradigms of person markers, which encode first and second person, but not third person ([Martin 2011](Source#cldf:martin2011creek): 168-169). In transitive verbs, both paradigms appear, while in an active intransitive clause, only the active paradigm appears (7).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(7)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ca-na:fk-íck-a’</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.PAT-hit.LGR-2SG.AG-Q</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘Are you hitting me?’ (<a class="Source" href="../sources/martin2011creek">Martin 2011</a>: 168)</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">póna:y-íck-i:-ti’</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">talk.LGR-2SG.AG-DUR-be</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘Do you speak (Creek)?’ / ‘Can you speak?’ (<a class="Source" href="../sources/martin2011creek">Martin 2011</a>: 305)</span></td>
  </tr>
</tbody>
</table>

The A and P paradigms only encode the persons 1SG, 1PL, 2SG, 2PL, while all 3rd persons (singular or plural) receive no marking. For this reason, the accusative alignment occurs for four out of five persons-number combinations distinguished by verbs (0.8) while the no marking alignment occurs for one out of five (0.2).

#### sensitive:1: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Nuu-chah-nulth verbs index a single argument with a clausal enclitic, which distinguishes between 1SG, 1PL, 2SG, 2PL, 3SG, and 3PL. In transitive verbs, the argument which these enclitics index is complicated by the passive-inverse *=!at* morpheme, which obligatorily appears in situations in which a third person acts upon a first or second person, and appears to also be used whenever a non-topical third person acts upon a topical third person ([Emanatian 1988](Source#cldf:emanatian1988nootka): 267-268). When *=!at* is present, the clausal enclitic indexes the patientive role, and when it is absent, the enclitic indexes the agentive role. This results in a “sensitive” pseudo-alignment across all persons, as the choice of marker is always dependent on both the A and P roles.

### [](ParameterTable#cldf:Align-08)
&emsp;**{ ; separated list of \[ no marking:\_frequency\_ , accusative:\_frequency\_ , ergative:\_frequency\_ , overt neutral:\_frequency\_ , tripartite:\_frequency\_ , horizontal:\_frequency\_ , sensitive:\_frequency\_ \] | NA }**

#### accusative:0.5; no marking:0.5: Dukha \[dukh1234\] (Turkic; Mongolia)
Verbs in non-completive aspect in Dukha have no indexation marked on them at all. This leads to a split according to the two aspectual categories: an accusative alignment when the verb is completive (see [above](#align-07-what-are-the-exemplar-alignments-of-indexing)), and no marking when it is non-completive.

#### ergative:0.4; accusative:0.4; no marking:0.2: Creek \[cree1270\] (Muskogean; United States)
In addition to the exemplar alignments of accusative and no marking, Creek verbs can also have an ergative alignment. This occurs in non-agentive intransitives, which are indexed with the paradigm of P markers, rather than the paradigm of A markers. Compare (8) below with (7) [above](#align-07-what-are-the-exemplar-alignments-of-indexing).

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(8)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ca-nókk-i:-s</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.PAT-be.sick-DUR-IND</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I am sick.’ (<a class="Source" href="../sources/martin2011creek">Martin 2011</a>: 170)</span></td>
  </tr>
</tbody>
</table>

Note that the 3rd person patientive paradigm still receives no marking. The split among all possible alignments is thus: (a) 20% no marking (one fifth of the person-number combinations are not indexed at all, i.e. 3rd person); (b) 40% accusative (the remaining person-number combinations when active intransitives and transitives are compared); (c) 40% ergative (the remaining person-number combinations when inactive intransitives and transitives are compared). Note that these percentages equally weight all person-number combinations distinguished by the language and all verb classes, and are not to be taken as a representation of alignment frequencies in a corpus or in fluent speech.

#### sensitive:1: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
There are no changes in alignment properties in Nuu-chah-nulth between exemplar and non-exemplar scenarios.

### [](ParameterTable#cldf:Align-09)
&emsp;**{ yes | no }**

#### yes: Shipibo-Conibo \[ship1254\] (Pano-Tacanan; Peru)
Both [nouns](#align-02-what-are-all-the-alignments-of-nouns) and [pronouns](#align-04-what-are-the-exemplar-alignments-of-pronouns) are fully ergative, in which case S and A always are flagged differently.

#### yes: Siuslaw \[sius1254\] (isolate; United States)
Siuslaw pronouns are split between accusative and tripartite alignments (see [above](#align-04-what-are-the-exemplar-alignments-of-pronouns)), in which case at least some of the time, S and A arguments are flagged differently.

#### no: Halh Mongolian \[halh1238\] (Mongolic-Khitan; Mongolia, Russia)
[Nouns](#align-02-what-are-all-the-alignments-of-nouns) in Halh Mongolian are split between accusative and neutral alignments, while [pronouns](#align-04-what-are-the-exemplar-alignments-of-pronouns) are fully accusative. In no case are S and A arguments flagged differently.

### [](ParameterTable#cldf:Align-10)
&emsp;**{ NA | yes | no }**

#### NA: Bulo Stieng \[bulo1242\] (Austroasiatic; Cambodia, Viet Nam)
Bulo Stieng does not have indexing.

#### yes: Creek \[cree1270\] (Muskogean; United States)
Creek has ergative indexing under some conditions (see [above](#align-08-what-are-all-the-alignments-of-indexing)).

#### no: Dukha \[dukh1234\] (Turkic; Mongolia)
Dukha has only accusative and no marking alignments (see [above](#align-08-what-are-all-the-alignments-of-indexing)), and thus S is never marked differently from A.

### [](ParameterTable#cldf:Align-11)
&emsp;**{ NA | yes | no }**

#### yes: Creek \[cree1270\] (Muskogean; United States)
Ergativity in Creek is associated with inactive monovalent verbs, while accusativity is associated with active monovalent predicates (see [above](#align-08-what-are-all-the-alignments-of-indexing)).

#### no: Kalaallisut \[kala1399\] (Eskimo-Aleut; Canada)
Kalaallisut exhibits tripartite, ergative, and no marking alignments in its flagging. These variations in alignment occur due to the differences between pronouns and nouns, and indefinite versus definite P roles ([Fortescue 1984](Source#cldf:fortescue1984kalaallisut): 206-211, 249-263). None of these alignments are associated with particular predicates.

### [](ParameterTable#cldf:Align-12)
&emsp;**{ NA | yes | no }**

#### yes: Creek \[cree1270\] (Muskogean; United States)
Inactive monovalent (intransitive) verbs have their S role indexed with the same paradigm that indexes P, while active monovalent (transitive) verbs have their S role indexed with the same paradigm that indexes A (see [above](#align-08-what-are-all-the-alignments-of-indexing)).

#### no: Kalaallisut \[kala1399\] (Eskimo-Aleut; Canada)
The S and A roles in Kalaallisut are never marked with the same case  ([Fortescue 1984](Source#cldf:fortescue1984kalaallisut): 206-211).

### [](ParameterTable#cldf:Align-13)
&emsp;**{ NA | yes | no }**

This feature tracks whether it is possible for A and P to be indexed on the verb, but not necessarily simultaneously. Languages which alternately mark the A or P argument, depending on the co-argument (e.g. languages that always mark 1st or 2nd person, regardless of their role) are still categorized as &lt;yes&gt;.

#### yes: Kalaallisut \[kala1399\] (Eskimo-Aleut; Canada)
Nearly all indexing on the Kalaallisut transitive verb is done through portmanteau morphemes that index both A and P roles ([Fortescue 1984](Source#cldf:fortescue1984kalaallisut): 288-289). Although elements of these morphemes are parseable, such as the presence of final *-si* when indexing a second person plural P, these portmanteaus cannot be fully analyzed into their A and P indexing constituents, as shown in Table 1.

<div class="datainset">
Table 1: Indicative transitive markers in Kalaallisut, reproduced from <a class="Source" href="../sources/fortescue1984kalaallisut">Fortescue (1984: 289)</a>.
<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">A \ P</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3s</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3p</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2s</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2p</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1s</span></th>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1p</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1s</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-varat</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vakka</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vakkit</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vassi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2s</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vat</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vatit</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-varma</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vatsigut</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3s</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaa</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vai</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaatit</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaasi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaanga</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaatigut</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1p</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-varput</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vavut</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vatsigit</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vassi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2p</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-varsi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vasi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">–</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vassinga</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vassigut</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3p</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaat</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaat</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaatsit</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaasi</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaannga</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-vaatigut</span></td>
  </tr>
</tbody></table>
</div>

#### yes: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Although only one argument is indexed at a time on the Nuu-chah-nulth verb, whether that argument is the A or P role depends on the co-arguments involved (see [above](#align-07-what-are-the-exemplar-alignments-of-indexing)). Thus, both A and P can be indexed.

#### no: Dukha \[dukh1234\] (Turkic; Mongolia)
Transitive verbs in Dukha only ever index the A role (see [above](#align-07-what-are-the-exemplar-alignments-of-indexing)).

### [](ParameterTable#cldf:Align-14) 
&emsp;**{ NA | yes | no }**

#### yes: Kalaallisut \[kala1399\] (Eskimo-Aleut; Canada)
There are person portmanteaus in Kalaallisut, as shown above.

#### no: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Only one role, either the A or P, is indexed in declarative Nuu-chah-nulth clauses. Note that this is not true of imperatives, which do index both A and P roles ([Nakayama 2001](Source#cldf:nakayama2001nuuchahnulth): 38). However, imperatives are outside of the scope of this feature set.

### [](ParameterTable#cldf:Align-15)
&emsp;**{ no | indexing | flagging | both }**

Co-argument sensitivity refers to cases where the marking of an argument is dependent not just on its role (A or P), but also on the referential properties of its co-argument, that is the other argument of a transitive verb. This can occur due to person portmanteaus (as tracked in [Align-14](#align-14-if-both-a-and-p-can-be-indexed-ie-if-yes-to-align13-are-there-person-portmanteaus)) or due to marking patterns that do not include portmanteaus. This latter case notably includes indexing systems that are traditionally described as hierarchical. Because co-argument sensitivity can occur in both flagging and indexing systems, there is no &lt;NA&gt; value for this feature.

#### no: Dukha \[dukh1234\] (Turkic; Mongolia)
There is no co-argument sensitivity in Dukha.

#### indexing: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Indexing sensitivity on the Nuu-chah-nulth verb is due entirely to co-argument conditions, and never to portmanteaus (see [above](#align-07-what-are-the-exemplar-alignments-of-indexing)). There is no sensitivity of this kind in the language’s flagging.

#### indexing: Teko \[emer1243\] (Tupian; French Guiana)
All verbs in Teko carry a person index, which either comes from the Set I (S/A indexing paradigm) or Set II (P indexing paradigm) of morphemes. However, both do not appear on the verb at the same time, and a hierarchy determines which person is indexed. In cases where speech act participants interact with third persons, the speech act participant is always indexed, regardless of their grammatical role. In local scenarios (in which speech act participants act on each other), portmanteau morphemes index both roles. In other scenarios, the A role is indexed ([Rose 2009](Source#cldf:rose2009hierarchical): 64-66).

#### flagging: Teribe \[teri1250\] (Chibchan; Costa Rica, Panama)
In Teribe, co-argument sensitivity occurs in the language’s flagging to the exclusion of indexing (of which there is none). In cases in which a 3rd person acts upon a speech act participant, or an obviative 3rd person acts upon a proximate 3rd person, the agents are marked with an obviative case marker *dë*, as in (9) below.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(9)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">plu</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(li)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ī-no-r</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">king</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(TOP)</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">see-PERF-1SG</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I saw the king.’ (<a class="Source" href="../sources/quesada2000teribe">Quesada 2000</a>: 154)</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ta</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">ī-na</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Juan</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">dë</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">see-PERF.INV</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Juan</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">OBV</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘Juan saw me.’ (<a class="Source" href="../sources/quesada2000teribe">Quesada 2000</a>: 155)</span></td>
  </tr>
</tbody></table>

Note that while there is an inverse marker on the verb, there is no person-indexing on the verb, and so Teribe is considered as expressing co-argument sensitivity strictly on the noun.

#### flagging: Southern Yukaghir \[sout2750\] (Yukaghir; Russia)
The case marking of core participants in Southern Yukaghir depends on the persons involved in the scenario. The P role is typically flagged as accusative, but a third person P is flagged as nominative if the A role is filled by a first or second person ([Maslova 2003](Source#cldf:maslova2003kolyma): 80-89).

#### both: Arizona Tewa \[ariz1237\] (Kiowa-Tanoan; United States)
Arizona Tewa has co-argument sensitivity expressed in both its indexing and flagging. In transitive expressions, indexation changes depending on whether a speech act participant is acting on a 3rd person, or a 3rd person is an agent ([Zúñiga 2002](Source#cldf:zuniga2002inverse): 184). In addition to the verbal co-argument sensitivity, an oblique (or instrumental) marker *-di* occurs on agent NPs when a 1st or 2nd person is acted upon, or when a 3rd person proximate is acted upon by a 3rd person obviative. A pair of examples from ([Zúñiga 2002](Source#cldf:zuniga2002inverse): 184-187) illustrating this is given in (10) below.

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(10)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">a.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Nɛ́’i</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">kʷiyó</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> dó-tay</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">this</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">woman</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1sII-know</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘I know this woman.’</span></td>
  </tr>
</tbody></table>

<table class="tg"><thead>
  <tr>
    <th class="tg-0lax">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">b.</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Hę’i</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">sen-</span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">di</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">’ų</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">wóː-kʰɛ̨gen-’án</span></th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">that</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">man-</span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">OBL</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2s</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">2sIII-help-COMPL</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"></td>
    <td class="tg-0lax"></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘That man helped you.’</span></td>
  </tr>
</tbody></table>

### [](ParameterTable#cldf:Align-16)
&emsp;**{ NA | yes | no }**

Direct/inverse marking is defined here as a non-indexical marker which only appears in certain scenarios (i.e. co-argument configurations). This could occur in only a specific scenario, such as 1st person acting on 2nd person plural, or it could occur in a bundle of scenarios, such as whenever 3rd person acts on 1st or 2nd. Markers which appear in scenarios that violate the general hierarchy of 1/2 > 3 are typically called *inverse*, while those which appear when this hierarchy is followed are generally called *direct*.

Definitionally, such markers can only appear if there is non-portmanteau based co-argument sensitivity. This feature only tracks whether some marker of this type is present, regardless of whether it is direct or inverse.

#### yes: Nuu-chah-nulth \[nuuc1236\] (Wakashan; Canada)
Whenever the P role is indexed on the Nuu-chah-nulth verb instead of the A role, a passive/inverse morpheme *=!at* appears (see [above](#align-07-what-are-the-exemplar-alignments-of-indexing)). Though this marker has been called variously a passive or inverse, its obligatory appearance in cases where the P role is indexed on the verb is sufficient to categorize it as an inverse for this typology.

#### yes: Teribe \[teri1250\] (Chibchan; Costa Rica, panama)
Despite the fact that Teribe lacks indexing, its verbs are marked for inverse scenarios, with morphology that cumulates inversion and aspect, as seen in example (9) [above](#align-15-is-there-any-coargument-sensitivity-that-is-not-exclusively-due-to-person-portmanteaus-and-if-so-where)

#### no: Teko \[emer1243\] (Tupian; French Guiana)
Although indexing in Teko follows a hierarchy, this is not accompanied by a morpheme marking when that hierarchy is followed or when it is violated.

## Derived features
In addition to the features described above, this feature set contains further derived features based on the main features. These are presented briefly in this section.

### [](ParameterTable#cldf:Align-01a)
&emsp;**{ no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

Rather than reporting on all possible exemplar alignments for nouns (as in [Align-01](#align-01-what-are-the-exemplar-alignments-of-nouns)), this feature selects the most common alignment according to referential type (if there is one) or gives &lt;no majority&gt; (if there is no most common alignment).

### [](ParameterTable#cldf:Align-01b)
&emsp;**{ no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

This feature removes from consideration all local scenarios present in Align-01a.

### [](ParameterTable#cldf:Align-04a)
&emsp;**{ no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

Rather than reporting on all possible exemplar alignments for pronouns (as in [Align-04](#align-04-what-are-the-exemplar-alignments-of-pronouns)), this feature selects the most common alignment according to referential type (if there is one) or gives &lt;no majority&gt; (if there is no most common alignment).

### [](ParameterTable#cldf:Align-04b)
&emsp;**{ no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

This feature removes from consideration all local scenarios present in Align-04a.

### [](ParameterTable#cldf:Align-07a)
&emsp;**{ NA | no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

Rather than reporting on all possible exemplar alignments for indexing (as in [Align-07](#align-07-what-are-the-exemplar-alignments-of-indexing)), this feature selects the most common alignment according to referential type (if there is one) or gives &lt;no majority&gt; (if there is no most common alignment).

### [](ParameterTable#cldf:Align-07b)
&emsp;**{ NA | no marking | accusative | ergative | overt neutral | tripartite | horizontal | sensitive | no majority }**

This feature removes from consideration all local scenarios present in Align-07a.

### [](ParameterTable#cldf:Align-15a)
&emsp;**{ yes | no }**

<table class="dconversion"><thead>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Align.15 is &lt;indexing&gt; OR Align.15 is &lt;flagging&gt; OR Align.15 is &lt;both&gt;</span></td>
  </td></thead>
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Align.15 is &lt;no&gt;</span></td>
  </tr>
</tbody>
</table>

This feature groups together all the different loci of co-argument sensitivity presented in [Align-15](#align-15-is-there-any-coargument-sensitivity-that-is-not-exclusively-due-to-person-portmanteaus-and-if-so-where).

## Results
The most widespread flagging pattern for both nouns and pronouns is absence of marking, followed by accusative alignment ([Align-01](../parameters/Align-01), [02](../parameters/Align-02), [04](../parameters/Align-04), [05](../parameters/Align-05)). In North America, accusativity is common among both nouns and pronouns in California, the southern United States, and the Gulf Coast north of the Chihuahuan Desert. In Central and South America, accusative flagging of pronouns is typical of the southern tip of Central America and the western Amazon, and accusativity across both pronouns and nouns occurs largely along the Andes. Outside of the Americas, accusativity is common in both Eurasia and Africa. Ergativity in flagging, in the broad sense of S≠A ([Align-09](../parameters/Align-09)), is widespread along the western coast of the Americas, occurring from Alaska to British Columbia, from Oregon to California, in northern Peru, and in the Southern Cone. It is also widely scattered throughout the Amazon. Outside of the Americas, S≠A in flagging is most common in Australia, Papunesia, and the Caucasus. DOM among nouns is typical of Eurasia and the Northwest Amazon, and appears with some frequency along the North American west coast ([Align-03](../parameters/Align-03)).

Indexing is widespread, though notably absent in Southeast and East Asia ([Align-06](../parameters/Align-06)). Accusative alignments predominate, with majority ergative alignments especially present among Mayan languages ([Align-07](../parameters/Align-07), [07a](../parameters/Align-07a)). Majority co-argument sensitive alignments are also extremely common, especially in North America and Australia. Once local scenarios are excluded, many of these majority co-argument sensitive alignments become accusative or overt neutral, although many remain in both North America and Australia ([Align-07b](../parameters/Align-07b)). Tripartite alignment is rare and is seldom dominant, but particularly occurs in eastern and northeastern Eurasia, Central America, and Bolivia ([Align-08](../parameters/Align-08)). The presence of ergativity in indexing, in the wide sense of S≠A ([Align-10](../parameters/Align-10)), is more common than ergativity in flagging ([Align-09](../parameters/Align-09)) and few languages have ergativity across both domains. Ergativity in indexing is common in eastern North America, Central America, the central Amazon, the Caucasus, and Northeast Asia. This pattern notably spans the Bering Strait.

Most, but not all languages with an active/stative distinction among monovalent predicates ([Align-11](../parameters/Align-11)) also are Split-S in the traditional sense ([Align-12](../parameters/Align-12)), a pattern that is typical of the North American plains and the Southeast, the northwest Amazon, and some languages of the eastern Amazon.

Many languages index both A and P ([Align-13](../parameters/Align-13)) and have portmanteau morphemes ([Align-14](../parameters/Align-14)), without exhibiting a clear areal pattern.

Co-argument sensitivity is predominantly found in indexing ([Align-15](../parameters/Align-15)) and is highly unevenly distributed ([Align-15a](../parameters/Align-15a)). It is typical of Australia, Northeast Asia, and much of North America (the notable exceptions being the north Pacific Northwest, Southern California, and the coastal Southeast). It is also highly present in northern Central America, whereas in South America it seems to follow largely familial patterns (especially present in Quechuan, Cariban, and Tupian). Of these languages, only a minority have dedicated direct/inverse marking ([Align-16](../parameters/Align-16)), and many of these are in the central region of the Pacific Northwest.

## Contributions

**Conceptualization**: [David Inman](Contributor#cldf:DI), [Marine Vuillermet](Contributor#cldf:MV), [Alena Witzlack-Makarevich](Contributor#cldf:AWM), [Balthasar Bickel](Contributor#cldf:BB)

**Data collection**: [David Inman](Contributor#cldf:DI), [Alena Witzlack-Makarevich](Contributor#cldf:AWM), [Alexandra Nogina](Contributor#cldf:AN), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Tai Hong](Contributor#cldf:HT), [Anna Graff](Contributor#cldf:AG)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Alena Witzlack-Makarevich](Contributor#cldf:AWM), [Natalia Chousou-Polydouri](Contributor#cldf:NCP)

**Computer code**: [David Inman](Contributor#cldf:DI), [Melvin Steiger](Contributor#cldf:MS), [Natalia Chousou-Polydouri](Contributor#cldf:NCP)

## References
[References](Source?cited_only#cldf:__all__)


[^1]: Alignment statements can also be made about the word order of arguments and their syntactic behavior in various constructions.