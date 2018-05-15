+++
title = "A Tale of Two Projects"
description = "A Tale of Two Projects, excerpt from \"Software Wasteland: How the Application-Centric Mindset is Hobbling Our Enterprises\""
date = 2018-02-28
path = "blog/tale-of-two-projects"
template = "about.html"

[extra]
  parent = 'read'

  author_id = "dave_mccomb"
  show_date = True
+++

&nbsp;&nbsp;&nbsp;&nbsp;
If someone has a $100 million project, the last thing that would occur to them would be to launch a second project in parallel using different methods to see which method works better. That would seem to be insane, almost asking for the price to be doubled. Besides, most sponsors of projects believe they know the best way to run such a project.

&nbsp;&nbsp;&nbsp;&nbsp;
However, setting up and running such a competition would establish once and for all what processes work best for large scale application implementations. There would be some logistical issues to be sure, but well worth it. To the best of my knowledge, though, this hasn’t happened.

&nbsp;&nbsp;&nbsp;&nbsp;
Thankfully, the next best thing has happened. Luckily, we have recently encountered a “natural experiment” in the world of enterprise application development and deployment. We are going to mine this natural experiment for as much as we can.

&nbsp;&nbsp;&nbsp;&nbsp;
President Barack Obama signed the Affordable Care Act into law in March 23, 2010. The project was awarded to CGI Federal, a division of the Canadian company, CGI, for $93.7 million. I’m always amused at the spurious precision the extra $0.7 million implies. It sort of signals that somebody knows exactly how much this project is going to cost. It is just the end product of some byzantine negotiating process. It was slated to go live October 2013. (I was blissfully unaware of this for the entire three years the project was in development).

&nbsp;&nbsp;&nbsp;&nbsp;
One day in October 2013, one of my developers came into my office and told me he had just heard of an application system comprising over 500,000,000 lines of code. He couldn’t fathom what you would need 500,000,000 lines of code to do. He was a recent college graduate, had been working for us for several years, and had written a few thousand lines of elegant architectural code. We were running major parts of our company on these few thousand lines of code so he was understandably puzzled at what this could be.

We sat down at my monitor and said, “Let’s see if we can work out what they are doing.”

&nbsp;&nbsp;&nbsp;&nbsp;
This was the original, much maligned rollout of Healthcare.gov. We were one of the few that first week who managed to log in and try our luck (99% of the people who tried to access healthcare.gov in its first two weeks were unable to complete a session).

&nbsp;&nbsp;&nbsp;&nbsp;
As each screen came up, I’d say “what do you think this screen is doing behind the scenes?” and we would postulate, guess a bit as to what else it might be doing, and jot down notes on the effort to recreate this. For instance, on the screen when we entered our fake address (our first run was aborted when we entered a Colorado address as Colorado was doing a state exchange) we said, “What would it take to write address validation software?” This was easy, as he had just built an address validation routine for our software.

&nbsp;&nbsp;&nbsp;&nbsp;
After we completed the very torturous process, we compiled our list of how much code would be needed to recreate something similar. We settled on perhaps tens of thousands of lines of code (if we were especially verbose). But no way in the world was there any evidence in the functionality of the system that there was a need for 500,000,000 lines of code.

Meanwhile news was leaking that the original $93 million project had now ballooned to $500 million.

&nbsp;&nbsp;&nbsp;&nbsp;
In the following month, I had a chance encounter with the CEO of Top Coder, a firm that organizes the equivalent of X prizes for difficult computer programming challenges. We discussed Healthcare.gov. My contention was that this was not the half-billion dollar project that it had already become, but was likely closer to the coding challenges that Top Coder specialized in. We agreed that this would make for a good Top Coder project and began looking for a sponsor.

&nbsp;&nbsp;&nbsp;&nbsp;
Life imitates art, and shortly after this exchange, we came across HealthSherpa.com. The Health Sherpa User Experience was a joy compared to Healthcare.gov. I was more interested in the small team that had rebuilt the equivalent for a fraction (a tiny fraction) of the cost.

&nbsp;&nbsp;&nbsp;&nbsp;
From what I could tell from a few published papers, a small team of three to four in two to three months had built equivalent functionality to that which hundreds of professionals had spent years laboring over. This isn’t exactly equivalent. It was much better in some ways, and fell a bit short in a few others.

&nbsp;&nbsp;&nbsp;&nbsp;
In the ensuing years, I’d used this as a case study of what is possible in the world of enterprise (or larger) applications. Over the course of the ensuing four years, I’ve been tracking both sides of this natural experiment from afar.

&nbsp;&nbsp;&nbsp;&nbsp;
I looked on in horror to watch the train wreck of the early rollout of Healthcare.org balloon from $1/2 billion to $1 billion (many firms have declared victory in “fixing” the failed install for a mere incremental $1/2 billion), and more recently to $2.1 billion. By the 2015 enrolment period, Healthcare.gov had adopted the HealthSherpa user experience, which they now call “Marketplace lite.” Meanwhile HealthSherpa persists, having enrolled over 800,000 members, and at times handles 5% of the traffic for the ACA.

&nbsp;&nbsp;&nbsp;&nbsp;
The writing of this book prompted me to research deeper, in order to crisp up this natural experiment playing out in front of us. I interviewed George Kalogeropoulos, CEO of HealthSherpa, several times in 2017, and have reviewed all the available public documentation for Healthcare.gov and HealthSherpa.

&nbsp;&nbsp;&nbsp;&nbsp;
The natural experiment that has played out here is around the hypothesis that there are application development and deployment process that can change the resource consumption and costs by a factor of 1,000. As with the Korean Peninsula, you can nominate either side to be the control group. In the Korea example, we could say that communism was the control group and market democracy the experiment. The hypothesis would be that the experiment would lead to increased prosperity. Alternatively, you could pose it the other way around: market democracy is the control and dictatorial communism is the experiment that leads to reduced prosperity.

&nbsp;&nbsp;&nbsp;&nbsp;
If we say that spending a billion dollars for a simple system is the norm (which it often is these days) then that becomes the control group, and agile development becomes the experiment. The hypothesis is that adopting agile principles can improve productivity by many orders of magnitude. In many settings, the agile solution is not the total solution, but in this one (as we will see), it was sufficient.

&nbsp;&nbsp;&nbsp;&nbsp;
This is not an isolated example – it is just one of the best side-by-side comparisons. What follows is more evidence that application development and implementation are far from waste-free.
