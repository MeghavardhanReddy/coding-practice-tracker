# ACDYON Technologies Frontend Challenge — TrackMyCode

## 1. Why this approach?

I chose **Part 2 — The Premium Home Page** and extended my existing Flask + MySQL Coding Practice Tracker instead of rebuilding the product with a new frontend stack.

The existing application already provides authentication, problem tracking, practice sessions, dashboard statistics, charts, and practice history. Keeping that foundation let me focus the limited challenge time on the areas ACDYON explicitly evaluates: product presentation, responsive UI, interaction design, and visual polish.

I chose a standalone Jinja2 landing page with dedicated homepage CSS rather than introducing React or a new build system. This kept the implementation small, preserved the existing application, and allowed the homepage to showcase real product capabilities without inventing a separate demo application.

The visual direction uses an obsidian background with electric cyan/blue and digital orange accents. The orange/cyan energy language is also used in the navigation transitions so the motion has a functional relationship with the product instead of being purely decorative.

## 2. Trade-off under the time limit

I prioritized the public homepage, product showcase, responsive behavior, and navigation transitions over adding new product functionality.

With a full week, I would spend additional time on deeper accessibility testing, more extensive cross-browser testing, performance optimization of the visual effects, and further refinement of the dashboard and mobile navigation states.

I deliberately avoided adding features that were not already supported by the application, such as new analytics systems, AI functionality, fake social proof, or additional product workflows.

## 3. AI usage and personal verification

I used AI tools during the implementation for repository analysis, UI/UX brainstorming, code generation, debugging, responsive-design review, and implementation planning.

I personally reviewed the generated changes, controlled which files could be modified, tested the application locally, checked the Git diffs, verified the existing authentication and application routes, and refined the implementation decisions.

The final implementation was kept aligned with the existing Flask/Jinja2 architecture rather than accepting a complete rewrite or introducing unnecessary frameworks.

The AI-assisted code was not treated as a black box: I reviewed the generated files and verified the behavior before committing the work.
