+++
title = "Washington State Secretary of State"
description = "Test Description"
date = 2018-03-01
template = "about.html"

[extra]
parent = 'clients'

title-image = "images/companies/ws-sos.png"
+++

We were engaged to perform a **feasibility and requirements study** for the Corporations and Charities Division of the Office of the Secretary of State. In our proposal we included developing a semantic model to help clarify the requirements. Another key part of the requirements was to examine some 2,000 individual statutes to identify any rules embedded in the laws and determine if they would need to be reflected in the new system.

If we had any regrets it was that we hadn't done the semantic work earlier. We believe that the explosion of schema complexity is a product of scale; most of our large clients have severely stove-piped systems which lend themselves to high levels of redundancy. Our other operating hypothesis is that the widespread adoption of packaged systems is another major contributing factor to schema bloat. But we found the same level of schema complexity at the SOS, where the scope was small and there were no packages implemented.

Their existing systems, which were still highly paper- and manual workflow-intense, were supported by four databases which consisted of 250 tables and 3,000 attributes (columns). We built a semantic model that unambiguously defined all their key concepts, and then reduced it to a model they could implement with relational technology.  (Due to the language in the RFP we were precluded from doing the implementation and they were not ready to do a semantic implementation on their own.) The relational version of their new system was completely on line and had more functionality than their existing system, and had only 20 tables and 110 unique attributes. This was a more than 25-fold reduction in complexity, and was instrumental in their decision to build a custom system.

We say we wish we could have done the semantic model first (there were other factors that dictated our sequencing) because, had we known how simple the semantic model would be, we would have been able to do the statute-to-rule exegesis straight to the semantic model terms. The extra effort we introduced with interim terms far exceeded the effort we spent in building the semantic model.

The project finished on time and in budget, and they are now working on User Experience, which they would like to solidify before they begin the build in earnest.
