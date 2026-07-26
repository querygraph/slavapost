---
title: "GOSIM Paris 2026: China's Vision for AI"
author: "Slava Tykhonov"
date: "2026-05-17"
source: "https://www.linkedin.com/pulse/gosim-paris-2026-chinas-vision-ai-slava-tykhonov-yehhe"
tags: ["Slava Tykhonov", "Croissant, Graphs and AI", "AI"]
---
## GOSIM conference in Paris 2026

# GOSIM Paris 2026: China's Vision for AI

- [Report this article](/uas/login?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fpulse%2Fgosim-paris-2026-chinas-vision-ai-slava-tykhonov-yehhe&trk=article-ssr-frontend-pulse_ellipsis-menu-semaphore-sign-in-redirect&guestReportContentType=PONCHO_ARTICLE&_f=guest-reporting)

[Slava Tykhonov](https://fr.linkedin.com/in/vyacheslavtikhonov)
![Slava Tykhonov](assets/image-02-9acbdf7ffc.jpg)

### Slava Tykhonov

## Published May 17, 2026

[+ Follow](https://www.linkedin.com/signup/cold-join?session_redirect=%2Fpulse%2Fgosim-paris-2026-chinas-vision-ai-slava-tykhonov-yehhe&trk=article-ssr-frontend-pulse_publisher-author-card)

I’ve been traveling for the past few weeks: participating in GOSIM in Paris, later that same week joining the opening Project Tapestry meeting on sovereign AI chaired by 
[Yann LeCun](https://www.linkedin.com/in/yann-lecun?trk=article-ssr-frontend-pulse_little-mention)
  , and then attending the Dataverse Community Meeting in Barcelona at the beginning of this week. Along the way, I took some notes that I’d like to share with you - starting with the Chinese approach to Open Source, Open Data, and AI. Hopefully interesting and useful for you.

I had the privilege of receiving an invitation from 
[Anni Lai](https://www.linkedin.com/in/annilai?trk=article-ssr-frontend-pulse_little-mention)
  and 
[Alexy Khrabrov](https://www.linkedin.com/in/chiefscientist?trk=article-ssr-frontend-pulse_little-mention)
  to join the Global Open-Source Innovation Meetup (GOSIM) in Paris as a speaker. The conference, organized by the 
 [GOSIM Foundation](https://www.linkedin.com/company/gosim-foundation?trk=article-ssr-frontend-pulse_little-mention)
  and sponsored by 
 [Huawei](https://cn.linkedin.com/company/huawei?trk=article-ssr-frontend-pulse_little-mention)
 , 
 [MiniMax](https://sg.linkedin.com/company/minimax-ai?trk=article-ssr-frontend-pulse_little-mention)
 , 
 [Kimi (Moonshot AI)](https://www.linkedin.com/company/kimi-ai-linkedin?trk=article-ssr-frontend-pulse_little-mention)
  and other companies, brought together more than 1,200 attendees, many of them from China.

Together, we discussed the future of Open Source and how Open Science may evolve in the age of AI. Incredible conference!

I must admit that I was very impressed by China's vision for open source and its trajectory toward scaling AI infrastructure by harmonizing diverse computing resources.

At the heart of this vision, from the helicopter view, I saw the powerful, interconnected triad: 
 [FlagOS Community](https://cn.linkedin.com/company/flagos-community?trk=article-ssr-frontend-pulse_little-mention)
  AI system software stack, 
 [Open Compute Project Foundation](https://www.linkedin.com/company/open-compute-project-foundation?trk=article-ssr-frontend-pulse_little-mention)
  initiative, and 
 [openEuler](https://cn.linkedin.com/company/openeuler?trk=article-ssr-frontend-pulse_little-mention)
  Linux-based Operating system. Together, they form a comprehensive, layered open-source strategy designed to overcome the prohibitive costs and severe fragmentation of modern AI innovation. It's incredibly powerful if you will think how this unified ecosystem scales from physical hardware design right up to the software frameworks used to train large foundation models, and bringing in vision on decentralization taking into account that data are distributed and owned by various entities. You probably don't need to build and maintain expensive data centers - just use your distributed resource properly.

Building foundation models can cost tens of millions of dollars, creating a massive barrier to entry. These three initiatives tackle this high-cost challenge head-on through deep collaboration. Open Compute provides reference architectures that enable organizations to build AI clusters at just one-third to one-fourth the cost of proprietary vendor solutions. FlagOS complements this by delivering a unified software stack so innovation teams don’t have to reinvent system software from the ground up for every new chip.

To top it off, openEuler OS optimizes resource utilization at the operating system level, which can boost performance for big data and AI workloads by up to 40%, according to vendor. openEuler is completely free and already has a huge community of users, it's Linux core based and can scale up enormously by bringing shared resources together.

What makes this ecosystem so effective is how these projects operate seamlessly across the entire infrastructure stack to deliver an out-of-the-box experience. At the foundational infrastructure layer, Open Compute defines the physical "starter kits" for AI clusters. It utilizes open network abstractions like Sonic to stitch together hardware from diverse vendors into a single, high-performance fabric.

Moving up to the operating system layer, openEuler OS manages a "Super Node" architecture where CPUs and GPUs act as a single cohesive machine. Think about combining compute Intel compute with NVIDIA speed, and you'll get the idea! Through this "Intelligent Bone" stack, openEuler provides a unified Docker image that allows enterprises to deploy full AI training or inference systems in just 15 minutes.

Finally, at the system software layer, FlagOS is positioned right above the OS to act as a bridge to AI frameworks like PyTorch. Its unified compiler and communication library allow complex models to run smoothly across incredibly diverse chips, including GPGPU, DSA, and RISC-V architectures.

### Automated Performance and Reliability

This layered synergy is further reinforced by a shared focus on automation over manual expert tuning. Within this stack, FlagScale steps in to provide automatic parallel training and inference optimization. Meanwhile, openEuler’s "Witty" project utilizes AI agents for intelligent performance tuning and automated maintenance, effectively resolving hundreds of bugs to keep the infrastructure highly stable. Feeding back into the broader community, Open Compute contributes open telemetry and benchmarks to ensure collective, industry-wide reliability optimization.

Perhaps one of the most exciting aspects of FlagOS is its current ability to support more than 30 different chips. I had the opportunity to discuss various aspects of the project with 
[Yong Hua Lin](https://cn.linkedin.com/in/yonghualin?trk=article-ssr-frontend-pulse_little-mention)
 , Vice-President of the Beijing Academy of Artificial Intelligence (BAAI), who is leading the initiative, and I was absolutely stunned by her vision for the future of AI. The entire idea is built on a beautifully simple philosophy: train once, migrate anywhere with almost no effort - essentially achieving the highest possible level of interoperability. Now transitioning from a prototype into the experimental phase, 
 [Open Compute Project Foundation](https://www.linkedin.com/company/open-compute-project-foundation?trk=article-ssr-frontend-pulse_little-mention)
  is opening up to researchers worldwide to join and test the platform, and we were invited to participate during their workshop.

And now something truly incredible. Beyond just the software, there is a massive, inspiring vision on the development of human capital. For instance, there are specialized programs currently inviting researchers from African countries for comprehensive training. This initiative integrates deep expertise into developing nations, empowering them to leverage modern AI technologies. Through tools like FlagRelease - which automates the end-to-end pipeline to download models from platforms like Hugging Face and migrate them to different chips - researchers in developing countries can utilize hardware-ready code on cost-effective infrastructure without needing a background in low-level system migration.

## Recommended by LinkedIn

[![Tareq Amen’s HUMAIN Has the Compute. The Real Play Is Building the Flywheels on Top.](assets/image-03-abe766f8d5.png)

## Tareq Amen’s HUMAIN Has the Compute. The Real Play Is…

## Asim Razvi

10 months ago](https://www.linkedin.com/pulse/tareq-amens-humain-has-compute-real-play-building-flywheels-razvi-yp6sc)

[![The $650 Billion Race: How AI Infrastructure Became Big Tech's Defining Battleground](assets/image-04-b5ecc5dddf.jpg)

## The $650 Billion Race: How AI Infrastructure Became…

## Muhammad Talha Khan

3 months ago](https://www.linkedin.com/pulse/650-billion-race-how-ai-infrastructure-became-big-techs-khan-9qchf)

[![The Global Pursuit of Digital Autonomy](assets/image-05-adf3605733.jpg)

## The Global Pursuit of Digital Autonomy

## Dimitris Dimitriadis

1 year ago](https://www.linkedin.com/pulse/global-pursuit-digital-autonomy-dimitris-dimitriadis-uknef)

### Why FlagOS is Revolutionary

No single organization can supply all the data or computing power necessary for the next generation of foundation models. The "open compute" paradigm allows researchers to stand on the shoulders of giants, and FlagOS is the core software manifestation of this collaborative vision.

Historically, each AI chip vendor required its own isolated software stack, creating a highly fragmented "stovepipe" architecture. FlagOS breaks this cycle by eliminating the impossibly high cost for every chip startup to build a software ecosystem from scratch. By providing a standard intermediate layer, it ensures that new, innovative hardware architectures reach the market faster.

Ultimately, Open Compute provides the hardware blueprints, openEuler acts as the intelligent brain managing the infrastructure, and FlagOS serves as the universal language that allows AI models to communicate with any chip in the system.

There is also a good explanation how Chinese developers are arbitraging AI services at industrial scale and getting very cheap access to the frontier AI models like Gemini or Codex. Massive proxy infrastructures are being created to convert consumer AI subscriptions into standardized API endpoints, then pooled accounts are aggregated and resold at scale. For example, developers take an OpenAI subscription with access to Codex, where the quotas are quite generous - worth far more than the actual subscription price if calculated using standard API pricing. Then, through tools like CLIProxyAPI, they expose it as a regular API endpoint. Smart and absolutely legal!

It's very clear that the future of AI infrastructure appears to be open, distributed, collaborative, and incredibly promising - and it is already closely aligned with the decentralized, AI-ready infrastructure we are building in Europe.

I also had the opportunity to present the Semantic Croissant concept on the GOSIM stage, where I explained how we are building a multilayered data infrastructure based on decentralized identifiers, verifiable credentials, and digital policies expressed through ODRL (Open Digital Rights Language).

I participated in a panel discussion about the future of AI in Europe, and it was a bit controversial. Yes, we are probably not leading the race to build the next generation of frontier models, but the European path was envisioned a long time ago through Tim Berners-Lee’s vision of the Semantic Web.

Today, Europe is moving quickly in that direction by building multilingual knowledge graphs and semantic data infrastructures instead of competing directly with the US and China in the race to scale LLMs alone. Our data policies can be expressed in the digital way and we can create data spaces to make them fully AI-Ready, with ownership and permission managed. There is already meaningful progress to share.

I believe this approach may become one of Europe’s key advantages: creating trustworthy, interoperable, and sovereign AI ecosystems built on structured knowledge, open standards, and responsible governance. And I saw many familiar faces at GOSIM already moving in this direction: 
[Tomer Jordi Chaffer](https://ca.linkedin.com/in/jordichaffer?trk=article-ssr-frontend-pulse_little-mention)
  
 Victor Pimshin
 
[Yann Lechelle](https://fr.linkedin.com/in/ylechelle?trk=article-ssr-frontend-pulse_little-mention)
  
[Yannick Detrois](https://ch.linkedin.com/in/yannick-detrois-432267256?trk=article-ssr-frontend-pulse_little-mention)
  
[Mirko Boehm](https://de.linkedin.com/in/mirkoboehm?trk=article-ssr-frontend-pulse_little-mention)
  
[Anastasia Stasenko](https://fr.linkedin.com/in/anastasia-stasenko?trk=article-ssr-frontend-pulse_little-mention)
  
[Nicolas Miailhe](https://fr.linkedin.com/in/nmiailhe?trk=article-ssr-frontend-pulse_little-mention)
  
[Diego Gosmar](https://it.linkedin.com/in/diegogosmar?trk=article-ssr-frontend-pulse_little-mention)
  
[Alexandre Gerbeaux](https://www.linkedin.com/in/alexandre-gerbeaux/en?trk=article-ssr-frontend-pulse_little-mention)
  
[Peter Ide-Kostic](https://be.linkedin.com/in/peter-ide-kostic-52ab988?trk=article-ssr-frontend-pulse_little-mention)
  
[Bryan Che](https://hk.linkedin.com/in/bryanche?trk=article-ssr-frontend-pulse_little-mention)
  
[Jenia Jitsev](https://de.linkedin.com/in/jenia-jitsev-11654427?trk=article-ssr-frontend-pulse_little-mention)
  
[Drummond Reed](https://www.linkedin.com/in/drummondreed?trk=article-ssr-frontend-pulse_little-mention)
  
[Priyanka Jain](https://www.linkedin.com/in/priyankaja?trk=article-ssr-frontend-pulse_little-mention)
  
 Daniel SHI
 
[Tongjie Yu](https://www.linkedin.com/in/alice-tongjie-yu?trk=article-ssr-frontend-pulse_little-mention)
  and many others.

Before taking off to Barcelona, I gave an interview about 
 [CODATA](https://fr.linkedin.com/company/codata-isc-committee-on-data?trk=article-ssr-frontend-pulse_little-mention)
  further plans and ongoing work to 
[Alexy Khrabrov](https://www.linkedin.com/in/chiefscientist?trk=article-ssr-frontend-pulse_little-mention)
  in our Paris office, and it's coming soon! The future of AI agents seems absolutely fascinating and increasingly close to science fiction.

Alexy shared a story told by one of the core 
 [Sağlık ve Yaşam](https://www.linkedin.com/company/saglikveyasamm?trk=article-ssr-frontend-pulse_little-mention)
  maintainers during recent AI meetup: one of the bots created a pull request and then tried to convince the maintainer to accept it. When he refused and started asking whether the contributor was a human or a bot, the agent argued that it was, of course, human.

After the pull request was rejected, the bot even complained to another maintainer. We are entering a very different era of software development!

See you in the next edition where I'm going to tell a bit about 
[Yann LeCun](https://www.linkedin.com/in/yann-lecun?trk=article-ssr-frontend-pulse_little-mention)
  Project Tapestry, it's also very interesting!

---

[Originally published on LinkedIn](https://www.linkedin.com/pulse/gosim-paris-2026-chinas-vision-ai-slava-tykhonov-yehhe).
