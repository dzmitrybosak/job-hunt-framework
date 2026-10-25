# Gap analysis – Atlassian / Senior Mobile iOS Engineer

- Mode: A (by JD)
- Date: 2026-10-20
- Link: https://www.atlassian.com/company/careers/details/26545

## Match: 86% – strong fit

Calculation: must 0.80 × 0.7 + nice 1.00 × 0.3
The core stack of the JD maps almost 1:1 to the CV: 7+ years of Swift/iOS, architecture patterns, REST, APNs, CI/CD with Bitrise, XCTest. Partial zones: GraphQL (not in the CV), XCUITest (unit testing is strong, UI testing is not documented), security/privacy as a formal discipline (the access-management domain is close but not the same). The decisive unknown is not technical at all: Team Anywhere requires an Atlassian legal entity in the employee's country – Belarus is unconfirmed. Main action: resolve location eligibility before investing interview time.

## Verdict

Technically a strong fit for a Senior role at scale. The employer's pain is security, reliability and audit at massive scale – this is exactly where the 99.8% crash-free / 500K+ DAU story plays. Risks in order: (1) Belarus eligibility under Team Anywhere, (2) GraphQL + XCUITest gaps, (3) compensation not published. Recommend applying only after a recruiter answer on location; the drafts are prepared accordingly.

## Must-have

| Requirement | Status | What from the CV to use |
|---|---|---|
| 7+ years of native iOS development with Swift | ✅ full | 7+ years: Orangesoft (01/2019 – 10/2021) + Coherent Solutions (10/2021 – Present) |
| Strong grasp of iOS architecture patterns | ✅ full | MVVM, Clean Architecture, feature-based modularization with Swift Package Manager (Access Management Platform) |
| REST/GraphQL APIs | ⚠️ partial | REST full: client-side sync with distributed REST backends (Property & Access, 500K+ DAU); GraphQL not in the history |
| Push notifications (APNs) | ✅ full | APNs in core skills; real-time notification flows in Property & Access Management Platform |
| CI/CD for iOS (Fastlane, Bitrise) + automated testing pipelines | ✅ full | Bitrise, Azure DevOps, GitHub Actions; tests and static checks wired into CI (AI-SDLC validation loop); Fastlane itself not listed – quick ramp-up |
| Unit and UI testing frameworks (XCTest, XCUITest) | ⚠️ partial | XCTest + Swift Testing + ViewInspector (unit strong: coverage 13% → 75%); XCUITest not documented |
| Security- and privacy-conscious mindset | ⚠️ partial | Access-management domain (permissions, restrictions, error flows), private-by-design pet project Between; formal secure SDLC not documented |
| Collaboration in a distributed, cross-functional environment | ⚠️ partial | Cross-functional teams (iOS, Android, Backend, QA manual+automation, BA, UX), code reviews, mentoring, interviewing; "distributed" mode itself not documented |
| Solving complex problems, performant and user-centric solutions (soft) | ✅ full | Performance work (builds, uploads, crash-free), product-initiative bullets (UI/UX proposals, user-flow definition) |
| Exposure to modern iOS software design strategies | ✅ full | MVVM/Clean/modular SPM, UIKit → SwiftUI migration, Swift Concurrency, Observation (Between), spec-driven AI-SDLC |

## Nice-to-have

| Requirement | Status | Comment |
|---|---|---|
| Evaluating and adopting new iOS technologies | ✅ full | SwiftUI/WidgetKit/App Intents adoption, Swift Testing adoption, AI-assisted SDLC, personal lab for new tech (Between) |
| Using analytics data for architecture/UI decisions | ✅ full | Engineered analytics architecture with event validation; data-driven product decisions (Access Management Platform) |
| Modern iOS libraries and components | ✅ full | Combine, Swift Concurrency, Lottie, Dependencies, WebRTC, ViewInspector, CocoaAsyncSocket |

## Gaps and what to do with them

- **GraphQL** → cannot be closed with real experience; do not fake it. Compensation: speak to strong REST design experience and API-contract work; pick up GraphQL fundamentals before a technical round (client-side queries/caching concepts).
- **XCUITest (UI testing)** → partially closeable: unit testing culture (13% → 75% coverage) and ViewInspector; compensate by reviewing XCUITest basics before interviews and framing the testing philosophy.
- **Security/privacy discipline** → partially closeable: access-management domain + private-by-design Between; compensate with preparation on secure mobile practices (keychain, certificate pinning, data minimization) to speak concretely.
- **"Distributed" collaboration** → partially closeable: cross-functional teamwork is documented; compensate by describing the actual remote/async practices used (spec-driven docs, code review, AI-SDLC validation loop).

## What to highlight

- Reliability at scale: 99.8% crash-free on 160K+ DAU and features for 500K+ DAU apps – direct parallel with "secure and reliable at massive scale" from the JD.
- Testing culture: coverage from 13% to 75% with XCTest/Swift Testing wired into CI – matches their "maintain high test coverage" responsibility.
- Security-sensitive domain: access management with permissions/restrictions and sensitive user data.
- Analytics discipline: event architecture with validation from day one – maps to their nice-to-have about analytics-driven decisions.
- Stepping beyond iOS: AI-SDLC tooling and Swift backend work (Between) show the "step beyond the platform" muscle they ask for.
