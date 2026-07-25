---
title: "Beyond Bigger Models: Why Europe's AI Future Is Different"
author: "Slava Tykhonov"
date: "2026-07-24"
source: "https://www.linkedin.com/pulse/beyond-bigger-models-why-europes-ai-future-different-slava-tykhonov-7txde"
tags: ["Slava Tykhonov", "Croissant, Graphs and AI", "AI"]
---
# Beyond Bigger Models: Why Europe's AI Future Is Different

- [Report this article](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fbeyond-bigger-models-why-europes-ai-future-different-slava-tykhonov-7txde&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[Slava Tykhonov](https://fr.linkedin.com/in/vyacheslavtikhonov)
![Slava Tykhonov](assets/image-02-9acbdf7ffc.jpg)

### Slava Tykhonov

Published Jul 24, 2026

[+ Follow](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fbeyond-bigger-models-why-europes-ai-future-different-slava-tykhonov-7txde&trk=article-ssr-frontend-pulse_publisher-author-card)

Today's edition is about what is fundamentally wrong with the current AI data ecosystem, and why I believe the current dominance of U.S. and Chinese AI companies may be temporary, despite the enormous investments being made.

The same question keeps coming up, and I really want to clarify my perspective here. Is Europe falling behind? Is it too slow to catch up with the United States and China in building large AI models?

First, let’s take a step back and look at what is actually happening in the AI space today. Much of the public discussion still focuses on large language models. Yes, we do see notable releases, such as Kimi K3, with more than one trillion parameters - but in reality, most models being developed and deployed are significantly smaller. Increasingly, companies are releasing models that can run locally, even on personal laptops. At the same time, hardware is rapidly improving, making it easier to run these models efficiently.

This suggests an important trend: the focus is shifting toward building capable models that can operate locally or in distributed environments. From this perspective, I believe Europe is on the right track. The goal is not necessarily to “catch up” by building massive, trillion-parameter models that attempt to do everything. Instead, Europe is prioritizing more focused, high-quality systems.

However, there is still a critical gap. What we currently lack is the ability to properly measure and validate AI outputs. When a model produces results, we often have no clear evidence of their correctness. Sometimes the outputs may be accurate, but in many cases we simply do not know - because these systems function as black boxes. This lack of verifiability is a fundamental challenge.

I have previously outlined, in several discussions, how European-funded projects aim to address this issue.

Today, I want to emphasize my broader view: in the long run, Europe will not only catch up, but may ultimately lead the way. By focusing on quality, transparency, and verifiability, Europe has the potential to set new standards that could shape the future of AI globally.

Reliability is the key

The first issue is that it is impossible to build truly reliable AI models without reliable data. Most of today's frontier models are trained on static datasets - collections of information that have been scraped, mined, or aggregated from countless sources. In many cases, we do not know exactly where this data came from, whether it was collected legally, whether it has changed over time, or who is responsible for maintaining it.

This creates a serious problem of provenance. We often have no transparent record of the origin of the data, how it was curated, what quality assurance processes were applied, or whether anyone continues to verify its accuracy. Once a dataset has been incorporated into a model, it effectively becomes part of a black box.

Without clear provenance, it becomes extremely difficult to establish trust. If we cannot inspect the data, understand how it was selected, or identify its maintainers, then we cannot confidently judge the quality of the model's outputs. Independent auditing becomes either prohibitively difficult or, in many situations, practically impossible.

This limitation may not matter much for certain commercial applications. AI companies can successfully sell services to startups, automate repetitive business processes, generate marketing content, or assist with customer support. These applications tolerate occasional mistakes because humans remain in the loop and the consequences of errors are relatively limited.

The situation changes completely when AI is introduced into serious scientific or professional domains.

Consider health research, scientific research, engineering, public administration, or regulatory decision-making. In these areas, reproducibility is not optional - it is a fundamental requirement. Researchers must be able to reproduce results, inspect every step of the process, verify the evidence, and understand why a particular conclusion was reached. If you don't believe in this, you mush check the guidelines on the AI Act and understand the future obligations for AI in Europe where every single chatbot should introduce itself properly, show its provenance and stop pretending to be human.

Current large language models struggle to satisfy these requirements. They rarely provide complete information about the underlying data used to generate an answer. They do not expose which training sources contributed to a specific response. Their outputs are probabilistic rather than deterministic. Consequently, two identical prompts may produce different answers, making rigorous scientific validation extremely difficult.

For domains where mistakes can have serious consequences, this is a significant limitation.

This is why I believe that simply building the world's most capable model is not enough, and you can read below what we're discussing in different meetings here in Europe.

The United States or China may well succeed in developing increasingly powerful foundation models. They may continue to lead in benchmark performance, model size, and computational resources. However, technological capability alone does not automatically translate into widespread adoption in regulated environments.

Where are baselines?

If some AI vendors want to become trusted providers within the European Union, they will need to satisfy a completely different set of requirements.

They will have to demonstrate transparency, establish clear governance processes, and provide evidence that their systems comply with European regulations. This includes not only legal compliance but also scientific accountability and reproducibility.

One of the biggest missing pieces today is the absence of a common evaluation baseline.

We already have numerous benchmarks that measure various aspects of AI performance. They test reasoning, coding ability, mathematical skills, multilingual capabilities, and many other tasks. These benchmarks are useful, but they are fragmented.

What we do not have is a universally accepted baseline against which every major model can be evaluated under identical conditions.

Such a baseline would allow independent organizations to ask the same questions of every model, compare their behaviour, evaluate consistency, identify strengths and weaknesses, and determine which models are suitable for specific domains.

It would also make it possible to test how models respond when presented with unexpected inputs, conflicting evidence, incomplete information, or deliberately misleading data. These situations are common in real-world applications but are not always adequately represented in existing benchmarks.

Without such a common baseline, it becomes difficult for customers, regulators, and researchers to make informed decisions. There are famous cases when US models are (sometimes wrongly) telling that Chinese models aren't suitable for specific tasks - but actually they are.

Another challenge is the pace at which foundation models evolve.

Every few months we see another major release - Claude, GPT, Gemini, and many others continue to improve rapidly. Each new version introduces new capabilities, different training data, modified architectures, and updated safety mechanisms.

However, every new release also raises a lot of important questions:

- How do we know that the latest version remains compliant with European requirements?
- How has the training data changed?
- What new sources have been incorporated?
- Which languages have improved, and which may have regressed?
- How well does the model perform in highly specialized domains?
- Has its behaviour changed in ways that matter for regulated applications?

These questions often remain unanswered because there is no standardized mechanism for continuous independent evaluation.

Knowledge is moving in time and space

An even bigger concern involves access to knowledge itself.

The vast majority of the world's information is not publicly available. Most valuable scientific datasets, industrial databases, government records, commercial repositories, medical archives, and enterprise knowledge remain private.

Public web content represents only a small fraction of humanity's collective knowledge.

If foundation models are primarily trained on publicly accessible information, then there is a fundamental limit to what they can truly understand about specialized domains.

Without access to trusted domain-specific data, there is no guarantee that the model can correctly recognize complex patterns or provide reliable answers in expert contexts.

This becomes especially important in medicine, climate science, engineering, chemistry, law, finance, and many other disciplines where specialized knowledge continuously evolves and is often unavailable on the public web.

The same concerns extend beyond data into software development.

Today's AI systems can generate remarkably sophisticated software. Many developers now rely heavily on AI-assisted coding or even so-called "vibe coding," where applications are created primarily through natural language prompts.

For many relatively simple applications, this works surprisingly well.

However, software engineering involves far more than producing code that compiles.

There are other important questions about copyright, licensing, intellectual property, and long-term maintenance.

We usually do not know precisely which repositories contributed to the generated code. Was it trained entirely on open-source software? Did it incorporate code from projects with restrictive licenses? Were proprietary repositories included? Who bears responsibility if generated code unintentionally reproduces copyrighted material or introduces legal risks?

These questions remain largely unresolved.

There is also the issue of sustainability.

Many open-source projects become popular for a short period and are then abandoned. New AI-generated software often builds upon libraries and frameworks maintained by relatively small communities, sometimes by just one or two developers.

If the community disappears, maintenance stops, security vulnerabilities accumulate, compatibility breaks, and the software gradually becomes obsolete.

Generating code is therefore only the beginning.

Maintaining it over many years requires human expertise, governance, documentation, testing, security reviews, architectural knowledge, and an active community.

No language model can replace the long-term stewardship provided by experienced developers and maintainers.

This is why clear specifications and reproducible engineering processes remain essential.

A software system should be understandable from first principles. Engineers should be able to recreate it from scratch, verify every component, test every dependency, validate every assumption, and demonstrate that it behaves exactly as intended.

Without transparent specifications and reproducible implementation, organizations become dependent on opaque systems that they cannot fully inspect or verify.

Ultimately, technology alone is not enough.

Reliable AI requires trusted data, clear provenance, transparent governance, reproducible evaluation, independent auditing, legal compliance, sustainable software ecosystems, and active human communities that continuously maintain both the underlying data and the software itself.

If these foundations are missing, then even the most powerful AI models become difficult to trust in the environments where trust matters most.

That is why I believe the current leadership of U.S. and Chinese AI companies may not be permanent. Building the largest models is only one part of the challenge.

Long-term success - particularly in highly regulated environments such as the European Union - will depend on openness, accountability, reproducibility, and governance rather than raw model capability alone. And that's something we're going to contribute, and other continents are already joining!

---

[Originally published on LinkedIn](https://www.linkedin.com/pulse/beyond-bigger-models-why-europes-ai-future-different-slava-tykhonov-7txde).
