---
title: "When Semantics is King: Bringing AI Back to Humans"
author: "Slava Tykhonov"
date: "2026-07-03"
source: "https://www.linkedin.com/pulse/when-semantics-king-bringing-ai-back-humans-slava-tykhonov-fx7ze"
tags: ["Slava Tykhonov", "Croissant, Graphs and AI", "AI"]
---
## Governing AI with Semantic Knowledge Graphs

# When Semantics is King: Bringing AI Back to Humans

- [Report this article](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fwhen-semantics-king-bringing-ai-back-humans-slava-tykhonov-fx7ze&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[Slava Tykhonov](https://fr.linkedin.com/in/vyacheslavtikhonov)
![Slava Tykhonov](assets/image-02-9acbdf7ffc.jpg)

### Slava Tykhonov

## Published Jul 3, 2026

[+ Follow](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fwhen-semantics-king-bringing-ai-back-humans-slava-tykhonov-fx7ze&trk=article-ssr-frontend-pulse_publisher-author-card)

It's time for the new edition of my newsletter and today I'm going to talk about what I believe the AI community is getting wrong. To begin with, I'll share something we recently discovered while working on a translation project for the 
 [United Nations Office for Disaster Risk Reduction (UNDRR)](https://ch.linkedin.com/company/undrr?trk=article-ssr-frontend-pulse_little-mention)
  . The project involved translating Hazard Information Profiles from English into multiple languages, including French, Spanish, Chinese, and others.

We completed the translations and obtained the preliminary evaluation results. At first glance, everything looked very promising. The overall quality was high-probably around 90% out of 100% in terms of correctness.

However, despite these encouraging evaluation scores, the system actually doesn't work well enough for the real-world use case. What we discovered was quite remarkable - there is no absolute ground truth in the translation process, and probably it matters for other traditional tasks where AI is being considered as a major solution.

Translation is fundamentally subjective. It depends heavily on the community for which the translation is intended. Even professional translators with official translation certifications can produce different translations of exactly the same sentence in the same context. Their wording may differ only slightly, but those differences reflect how they personally understand the concepts and how their communities use the terminology. Last week 
[Maria Carmen Staiano](https://it.linkedin.com/in/maria-carmen-staiano?trk=article-ssr-frontend-pulse_little-mention)
  did a talk on the current approach at the 3rd International Conference on New Trends in Translation and Interpreting Technology ([NeTTIT 2026](https://www.linkedin.com/company/nettit2026/?trk=article-ssr-frontend-pulse_little-text-block)) in Dubrovnik, and you can find the full paper there.

Anyway, our observations related to community acceptance for translations directly contradict the current direction taken by LLMs, Large Language Models. Everybody knows that today's language models are trained through optimization. During training, they effectively converge toward what the model considers to be the single most probable or optimal solution. As a result, when you ask the model to translate something, it typically produces one preferred answer.

But that is precisely what we want to avoid!

We work with many different communities, and each community expects translations that reflect its own terminology, context, conventions, and language usage. Two communities speaking the same language may legitimately expect different translations because they use different vocabularies or domain-specific expressions.

Current language models don't handle this particularly well.

Because of that, our vision for organizing AI systems in the future is fundamentally different from the approach currently pursued by most major technology companies.

Our work is centered around a knowledge graph. More specifically, we are not using what is commonly referred to as a labeled property knowledge graph, which has become popular in Silicon Valley and elsewhere. Instead, we use a Semantic Web knowledge graph.

This means working with ontologies, controlled vocabularies, taxonomies, and representing knowledge as RDF triples. Every triple should also have a resolvable URI so that every concept, relationship, and resource can be uniquely identified and accessed.

I myself did a few talks in Manchester for the European funded 
 [Climate-Adapt4EOSC](https://gr.linkedin.com/company/eosc-climate-adapt-4?trk=article-ssr-frontend-pulse_little-mention)
  project and showcased how we're organizing the research infrastructure in terms of legal and organizational interoperability, and my 
 [CODATA](https://fr.linkedin.com/company/codata-isc-committee-on-data?trk=article-ssr-frontend-pulse_little-mention)
  colleagues 
[Simon Hodson](https://fr.linkedin.com/in/simon-hodson-b3711a11?trk=article-ssr-frontend-pulse_little-mention)
 , 
[Matti Heikkurinen](https://ch.linkedin.com/in/mattiheikkurinen?trk=article-ssr-frontend-pulse_little-mention)
  and 
[nina G.](https://fr.linkedin.com/in/ninagrau?trk=article-ssr-frontend-pulse_little-mention)
  had a few presentations from different angles of CDIF, Cross-Domain Interoperability Framework.

So why is CDIF so important and has worldwide influence, not only in Europe?

Traditionally, AI systems rely almost entirely on the output of Large Language Models. Everyone knows that these models are not perfectly accurate and that they can sometimes hallucinate. There is a fundamental reason for this. The information generated by these models is not being measured properly.

What we want is something fundamentally different. We want to introduce a measurement process that allows us to describe any kind of action, observation, or measurement using trustworthy concepts. That means every variable should have a precise definition, every value should be associated with the appropriate unit of measure, every relationship should be explicitly represented. We want to add scientific credibility to AI.

According to this vision, all the information necessary to identify and describe a phenomenon without ambiguity should be linked together in the knowledge graph, and the entire structure should also be digitally signed, with keeping the origin and provenance of the information.

Furthermore, this approach should work consistently across every AI model and every large language model in the world. Regardless of which AI vendor provides the model, the information should be interpreted in exactly the same way, to guarantee that the underlying knowledge is scientifically credible, interoperable, and machine-readable across different AI platforms.

Only then can we establish meaningful benchmarks that are comparable across models and applications. More importantly, this is how we can finally bring trust to AI systems.

As soon as you know the source, the origin, and the complete provenance of the information being reported by a large language model - and you can verify every piece of that information through the knowledge graph - you have a solid foundation for trusting that the model is producing the correct results.

To support this architecture, we have started using Decentralized Identifiers (DIDs).

Every DID carries provenance information. It is associated with digital certificates as well as public and private cryptographic keys. The private key is used to authorize modifications to a resource, while the public key allows anyone to verify authorship and authenticity.

But that is only one part of the system.

We have also started using UNF-6 (the Universal Numerical Fingerprint) to generate digital fingerprints for every piece of content. You can read about UNF-6 in [excellent article](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fplgah%2Emedium%2Ecom%2Funiversal-numerical-fingerprint-unf-the-format-agnostic-key-to-data-trust-cf9d38482671&urlhash=Smpy&trk=article-ssr-frontend-pulse_little-text-block) of 
[Pascal Heus](https://ca.linkedin.com/in/pascal?trk=article-ssr-frontend-pulse_little-mention)
 , he reconstructed and reimplemented the whole algorithm from scratch.

Nobody realize this yet but Universal Numerical Fingerprint is extremely important.

If you look at how traditional knowledge graphs are organized today, you'll notice that they often reference external resources located somewhere on the web. The problem is that these references are inherently unreliable - a website may disappear, a server may become unavailable, a document may be modified without notice.

Even more, someone else may alter the contents, and the knowledge graph has no reliable way to detect that change.

We want to eliminate this problem, and our approach is to compute a unique cryptographic fingerprint (or digital hash) for every referenced resource.

That fingerprint is stored inside the knowledge graph as evidence of the exact version of the resource that was referenced. Additionally, the fingerprint itself is digitally signed, and as a result, we know who created it, who owns the resource, who collected it, and who inserted it into the knowledge graph.

This gives us a much stronger foundation for trust, provenance, and reproducibility.

Now imagine how today's language models typically work.

Knowledge is packaged into the model during training or fine-tuning. Once the model has been trained, that knowledge is effectively static until another training cycle takes place.

Instead, we introduce the way for language models to get up-to-date knowledge by querying a live knowledge graph.

Rather than relying on frozen knowledge embedded in model weights, the model should retrieve current, verified information that remains under organizational control.

With this architecture, we can define different governance policies and we can control who has access to specific information. We can also establish conditions under which information may be retrieved, and even connect restricted information sources. This is where digital policies expressed with ODRL (Open Digital Rights Language) will play a role.

For example, if data resides inside a organization's internal database, we can expose it through controlled interfaces without ever using that data to train the language model. The language model does not need to see that information during training, and in many cases it absolutely should not.

Instead, it should access that information only at inference time, subject to the appropriate permissions and policies.

Ultimately, our vision is to connect this "hidden web" of organizational knowledge through standardized interfaces - something like the Model Context Protocol (MCP).

By using that approach, language models become dynamic systems that retrieve trustworthy, governed, and continuously updated knowledge instead of relying solely on static knowledge learned during training.

While automation with AI can perform initial screening, we see the increasing demand to involve domain experts as for high quality translations it's still nessecary to provide deeper validation and contextual understanding.

That's something only human experts can do (at the moment):

- Verify that automated assessments are correct.
- Add missing contextual knowledge.
- Confirm scientific validity.
- Improve metadata quality.
- Evaluate whether the dataset accurately represents the underlying research.

We believe that something with the stamp of 
 [United Nations](https://www.linkedin.com/company/united-nations?trk=article-ssr-frontend-pulse_little-mention)
  and any other trustworthy organizations still requires the validation from experts understanding the meaning of the data in ways automated systems currently cannot.

I'm off to Spain for the next week and will have my next talk about the future of AI in Alicante on Saturday, so you're more than welcome to join if you're interested and somewhere around!

And the next edition is about the future of software and "vibe coding" at the age of AI, don't miss it and subscribe right now.

---

[Originally published on LinkedIn](https://www.linkedin.com/pulse/when-semantics-king-bringing-ai-back-humans-slava-tykhonov-fx7ze).
