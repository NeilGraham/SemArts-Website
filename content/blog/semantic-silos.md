+++
title = "Enterprise Ontology, Semantic Silos, and Cowpaths"
description = "Use an enterprise ontology to avoid the trap of paving over your siloed information systems with semantic technology"
date = 2017-07-12
path = "blog/semantic-silos"
template = "about.html"

[extra]
  parent = 'read'

  author_id = "michael_uschold"
  show_date = True
+++

## Paving cow paths

&nbsp;&nbsp;&nbsp;&nbsp;
Numerous modern day streets in downtown Boston defy logic – until you realize that the city fathers literally paved over the transit system created and used by cows.*  This gave the immediate benefit of getting places faster, while losing out on longer-term gains that designing a purpose-built street plan could have yielded.  This type of thing is pervasive in today’s enterprise ranging from computerizing paper forms to the plethora of information silos – the subject of today’s blog.

![Figure 1: Paving the cowpaths in Boston**](../../images/blog/semantic-silos/figure1.png)

## Semantic technology

&nbsp;&nbsp;&nbsp;&nbsp;
Semantic Arts works with a wide variety of companies and, unlike just a few years ago, it is now common for our new clients to already have a number of efforts and groups exploring semantic technology in-house.  Gone is fear of the ‘O word’. In its place are a range of projects and activities such as creating ontologies, working with triple stores, and creating proofs of concept. Unfortunately, what we see very little of is coordination of these efforts throughout the enterprise.

&nbsp;&nbsp;&nbsp;&nbsp;
It would be mistaken to regard this as a misuse of the technology, because point solutions will often result in significant benefits locally – just like paving cow paths gave immediate gains. It’s more a missed opportunity in the form of a great irony. The very technology designed to break down silos gets used to build yet more silos – Semantic Silos.

![Figure 2: Avoid Semantic Silos](../../images/blog/semantic-silos/figure2.png)

&nbsp;&nbsp;&nbsp;&nbsp;
Building semantic silos is an easy trap to fall into, because it takes a while to fully comprehend the power of semantic technology (or any other disruptive technology).  Information silos arise for many reasons, both technological and organizational.  Key technological factors include the inability of relational databases to (1) reuse schema and (2) uniquely identify data elements globally across databases.  That’s where the URI and RDF triples come in. It is hard to overstate the power of the URI in semantic technology. URIs uniquely identify not only data elements but also the schema elements. The former eliminates the need for joins, and the coordination of URIs makes the snapping together of disparate databases, well, a snap.  The latter enables something entirely foreign to relational technology: the ability to easily share and reuse all or parts of existing schema.

## Enterprise ontology

&nbsp;&nbsp;&nbsp;&nbsp;
The key to avoiding semantic silos is to use an enterprise ontology, which is a small and elegant representation of the core concepts and relationships in your enterprise that are stable over time.  It is at the same time both a conceptual model, and a computable artifact that plays the role of a physical data schema. The enterprise ontology is a foundation for building more specialized ontologies that are loaded into dozens, hundreds or thousands of graph databases, called triple stores that are populated with data.  Data elements are also shared across multiple databases.  This is depicted in figure 3.

&nbsp;&nbsp;&nbsp;&nbsp;
These stores can be used by many applications, not just one or two, as is common in today’s siloed, application-centric enterprise.  Collectively, these ontologies and their data form an enterprise knowledge graph. Such graphs are hugely important for modern companies such as Google, Facebook and LinkedIn.

![Figure 3: The triple stores depicted in the top row are not silos. Globally unique URIs snap together to form a single enterprise knowledge graph that is accessible using federated SPARQL queries.  Letters denote ontology URIs and numbers denote data URIs.](../../images/blog/semantic-silos/figure3.png)

&nbsp;&nbsp;&nbsp;&nbsp;
Having built enterprise ontologies now in a variety of industries, we are confident in stating the surprising result that there are only a few hundred such concepts that form this core for any given enterprise.  This is what makes it possible to build an enterprise ontology, where building enterprise-wide data models has failed for decades. There is no need to have millions of attributes in the core model.

## Summary and conclusion

1. It is entirely possible to use semantic technology to develop point solutions around your enterprise and unwittingly end up recreating the very silos that semantic technology aims to get rid of.
2. We see this happening in organizations that are using semantic technology.
3. You don’t want to do that, you will miss out on some of the main benefits of the technology. The data will not snap together if there is no coordination.
4. The answer is to use an enterprise ontology as a core data model that is shared among all the applications and data stores that collectively make up your enterprise knowledge graph.
5. The URI is the hero: they are globally unique identifiers that allow seamless sharing of data and schema, joins are history.

&nbsp;&nbsp;&nbsp;&nbsp;
Keep in mind that technology as enabler is only part of the story. To get real traction in breaking up silos also requires meeting plenty of social and organizational challenges and putting governance policies into place.  But that’s another topic for another day.

Don't fall in the trap of paving the cow paths to semantic silos. Use an enterprise ontology to create the beginning of an integrated enterprise.

## Afterward

See also the delightful and well-known poem by S.W. Foss called, ["The Calf Path".***](***)

---

\* Change Management: Paving the Cowpaths

[https://www.fastcompany.com/1769710/change-management-paving-cowpaths](https://www.fastcompany.com/1769710/change-management-paving-cowpaths)

\*\* Picture credit:

[http://bostonography.com/2011/cartographic-greetings-from-boston/bostontownoldrenown/](http://bostonography.com/2011/cartographic-greetings-from-boston/bostontownoldrenown/)

\*\*\*

[https://m.poets.org/poetsorg/poem/calf-path](https://m.poets.org/poetsorg/poem/calf-path)
