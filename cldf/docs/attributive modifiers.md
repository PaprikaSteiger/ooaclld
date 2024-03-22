**Authors**: [David Inman](Contributor#cldf:DI)

**Acknowledgements**: [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Nora Muheim](Contributor#cldf:NJM)

[TOC]

## What?
This questionnaire is about the syntactic category of attributive modifiers, and data was collected simultaneously with the [Word Order](WO) questionnaire. “Attributive modifiers” (or as we will sometimes call them “attributives”) is a cross-comparative category meant to encompass whatever word class is most typically (or dedicatedly) used to modify nouns non-predicatively in phrases like ‘a **nice** house’. The attributive stem, outside of its use as a nominal modifier, may behave as a verb, a noun, an adverb, or it may be its own category that does not behave like other parts of speech (“adjective”).

The conceptualization of this feature arose out of a potential theoretical problem with the formulation of “adjectives” in [Dryer (2013)](Source#cldf:dryer2013wals87), which has been largely repeated in the current survey in feature [WO-02](WO). This definition of “adjectives” (for which we have used the term “attributive”) compares proper classes of adjectives with attributive verbs. Although [Dryer (1992: 96)](Source#cldf:dryer1992wordorder) does not find that adjective-noun ordering follows verb-object ordering on a global scale, he nevertheless states that it is possible that the order might correlate with nouns and relative clauses, for languages that use verbs for nominal attribution. We did not collect data on the order of nouns and relative clauses, but it is still possible that straightforward data about attributive order, without category information, hid either feature dependency or a separate areal pattern. We thus collected data about the part of speech category of attributive modifiers.

The problems with assuming pre-existing cross-linguistic grammatical categories has been widely discussed, especially in recent years (see [Haspelmath 2019](Source#cldf:haspelmath2019comparative)). The present questionnaire still assumes the minimal presence of two parts of speech in every language, namely “nouns” and “verbs”, which are roughly the lexical and syntactic correlates of semantic *entities* and semantic *events*. This minimal distinction, even if challenged for a few ambiguous cases, has always been confirmed under detailed scrutiny ([Jacobsen 1979](Source#cldf:jacobsen1979noun), [Hess and van Eijk 1985](Source#cldf:hess1985noun), [Evans and Osada 2005](Source#cldf:evans2005mundari)). This questionnaire thus asks if attributive modifiers form a distinct class that can only be used to modify nouns (an “adjective” class), a distinct class that can be used to modify both nouns and verbs (a “modifier” class), or if they remain inseparable from the noun class or the verb class. A few other special edge cases are discussed in Attr-01 below. In addition, we have tracked whether the dedicated adjective class, if there is one, is an open or closed lexical category.

## Why?
The areality of the lexical classes of attributives is not well-established in the literature. However, it has been occasionally noted that some languages lack a special category of adjectives because they are verbal (true for much of North America, [Mithun 2001](Source#cldf:mithun2001languages): 56). This questionnaire was designed to investigate a possible relationship between part of speech categories (Attr-01) and the ordering of noun and attributive (WO-02), as well as whether there is a larger pattern to this syntactic categorization on its own.

## How?
In some cases, it is difficult to decide whether a language truly has a small, closed class of adjectives (and uses verbs or nouns as nominal attributives), or if the language has no adjectives at all. The expectation from previous linguistic research ([Dixon 2004](Source#cldf:dixon2004adjectives): 3-4) is that a small class of adjectives consists largely of dimension, age, value, and color semantics. If the potential class of adjectives is very small and does not conform to this expectation, or if it only consists of elements which could be understood as grammaticalized (e.g. adjectives ‘big’ and ‘small’ could be in fact augmentative and diminutive morphemes), or morphemes which may belong to a non-adjectival category (e.g. adverbs), then the determination becomes even more difficult. In such cases, we have only coded an adjective class if the nature of the class is beyond dispute: either because it contains the expected semantic categories, or because its members cannot reasonably be interpreted as belonging to another lexical category.

For instance, Seri \[seri1257\] (isolate; Mexico) could be argued to have a small category of adjectives. The two terms of this category, namely ‘small’ and ‘crazy’, do not require the subject nominalizer *k-* to be used attributively and they are analyzed as “defective verbs” in the grammar ([Marlett 1981](Source#cldf:marlett1981seri): 128; [Marlett 2005](Source#cldf:marlett2005seri): 67). Outside of this small set, attributives are unambiguously verbs with a nominalized subject. We considered Seri to have a verbal attributive category, since only ‘small’ belongs to the expected semantics (for more details see Attr-01 below).

## Features
### [](ParameterTable#cldf:Attr-01)
&emsp;**{ adjective | modifier | adverb | noun | verb | predicative only }**

As described in the [“What?” section](#what), the possible syntactic categories are determined by reference to the noun and verb categories, which we assume to be distinguishable for every language.

An &lt;adjective&gt; category is one whose members can be freely used to attributively modify nouns (but not verbs) and are somehow differentiated from both nouns and verbs. The exact type of this differentiation is language-dependent and cannot be universalized, but common points of differentiation are inflection for gender, case, or number (which may be shared with nouns), the lack of possible inflection for tense, aspect, and mood, the possibility of comparative and superlative morphology (which is often unique to the class of adjectives), the obligation of a copula when used as predicates, and so on. This category may be open or closed (as is addressed in Attr-02), and if a closed adjective class is present, &lt;adjective&gt; is the value chosen, rather than the open class. However, a closed category of adjectives must contain multiple members with different property concept semantics, and cannot be a very small set of a handful of highly grammaticalized and semantically broad particles (such as diminutive and augmentative; see the complex case of Hixkaryana below).

A &lt;modifier&gt; category is one whose members can be freely used to attributively modify both nouns and verbs (i.e. they serve both the adjectival and adverbial functions). In some cases, modifiers can serve both functions without modification, and in others they are marked overtly for adjectival vs adverbial use.

An &lt;adverb&gt; category is one whose members are by default adverbs, and their adjectival use strictly requires derivational morphology. Only one such case was encountered, Trió, exemplified below.

A &lt;noun&gt; category signifies that there is no syntactic differentiation between attributive nominal modifiers and nouns themselves.

A &lt;verb&gt; category signifies that there is no syntactic differentiation between attributive nominal modifiers and verbs as a lexical category. We do not distinguish among the syntactic requirements for the verb category to be used attributively. There are a variety of ways a language may mark verbs in their attributive use case: the use of an overt relative pronoun and a subordinate clause (e.g., *the dog **who** is-big*), some dedicated derivational or inflectional morphology marking the verb as attributive, or verbs may be used attributively with no marking whatsoever. This question does not distinguish between these syntactic requirements, but only encodes the lexical category of the attributive modifiers. When sources described a subordinate clause, this was entered into the remarks.

The &lt;predicative only&gt; category indicates that property concepts are only expressed predicatively, and cannot attributively modify a noun within a noun phrase. In such languages, it is not possible to create phrases such as *the red house*: the semantics of ‘red’ must always be expressed predicatively, either in a clause in which ‘red’ is the sole predicate (‘it is red’), or by adding the concept property to the main predicate, e.g. through affixation.

#### adjective: Nanti \[nant1250\] (Arawakan; Peru)

Nanti has a class of approximately 25 underived adjectives, which differ from the open class of (morphologically-derived) verbal attributives by manifesting (sometimes highly irregular) agreement with their head noun ([Michael 2008](Source#cldf:michael2008nanti): 311). Some adjectives can also participate in noun incorporation.

#### adjective: Bauni \[wara1302\] (Sko; Papua New Guinea)

Although described as a subclass of verbs on account of their ability to be used predicatively with verbal morphology, the adjective class in Bauni can appear pre-nominally in a noun phrase, without inflection, in which case they are interpreted as attributively modifying the head noun, or can serve as the head of the NP ([Corris 2006](Source#cldf:corris2006grammar): 112,142-143). They can also be used predicatively, but this syntactic behavior distinguishes them from other verbs. Another analysis could even fully separate the two categories, simply stating that adjectives take verbal morphology when being used predicatively. On the basis of this differentiation, we treat the attributive class in Bauni as forming its own category. Both predicative and attributive uses are given for *páko* ‘big’ in (1) and (2) below, from [Corris (2006: 112)](Source#cldf:corris2006grammar).

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">K-a-páko</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">RL-3SG.M-big</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘He is big.’</span></td>
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">rau</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">páko</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">nění</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">pig</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">big</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">1SG.F</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘my big pig’</span></td>
  </tr>
</tbody>
</table>

#### adjective: Eyak \[eyak1241\] (Athabaskan-Eyak-Tlingit; United States)

There is a small, closed class of 13 to 20 attributives in Eyak which attach suffixally to nouns, with the rest of the semantic space of attribution being handled through the relativization of verbs ([Krauss 2015](Source#cldf:krauss2015eyak): 546). Though it is unusual that these forms are bound, they are nevertheless restricted to modifying nouns, so we count them as an adjective part of speech. An example of one of these suffixes is *-dzu*: ‘good’, which can incorporate in a word like *XAwa:dzu:* ‘good dog’.

#### modifier: Pirahã \[pira1253\] (isolate; Brazil)

[Everett (1986: 272-275)](Source#cldf:everett1986piraha) states explicitly that there is little ground on which to separate adjectives from adverbs, as generally speaking the same class of words can modify either nouns or verbs. This is exemplified for the modifier *xaibogí* ‘fast’, repeated below. Though this particular adjective can also be used adverbially in English, it is a small category of the English adjectives which can be used to modify verbs, while in Pirahã it is apparently the rule.

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
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xaoói</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xaibogí</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">gáihi</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">foreigner</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">fast</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">that</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="3"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘That fast foreigner’ or ‘That is a fast foreigner.’</span></td>
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
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">(4)</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">xaibogí</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:italic;text-decoration:none;color:#000;background-color:transparent">áp-a-áti</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">fast</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">go-REMOTE-UNCERT</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent"> </span></td>
    <td class="tg-0lax" colspan="2"><span style="font-weight:400;font-style:normal;text-decoration:none;color:#000;background-color:transparent">‘Go fast.’</span></td>
  </tr>
</tbody>
</table>

#### modifier: Esselen \[esse1238\] (isolate; US)

A single class of lexical stems in Esselen may be used adjectivally, with the suffix *-ki*, or adverbially, with the suffix *-wa*, as seen in the pair *sale-ki* ‘good’ ～ *sale-gua* ‘well’ ([Shaul 2019](Source#cldf:shaul2019esselen): 101-102). Though Shaul describes the adverb class as derived from adjective stems, both adjectival and adverbial uses require affixal morphology, so we categorize Esselen attributive modifiers as an undifferentiated &lt;modifier&gt; class.

#### noun: Thayore \[thay1249\] (Pama-Nyungan; Australia)

[Gaby (2006: 78)](Source#cldf:gaby2006kuuk) groups all generic nouns, specific nouns, adjectives, and quantifiers into a single category of “nomens”, following the work of Wilkinson (1991). Some members of this category have semantics which lend themselves more easily to modification or classification. In the words of [Gaby (2006: 283-284)](Source#cldf:gaby2006kuuk), “The parts of speech ‘generic noun', ‘specific noun' and ‘adjective', then, are constructional, coming into being only in the noun phrase.”

Although Thayore has in general a great degree of freedom between attributive and noun uses of lexical items, there are some lexemes which change their meaning depending on their use as a noun or an attributive. An example discussed in [Gaby (2006)](Source#cldf:gaby2006kuuk) is the word *wang*, which means ‘white’ when used attributively, and refers to ghosts or spirits when used nominally. Gaby nevertheless considers nouns and adjectives to be members of the same category *nomen*, and suggests that perhaps some lexemes simply have polysemous meanings. We follow her analysis and consider attributives in Thayore to be lexical nouns.

#### verb: Seri \[seri1257\] (isolate; Mexico)

As discussed above, [Marlett (2005: 54)](Source#cldf:marlett2005seri) does not include an adjective category when describing Seri, because “they are such an unusual category in the language” and the small set of terms that may be adjectives “could be argued \[to be\] morphologically-deficient verbs” ([Marlett 2005](Source#cldf:marlett2005seri): 67). The “deficient” nature of this small category is the fact that some lexemes, namely ‘small’ and ‘crazy’ do not require the subject nominalizer *k-* to be used attributively ([Marlett 1981](Source#cldf:marlett1981seri): 128). Beyond these, a further two words, ‘imitation; kind of’ and ‘another’ are totally inflectionless (thus behaving neither like verbs nor nouns), but they clearly derive from a reduced nominalized verbal phrase. We thus do not consider these to be adjectives either, but a sort of particle (akin to the cliticized use of English *-ish*). Outside of this small set, attributives are unambiguously verbs with a nominalized subject. This attributive category is thus categorized as verbal, with a remark about the nominalized subject.

#### predicative only: Ese Ejja \[esee 1248\] (Pano-Tacanan; Bolivia, Peru)

Property concepts are expressed via a dedicated part of speech (adjective/adverb), which constitute an open class of about 100 lexemes, and are overwhelmingly used predicatively. For predicative adjectives to modify a noun, there are three strategies:

1. the most frequent is **noun incorporation into adjectives**, *kia-sapa-kemo* 'he has a big head', literally he is big-headed, i.e. only a 'sort of' attributive construction since it is really a predicative construction incorporating a noun;
2. **Noun juxtaposition/zero-relativization**, where Vuillermet (p.c. 2023) believes the adjective and the noun words to belong to distinct constituents, because of the intonation pattern, literally the equivalent of ‘the person (which is) big’;
3. **explicit relativization**, just like verbs can modify nouns.

Property concepts modify Nouns so rarely that most examples didn't occur in the corpus and were elicited, and the text examples were mostly 1) lexicalized (big-tooth ‘agouti (rodent sp.)’, 2) derived NPs (bag-white-ADJVZ) ([Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 323-326). The adjective/adverb roots form compounds with nouns and seem to be used attributively to create proper nouns (and/)or insults, like ‘head-big’ ([Vuillermet 2012](Source#cldf:vuillermet2012eseejja): 311).

The absence of nominal attributive modification is consistent with our category &lt;predicative only&gt;.

#### predicative only: Hixkaryana \[hixk1239\] (Cariban; Brazil)

Hixkaryana has a small set of “modifying particles”, but their semantics are extremely vague and highly grammaticalized or quantificational: *heno* ‘dead (late); a big amount’, *komo* ‘collective’, *tho* ‘devaluated (including old)’, *txko* ‘diminutive (small or hypocoristic)’, and *ymo* ‘augmentative (big or pejorative/bad)’ ([Derbyshire 1985](Source#cldf:derbyshire1985hixkaryana): 245-247). Each of these particles has extremely broad semantics or is quantificational in nature. We thus consider them to have largely grammatical rather than lexical (and property concept) semantics, and have **not** considered Hixkaryana to have a closed class of adjectives.

Property semantics that go beyond this set of grammaticalized and quantificational meanings are done through the nominalization of adverbial roots; however, they are always used predicatively, and not attributively ([Derbyshire 1985](Source#cldf:derbyshire1985hixkaryana): 234-235).
 

### [](ParameterTable#cldf:Attr-02)
&emsp;**{ NA | closed | open | open but }**

This question targets whether a language has a closed or open category of nominal attributives (&lt;adjective&gt; or &lt;modifier&gt;, as defined in Attr-01). Though a rare category, &lt;modifier&gt; is included with &lt;adjective&gt; because it is also a special lexical class which is syntactically marked as a modifier of nominals (just not *only* nominals). Many languages have a limited number of adjectives, and use other parts of speech (often verbs) for other attributive properties. If the adjective class was not mentioned in sources as being a limited set, we assumed during coding that the category was open. When coding for this feature began, we intended to collect data about where non-adjectival attributives came from, if the adjective category was closed. However, most linguistic resources do not provide this information, and so this question was abandoned.

In addition to having a small, closed category of adjectives, a language can have two adjective categories: one of which is closed, and one of which is open. In such languages, it is meaningful to refer to the adjective category as split into an open category and a closed category. An example of such a language is French \[stan1290\] (Indo-European; world), where a small class of adjectives occur before the noun they modify (mostly adjectives referring to the semantics of age, size, and sometimes value), while the much larger, open class of adjectives occur after the noun they modify. This is a mixed state, which we have called &lt;open but&gt;.

#### closed: Nanti \[nant1250\] (Arawakan; Peru)

As mentioned under Attr-01, Nanti has a small category of about 25 true adjectives (‘large’, ‘small’, etc), which is opposed to a productive process of derivation from verbs (‘be red’, ‘be sour’, etc) ([Michael 2008](Source#cldf:michael2008nanti): 310-318). 

#### open: Bauni \[wara1302\] (Sto; Papua New Guinea)

The adjective class in Bauni, which are called a subclass of verbs in [Corris (2006: 112-115)](Source#cldf:corris2006grammar), appears to be an open category, as no limitation on its membership is discussed or mentioned by Corris.

#### open but: Basque \[basq1248\] (isolate; Spain, France)

Like French (and Spanish), Basque has a large, open class of adjectives which syntactically follow the head noun, but a minority of specific adjectives (‘other’, ‘right’, ‘left’, ordinals, nationality and religious terms) either may or must precede the head noun, with a preference for preceding it ([Hualde and Ortiz de Urbina 2003](Source#cldf:hualde2003basque): 138-139). Since this is a kind of subcategorization within the adjective class, with open and closed sub-domains, Basque receives the encoding &lt;open but&gt;.


### [](ParameterTable#cldf:Attr-03)
&emsp;**{ NA | Adj-N | N-Adj | No dominant order }**

This question only applies to languages which have two categories of adjectives. Sometimes, when this is the case, the closed class and the open class have different orders. The value of this question can be compared with [WO-02](WO), which captures the word order for the open adjective class (if there are two).

#### Adj-N: Basque \[basq1248\] (isolate; Spain, France)

As explained above, the closed adjective class in Basque allows for both the normal order of N-Adj, as well as a preferential ordering of Adj-N ([Hualde and Ortiz de Urbina 2003](Source#cldf:hualde2003basque): 138-139). We code the preferred ordering for this closed class.

## Derived Questions
Derived questions offer different views of the same data included in the base questions. Often, this is done to group together some states of multi-state questions, to capture specific similarities. In other cases, derived questions are designed so that they are independent from other questions used in the same computational analyses that assume feature independence,  e.g. the Bayesian software sBayes, which detects areal signal ([Ranacher 2021](Source#cldf:ranacher2021sbayes)).

### [](ParameterTable#cldf:Attr-01a)

<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:5px 5px;
  word-break:normal;}
.tg th{border-style:solid;border-width:0px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:5px 5px;word-break:normal;}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg dconversion">
<thead>
  <tr>
    <th class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none">modifier pos</span></th>
    <th class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Attr-01 is &lt;adjective&gt; AND Attr-02 is &lt;open&gt; OR &lt;open but&gt; </span><br>OR if Attr-01 is &lt;modifier&gt;<br><span style="font-weight:400;font-style:normal;text-decoration:none">OR if Attr-01 is &lt;adverb&gt;</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none">noun</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Attr-01 is &lt;noun&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none">verb</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Attr-01 is &lt;verb&gt;</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700;font-style:normal;text-decoration:none">NA</span></td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal;text-decoration:none">if Attr-01 is &lt;predicative only&gt;</span></td>
  </tr>
</tbody>
</table>

## Results
As noted in [Mithun (2001: 56)](Source#cldf:mithun2001languages), the use of the verb category for attributives (Attr-01) is especially common in North America, but we find that this is to the exclusion of Central America. Verbal attributives are also common in the Amazon, and possibly in East Asia, although our sampling is not dense enough to confirm the latter. The use of the noun category for attributives is most frequent in Australia and in Peru, the latter of which includes the Quechuan and Aymaran families.

The presence of a closed class of adjectives (Attr-02) is common on the eastern side of the Andes. Two classes of syntactically distinct adjectives, one open and one closed, are uncommon in our sample, but occur most often in Central America and in the Uto-Aztecan family.

We did not uncover any relationship between part of speech categories (Attr-01) and the ordering of noun and attributive (WO-02).

## Contributions
**Conceptualization**: [David Inman](Contributor#cldf:DI)

**Data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP), [Marine Vuillermet](Contributor#cldf:MV), [Nora Muheim](Contributor#cldf:NJM)

**Supervision of data collection**: [David Inman](Contributor#cldf:DI), [Natalia Chousou-Polydouri](Contributor#cldf:NCP)


## References
[References](Source?cited_only#cldf:__all__)
