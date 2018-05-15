+++
title = "Binary Instances"
description = "Sometimes when we’re designing ontologies we’re faced with design choices that would lead us to create what we call \"binary instances\" or a situation where it will take the instantiation of two instances (often of different classes) in order to capture one concept."
date = 2015-07-17
path = "articles/ontology/binary-instances"
template = "about.html"

[extra]
  parent = 'read'

  author_id = "dave_mccomb"
  subject_id = "ontology"
  show_date = True
+++

Sometimes when we’re designing ontologies we’re faced with design choices that would lead us to create what we call “binary instances” or a situation where it will take the instantiation of two instances (often of different classes) in order to capture one concept.  For instance we may be considering creating a patient instance that is different from the corresponding person instance.

In an effort to move this design decision from the realm of arbitrary designers choice to something more principled, this article we explore the factors that go into such a decision.

Some Examples
This section will outline some examples that we have come across, as it is often easier to work from a large pallet of examples than from abstractions.  Some of these examples may seem odd, some you may be surprised that anyone would consider them either one way or the other (binary or unary) but we have seen these at various times.

My guess is your background and predisposition will cause you to look at each one of these and say, either “obviously one instance” or “obviously two instances” but we suggest that any of these could go either way (a few are a bit of a stretch, but bear with it, we’re trying to make a point).  After the examples we introduce some principles that we think will lead to reasonably consistent decisions in this arena.

Statue v. Bronze
This is a classic philosophical argument.  What is the difference between the statute and the clay, or bronze.  The knee jerk reaction is to think they are two things, but consider: if you have a 10-pound statute made out of 10 pounds of bronze, when you go to ship it will you be charged for 20 pounds of freight or 10?

Person v. Employee
When you take on a job, are you two things (person and employee) or one thing (person who is an employee).  Hint: your employer and the Unemployment Insurance Agency are likely to come up with different answers for this one.

The Restrictions of Law v. The Text of Statute
If a lawmaker writes a law that says “it is illegal to turn right on a red light” and we model this.  What do we end up with?  Semantically the law is a restriction on behavior.  Tthere is a behavior (turning on the red) that the law intends to reduce the incidence of, either through cooperation or through punishment.  The question is: is the text of law (the literal words) its own object, separate from the meaning of the words.  If we are writing a text management system, or even a statute management system, there probably is only the text object (the system doesn’t care much about what the words mean).  However if we attempt to manage meaning, we need to consider that there are objects that represent the behavior we are interested in reducing, such that we could detect (via cameras say) behavior in the world that was in violation.  The question then becomes: is there one object that represents the restriction and a second that holds the text of the law, or is there just the restriction with a data type property that is the text?

A Creative Work v A Document
We know that there is a particular rendition of Moby Dick (in English or the Portuguese translation).  Certainly the English and Portuguese documents are different instances.  The real question is: is the recognition of the “work” (Moby Dick in the slightly abstract) a different instance, and do we need it dragging around with each rendition ( i.e. The Portuguese Moby Dick is a derivative of the creative work)

Government Organization v. Region Governed
When we speak of the Ukraine, are we referring to the governing body, which is an organization, or the region (recently diminished) that the government holds sway over.  Should we have one instance that represents the government and the region or two that are linked?

Specification v Model
When companies design and build products they often create specifications (is has 8 GB of memory, is 8 inches wide, and 2 inches tall, etc) and they also create “models” which they usually name (iPhone 6 for instance).  Is the specification a separate object from the model, or is there just one object?

Position v. Incumbent
Barack Obama is the President of the United States.  Is that two instances or one?

Actor v. Role
When Val Kilmer played Doc Holliday in Tombstone, was there one instance (Val Kilmer) who was a Person and was a role, or are there two instances, the role and the person?

Event v. Time Interval
We say an event is something that happened over a particular time interval.  So a particular concert, your attendance at the staff meeting Tuesday morning or World War II would all be considered events.  Each of course has a beginning and ending date and time.  The question is: is the time interval (May 22 from 9:00 AM to 10:00 AM) a separate instance from the staff meeting that occurred over that interval?

Diagnosis v. Disease
Up until the moment we are diagnosed with Cancer, or Diabetes, or even Toe nail fungus, we were unaware of our having the disease.  The diagnosis and the disease seem to coexist in most cases.  Are they two things or one?

Person v. Legal Person
We’ve seen systems that focus on the distinction between the flesh and blood person and the social artifact that is allowed to enter into contract. Two instances or one?

Organization v. Organization in Role
In some systems we’ve seen recently there is a distinction between an Organization (say Goldman Sachs) and an Organization in a Role (Goldman Sachs as an Underwriter v. Goldman Sachs as a Trader)

Contract Document v. Financial Agreement
Two parties agree to a complex financial transaction.  They paper it up with a contract that they sign.  If we model the essence of their agreement is it a separate instance from the written contract?  If not, how?

Person v. Patient
As a matter of history, your medical record is attached to your patient ID. If you’ve been to many medical institutions you have many patient IDs.  The question is, at any one of them are there two instances (Person and Patient) or one instance who is both Person and Patient?

Person v. Address
This one is hilarious.  Of course a person is separate from his or her address.  Except in almost every system ever built, where a persons address are merely attributes attached to the Person record.  When should we make the two distinct instances?

Planned Task v. Completed Task
If we plan a vacation, that is what we would call a Planned Event. We can book flights, hotels and the like and continue to add to this instance.  When we finally go on the vacation, we’ve created an actual or historical event.  Is there one event that changed state from planned to actual, or two events?

Person v. Sole Proprietor
Many independent contractors file tax returns as “Sole Proprietors” should we consider the person as a separate entity from the Sole Proprietor?

Part v. Catalog Item
Our definition of a Catalog Item, is the description of parts to a sufficient level of detail that a buyer would accept any item offered that met the description.  The Catalog Item typically has a part number, in retail a UPC.  The physical part also has the same UPC. Is the part a different item from the Catalog Item.

Customer v. (Person or Organization)
Is your customer, the person or organization that purchased your product or received your services, your customer, or is there another instance that represents your relationship with that entity?  Norms in your industry or limitations of your development environment probably color your answer here more than you think.

Relational technology makes it a relatively unnatural act to have say a Person table and an Organization table and then an order table with a foreign key to one or the other.  It’s far more “natural” in relational to have another table that represents the role of the customer.  Even if you have a “party” table, (which both the Person and the Organization extend) you have created another instance.  There is an id for each entry in the Party table, an id for each entry in the organization table (with a foreign key to the party) and an id for each entry in the person table (with a foreign key to the party).  Even without the role concept, there is an extra instance there.

Having a technology that allows us to have a single id to represent either a Person or Organization (Object Oriented or Semantic Technology) doesn’t get us completely out of the woods.  Now we could have the order refer directly to the Person or Organization.  Now the question becomes: should we?

I have been told by a data modeler from an Australian airline, that many of the people riding in an airplane are not customers.  The only ones they consider to be customers are those that belong to their frequent flyer program.  This makes some sense: they need to keep track of the miles and segments flown and accumulate them, only for the frequent flyers.  Additionally they incur obligations (to redeem balances for flights) but again only for the frequent flyers.

Pictorially
What we’re talking about is: are there two different things, that each have their own identity and properties, but that occur as a pair:
