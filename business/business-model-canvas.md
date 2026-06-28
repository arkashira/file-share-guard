# Business Model Canvas

## Customer Segments
- Small and medium businesses (SMBs) needing secure internal file transfer – ~500 USD/month per seat (~17,500 THB)  
- Remote/distributed teams (developers, designers) sharing large assets – ~30 USD/user‑month (~1,050 THB)  
- Privacy‑conscious individuals & freelancers seeking self‑hosted alternatives to public file‑share services – ~5 USD/user‑month (~175 THB)  
- Educational institutions & NGOs with budget constraints looking for free, auditable solutions – potential grant‑funded deployments  
- Managed service providers (MSPs) offering secure file‑share as a value‑added service – revenue share model  

## Value Propositions
- Fully self‑hosted, open‑source code – zero vendor lock‑in, auditability  
- Automated link expiration (configurable TTL) reduces exposure window – average risk reduction 70% vs. static links  
- Optional password protection adds a second factor for sensitive files – compliance‑friendly (GDPR, PDPA)  
- Lightweight (<10 MB Docker image) and fast deployment (<5 min) – low ops overhead  
- No per‑file or bandwidth fees – predictable OPEX, cost savings vs. SaaS alternatives (~30‑50 % lower)  

## Channels
- GitHub repository (stars, forks, issues) – primary acquisition for dev‑centric users  
- Docker Hub & Helm charts – easy one‑click deployments for sysadmins  
- Technical blog posts & YouTube tutorials – SEO‑driven inbound traffic (~2 k monthly visits)  
- Community forums (Discord, Reddit r/selfhosted) – peer‑to‑peer support & word‑of‑mouth  
- Partnerships with MSPs & VARs – co‑marketing and referral fees  

## Customer Relationships
- Community‑driven support via GitHub Issues & Discord – SLA‑free, rapid peer response  
- Comprehensive documentation & setup guides – self‑service onboarding  
- Optional paid support tiers (email/chat, 2‑hour response) – $150/month per contract (~5,250 THB)  
- Enterprise consulting & customization engagements – $2,000‑$5,000 per project (~70‑175 k THB)  
- Regular security audit reports & CVE notifications – trust building for compliance‑focused buyers  

## Revenue Streams
- Paid support subscriptions (Standard: $150/mo, Pro: $350/mo) – 5‑10 % of active installs  
- Custom feature development & integration services – $120‑$180/hr (~4,200‑6,300 THB/hr)  
- Hosted SaaS offering (managed file‑share‑guard) – $10/user‑month (~350 THB) for users preferring no‑ops  
- Annual enterprise license (includes priority support & warranty) – $5,000‑$15,000 (~175‑525 k THB)  
- Donations / GitHub Sponsors & Open Collective – supplemental community funding  

## Key Resources
- Core codebase (Go/React) and CI/CD pipeline (GitHub Actions)  
- Active contributor community (~30 regular contributors)  
- Documentation site & multilingual FAQ (EN/TH)  
- Docker images & Helm charts hosted on Docker Hub & GitHub Packages  
- Security audit reports & vulnerability disclosure process  

## Key Activities
- Continuous development & bi‑weekly release cycle (feature + security patches)  
- Community engagement (triaging issues, PR reviews, AMAs)  
- Maintenance of Docker/Helm charts and compatibility testing (K8s, VM, bare‑metal)  
- Conducting annual third‑party security audits & penetration testing  
- Marketing & outreach (blog, webinars, conference talks)  

## Key Partners
- Cloud providers (AWS, GCP, Azure) for marketplace listings & referral credits  
- Open‑source foundations (CNCF, Apache) for credibility & joint events  
- Security firms (e.g., HackerOne, Bugcrowd) for bounty programs & audits  
- Localization volunteers for Thai language support & TH‑market outreach  
- MSPs & VARs that bundle file‑share‑guard into broader IT service packages  

## Cost Structure
- Developer salaries (2 FTE engineers) – $12,000/mo (~420 k THB)  
- Cloud infra for CI/CD, demo instances, and monitoring – $800/mo (~28 k THB)  
- Security audit & penetration testing (annual) – $4,000 (~140 k THB)  
- Legal & compliance (licensing, DPAs) – $500/mo (~17.5 k THB)  
- Marketing & community events (swag, webinars, local meetups) – $1,000/mo (~35 k THB)  
- Miscellaneous (domain, banking, office) – $300/mo (~10.5 k THB)