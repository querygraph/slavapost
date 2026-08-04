---
title: "Intelligence is not Inside the AI Model, it's in your Harness"
author: "Slava Tykhonov"
date: "2026-08-04"
source: "https://www.linkedin.com/pulse/intelligence-inside-ai-model-its-your-harness-slava-tykhonov-2uo4e"
tags: ["Slava Tykhonov", "Croissant, Graphs and AI", "AI"]
---
## Poisoning AI

# Intelligence is not Inside the AI Model, it's in your Harness

- [Report this article](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fintelligence-inside-ai-model-its-your-harness-slava-tykhonov-2uo4e&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[Slava Tykhonov](https://fr.linkedin.com/in/vyacheslavtikhonov)
![Slava Tykhonov](assets/image-02-9acbdf7ffc.jpg)

### Slava Tykhonov

## Published Aug 4, 2026

[+ Follow](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fintelligence-inside-ai-model-its-your-harness-slava-tykhonov-2uo4e&trk=article-ssr-frontend-pulse_publisher-author-card)

Today's edition is about intelligence and where it actually comes from.

I believe one of the biggest misconceptions in AI today is the assumption that intelligence is stored inside a static language model. In reality, what we often call intelligence is something much broader. A model by itself is simply a frozen collection of parameters trained on historical data. The real intelligence emerges from how that model interacts with the outside world.

What really matters is what I would call the AI harness. The harness is the entire system surrounding the model that enables it to communicate with different sources of information, retrieve relevant knowledge, process it, reason over it, and combine it into useful answers. Intelligence, therefore, is not simply a property of a neural network. It is a property of the entire system: the model, its harness, the tools it can use, the data it can access, and the governance mechanisms controlling that access.

A good example of this idea can be found in recent interview with the founder of Moonshot AI discussing the development of the Kimi K3 model and its expert-layer architecture. Much of the discussion focuses on how expert capabilities are embedded into the model itself.

However, I think this is only one [possible implementation](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flinas%2Esubstack%2Ecom%2Fp%2Fkimi-k3-ultimate-guide&urlhash=0Ktu&trk=article-ssr-frontend-pulse_little-text-block), and we can reproduce the same organization and setup in the decentralized way, and make it more sustainable and trustworthy.

There is nothing fundamentally requiring those expert capabilities to live inside the neural network. Instead, they can exist outside the model as part of the harness.

Imagine taking an open model such as Gemma or LLaMa. By applying an appropriate model configuration, routing layer, or expert profile, you can transform that general-purpose model into a domain expert. The expertise is not necessarily encoded in additional model weights. Instead, it comes from the way the model is orchestrated, what tools it can access, and which information sources it is connected to.

This expert can run entirely inside your own local environment, fully under your control. Rather than depending on a centralized cloud provider, it can communicate through the Model Context Protocol (MCP) with databases, document repositories, APIs, scientific infrastructures, or enterprise knowledge bases. Every connection can be protected by authentication, authorization, and fine-grained access-control policies.

In this architecture, intelligence is distributed, the language model performs reasoning and MCP layer provides secure communication.

Furthermore, the connected repositories provide authoritative and continuously updated knowledge, the governance layer determines which information the model is allowed to access. Together, these components form an intelligent system or, basically, what we call intelligence.

With such an architecture, it becomes possible to reproduce much of what systems like Kimi appear to be doing. Instead of permanently embedding every possible expert into the neural network, expert behavior can be activated dynamically whenever it is needed. For each task, the appropriate expert configuration is selected, connected to relevant knowledge sources, and used to solve the problem. When another task arrives, a different expert can be activated without retraining the underlying model.

This means there is no fundamental reason why expert capabilities must belong exclusively to proprietary frontier models. A locally running model equipped with the right harness, secure access mechanisms, and external knowledge sources can provide remarkably similar functionality while remaining completely under the user's control.

In many respects, this is already how modern cloud AI systems appear to operate.

When users invoke web search or retrieval functions, the model is rarely answering solely from its internal parameters. Instead, it searches external sources, retrieves documents, analyzes them, reasons over their content, and generates a response based on both the retrieved information and its own reasoning capabilities.

When a cloud AI system performs a web search, users generally have no visibility into the retrieval pipeline. Which search engine is being used? Is the information coming from Google, DuckDuckGo, Bing, or a proprietary index? How are documents ranked? What filtering mechanisms are applied? How recent is the information? How are conflicting sources resolved? What criteria determine whether a source is trustworthy?

These questions usually remain unanswered and create a lot of confusion.

The lack of transparency leads to an even more fundamental issue: Can we trust the information entering the AI harness?

If cloud AI systems rely on conventional search engines as part of their retrieval process, then they are consuming information that has already been filtered through search engine optimization (SEO). The content appearing at the top of search results is not necessarily the most accurate or scientifically reliable. More often, it is the content that has been optimized to achieve high rankings according to search engine algorithms.

This creates a significant challenge for all of us. Can we really trust AI which is not transparent?

The retrieved information may be treated by the AI as reliable evidence even though its visibility is the result of optimization rather than objective quality. In other words, the language model itself may reason perfectly well, but the AI harness is being supplied with biased or manipulated information.

A model does not necessarily fail because its reasoning is incorrect. It can fail because the evidence entering the reasoning process is flawed. Even the world's best expert will produce poor conclusions if the underlying information is unreliable.

The situation becomes even more concerning when we consider retrieval poisoning.

Someone could deliberately publish content specifically designed to rank highly in search engines. That content may appear authoritative while actually containing misleading, incomplete, or entirely false information. If an AI system retrieves it without verifying provenance or trustworthiness, those errors become part of the reasoning process and may be presented confidently to users.

There is another growing challenge where an increasing proportion of web content is no longer written by humans. Much of it is generated automatically by AI systems. In many cases, users have no way of determining who created the content, whether it was reviewed by a domain expert, or whether it simply represents another AI model repeating information produced by previous AI models.

This creates a dangerous feedback loop:

1. AI-generated content is indexed by search engines.
2. Cloud AI systems retrieve that content.
3. New AI-generated articles are then created from those summaries.
4. Those articles are again indexed and retrieved.
5. This cycle repeats.

Over time, errors become reinforced, misconceptions become amplified, and genuinely authoritative information becomes harder to distinguish from automatically generated material.

We are already witnessing the rapid growth of what many people call AI slop - large volumes of automatically generated content whose primary purpose is attracting search traffic rather than sharing knowledge. These pages are often heavily optimized for SEO and therefore become highly visible despite containing little evidence, little expertise, and little human verification.

If the retrieval layer cannot distinguish between authoritative scientific knowledge and AI-generated noise, then the entire AI harness becomes vulnerable. The reasoning model itself may remain technically excellent, but the quality of its answers will increasingly depend on information that has been manipulated, optimized for visibility instead of truth, or generated without meaningful human oversight.

This is why I believe the future of AI is not primarily about building larger language models.

It is about building better AI harnesses.

A trustworthy AI harness should provide transparent retrieval, provenance tracking, governance, access control, authentication, digital policies, reproducibility, and mechanisms for evaluating the trustworthiness of every piece of information entering the reasoning process. Standards such as MCP for connecting tools and repositories, together with governance frameworks for data access and provenance, are likely to become just as important as advances in the models themselves.

In the long run, intelligence will not be measured by the number of parameters inside a neural network, or tokens. It will be measured by the quality of the ecosystem surrounding it: how effectively it connects to trusted knowledge, how transparently it reasons, how securely it accesses information, and how reliably it distinguishes evidence from noise.

The future of AI, therefore, is not just about better models. It is about building intelligent, transparent, and governed ecosystems in which models become reasoning engines connected to trustworthy sources of knowledge rather than isolated repositories of static information.

### From Tool Connectivity to Trustworthy AI Coordination

Another important topic is the Model Context Protocol (MCP). In my opinion, MCP is one of the most significant innovations introduced to the AI ecosystem in recent years. It was originally developed by 
 [Anthropic](https://www.linkedin.com/company/anthropicresearch?trk=article-ssr-frontend-pulse_little-mention)
  , and it fundamentally changed the way we think about connecting language models to external systems.

Before MCP, every application needed its own custom integration with every model. Every database, every API, every repository, every enterprise system required its own connector. MCP introduced the idea of a standardized interface - a common protocol that allows any compatible language model to communicate with external tools and data sources through a unified mechanism.

That alone is revolutionary, instead of writing separate integrations for every model and every application, developers can build MCP servers once and make them available to any compatible AI system.

However, I believe there were actually two different visions for MCP emerging during its early development.

The first vision is the one that most people know today.

MCP acts as a smart API layer. It exposes tools, databases, document repositories, APIs, and services through a standardized interface. The language model can discover available capabilities, invoke tools, retrieve information, and extend its functionality beyond the static knowledge encoded in its parameters.

This is the direction that the current MCP ecosystem has largely followed.

The second vision, however, was much more ambitious: instead of simply connecting a model to external tools, MCP could become a coordination protocol for intelligent systems.

Rather than treating every tool invocation as an isolated API call, MCP could synchronize multiple processes, coordinate workflows, and allow different AI agents to collaborate as a team. Individual agents could specialize in planning, retrieval, reasoning, verification, or execution, while MCP would orchestrate their communication and synchronize their state throughout a complex task.

For AI agents, this would be an incredibly powerful capability.

Instead of having one monolithic assistant attempting to solve every problem, you could have teams of specialized agents working together, exchanging information, validating each other's conclusions, and coordinating their activities through a common protocol.

Unfortunately, I feel this second direction has received much less attention.

When Anthropic donated MCP to the @Linux Foundation, creating an open community around the protocol was undoubtedly the right decision. Open governance encourages adoption, interoperability, and long-term sustainability.

However, at the same time, the synchronization aspects of MCP seem to have been largely neglected.

Today, most discussions focus on tool calling and API connectivity rather than process coordination and multi-agent collaboration.

I do not know exactly why this happened, perhaps the community prioritized interoperability because it was easier to standardize, or complexity of synchronizing autonomous agents proved too difficult.

Or perhaps the industry simply focused on the immediate commercial value of connecting language models to existing software systems.

Whatever the reason, I believe an important opportunity has been missed.

A protocol capable of synchronizing multiple intelligent agents could become the foundation for the next generation of AI systems, where collaboration, not individual models, becomes the primary source of intelligence.

There is another limitation of today's MCP ecosystem that deserves even more attention.

MCP provides connectivity, but it does not provide trust.

An MCP server can expose virtually any information source to a language model. It might connect to a curated scientific repository or enterprise knowledge base, or it might simply expose content scraped from random websites on the Internet. From the model's perspective, these resources often appear identical.

The protocol itself does not communicate whether a particular source has been scientifically reviewed, whether it has trusted provenance, whether it is maintained by recognized experts, or whether it consists entirely of AI-generated content.

This is a critical distinction: connectivity alone does not guarantee reliability.

Just because a model can access a resource does not mean that resource deserves to influence the model's reasoning.

Today, developers can connect hundreds of MCP servers to a language model with very little understanding of the quality of the information those servers provide. Some may expose authoritative databases with well-defined governance and provenance. Others may retrieve information from websites filled with SEO-optimized content, unverified claims, or AI-generated material whose origin is impossible to determine.

From the model's perspective, all of these sources are simply additional inputs.

Without mechanisms for evaluating trustworthiness, provenance, authorship, evidence, and governance, the AI harness becomes vulnerable to retrieval poisoning.

The model itself may reason correctly.

The MCP protocol may function exactly as designed.

But if the connected information sources are unreliable, manipulated, or intentionally deceptive, the final answer will also be unreliable.

This is why I believe the next evolution of MCP should go beyond interoperability.

It should become a protocol for trustworthy interoperability.

Every connected resource should carry metadata describing its provenance, ownership, governance policies, licensing, update frequency, quality indicators, and level of trust. AI systems should be able to distinguish between a peer-reviewed scientific repository, an institutional knowledge base, an enterprise document store, and an anonymous web page generated automatically by another AI system.

Only then can the model reason not just about information, but also about the credibility of that information.

In the future, MCP should not merely answer the question, "What resources can I access?"

It should also answer the far more important question:

## "Which of these resources should I trust, and why?"

That, in my view, this is where we have the missing piece of today's AI infrastructure. Without trust, provenance, and governance, interoperability alone is not enough. The future of AI depends not only on connecting models to more information, but on ensuring they can distinguish authoritative knowledge from manipulated content, verified evidence from AI slop, and trusted repositories from ungoverned sources. Only then will MCP realize its full potential as the foundation for intelligent, collaborative, and trustworthy AI ecosystems.

That's all for today. Hope to see some of you very soon in Benidorm, Costa Blanca!

---

[Originally published on LinkedIn](https://www.linkedin.com/pulse/intelligence-inside-ai-model-its-your-harness-slava-tykhonov-2uo4e).
