# TOGAF Diagrams

[![GitHub Repository Star Count](https://img.shields.io/github/stars/nelsambrose/togaf-diagrams?style=social)](https://github.com/nelsambrose/togaf-diagrams/stargazers)
[![Date of Last Repository Commit](https://img.shields.io/github/last-commit/nelsambrose/togaf-diagrams)](https://github.com/nelsambrose/togaf-diagrams/commits/main)
[![View Diagrams Online via GitHub Pages](https://img.shields.io/badge/View%20Online-GitHub%20Pages-blue)](https://nelsambrose.github.io/togaf-diagrams/)

![TOGAF Diagrams Banner](docs/images/banner.png)

A free visual library of TOGAF 10 enterprise architecture diagrams — clear, simplified visuals covering the ADM lifecycle, architecture governance, capability planning, stakeholder management, compliance, risk, and more.

> All diagrams in this repository were created by me and are free to use under the MIT License.
> 
> They are free to use for any purpose, personal or commercial, with no attribution required, though it’s always appreciated.
> 
> If you find them useful, consider leaving a ⭐ it helps others find the library too.

## Repository structure

- `docs/images/`: repository presentation assets for GitHub-facing documentation.
- `docs/diagrams/`: active, published diagram PNG files grouped by domain.
- `archive/`: superseded or historical diagram files.
- `README.md`: repository overview for GitHub.
- `index.md`: GitHub Pages landing page.

## Recommended Learning Path

<details>
<summary>Click to expand</summary>

### 🚀 Foundation
1. **Start here →** [TOGAF ADM Cycle](#2-togaf-adm-cycle) — understand the overall framework before anything else
2. [TOGAF ADM End-to-End Reference Map](#1-togaf-adm-end-to-end-reference-map) — see all phases, inputs, and outputs in detail
3. [TOGAF Architecture Vision](#10-togaf-architecture-vision) — how Phase A sets direction and stakeholder alignment
4. [TOGAF Requirements Management](#40-togaf-requirements-management) — continuous requirements flow across the ADM

### 🏛️ Core Architecture Domains
5. [TOGAF Business Architecture](#13-togaf-business-architecture) — capabilities, value streams, and organisational structure
6. [TOGAF Data Architecture](#14-togaf-data-architecture) — data assets, governance, and lifecycle
7. [TOGAF Application Architecture](#15-togaf-application-architecture) — application structure, integration, and services
8. [TOGAF Technology Architecture](#d-togaf-technology-architecture) — infrastructure, platforms, and operational resilience

### 📐 Structure & Content
9. [Architecture Content Framework](#3-architecture-content-framework) — what gets produced across the ADM
10. [TOGAF Architecture Metamodel](#20-togaf-architecture-metamodel) — structural relationships between architecture elements
11. [TOGAF Architecture Artifacts](#18-togaf-architecture-artifacts) — catalogs, matrices, and diagrams used throughout
12. [TOGAF Architecture Deliverables](#17-togaf-architecture-deliverables) — formal outputs at each ADM phase

### ⚖️ Governance & Control
13. [Architecture Governance Model](#8-architecture-governance-model) — oversight structures and accountability flows
14. [TOGAF Architecture Principles](#30-togaf-architecture-principles) — guiding rules for enterprise decision-making
15. [TOGAF Compliance Assessment](#34-togaf-compliance-assessment) — validating solutions against standards
16. [TOGAF Risk Management](#38-togaf-risk-management) — identifying and mitigating architecture risks

### 🎓 Advanced Enterprise Architecture
17. [Enterprise Continuum & Architecture Repository](#4-enterprise-continuum--architecture-repository) — how architecture assets are classified and reused
18. [TOGAF Capability-Based Planning](#19-togaf-capability-based-planning) — aligning capabilities to strategic transformation
19. [TOGAF Architecture Partitioning](#21-togaf-architecture-partitioning) — scaling governance across the enterprise
20. [TOGAF Architecture Decisions & Traceability](#36-togaf-architecture-decisions--traceability) — tracking rationale across transformation initiatives

</details>

## Browse by Category

<details>
<summary>Click to expand</summary>

### ADM & Lifecycle (4)
- [TOGAF ADM End-to-End Reference Map](#1-togaf-adm-end-to-end-reference-map)
- [TOGAF ADM Cycle](#2-togaf-adm-cycle)
- [TOGAF Architecture Vision](#10-togaf-architecture-vision)
- [TOGAF Requirements Management](#40-togaf-requirements-management)

### Architecture Domains (4)
- [TOGAF Business Architecture](#13-togaf-business-architecture)
- [TOGAF Data Architecture](#14-togaf-data-architecture)
- [TOGAF Application Architecture](#15-togaf-application-architecture)
- [TOGAF Technology Architecture](#d-togaf-technology-architecture)

### Content, Metamodel & Structure (6)
- [Architecture Content Framework](#3-architecture-content-framework)
- [TOGAF Architecture Metamodel](#20-togaf-architecture-metamodel)
- [TOGAF Architecture Deliverables](#17-togaf-architecture-deliverables)
- [TOGAF Architecture Artifacts](#18-togaf-architecture-artifacts)
- [TOGAF Architecture Partitioning](#21-togaf-architecture-partitioning)
- [TOGAF Architecture Views & Viewpoints](#11-togaf-architecture-views--viewpoints)

### Repository & Continuum (6)
- [Enterprise Continuum & Architecture Repository](#4-enterprise-continuum--architecture-repository)
- [TOGAF Enterprise Continuum](#24-togaf-enterprise-continuum)
- [TOGAF Architecture Repository](#16-togaf-architecture-repository)
- [TOGAF Architecture Landscape](#23-togaf-architecture-landscape)
- [TOGAF Reference Architectures](#25-togaf-reference-architectures)
- [Standards Information Base](#28-standards-information-base)

### Building Blocks (3)
- [Architecture Building Blocks vs. Solution Building Blocks](#6-architecture-building-blocks-vs-solution-building-blocks)
- [TOGAF Architecture Building Blocks (ABBs)](#26-togaf-architecture-building-blocks-abbs)
- [TOGAF Solution Building Blocks (SBBs)](#27-togaf-solution-building-blocks-sbbs)

### Capability & Planning (5)
- [Capability Assessment & Maturity Models](#5-capability-assessment--maturity-models)
- [TOGAF Capability-Based Planning](#19-togaf-capability-based-planning)
- [TOGAF Architecture Capability](#31-togaf-architecture-capability)
- [Opportunities & Solutions](#e-opportunities--solutions)
- [Migration Planning](#f-migration-planning)

### Stakeholders & Communication (4)
- [Stakeholder Map with Views & Concerns](#7-stakeholder-map-with-views--concerns)
- [TOGAF Stakeholder Management](#12-togaf-stakeholder-management)
- [Business Scenarios](#9-business-scenarios)
- [TOGAF Architecture Communication](#22-togaf-architecture-communication)

### Governance & Compliance (11)
- [Architecture Governance Model](#8-architecture-governance-model)
- [TOGAF Architecture Principles](#30-togaf-architecture-principles)
- [TOGAF Architecture Contracts](#32-togaf-architecture-contracts)
- [TOGAF Architecture Compliance Reviews](#33-togaf-architecture-compliance-reviews)
- [TOGAF Compliance Assessment](#34-togaf-compliance-assessment)
- [TOGAF Governance Log](#29-togaf-governance-log)
- [TOGAF Governance Repository](#35-togaf-governance-repository)
- [TOGAF Architecture Decisions & Traceability](#36-togaf-architecture-decisions--traceability)
- [TOGAF Architecture Change Requests](#37-togaf-architecture-change-requests)
- [TOGAF Architecture Change Management](#h-togaf-architecture-change-management)
- [TOGAF Implementation Governance](#g-togaf-implementation-governance)

### Risk & Security (2)
- [TOGAF Risk Management](#38-togaf-risk-management)
- [TOGAF Security Architecture Integration](#39-togaf-security-architecture-integration)

</details>

## Diagrams

### 1. TOGAF ADM End-to-End Reference Map

A full TOGAF ADM end-to-end reference view connecting all Architecture Development Method phases with their key inputs, outputs, and inter-phase relationships in a single swimlane map.

<p align="center">
  <img src="docs/diagrams/adm/togaf-adm-end-to-end-architecture.png" alt="TOGAF ADM End-to-End Reference Map — horizontal swimlane diagram mapping all ADM phases with inputs, outputs, and cross-phase dependencies across the enterprise architecture lifecycle" width="90%"><br>
  <em>TOGAF ADM End-to-End Reference Map</em>
</p>

### 2. TOGAF ADM Cycle

The iterative TOGAF ADM cycle diagram showing all Architecture Development Method phases — Preliminary through A to H — organized around a central Requirements Management process at the core.

<p align="center">
  <img src="docs/diagrams/adm/togaf-adm-cycle-v2.png" alt="TOGAF ADM Cycle — circular flow diagram of ADM phases from Preliminary through H arranged around a central Requirements Management core in enterprise architecture" width="90%"><br>
  <em>TOGAF ADM Cycle — Architecture Development Method phases diagram</em>
</p>

<table>
<tr>
<td width="50%" valign="top">

### 3. Architecture Content Framework

A structured metamodel defining the types of architectural work products — deliverables, artifacts, and building blocks — produced across the ADM. The TOGAF Architecture Content Framework diagram illustrates how these work products are categorized and related within the overall enterprise architecture lifecycle.

</td>
<td width="50%" valign="top">

### 4. Enterprise Continuum & Architecture Repository

The TOGAF Enterprise Continuum is a classification system for architecture assets ranging from generic foundation architectures to organization-specific solutions, maintained in the TOGAF Architecture Repository.

</td>
</tr>
<tr>
<td width="50%" align="center">
  <img src="docs/diagrams/content-framework/togaf-phase-c-architecture-content-framework-v2.png" alt="TOGAF Architecture Content Framework — hierarchical diagram organizing enterprise architecture deliverables into metamodel categories, artifacts, and building blocks across the ADM lifecycle" width="100%"><br>
  <em>TOGAF Architecture Content Framework Diagram</em>
</td>
<td width="50%" align="center">
  <img src="docs/diagrams/continuum/togaf-phase-a-enterprise-continuum-architecture-repository-v2.png" alt="TOGAF Enterprise Continuum and Architecture Repository — spectrum diagram positioning enterprise architecture assets from generic foundation architectures to organization-specific solutions with repository classification layers" width="100%"><br>
  <em>TOGAF Enterprise Continuum & Architecture Repository</em>
</td>
</tr>
</table>

<table>
<tr>
<td width="50%" valign="top">

### 5. Capability Assessment & Maturity Models

Use this TOGAF capability assessment diagram to evaluate the maturity of your organization's enterprise architecture capabilities across key dimensions — from initial, ad-hoc practices through to optimising, repeatable governance. Based on the TOGAF capability maturity model, it supports architecture teams and CIOs in benchmarking current-state capability levels and identifying targeted improvement roadmaps aligned with ADM Phase B and Phase E planning.

</td>
<td width="50%" valign="top">

### 6. Architecture Building Blocks vs. Solution Building Blocks

This TOGAF diagram clarifies the distinction between Architecture Building Blocks (ABBs) and Solution Building Blocks (SBBs) — a core concept in the TOGAF content framework and reuse strategy. ABBs define what an architecture needs in vendor-neutral, abstract terms; SBBs deliver those needs as concrete, product-specific components. Use this comparison to guide reuse decisions, procurement strategies, and architecture-to-solution traceability throughout the ADM lifecycle.

</td>
</tr>
<tr>
<td width="50%" align="center">
  <img src="docs/diagrams/capability/togaf-phase-b-capability-assessment-maturity-models-v2.png" alt="TOGAF Capability Assessment and Maturity Models — grid-based maturity model rating enterprise architecture capabilities across defined levels from initial to optimising" width="100%"><br>
  <em>TOGAF Capability Assessment & Maturity Model — rate enterprise architecture capability levels from initial to optimising</em>
</td>
<td width="50%" align="center" valign="top">
  <img src="docs/diagrams/building-blocks/togaf-phase-a-architecture-building-blocks-vs-solution-building-blocks-v2.png" alt="TOGAF Architecture Building Blocks versus Solution Building Blocks — side-by-side comparison of abstract enterprise architecture building blocks against vendor-specific solution building blocks" width="100%"><br>
  <em>TOGAF Architecture Building Blocks (ABBs) vs Solution Building Blocks (SBBs) — abstract vs vendor-specific components</em>
</td>
</tr>
</table>

<table>
<tr>
<td width="50%" valign="top">

### 7. Stakeholder Map with Views & Concerns

This TOGAF stakeholder map shows how key enterprise architecture stakeholders — from business sponsors and CxOs to solution architects and operations teams — are matched to the architecture views and concerns most relevant to their role. Used in Phase A (Architecture Vision) and throughout the ADM, it drives stakeholder engagement planning, ensures the right views are produced for the right audiences, and supports targeted architecture communication.

</td>
<td width="50%" valign="top">

### 8. Architecture Governance Model

An overview of the TOGAF architecture governance framework — covering governance structures, oversight bodies, accountability mechanisms, and compliance controls that ensure architecture quality across the enterprise.

</td>
</tr>
<tr>
<td width="50%" align="center" valign="top">
  <img src="docs/diagrams/stakeholder/togaf-phase-a-stakeholder-map-views-concerns-v2.png" alt="TOGAF Stakeholder Map with Views and Concerns — matrix diagram mapping stakeholder roles to their relevant enterprise architecture views and primary concerns" width="100%"><br>
  <em>TOGAF Stakeholder Map with Views & Concerns — matching stakeholder roles to relevant architecture views and concerns</em>
</td>
<td width="50%" align="center" valign="top">
  <img src="docs/diagrams/governance/togaf-phase-a-architecture-governance-model-v2.png" alt="TOGAF Architecture Governance Model — layered governance diagram showing oversight structures, compliance review boards, and accountability flows between architecture levels" width="100%"><br>
  <em>TOGAF Architecture Governance Framework Diagram</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 9. Business Scenarios

In Phase A (Architecture Vision), Business Scenarios are used to identify and articulate the business problem, the environment in which it occurs, the key actors involved, and the desired outcomes. They provide the foundation for validating that the proposed architecture vision genuinely addresses real business needs and stakeholder goals. The diagrams below show two complementary perspectives: the ADM Phase A scenario structure, and a broader view of how business problems, stakeholder interactions, operational processes, and solution requirements support enterprise architecture development and transformation planning.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/stakeholder/togaf-phase-a-business-scenarios.png" alt="TOGAF Business Scenarios — flowchart showing how business drivers and problems are structured into scenarios that inform the Architecture Vision in Phase A" width="90%"><br>
  <em>Business Scenarios — Phase A ADM View</em>
</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/business/togaf-business-scenarios.png" alt="Diagram of TOGAF Business Scenarios showing how business problems, stakeholder interactions, operational processes, and solution requirements support enterprise architecture development and transformation planning" width="90%"><br>
  <em>Business Scenarios — Enterprise Architecture View</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 10. TOGAF Architecture Vision

Defines the high-level aspirational target architecture, stakeholder alignment, business value, scope, and transformation objectives that guide the enterprise architecture initiative. As the key TOGAF Phase A ADM deliverable, the Architecture Vision diagram sets the direction for all subsequent ADM phases.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/adm/togaf-architecture-vision.png" alt="Diagram of TOGAF Architecture Vision showing the high-level aspirational target architecture, stakeholder alignment, business value, scope, and transformation objectives" width="90%"><br>
  <em>TOGAF Architecture Vision</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 11. TOGAF Architecture Views & Viewpoints

This TOGAF architecture views and viewpoints diagram explains how enterprise architecture is communicated to different audiences. In TOGAF, a viewpoint defines the conventions for constructing a view; a view is what a stakeholder actually sees. This diagram shows how stakeholder concerns are mapped to defined viewpoints — business, data, application, technology — and how the resulting views support governance, decision-making, and transformation alignment throughout the ADM lifecycle.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-architecture-views-viewpoints.png" alt="Diagram of TOGAF Architecture Views and Viewpoints showing how stakeholder concerns are mapped to architecture viewpoints, views, governance communication, and transformation alignment" width="90%"><br>
  <em>TOGAF Architecture Views & Viewpoints — mapping stakeholder concerns to architecture views for governance and communication</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 12. TOGAF Stakeholder Management

This TOGAF stakeholder management diagram shows the structured, iterative process for identifying, classifying, engaging, and governing stakeholders across the enterprise architecture lifecycle. Effective stakeholder management is central to Phase A and runs continuously through the ADM — from understanding stakeholder power and interest through to managing concerns, tailoring communication, and ensuring architecture buy-in at all levels of the organization.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/stakeholder/togaf-stakeholder-management.png" alt="Diagram of TOGAF Stakeholder Management showing a structured approach for identifying, analysing, engaging, and governing stakeholders to support architecture alignment and transformation success" width="90%"><br>
  <em>TOGAF Stakeholder Management — identifying, engaging, and governing stakeholders across the ADM lifecycle</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 13. TOGAF Business Architecture

Defines the baseline and target business architecture, business capabilities, value streams, organizational structures, and business processes that support enterprise strategy and transformation objectives. This TOGAF Phase B business architecture diagram is a core deliverable of the ADM Business Architecture phase.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/business/togaf-business-architecture.png" alt="Diagram of TOGAF Business Architecture showing baseline and target business capabilities, value streams, organisational structures, and business processes supporting enterprise strategy" width="90%"><br>
  <em>TOGAF Business Architecture</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 14. TOGAF Data Architecture

This TOGAF Data Architecture diagram covers Phase C of the ADM, defining the structure, governance, lifecycle, and integration of enterprise data assets. It maps how data entities, logical data models, data flows, and governance policies support business capabilities, analytics platforms, regulatory compliance, and interoperability. Use it to align data strategy with business objectives and to plan baseline-to-target data architecture transitions.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/data/togaf-data-architecture.png" alt="Diagram of TOGAF Data Architecture showing the structure, governance, lifecycle, integration, and management of enterprise data assets supporting business capabilities and analytics" width="90%"><br>
  <em>TOGAF Data Architecture — Phase C data entities, governance, lifecycle, and integration across the enterprise</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 15. TOGAF Application Architecture

This TOGAF Application Architecture diagram covers Phase C of the ADM, mapping the enterprise application landscape — application components, services, interactions, integration patterns, and governance controls. It shows how application portfolios are structured to deliver business capabilities, support operational processes, and enable digital transformation. Use it to plan application rationalization, service-oriented architecture alignment, and baseline-to-target application transitions.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/application/togaf-application-architecture.png" alt="Diagram of TOGAF Application Architecture showing the structure, interaction, integration, governance, and lifecycle of enterprise applications and services supporting business capabilities" width="90%"><br>
  <em>TOGAF Application Architecture — Phase C application components, services, integration, and governance</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 16. TOGAF Architecture Repository

The TOGAF Architecture Repository is the central store for all architecture-related assets across the enterprise. This diagram shows its six components — Architecture Metamodel, Architecture Capability, Architecture Landscape, Standards Information Base, Reference Library, and Governance Log — and how repository consumers such as architecture teams, governance boards, and project delivery teams interact with them. It is essential for managing architecture reuse, standards compliance, and knowledge retention across the ADM.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/repository/togaf-architecture-repository.png" alt="Diagram of the TOGAF Architecture Repository showing governance assets, standards, reusable architecture knowledge, capability structures, and repository consumers" width="90%"><br>
  <em>TOGAF Architecture Repository — six components including Standards Information Base, Governance Log, and Reference Library</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 17. TOGAF Architecture Deliverables

This TOGAF Architecture Deliverables diagram maps the formal outputs produced at each ADM phase — from Architecture Vision and Architecture Definition Documents through to Transition Plans, Implementation Governance specs, and Architecture Compliance assessments. Unlike artifacts (which are internal working documents), TOGAF deliverables are contractual outputs subject to stakeholder review and sign-off. Use this diagram to understand what must be produced, reviewed, and baselined at each stage of the ADM lifecycle.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/content-framework/togaf-architecture-deliverables.png" alt="Diagram of TOGAF Architecture Deliverables showing formal ADM deliverables including architecture definitions, governance artifacts, transition plans, compliance outputs, and stakeholder communication packages" width="90%"><br>
  <em>TOGAF Architecture Deliverables — formal ADM outputs from Architecture Vision through Transition Plans and Compliance assessments</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 18. TOGAF Architecture Artifacts

This TOGAF Architecture Artifacts diagram organizes the full set of catalogs, matrices, and diagrams used throughout the ADM lifecycle. Catalogs list architecture entities (applications, data entities, technology components); matrices show relationships between them; diagrams visualize structures and flows. Each ADM phase produces a defined set of artifacts as working documents that support analysis, governance, and stakeholder communication — and feed into the formal deliverables.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-architecture-artifacts.png" alt="Diagram of TOGAF Architecture Artifacts showing catalogs, matrices, diagrams, and supporting artifacts used throughout the ADM lifecycle to document, analyze, communicate, and govern enterprise architecture" width="90%"><br>
  <em>TOGAF Architecture Artifacts — catalogs, matrices, and diagrams produced across ADM phases for governance and communication</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 19. TOGAF Capability-Based Planning

Explains how TOGAF uses capability-based planning and business capability planning to identify, assess, prioritize, and roadmap enterprise capabilities that support strategic transformation and business value realization.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-capability-based-planning.png" alt="Diagram of TOGAF Capability-Based Planning showing how enterprise capabilities are identified, assessed, prioritized, and roadmapped to support strategic transformation and business value realization" width="90%"><br>
  <em>TOGAF Capability-Based Planning</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 20. TOGAF Architecture Metamodel

The TOGAF Architecture Metamodel is the formal definition of architecture element types — motivations, actors, business services, data entities, application components, and technology nodes — and the relationships between them that make enterprise architecture coherent and traceable. Applied across Phases B, C, and D of the ADM, it ensures that models produced by different teams share a common vocabulary and structural grammar, enabling cross-domain impact analysis, governance enforcement, and consistent architecture documentation. Enterprise architects, modeling practitioners, and governance boards use this metamodel to align deliverables, validate work products, and maintain a single authoritative view of architecture structure across the enterprise portfolio.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-architecture-metamodel.png" alt="Diagram of the TOGAF Architecture Metamodel showing structural relationships between business, data, application, and technology architecture elements supporting consistency, traceability, and governance alignment" width="90%"><br>
  <em>TOGAF Architecture Metamodel — element types and cross-domain structural relationships for consistent, traceable enterprise architecture modeling</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 21. TOGAF Architecture Partitioning

A visual overview of TOGAF Architecture Partitioning showing how enterprise architectures are separated across strategic, segment, capability, business unit, and solution levels to support governance, scalability, reuse, and controlled transformation. This enterprise architecture partitioning diagram is essential for managing complexity across large-scale architecture programs.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-architecture-partitioning.png" alt="Diagram of TOGAF Architecture Partitioning showing how enterprise architectures are separated across strategic, segment, capability, business unit, and solution levels to support governance, scalability, reuse, and controlled transformation" width="90%"><br>
  <em>TOGAF Architecture Partitioning</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 22. TOGAF Architecture Communication

Architecture communication in TOGAF is the structured practice of ensuring that the right architecture information reaches the right stakeholders — in formats, language, and channels suited to their role, concerns, and decision-making needs. This diagram covers how communication plans are developed in Phase A, maintained throughout the ADM, and tailored for audiences ranging from executive sponsors and governance boards to solution delivery teams and operational managers. It illustrates the feedback loops, reporting cadences, and escalation paths that keep stakeholders aligned with architecture decisions and transformation progress across the full enterprise architecture lifecycle.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/architecture/togaf-architecture-communication.png" alt="Diagram of TOGAF Architecture Communication showing how architecture information, governance messaging, stakeholder alignment, executive reporting, and delivery coordination support enterprise transformation success" width="90%"><br>
  <em>TOGAF Architecture Communication — communication plans, stakeholder reporting channels, and governance messaging across all ADM phases</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 23. TOGAF Architecture Landscape

The TOGAF Architecture Landscape is the Architecture Repository component that holds a structured inventory of all enterprise architecture descriptions — organized across three levels: Strategic Architecture (enterprise-wide direction), Segment Architecture (business unit or domain scope), and Capability Architecture (focused, time-boxed solutions). Architecture and governance teams consult the Landscape throughout the ADM — especially in Phase E and Phase F — to identify gaps between baseline and target states, surface reuse opportunities, sequence work packages, and ensure that new initiatives build on approved architecture rather than creating isolated solutions. This diagram shows how the Landscape layers interrelate and feed into planning, governance, and change management processes.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/repository/togaf-architecture-landscape.png" alt="Diagram showing enterprise architecture assets organised across strategic, segment, and capability levels with links to governance, reuse, and planning" width="90%"><br>
  <em>TOGAF Architecture Landscape — Strategic, Segment, and Capability Architecture levels supporting gap analysis, reuse, and governance-controlled evolution</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 24. TOGAF Enterprise Continuum

The TOGAF Enterprise Continuum is the classification framework that organizes the full spectrum of reusable architecture assets — from generic Foundation Architectures (TOGAF itself, Zachman, ISO standards) through Common Systems Architectures and Industry Architectures, to organization-specific Enterprise Architectures tailored to a particular company's context. Moving from left to right along the continuum, assets become progressively more specific and contextualized, giving architecture teams a governed pathway from generic best-practice patterns to bespoke enterprise solutions. Used during Phase A and reinforced throughout the ADM, the Enterprise Continuum enables architects to leverage existing investments, accelerate delivery by reusing approved patterns, and avoid duplication across business units or solution domains.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/continuum/togaf-enterprise-continuum.png" alt="Diagram of the TOGAF Enterprise Continuum showing architecture assets evolving from generic foundation architectures to organization-specific enterprise solutions" width="90%"><br>
  <em>TOGAF Enterprise Continuum — spectrum from Foundation and Common Systems Architectures to organization-specific Industry and Enterprise Architectures</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 25. TOGAF Reference Architectures

TOGAF Reference Architectures are formally validated, reusable architecture templates that encapsulate proven patterns, technology standards, and implementation guidance for specific problem domains — covering areas such as cloud platform architectures, enterprise integration layers, security reference models, and data platform designs. Stored in the Architecture Repository's Reference Library, they give architecture teams a pre-approved, governance-aligned starting point for designing solutions during Phases B, C, D, and E of the ADM, dramatically reducing time-to-design and limiting delivery risk. This diagram shows how reference architectures are sourced, classified, maintained, and applied — and how they interact with Building Blocks, the Standards Information Base, and the broader Enterprise Continuum to support consistent, standards-aligned solution delivery across the enterprise.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/repository/togaf-reference-architectures.png" alt="Diagram of TOGAF Reference Architectures showing reusable architecture models, standards, patterns, and implementation guidance supporting solution delivery and enterprise governance" width="90%"><br>
  <em>TOGAF Reference Architectures — validated reusable architecture patterns and templates from the Architecture Repository Reference Library</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 26. TOGAF Architecture Building Blocks (ABBs)

A visual overview of TOGAF Architecture Building Blocks (ABBs) showing how reusable logical architecture capabilities, standards, services, and governance models define enterprise architecture intent and guide the realization of Solution Building Blocks and enterprise solutions.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/building-blocks/togaf-architecture-building-blocks.png" alt="Diagram of TOGAF Architecture Building Blocks showing reusable logical capabilities, standards, services, and governance models guiding the realization of Solution Building Blocks" width="90%"><br>
  <em>TOGAF Architecture Building Blocks (ABBs)</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 27. TOGAF Solution Building Blocks (SBBs)

A visual overview of TOGAF Solution Building Blocks (SBBs) showing how reusable technology components, platforms, integrations, operational services, and governance capabilities implement enterprise architecture solutions and enable standardized, scalable delivery.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/building-blocks/togaf-solution-building-blocks.png" alt="Diagram of TOGAF Solution Building Blocks showing reusable technology components, platforms, integrations, operational services, and governance capabilities implementing enterprise architecture solutions" width="90%"><br>
  <em>TOGAF Solution Building Blocks (SBBs)</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 28. Standards Information Base

A visual overview of the TOGAF Standards Information Base showing approved enterprise standards, technology policies, security controls, compliance requirements, governance lifecycle, and consumers who use standards to support architecture consistency and enterprise compliance.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/repository/togaf-standards-information-base.png" alt="Diagram of the TOGAF Standards Information Base showing approved enterprise standards, technology policies, security controls, compliance requirements, governance lifecycle, and standards consumers" width="90%"><br>
  <em>Standards Information Base</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 29. TOGAF Governance Log

A visual overview of the TOGAF Governance Log showing architecture decisions, compliance activities, governance oversight, risk and exception management, audit traceability, and continuous governance evolution supporting enterprise accountability and compliance.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/repository/togaf-governance-log.png" alt="Diagram of the TOGAF Governance Log showing architecture decisions, compliance activities, governance oversight, risk and exception management, audit traceability, and continuous governance evolution" width="90%"><br>
  <em>TOGAF Governance Log</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 30. TOGAF Architecture Principles

A visual overview of TOGAF Architecture Principles showing how business, data, application, technology, and governance principles guide enterprise decision-making, standards alignment, architecture quality, and consistent solution delivery.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-architecture-principles.png" alt="Diagram of TOGAF Architecture Principles showing business, data, application, technology, and governance principles guiding enterprise decision-making and architecture quality" width="90%"><br>
  <em>TOGAF Architecture Principles</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 31. TOGAF Architecture Capability

A visual overview of TOGAF Architecture Capability showing the governance structures, people, processes, tools, repository support, maturity practices, and continuous improvement mechanisms required to develop, govern, and sustain enterprise architecture across the organization.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/capability/togaf-architecture-capability.png" alt="Diagram of TOGAF Architecture Capability showing governance structures, people, processes, tools, repository support, maturity practices, and continuous improvement mechanisms for enterprise architecture" width="90%"><br>
  <em>TOGAF Architecture Capability</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 32. TOGAF Architecture Contracts

A visual overview of TOGAF Architecture Contracts showing governance agreements, architecture expectations, compliance obligations, responsibilities, delivery alignment, risk and exception management, and implementation accountability across the enterprise.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-architecture-contracts.png" alt="Diagram of TOGAF Architecture Contracts showing governance agreements, compliance obligations, responsibilities, delivery alignment, and implementation accountability" width="90%"><br>
  <em>TOGAF Architecture Contracts</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 33. TOGAF Architecture Compliance Reviews

A visual overview of TOGAF Architecture Compliance Reviews showing how enterprise solutions are assessed against architecture principles, standards, governance requirements, risks, and compliance obligations to ensure alignment and delivery readiness.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-architecture-compliance-reviews.png" alt="Diagram of TOGAF Architecture Compliance Reviews showing assessment of solutions against architecture principles, standards, governance requirements, risks, and compliance obligations" width="90%"><br>
  <em>TOGAF Architecture Compliance Reviews</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 34. TOGAF Compliance Assessment

A visual overview of TOGAF Compliance Assessment showing how enterprise architecture compliance, governance validation, standards alignment, and delivery oversight support controlled enterprise transformation.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-compliance-assessment.png" alt="Diagram of TOGAF Compliance Assessment showing how enterprise architecture compliance, governance validation, standards alignment, and delivery oversight support controlled enterprise transformation" width="90%"><br>
  <em>TOGAF Compliance Assessment</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 35. TOGAF Governance Repository

A centralized governance repository that stores architecture decisions, compliance records, policies, audit evidence, approvals, and governance outcomes supporting enterprise accountability, traceability, and regulatory alignment.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-governance-repository.png" alt="A centralized governance repository that stores architecture decisions, compliance records, policies, audit evidence, approvals, and governance outcomes supporting enterprise accountability, traceability, and regulatory alignment." width="90%"><br>
  <em>TOGAF Governance Repository</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 36. TOGAF Architecture Decisions & Traceability

A visual overview of TOGAF Architecture Decisions & Traceability showing how architecture decisions, governance approvals, rationale, dependencies, and traceability relationships are managed across enterprise transformation initiatives.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-architecture-decisions-traceability.png" alt="Diagram of TOGAF Architecture Decisions and Traceability showing how architecture decisions, governance approvals, rationale, dependencies, and traceability relationships are managed across enterprise transformation initiatives" width="90%"><br>
  <em>TOGAF Architecture Decisions & Traceability</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 37. TOGAF Architecture Change Requests

A visual overview of TOGAF Architecture Change Requests showing how enterprise architecture changes are identified, assessed, governed, approved, and implemented across transformation initiatives.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-architecture-change-requests.png" alt="Diagram of TOGAF Architecture Change Requests showing how enterprise architecture changes are identified, assessed, governed, approved, and implemented across transformation initiatives" width="90%"><br>
  <em>TOGAF Architecture Change Requests</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 38. TOGAF Risk Management

A visual overview of TOGAF Risk Management showing how enterprise architecture risks are identified, assessed, governed, mitigated, and continuously monitored across transformation initiatives and ADM activities.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-risk-management.png" alt="Diagram of TOGAF Risk Management showing how enterprise architecture risks are identified, assessed, governed, mitigated, and continuously monitored across transformation initiatives and ADM activities" width="90%"><br>
  <em>TOGAF Risk Management</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 39. TOGAF Security Architecture Integration

A visual overview of TOGAF Security Architecture Integration showing how security controls, governance, compliance, resilience, and risk management are embedded across business, data, application, and technology architecture domains.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/security/togaf-security-architecture-integration.png" alt="Diagram of TOGAF Security Architecture Integration showing how security controls, governance, compliance, resilience, and risk management are embedded across business, data, application, and technology architecture domains" width="90%"><br>
  <em>TOGAF Security Architecture Integration</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### 40. TOGAF Requirements Management

The TOGAF ADM Architecture Requirements Management process is continuous and shown at the core of the ADM cycle — it captures, validates, prioritizes, manages, and governs architecture requirements across all ADM phases to ensure alignment with business objectives and solution delivery.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-requirements-management.png" alt="Diagram of TOGAF Requirements Management showing the continuous process of capturing, validating, prioritising, managing, and governing architecture requirements across all ADM phases" width="90%"><br>
  <em>TOGAF Requirements Management</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### D. TOGAF Technology Architecture

A layered view of TOGAF Technology Architecture showing infrastructure foundations, platform services, integration capabilities, security architecture, operational resilience, and key technology outputs.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/technology/togaf-phase-d-technology-architecture.png" alt="Layered diagram of TOGAF Technology Architecture covering infrastructure, platform services, integration, security, and operational resilience" width="90%"><br>
  <em>TOGAF Technology Architecture</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### E. Opportunities & Solutions

A Phase E diagram illustrating gap analysis, candidate solutions, work packages, transition architectures, and roadmap planning used to move from baseline to target architecture.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/planning/togaf-phase-e-opportunities-solutions-v1.png" alt="TOGAF Opportunities and Solutions Diagram - Phase E - gap analysis candidate solutions work packages and roadmap planning" width="90%"><br>
  <em>Opportunities & Solutions</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### F. Migration Planning

A TOGAF Phase F diagram illustrating implementation sequencing, migration planning, dependency management, governance alignment, and realization of the target architecture.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/planning/togaf-phase-f-migration-planning.png" alt="TOGAF Migration Planning Diagram - Phase F - implementation sequencing dependency management and governance alignment" width="90%"><br>
  <em>Migration Planning</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### G. TOGAF Implementation Governance

A TOGAF Phase G diagram illustrating architecture compliance, governance oversight, change management, implementation support, and realization of approved target architectures.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/phase-g-implementation-governance.png" alt="Phase G diagram showing architecture compliance, governance oversight, change management, and implementation support for target architecture realization" width="90%"><br>
  <em>TOGAF Implementation Governance</em>
</td>
</tr>
</table>

<table>
<tr>
<td valign="top">

### H. TOGAF Architecture Change Management

A TOGAF Phase H diagram illustrating change assessment, governance decisioning, architecture evolution, continuous improvement, and re-initiation of the ADM lifecycle.

</td>
</tr>
<tr>
<td align="center">
  <img src="docs/diagrams/governance/togaf-phase-h-architecture-change-management.png" alt="TOGAF Architecture Change Management Diagram - Phase H - change assessment governance decisioning and ADM re-initiation" width="90%"><br>
  <em>TOGAF Architecture Change Management</em>
</td>
</tr>
</table>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This repository is licensed under the [MIT License](./LICENSE).
