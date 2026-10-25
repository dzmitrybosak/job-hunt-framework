# Gap close – Atlassian / Senior Mobile iOS Engineer

Date: 2026-10-20
Based on: gap-analysis from 2026-10-20

## Gap 1: GraphQL APIs (partial in requirements)

There is no GraphQL in the work history, so this gap cannot be closed with real experience and must not be faked. What transfers is API-contract work at scale: the client-side synchronization between mobile apps, user accounts and distributed backends was designed around explicit REST contracts, versioning and error semantics – the same design muscle GraphQL schemas demand. For the interview, be upfront: strong REST design experience, GraphQL fundamentals learned on the side.

- Designed client-side synchronization between mobile apps, user accounts and distributed REST/JSON backends, including contract versioning and error handling (Property & Access Management Platform, 500K+ DAU).
- Compensation: learn GraphQL client fundamentals (queries, mutations, caching) before a technical round; describe REST-to-GraphQL as a transferable API-design skill, not as hands-on experience.

## Gap 2: XCUITest / UI testing (partial in requirements)

Unit testing is strong and documented; UI test automation is not. The honest close is the testing culture itself: taking coverage from 13% to 75% with XCTest and Swift Testing, wiring checks into CI, and using ViewInspector for view-level assertions – the same discipline XCUITest extends to the UI layer.

- Increased unit test coverage from 13% to 75% and wired tests and static checks into the CI pipeline (XCTest, Swift Testing, ViewInspector; Azure DevOps, Bitrise, GitHub Actions).
- Compensation: review XCUITest basics (synchronization, page objects, CI integration) before interviews and frame the testing philosophy: catch regressions before release at the cheapest possible layer.

## Gap 3: Security and privacy discipline (partial in requirements)

The JD is about Guard – security and data governance – and asks for a security-conscious mindset when handling sensitive data. Direct secure-SDLC documentation is thin in the CV, but the domain is close: access management flows with permissions, restrictions and error handling on products with sensitive user data, plus a private-by-design personal product. The close is to make this domain experience visible rather than to claim security certifications.

- Developed access-management flows with permissions, restrictions and error handling for a platform serving 160K+ DAU, working with sensitive user data and account states (Swift, UIKit, Combine).
- Designed a private-by-design personal product (Between: Decision Journal): user reflections stay in a private journal with user-controlled data lifecycle (SwiftUI, Swift backend).
- Compensation: prepare concrete mobile security practices to speak about (Keychain storage, certificate pinning, data minimization, jailbreak/root detection) as working knowledge.

## What cannot be closed (honestly)

- **Hands-on GraphQL** → compensation: transferable REST API design + fast self-study; state it openly in interviews.
- **XCUITest hands-on** → compensation: XCUITest basics before interviews; strong unit-testing culture as the foundation.
- **Formal security/privacy engineering** → compensation: domain adjacency (access management) + prepared talking points on mobile security practices.
- **Location eligibility (Belarus under Team Anywhere)** → not a CV gap but the hard gate: resolve with the recruiter before any interview investment.
