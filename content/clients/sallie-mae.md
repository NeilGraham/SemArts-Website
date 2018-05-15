+++
title = "Sallie Mae"
description = "Test Description"
date = 2018-03-01
template = "about.html"

[extra]
parent = 'clients'

title-image = "images/companies/salliemae.svg"
+++

# SOA Message Generation from Ontology

On a previous project we worked with Sallie Mae to build an enterprise ontology for their loan business. After the ontology was complete, they decided to outsource a new line of loans to a third party SaaS vendor. Shortly after making that decision, they realized that the new system would have completely different screens, and completely different messages and APIs from their existing systems.

Their existing loan servicing systems had, collectively, about 50,000 attributes. The enterprise ontology we had previously designed had 1,500 concepts. They decided to use their ontology as a unifying principle to conform the old and new messages such that their customer-facing systems would not look schizophrenic. They had a mature SOA architecture, but had not done much to unify or rationalize their messages.

We helped them select the DXSI toolkit from Progress Software. We created a set of programs that converted the ontology into a form that DXSI could consume. (There were many issues around translating multiple inheritance to single, and converting many fully-expressed notions from the ontology into flatter representations.)

Much of our work for the remainder of this project involved discovering at a very specific level of detail: exactly what each of the fields in each of the new system's messages actually meant. In many cases this required extensions to the original ontology, but for the most part the extensions were consistent with the original design. In the end we extended the enterprise ontology by only about 10%.

The new system was implemented on time with a set of conformed messages that allowed a single presentation to the customer.

# Enterprise Ontology Development

We were retained by the leading provider of Student Loans to build an Enterprise Ontology.

We conducted over a dozen workshops and facilitated brainstorming sessions and many dozen more one-on-one interviews, and reviewed reams of documentation. In the end we built an Ontology that represented the complexity of their business in just over 1,000 concepts, including classes and properties. This is a dramatic reduction in complexity from the data models of the systems being used to run their business which have far in excess of 50,000 tables and attributes.

The value of this reduction in complexity is a great strategic asset. Going forward, it means that new systems built to conform to the shared model will automatically be in conformance with each other. Integrating existing systems to each other can be done through the lens of the shared ontology, which, besides being much simpler, has the benefit of not being tied to legacy concepts. This truly is building a data bridge to the future.

One of the open questions with something as broad as an Enterprise Ontology is: does it really cover the breadth of the organization and does it have sufficiently granular data to represent all the details that are involved with the many applications that it represents? Our original test case was to be a document management system that was being implemented in parallel with our Ontology. The idea was that if the tags that were going to be implemented in the document management were aligned with the concepts in the ontology that primarily described data in the structured systems, it would then be possible to achieve one of the holy grails in this business: the integration of structured and unstructured data.

Unfortunately, the document management project was cancelled before we could test the theory, but as we describe in another use case, another project came along and provided a different use case: use the Enterprise Ontology as the basis for alignment of SOA messages between legacy systems and a newly outsourced service.

As we describe in the SOA case study, we were able to use the Enterprise Ontology to drive down to field-level detail for the SOA messages. It required about a 20% increase in the core ontology (mostly in creating a bit more detail for specific financial transaction codes and the like) and we added two other lower-level ontologies, one specifically for mapping to the legacy systems, and one to help describe concepts that only occur in the SOA layer (message headers and the like).
