+++
title = "Washington State Department of Labor & Industries"
description = "Test Description"
date = 2018-03-01
template = "about.html"

[extra]
parent = 'clients'

title-image = "images/companies/ws-doli.png"
+++

# Enterprise Referrals Tracking

We were retained by L&I to determine if it was feasible to design and build an **"Enterprise Referral Tracking System."** One of the first challenges was to figure out what constituted a referral. After a few straw man definitions and a lot of polling, we came up with a short list of about 60 different types of referrals, which were being independently managed in over a dozen major, and about as many minor, systems throughout the agency.

The agency already had a great deal of expertise in this particular functionality. Of the dozen or so systems described above with referral tracking functionality built in, three (RTS1, RST2 and RTS3) were explicitly aimed at potentially broad-based referral functionality. It had proved harder than it would sound to grow any of these good starting points into an enterprise-wide system, partly because of best practices and partly because of agile development. The best practices angle was that they had a great deal of experience with traditional application development where it is far easier to build functionality around local database instances. This has the side effect of causing the system to have an increasingly larger footprint of shared concepts with the rest of the agency to support what was essentially MDM functionality. The agile problem emerged because inevitably one program had been funded to create the RTS system and their needs were driving other projects throughout the agency. Because there was no guard, any additional functionality that the program needed, if it were at all related to referrals, was added to the scope. Often these additions were an impediment rather than an aid in getting other programs to adopt the system.

We designed a truly elegant system. The cost to build it was estimated at about 10% of the initially expected cost. As it turns out, the entire project will cost more than that, but still less than half what they had originally thought because most of the effort is in integrating legacy systems through SOA messaging. Since they have the necessary resources in-house, the incremental costs are far less.

This was another on- time, on-budget project with a much better outcome than had been anticipated at the outset.

# Redesigning Locations and Entity Identity

We were retained to help with this two pronged project. One prong was to create a feasibility study to determine whether collecting additional data from employers would aid in targeting workplace safety inspections.

The other half of the project was to do a high-level redesign and feasibility study on how they were tracking addresses and business locations in their many applications. It turned out that there were nearly 100 different places in applications where location and address were being maintained. This was a major issue as they were embarking on an initiative to provide customer self-service to many functions. The multitude of end points for potential address change was daunting.

Through an ontological design, we first helped them clarify the differences between a work location, a work site and an address. We also created a high level design that accommodated the many different needs for addresses and locations without being overly burdensome.

# SOA Design

The long range plan at L&I called for organizing their future application initiatives around shared services and shared messages on a message bus.

In this project we created detailed requirements specs for the dozen major shared services and created an inventory of the key messages they would need to form the backbone of their SOA.

One of the interesting early wins was with their Accounts Receivable system. They had just started an AR project, and we convinced them to think of AR as a service rather than an application. They had discovered that 23 of their 200 applications had implemented AR functionality and this project was intended to rationalize this. The pilot application to be converted (Claims Overpayment) wanted to implement an AR message that was highly specific to Claims Overpayment, and therefore would not be reusable. This was contrary to the idea we were promoting of reusable messages.

We did a bit of semantic modeling to find the commonalities and differences, and constructed a common message that had variable payloads for the few fields that really needed to be specialized for each case. On a follow up visit several years later, they reported they have successfully converted all 23 of the satellite AR functions, which has provided benefits including consistent revenue reporting and a single place to check to see if someone owes the Agency money before they pay them from their Accounts Payable systems.

# Shared Security Services

L&I, like most organizations, has implemented security separately for each of its applications. The more applications you get, the more redundancy is introduced, and the more likely it is that you are inconsistently applying the law and your own internal policy.

We began this project with an exercise we called the "exegesis." In this case it was an exegesis of all the laws, regulations and policies that applied to data security within the Department. In addition to a lot of reading and excerpting, this required semantic analysis, as each of the laws had a different aspect. Some of the laws (such as HIPAA) discuss patients' rights. A special subclass of workers, injured workers who have been treated by medical professionals, are patients under this definition. There were dozens of such nuanced distinctions.

From this we constructed a set of rules that needed to be implemented in order for the applications to comply. This was also at a time when the State was beginning to open up its system to the general constituency, and therefore the number of users was about to go from 3,000 mostly internal users to up to 3,000,000 total users (workers, employers, and providers in the State).

We built a set of requirements and brought in all the usual security software suspects. At the time, the business models of these companies did not allow them to separate Authentication from Authorization (they priced their products based on number of authenticated users). However, the State was mandating the use of its own Authentication service. We found no vendor who could solve the Authorization requirements we had without including a redundant Authentication service. While we were disappointed, one of the analysts on this project was elated. "In the past we would have selected one anyway and dealt with the fact that couldn't handle our requirements separately."

As a result of our findings, we designed a custom shared security service, which was then let to an implementation company in a competitive bid. In our original design the service would have relied on a rules engine to evaluate the authorization rules. Perhaps because we had done such a good job on the exegesis and significantly reduced the number of rules, the implementation team hard coded the rules. The service has been in use for over five years; all new applications use it, and existing systems are being retrofitted to it.

# Web Facing Services

One of the shared services we designed in the L&I long-term plan was "Web Facing Services."  When it came time to implement this they asked us to help them define the requirements and select a software product on which to base the service.

Our original concept featured a service that would consume SOA messages off their message bus and compose them into a browser. (This was essentially the design of a mash up service, long before the term had been coined.) We created a set of requirements and helped them select and configure the Plumtree product (which was essentially a portal product) to do what we intended.

# Long-Range Systems Plan

Our first project with Labor & Industries started as an investigation of what dependencies their many applications had on technology that might become technically obsolete, thereby putting them at risk.

We did this, and developed a high-level conceptual model, "as-is" architecture and a detailed dependency diagram that revealed many deep and subtle risks to their system.

We were then retained to construct their long-range vision and strategic plan. This was the first time we had built an information system plan with a ten-year duration, but this was what was appropriate. They have been working toward this plan, with adjustments as things change, ever since.

"Semantic Arts were crucial to helping us define and stick to our Service Oriented Architecture plan and implementation. They have been pleasure a to work with; and always had our interests and capability foremost in their minds. I wouldn't hesitate recommending them for any task, particularly those that are design intensive."

-Shelagh Taylor
Deputy Director [CIO]
Washington State Department of Labor & Industries
