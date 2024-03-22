**Authors**: [David Inman](Contributor#cldf:DI)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Nora Muheim](Contributor#cldf:NJM)

[TOC]

## What?
This feature set encompasses some of the common typological questions about syntactic word order: the relative orders of subject, object, and verb in an unmarked matrix declarative transitive clause,[^1,^2] the ordering of attributive and noun, and the ordering of genitive (or possessor) and (possessed) noun ([Greenberg 1963](Source#cldf:greenberg1963universals), [Dryer 2013a](Source#cldf:dryer2013wals81), [Dryer 2013b](Source#cldf:dryer2013wals86), [Dryer 2013c](Source#cldf:dryer2013wals87), [Krasnoukhova 2016](Source#cldf:krasnoukhova2016sailsnp)). Each of these language-wide comparanda have their own difficulties and must be defined narrowly to ensure cross-linguistic comparability.

In particular, the order of subject, object, and verb is fraught with issues, as has been pointed out by many previous researchers. Some of these problems are:

- A topic/comment syntactic structure may be more salient than subject/object order ([LaPolla and Poa 2008](Source#cldf:lapollapoa2006wordorder), [Li and Thompson 1981](Source#cldf:lithompson1981mandarin)).
- Languages may vary their word order according to information structure, and it is not always clear what the “basic” or “unmarked” or "default" order is, or if one even exists ([Hale 1980](Source#cldf:hale1980warlpiri), [Hale 1983](Source#cldf:hale1983warlpiri)).
- Languages may have truly unconstrained word order with no difference in information structure. This may (or may not) correlate with other syntactic phenomena ([Austin et al 2001](Source#cldf:austin2001warlpiri)).
- Languages may have only a partially restricted basic word order, e.g. verb-initial, with free order between subject and object. These partially restricted orders still contain information about relative ordering (e.g. verb before subject), which some typologists argue are more significant than the full, six-way order ([Dryer 1997](Source#cldf:dryer1997wordorder), [Dryer 2013d](Source#cldf:dryer2013wordorder)).

Despite these issues, which are addressed below, most languages do have a clear transitive clause word order, and several rigorous studies have yielded interesting results using typological data of this sort ([Comrie 1989](Source#cldf:comrie1989universals), [Dryer 1992](Source#cldf:dryer1992wordorder), [Dryer 1996](Source#cldf:dryer1996wordorder)).

In order to compare the languages in our sample, we first defined the comparative concepts to do so: the “basic” transitive clause (WO-01), what counts as an attributive for attributive-noun constructions (WO-02), and the “basic” order in nominal possession constructions (WO-03).

### The “basic” transitive clause
Our comparative concept for the basic transitive clause contains the following properties:

1. It stands alone as a grammatical utterance
2. It has declarative force (i.e., it is not interrogative or imperative)
3. It has sentential focus and no argument is information structurally marked

For many languages, these constraints are sufficient to unambiguously assign a word order to the language as a whole. Even in cases that are traditionally described as having more complex word order constraints, such as the V-second order in German, the constraint of sentential focus (3 above) unambiguously forces the system to be categorized as “SVO”.

However, in some languages, the determination of the basic word order can remain difficult, typically because of difficulty determining which sentences have sentential focus. All else being equal:

1. The word order of “out of the blue” declarative sentences reflects the basic word order.
2. The most frequent word order of matrix declarative sentences in large corpora across many domains (conversation, instruction, narrative, news, etc) reflects the basic word order.
3. The most typical positions of S and O when they are neither focus nor topic reflects the basic word order. To this end, the more syntactically complex S and O constituents are, the less likely they are to carry focus or topic information.

Since large corpora studies are often not available for minority languages, for consistency in our data, we *a priori* selected known problems with transitive clause word order typology and defined methods to approach them, as described in the [How? section](#how) below.

### The attributive-nominal construction
The order of attributive and noun (sometimes simply called adjective and noun) required a comparative concept of both the attributive and the construction being compared. We have used the term “attributive” rather than adjective to refer to property concept modifiers because many languages lack a well-defined syntactic category of adjectives, but there is nevertheless an ordering constraint between the modifier and noun. When modifying a noun with a property concept word, a language may have:

- a dedicated syntactic category of adjectives and a single word order;
- two or more dedicated syntactic categories of adjectives, each with different word orders;
- no dedicated syntactic category of adjectives, with property concepts being encoded by nouns, verbs, bound elements, or a generic modifier class.

The comparative concept we chose, and for which the term “attributive” is reserved in this questionnaire, is the category of basic, qualificational property concepts, with a primary preference for the category which is dedicated to modifying nouns (if one exists), and a secondary preference for the lexically open class.

The class must include basic lexical terms, which means that they are underived. The class must also be qualificational, which means we definitionally exclude numerals and quantificational adjectives. When these properties are not enough to select a single lexical class in a language, we prefer the class dedicated to modifying nouns, meaning that when there is a closed class of adjectives, we select this over the open class of non-adjective property concepts. In most cases where a language lacks a clear class of adjectives, attributives are drawn from the class of verbs or a subclass of verbs (as mentioned in [Dryer 2013c](Source#cldf:dryer2013wals87)). The syntactic category to which the attributive class belongs is recorded in the [Attributives](Attr) feature set.

The secondary preference for an open class means that, in cases where adjectives behave differently according to sub-categories, we select the class whose lexical membership is open. Once the attributive class is selected, we narrowly code the surface word order of the attributive and noun, regardless of their syntactic properties.

### The “basic” order in nominal possession constructions
Some languages have multiple categories of possession, depending on what is being possessed (e.g. alienable vs inalienable). For this comparative concept, we always selected the order used with the default (i.e. open) class of possessed nouns (alienable). If two or more constructions are used with different orders we prefer the order of the most common construction.

## Why?
Word order has been claimed to have a regional areal effect in the linguistic literature, for example:

- exclusively VO order in the Venezuelan-Antillean Linguistic Area ([Umaña 1991](Source#cldf:umana1991area): 125-126);
- exclusively SOV order in the Colombian-Central American area ([Umaña 1991](Source#cldf:umana1991area): 127);
- mostly SVO order in the languages of the Chaco region ([Campbell et al 2012](Source#cldf:campbellgrondona2012southamerica));
- Exclusively predicate-initial order (VSO or VOS) in the Pacific Northwest ([Beck 2000](Source#cldf:beck2000nwcoast)).
- Possessed Noun - Possessor Noun order in Central America ([Campbell 1997](Source#cldf:campbell1997america): 344)
- Possessor Noun - Possessed Noun in Lowland South America ([Campbell 1997](Source#cldf:campbell1997america): 350)
- Noun - Attributive order in both the Andes and Lowland South America ([Campbell 1997](Source#cldf:campbell1997america): 348-350)

## How?
The typologization of word order requires solving unique and often complex problems, especially for the basic transitive clause. Prior to coding, we selected known problems and decided how exemplar problematic cases should be coded.

### Problem 1: Determining “basic” ordering in a language with obligatory syntactic information structure
Some languages obligatorily mark information structure in the sentence, so that there is never an unmarked order. Thus, condition (3) of our criteria is never fully met. We still find it desirable to determine a basic word order for these languages, which we do by relaxing condition (3) and determining where each constituent occurs when it is unmarked. To the extent possible, the way we decide on the basic word order for such languages is to first determine: 

1. Where does the typical S occur when unmarked for information structure (and O is informationally-marked instead)?
2. Where does the typical O occur when unmarked for information structure (and S is marked instead)?

The “neutral” position of S is decided according to its position in the (1) condition, and likewise the “neutral” position of O is decided according to its position in (2).

#### SVO: Mandarin Chinese \[mand1415\] (Sino-Tibetan)
[Li and Thompson (1981: 15-21)](Source#cldf:lithompson1981mandarin) call Mandarin a “topic prominent” language, rather than a subject prominent one, in that the topic must always occur first, while the subject may be completely absent. In addition, the pre- or post-verbal position is how definiteness is expressed. In the common (or “basic”) case of a definite subject and an indefinite object, an SVO word order appears, but OSV and SOV are also possible and, according to them, Mandarin Chinese has other features typical of SOV languages.

[Li and Thompson (1981: 26)](Source#cldf:lithompson1981mandarin) suggest that Mandarin is in the middle of a shift from basic SVO to basic SOV word order, and deciding between the two orders depends in part on the acceptance of the “basic” object as indefinite. Our definition of the basic transitive clause does not include definiteness, so it does not resolve the order question. However, Li and Thompson also state that their sample text yields more frequent SVO than SOV sentences, and that the more complex a sentence is, the more likely it is to have SVO. The frequency of SVO in a corpus should reflect the basic word order, and the more complex a sentence is, the more likely it is that the individual S and O noun phrases are not the bearers of information structure. Thus, both of these factors suggest that SVO is the most “basic” order in the language. From this data, we would encode Mandarin Chinese as having an SVO basic word order, but with a detailed remark about the frequency of SOV.

#### VSO: Machiguenga \[mach1267\] (Arawakan; Peru)
[Emlen (2014: 22)](Source#cldf:emlen2014matsigenka) mentions in passing that Machiguenga has SVO word order, and [Michael (2014)](Source#cldf:michael2014nanti) says that the basic word order of closely-related Nanti \[nant1250\] (Arawakan; Peru) is arguably SVO. The subject prefix and object enclitic on the Machiguenga verb also suggest an SVO order (subj-\[...\]-V-\[...\]=obj). However, [O'Hagan (2018)](Source#cldf:ohagan2018syntax) claims the basic word order of Machiguenga is VSO, although this is infrequent because information-structural marking typically requires one argument or another to move to the front.

In Inman’s (ms) corpus study, SVO was essentially equally common as VSO when both arguments were expressed by overt NPs. However, it was relatively rare for both arguments to be present. New participants in the discourse were always introduced post-verbally, while pre-verbal ordering was highly correlated with contrastive marking and question-answering. Inman suggests two plausible restrictions driving this distribution: (1) left-of-verb constituents *must* be given within the discourse context; (2) right-of-verb constituents *must not* carry focus or topic information (while left-of-verb constituents *can*, but don’t have to, be focus or topic). If true, this means that right-of-verb constituents are always unmarked. Though the fieldwork has not been done to confirm all hypotheses, it is compatible with O’Hagan’s interpretation of an unmarked VSO order, with discourse-specific information (topic, focus, and givenness) generating other orders.

Like Mandarin Chinese, the determination of word order in Machiguenga is complex, and would require a remark in the database describing alternative analyses. However, the data available suggest that Machiguenga has an information structurally neutral VSO order, which is how we would code this language.

### Problem 2: Determining S and O ordering in languages with co-occurrence constraints.

Some languages do not allow both subject and object to appear overtly in the same clause as NPs, or this occurs so infrequently that it is difficult to determine what the basic order is. In these cases, subject and object are first ordered independently with respect to the verb and, if possible, the relative ordering of subject and object is inferred by determining special cases where both arguments are expressed (e.g., with pronouns). If an order between S and O cannot be determined at all, these languages should be encoded with a partially-restricted ordering, e.g. V-first.

#### VSO: Northern Lushootseed \[lush1252\] (Salishan; United States)

Lushootseed does not allow two non-oblique overt third person NPs ([Beck 1996](Source#cldf:beck1996lushootseed): 1-14). If both subject and object are present in the clause, the subject must be first or second person, expressed through a second position agreement enclitic. This necessarily yields a VSO order, if the subject is a speech act participant. In addition, objects that must be case-marked as oblique (as is the case for the verb ‘look for’) occur after the subject, yielding a V S oblique-O order. This also suggests a larger subject-before-complement pattern, which accords with the pattern seen for the second position elements. In this case, we would categorize the language as VSO, with a remark on the particularities of the system.

### Problem 3: Determining if a language really has no basic word order
It may be the case that a language truly has no basic word order. However, we attempt to separate languages with truly free word order (where order is flexible even without information structure constraints) and languages with flexible word order (with associated, distinct information structure) that nevertheless have a basic word order.

#### VSO: Russian \[russ1263\] (Indo-European)
Russian has quite free word order depending on the discourse context and information structure, but is typically characterized as having basic SVO word order. [Krupp (1983: 1-2)](Source#cldf:krupp1983russian) summarizes the reasoning for this in three points, which closely follow our assumptions about “basic” order:

1. Approximately 80% of transitive sentences in Russian are SVO.
2. When there is no inflectional information giving grammatical information for arguments, the ordering is SVO.
3. Unmarked sentences, “out of the blue” sentences, and semantically nonsense sentences are given in SVO ordering.

Despite its flexibility, we would code Russian as having a basic SVO ordering.

#### no dominant order: Warlpiri \[warl1254\] (Pama-Nyungan; Australia)
Warlpiri, like Russian, has flexible word order, but unlike Russian it has no basic order. At least since [Hale (1983)](Source#cldf:hale1983warlpiri), it has been described as “non-configurational.” In Hale’s words “it is true of Warlpiri that sentences containing the same content words in different linear arrangements count as repetitions of one another.” [Simpson (1983: 140)](Source#cldf:simpson1983warlpiri) agrees with Hale, saying “Like an intransitive sentence, [a transitive sentence] has completely free word order, except that the AUX \[...\] must remain in second position”.

There has been some recent work claiming the word order of Warlpiri is more constrained than it appears. [Legate (2002: Chapter 4)](Source#cldf:legate2002warlpiri) argues that Warlpiri has “an articulated left periphery” which hosts topic and focus, which must be used in an obligatory and non-random manner. However, this is not a structure that makes reference to the status of verbal arguments (properties like subject and object), and so it cannot be categorized as a language that has any basic order of its S, V, and O elements.

### Extracting data from WALS
Some data for this question was extracted from WALS chapters 81, 86, and 87 ([Dryer 2013a](Source#cldf:dryer2013wals81), [Dryer 2013b](Source#cldf:dryer2013wals86), [Dryer 2013c](Source#cldf:dryer2013wals87)) using custom R scripts. For ATLAs languages that were also present in one of these chapters, values were extracted directly from the WALS data. Basic transitive clause order (WO-01) was extracted from WALS 81, but given the differences in our typologization, all cases of &lt;No dominant word order&gt; were reviewed manually by checking grammars and changed appropriately. The order of attributive and noun (WO-02) was extracted from WALS 86, and given the differences in our typologization, all cases of &lt;Only internally-headed relative clauses&gt; were also reviewed manually and changed appropriately. Finally, the order of possessor and possessed noun was extracted from WALS 87. There was no difference in typological definitions in this last case, but WALS values were checked opportunistically as the coding of another of our feature set proceeded, namely [Noun Possession Classes](NounPoss).

## Questionnaire
### [](ParameterTable#cldf:WO-01)
&emsp;**{ no dominant order | SVO | SOV | VSO | OVS | OSV | VOS | V-first | V-last | S-last }**

The definition of “basic” transitive clauses, for the purposes of this question, is given in the What? section above, with details about specific types of problems in determining the basic word order given in the [How? section](#how).

The number of possible states for this question is rather large and encompasses all claims about complete and partial word orders found in the grammars consulted for this survey. The partial word orders encountered during coding were V-first, V-last, and S-last (the latter only in Hanis, [Frachtenberg 1922](Source#cldf:frachtenberg1922hanis): 414). There are other conceivable partially restricted orders such as “O-last” or “S-first”, but these were not encountered.

This question was designed to be mostly compatible with [SAILS NP2](https://sails.clld.org/parameters/NP2#5/1.746/289.565) and partially compatible with [WALS chapter 81](https://wals.info/chapter/81), from which some data was extracted (and then checked for consistency with our definitions, especially for “no dominant order”). Where this question departs from these other databases is in allowing for the partial orders V-first, V-last and S-last.

#### V-first: Alsea-Yaquina \[alse1251\] (isolate; United States)

Alsea-Yaquina has relatively flexible word order and the earliest account states that most clauses are verb-initial, but the ordering of object and subject is flexible ([Frachtenberg 1918](Source#cldf:frachtenberg1918alsea): 421). A later corpus study confirms these observations, with all orders of VOS, VSO, SVO, and OVS attested and the two V-initial orders being the most common. No clear discourse pragmatic analysis could easily distinguish between VSO and VOS ([Morgan et al 1985](Source#cldf:morgan1985northwest): 46), so we have thus coded Alsea-Yaquina as V-first.

#### SVO: Nanti \[nant1250\] (Arawakan; Peru)

[Michael (2008: 342-345)](Source#cldf:michael2008nanti) notes that only one argument at a time can be expressed by a phonologically free NP, and subjects prototypically precede the verb when expressed, while objects prototypically follow the verb. However, all focused elements (including objects) are preverbal. He concludes by saying the language is basically SVO, even though the actual order Subject-Verb-Object is unobservable due to the one-NP constraint. However, the partial orderings SV and VO can allow us to construct a hypothetical SVO order, if two NPs were permitted.

### [](ParameterTable#cldf:WO-02)
&emsp;**{ Attr-N | N-Attr | no dominant order }**

The “attributive” category for this question is described in the [What? section](#what) above: the class of basic, qualificational property concepts, preferentially the category dedicated to modifying nouns, and preferentially the lexically open class.

The definitions for this question are by design mostly compatible with [Dryer (2013c)](Source#cldf:dryer2013wals87), from which we imported some data, with the exception of Dryer’s “internally-headed relative clauses”. While Dryer assigns these internally-headed relative clauses their own distinct state, we have narrowly focused on surface word order, and encoded such cases according to the order of the attributive element and the head noun. This decision belies a potential comparative problem: the order of a head noun and a direct attributive modifier (the **be.beautiful(-ADJVZ)** dog) is perhaps not directly comparative with a head noun and a verbal modifier which is inside a relative clause (the dog, **which be.beautiful**). Ideally, modifiers which must be in a relative clause would receive their own state (such as &lt;NA&gt;). However, we did not collect the data to distinguish between these cases, and the determination of whether there is a relative clause or not (especially if the relative clause is headless) can be quite complex and even indeterminate. Therefore, this question has only targeted the surface order of the attributive and head noun, even though we acknowledge this may not be the most ideal encoding.

In addition, some languages incorporate the noun and the attributive into a single word rather than expressing them independently, a phenomenon which typically correlates with attributives expressed as a verb. Analogous to how we have treated internally-headed relative clauses, we have again coded only the surface order of the attributive and noun. A complex example of such a case is described below for Tonkawa \[tonk1249\] (isolate; US).

#### N-Attr: Spanish \[stan1288\] (Indo-European)

Spanish has two sets of adjectives: a small, closed set which can come before the noun (typically with a different meaning than when they come after the noun): *grande* ‘great/big’, *nuevo* ‘new’, *viejo* ‘old’, etc. Although this Attr-N order is possible, it is not true for the open class of adjectives, and so the order would be N-Attr.

#### Attr-N: Nanti \[nant1250\] (Arawakan; Peru)

Nanti has approximately 25 underived adjectives, mainly restricted to the semantic classes of value, dimension, quantification, and number ([Michael 2008](Source#cldf:michael2008nanti): 311), which occur like all modifiers before the noun ([Michael 2008](Source#cldf:michael2008nanti): 369).

#### N-Attr: Tonkawa \[tonk1249\] (isolate; United States)

Tonkawa has predicative adjectives, which readily (and perhaps typically) are incorporated into the noun as a suffix ([Wier 2016](Source#cldf:wier2016tonkawa): 31). When an adjective is not incorporated, it can appear in either order, but N-Attr is the most typical (1). Incidentally, when the adjective is incorporated, the order is the same (2) ([Wier 2016](Source#cldf:wier2016tonkawa): 32).

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">no-noto·-n</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">we·ʔis-pax</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">naxc-an-ʔa·-la</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">wixwan-tak</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ye·la-k-laknoʔo</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">RED-touch-GER</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">one-just</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">build.fire-GER-DEF-NOM.SG</span></td>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">small</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-very</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">sit-PART-EVID</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="5"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘A tiny little spark lay [on] just one finger.’</span></td>
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">caka-</span><span style="font-weight:700;font-style:italic;text-decoration:none;color:#000;background-color:transparent">wixwan</span><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">-ʔa·-yʔik</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">river-</span><span style="font-weight:700;font-style:normal;text-decoration:none;color:#000;background-color:transparent">small</span><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">-DEF-ALL</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘the small river’</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-03)
&emsp;**{ NA | PSSR-PSSD | PSSD-PSSR | no dominant order }**

As described in the [What? section](#what), there may be different orders for different possession constructions and/or different noun possession classes. We code for the open class of nouns (sometimes called the alienable class), and if the relative frequencies of available constructions are known, we prefer the most common one. If only information about pronominal possession is available, then this question is coded as unknown &lt;?&gt;.

The state &lt;no dominant order&gt; refers to a single construction which has both orderings or when the grammar explicitly says that two constructions with different orders are equally common or basic. In cases where two different constructions exist for the default class with different orderings of possessor and possessed noun and there is no indication of which is more frequent or basic, we have opted to code this as &lt;?&gt;.

Though the ordering of these constituents is largely determined by the surface structure, there are two particular types of constructions for which we believe &lt;NA&gt; and &lt;?&gt; values are most appropriate. These are constructions in which there is an intervening lexical head between the possessor and possessed nouns: clausal possessive constructions and classifier possessive constructions.

In the rare case where the open class of nouns is possessed through a clausal construction, then the order is coded as &lt;NA&gt;. In this case, the subordinated verb in the construction is an intervening lexical head between the possessor and the possessed noun, which causes the two not to be sister nodes in the syntactic structure. We do not believe that the surface word order of such a construction is meaningfully comparable to constructions where the possessor and possessed are syntactic sisters.

In the case where the open class of nouns is possessed through a classifier construction (where the possessor syntactically possesses a classifier rather than the conceptually possessed noun), there is a potential for the conceptually possessed and syntactically possessed nouns to have different surface orders. For example, in a surface order of PSSD PSSR CLASSIFIER, the order of the possessor and syntactically possessed classifier is &lt;PSSR-PSSD&gt;, but the order of the possessor and conceptually possessed noun is &lt;PSSD-PSSR&gt;. In other cases, the relative order of the possessor with the syntactically possessed and conceptually possessed nouns is the same, as in the order PSSR CLASSIFIER PSSD. We made the analytical decision to encode the former case as a &lt;?&gt; (though no such case was encountered), and the latter according to the order of both syntactically and conceptually possessed nouns (e.g., PSSR-PSSD in the previous example).

#### PSSR-PSSD: Alsea-Yaquina \[alse1251\] (isolate; United States)

Both orders are possible in Alsea-Yaquina possession, but possessors typically occur before the possessed noun, with an agreeing element occuring on the possessed noun ([Buckley 1989](Source#cldf:buckley1989alsea): 22)

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(3)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">a-s</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xámni</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">c-ɬaqúsin-ḵ</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">DEI-REF</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">whale</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">POSS-skin-POSS</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘the whale’s skin’</span></td>
  </tr>
</tbody>
</table>

#### PSSD-PSSR: Nanti \[nant1250\] (Arawakan; Peru)

The possessor in Nanti follows the possessed noun, which receives a possessive prefix, as exemplified below ([Michael 2008](Source#cldf:michael2008nanti): 318, Michael p.c.).

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(4)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">pine</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">Soira</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">ir-ishinto</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">Bikotoro</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">you.see</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Soira</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">3mP-daughter</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">Bikotoro</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="4"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘You see, Soira, BIkotoro’s daughter.’ </span></td>
  </tr>
</tbody>
</table>

## Derived Questions
### [](ParameterTable#cldf:WO-01a)
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
<tbody>
  <tr>
    <td class="tg-1wig">no</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;no dominant order&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">yes</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is anything else</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01b)
&emsp;**{ NA | S>V | V>S }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;no dominant order&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">S&gt;V</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SVO&gt; OR &lt;SOV&gt; OR &lt;OSV&gt; OR &lt;V-last&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">V&gt;S</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;VSO&gt; OR &lt;VOS&gt; OR &lt;OVS&gt; or &lt;V-first&gt; OR &lt;S-last&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01c)
&emsp;**{ NA | S>O | O>S }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;no dominant order&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">S&gt;O</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SVO&gt; OR &lt;SOV&gt; OR &lt;VSO&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">O&gt;S</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;OSV&gt; OR &lt;OVS&gt; OR &lt;VOS&gt; OR &lt;S-last&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01d)
&emsp;**{ NA | V>O | O>V }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;no dominant order&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">V&gt;O</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SVO&gt; OR &lt;VSO&gt; OR &lt;VOS&gt; OR &lt;V-first&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">O&gt;V</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SOV&gt; OR &lt;OSV&gt; OR &lt;OVS&gt; OR &lt;V-last&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01e)
&emsp;**{ V-first | S-first | O-first | no dominant order }**

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
    <th class="tg-1wig">no dominant order</th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;no dominant order&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">V-first</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;VSO&gt; OR &lt;VOS&gt; OR &lt;V-first&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">S-first</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SVO&gt; OR &lt;SOV&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">O-first</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;OVS&gt; OR &lt;OSV&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01f)
&emsp;**{ NA | SVO | SOV }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01e is &lt;O-first&gt; OR &lt;V-first&gt; OR &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">SVO</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SVO&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">SOV</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;SOV&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01g)
&emsp;**{ NA | VSO | VOS }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01e is &lt;S-first&gt; OR &lt;O-first&gt; OR &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">VSO</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;VSO&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">VOS</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;VOS&gt;</span></td>
  </tr>
</tbody>
</table>

### [](ParameterTable#cldf:WO-01h)
&emsp;**{ NA | OVS | OSV }**

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01e is &lt;S-first&gt; OR &lt;V-first&gt; OR &lt;NA&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig">OVS</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;OVS&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-1wig">OSV</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if WO-01 is &lt;OSV&gt;</span></td>
  </tr>
</tbody>
</table>

## Results
As expected, V-initial word orders are dominant in the Pacific Northwest and common in Central America, and VSO is much more frequent than VOS (WO-01). SOV is the most common word order in the sample, with SVO orders more common in California and Oregon, northern Central America, and parts of the Andes and the Gran Chaco. Outside of the more densely-sampled Americas, SVO is especially present in Southeast Asia and Africa. Absence of any dominant order is most frequent in Australia, and occurs with some regularity in the Americas, but without forming clear geographic clusters.

The order of attributive and noun (WO-02) shows clear macroareal patterns, with Asia largely Attr-N and Africa largely N-Attr. North and South America are split: the Pacific Northwest and the Andes largely display Attr-N order; the Amazon largely displays N-Attr order; and Central America has several well-grouped regions displaying each order. The absence of any dominant order is most common in Australia and in South America, especially in the transition region between the Attr-N Andes and the N-Attr Amazon.

The order of possessor and possessed noun (WO-03) is strongly PSSR-PSSD in the sample as a whole, with the PSSD-PSSR order clustering among the Pacific Northwest and Central American languages. These are both regions that are characterized by a V-initial transitive word order (WO-01), although a typological (rather than areal and coincidental) correlation between the two features is not apparent. As with other features, the absence of any dominant order is especially common in Australia, although even there it is a minority state.

## Contributions
**Conceptualization**: [David Inman](Contributor#cldf:DI)

**Data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Nora Muheim](Contributor#cldf:NJM)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP)

**Computer code**: [David Inman](Contributor#cldf:DI)

## References
[References](Source?cited_only#cldf:__all__)

[^1]: This excludes existential (“NP is NP”) and attributive (“NP is Adj”) sentences, which often have special syntax or special marking.
[^2]: The order of the intransitive clause was not investigated because of an overarching concern with feature independence. Rather than collecting both and then attempting to disentangle the dependencies between them, we only collected data on the transitive clause, following prior research emphasizing its importance.