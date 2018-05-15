+++
title = "Investment Bank"
description = "Test Description"
date = 2018-03-01
template = "about.html"

[extra]
parent = 'clients'

title-image = "images/companies/investmentbank.svg"
+++

# Resolution Planning

This is one of the “too big to fail” banks, who are required by regulators to have a “resolution plan” or as it’s known on the street a “living will.” The first few generations of resolution plan were long on long textual descriptions of the nature of the interactions between various legal entities within the bank.

Our sponsor recognized that the key to making a resolution plan workable is to make it data driven rather than document driven. Document driven resolution plans are out of date as soon as they are written, and require humans to read and interpret. While the firm, as with most large financial services firms, consists of thousands of legal entities, there are “only” a few dozen that are significant from a resolution standpoint. However, this is made more complex because any of hundreds of departments may and do have service relationships with their peers in other countries and timezones. Often these arrangements are tacit rather than spelled out, and even those that are written fall far short of the regulators desire to see specific mechanisms for controlling the work and assuring it gets completed.

We based this project around the concept of Inter-affiliate Service Level Agreements. We designed an ontology of Service Level Agreements and in the course of four months iterated it through 8 versions as we learned more and more about the specifics of getting a new system designed and built.

In addition to, and in parallel with the ontology development we built an operating system, using our model driven development environment. We populated a triple store with data sourced from many of their existing systems (HR for personnel and departments, finance for legal entities and jurisdictions, IT for applications, hosting and data centers and the activity taxonomy from the project we had performed the previous year. On top of this we built user interfaces that allowed managers to document the agreements that were in place between themselves and other departments in other legal entities.

We completed the project in time to demo to the regulators and is now being used as the basis for their go forward Resolution Plan.

# Risk and Controls

This investment bank is required by regulators to assess the adequacy of their controls on a quarterly basis. This is a very labor intensive process, as there are more than 5,000 controls that have to be assessed independently.

In the process of building an ontology of financial risks and controls, we discovered that while everyone “knows” what risks and controls are, the act of creating formal definitions for these core concepts shone a light on the fact that there were multiple definitions of risk and control that were being used interchangeably. We were able to build a very rigorous ontology in the area, and gained agreement on what all their terms meant, and how they mapped to current concepts.

As far as we know they haven’t yet incorporated this into their evaluation systems, but they have the materials they need to should they choose.

# Economic Architecture

We worked with a large investment bank who are embarking on a series of projects to further automate their back office. One of their first tasks was to understand in greater detail what all the 5,000 people in the back office were doing. They built an “Economic Architecture” that was essentially the equivalent of a continually running Activity Based Costing project. They asked managers to estimate the percentage of time each of their reports spent on a standard list of activities. However the activity list was not stabilizing, and many managers had difficulty deciding which of the many activities they should use. As this was slated to eventually become part of the reporting and perhaps eventually the charge back to the front office for the activities performed to settle some of these very complex instruments.

We were called in to create a rational basis for the activity taxonomy. We ended up decomposing the working list of 800 or so activities into a set of orthogonal facets. What was fascinating was that the facets were far, far simpler than the long complex list of activities. Once someone knew the facets (such as financial product, market, as well as a simple set of verbs and modifiers) they would know what all the activities were, as they were just concatenations of the facets. More interestingly we discovered as we performed this that the facets provided a level of categorization that it would be possible to instrument in the work flow and source systems. (The list of 800 activities were too arbitrary to allow for automation, but he facets were closely aligned with primitive concepts found in most systems).

We completed the redefinition, and got agreement on the new activities. The new activities are in production and they are looking at applying this concept beyond the back office operations.
