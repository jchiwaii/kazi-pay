import { useState } from "react";

const navLinks = [
  { label: "About", href: "#about" },
  { label: "Features", href: "#features" },
  { label: "Trust", href: "#trust" },
  { label: "Contact", href: "#footer" },
];

const quickPoints = [
  "Escrow locked before work",
  "Client approves release",
  "USSD and SMS ready",
];

const sectors = [
  "Plumbers",
  "Electricians",
  "Boda riders",
  "Repair crews",
  "Movers",
  "Home services",
];

const featureCards = [
  {
    icon: "shield",
    title: "Escrow comes first",
    text: "Money is secured at the beginning, so the worker is not gambling on whether payment will appear later.",
  },
  {
    icon: "layers",
    title: "Job flow stays visible",
    text: "Clients and workers can both follow the status from payment request to active work to final release.",
  },
  {
    icon: "spark",
    title: "Release stays intentional",
    text: "The payout happens when the work is confirmed, giving the client control without making the worker wait forever.",
  },
];

const showcaseRows = [
  {
    title: "Kitchen sink repair",
    owner: "Amina Njoroge",
    initials: "AN",
    status: "Approved",
    statusTone: "positive",
    team: "Plumbing",
    priority: "High",
    priorityTone: "warning",
    updated: "1 hr ago",
  },
  {
    title: "Generator service",
    owner: "Brian Odhiambo",
    initials: "BO",
    status: "Review",
    statusTone: "warning",
    team: "Field Ops",
    priority: "Medium",
    priorityTone: "neutral",
    updated: "2 hrs ago",
  },
  {
    title: "Office rewiring",
    owner: "Faith Wanjiku",
    initials: "FW",
    status: "Locked",
    statusTone: "neutral",
    team: "Electrical",
    priority: "High",
    priorityTone: "warning",
    updated: "Yesterday",
  },
  {
    title: "Move-out cleaning",
    owner: "Kevin Maina",
    initials: "KM",
    status: "Approved",
    statusTone: "positive",
    team: "Cleaning",
    priority: "Low",
    priorityTone: "positive",
    updated: "4 hrs ago",
  },
  {
    title: "Courier payout release",
    owner: "Janet Atieno",
    initials: "JA",
    status: "Review",
    statusTone: "warning",
    team: "Operations",
    priority: "Low",
    priorityTone: "positive",
    updated: "1 hr ago",
  },
  {
    title: "Water tank cleaning",
    owner: "Peter Mwangi",
    initials: "PM",
    status: "Locked",
    statusTone: "neutral",
    team: "Field Ops",
    priority: "Medium",
    priorityTone: "neutral",
    updated: "2 hrs ago",
  },
];

const trustCards = [
  {
    size: "large",
    eyebrow: "Client confidence",
    title: "You can commit funds without losing control of the outcome.",
    text: "KaziPay separates paying from overpaying. The client locks the amount, the task moves, and the final release still waits for confirmation.",
  },
  {
    size: "large",
    eyebrow: "Worker confidence",
    title: "A funded job feels completely different from a verbal promise.",
    text: "Workers accept with more certainty because the money is already reserved through a familiar payment rail.",
  },
  {
    size: "small",
    eyebrow: "Clear states",
    title: "Posted, funded, active, completed.",
    text: "The system should always answer where the money is and what happens next.",
  },
  {
    size: "small",
    eyebrow: "Fast release",
    title: "Completion should feel immediate.",
    text: "Once the client approves, the payout moves without an awkward gap between work and payment.",
  },
  {
    size: "small",
    eyebrow: "Low-data friendly",
    title: "Modern without excluding real conditions.",
    text: "The experience should still make sense when internet is patchy and phones are basic.",
  },
];

const footerColumns = [
  {
    title: "Explore",
    links: [
      { label: "About", href: "#about" },
      { label: "Features", href: "#features" },
      { label: "Operations", href: "#showcase" },
      { label: "Trust", href: "#trust" },
    ],
  },
  {
    title: "Platform",
    links: [
      { label: "Escrow-first jobs", href: "#features" },
      { label: "Release reviews", href: "#showcase" },
      { label: "Client approval flow", href: "#trust" },
      { label: "Back to top", href: "#top" },
    ],
  },
];

const footerSocials = ["in", "ig", "tg"];

function AuroraBackdrop() {
  return (
    <div aria-hidden="true" className="aurora">
      <div className="aurora__layer aurora__layer--one" />
      <div className="aurora__layer aurora__layer--two" />
      <div className="aurora__layer aurora__layer--three" />
      <div className="aurora__grid" />
      <div className="aurora__veil" />
    </div>
  );
}

function LogoMark() {
  return (
    <a href="#top" className="flex items-center gap-3">
      <div className="brand-chip">
        <span />
      </div>
      <div>
        <p className="text-base font-extrabold tracking-[-0.04em] text-white">
          KaziPay
        </p>
        <p className="text-[11px] font-extralight uppercase tracking-[0.28em] text-white/60">
          Escrow for gig work
        </p>
      </div>
    </a>
  );
}

function CheckIcon() {
  return (
    <svg aria-hidden="true" className="h-4 w-4" fill="none" viewBox="0 0 24 24">
      <path
        d="M6.5 12.5 10 16l7.5-8"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="2.2"
      />
    </svg>
  );
}

function FeatureIcon({ type }) {
  if (type === "chart") {
    return (
      <svg aria-hidden="true" className="h-5 w-5" fill="none" viewBox="0 0 24 24">
        <path
          d="M4 18.5h16M7 15l3-3 2.5 2.5L17 9"
          stroke="currentColor"
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="1.8"
        />
        <path
          d="M7 18.5v-3.5m5.5 3.5v-4m4.5 4V9"
          stroke="currentColor"
          strokeLinecap="round"
          strokeWidth="1.8"
        />
      </svg>
    );
  }

  if (type === "shield") {
    return (
      <svg aria-hidden="true" className="h-5 w-5" fill="none" viewBox="0 0 24 24">
        <path
          d="M12 3.5 6 6v5.7c0 4 2.5 7 6 8.8 3.5-1.8 6-4.8 6-8.8V6l-6-2.5Z"
          stroke="currentColor"
          strokeWidth="1.8"
        />
      </svg>
    );
  }

  if (type === "layers") {
    return (
      <svg aria-hidden="true" className="h-5 w-5" fill="none" viewBox="0 0 24 24">
        <path
          d="m12 5 8 4.5L12 14 4 9.5 12 5Zm0 7.5 8 4.5L12 21 4 17l8-4.5Z"
          stroke="currentColor"
          strokeWidth="1.8"
        />
      </svg>
    );
  }

  return (
    <svg aria-hidden="true" className="h-5 w-5" fill="none" viewBox="0 0 24 24">
      <path
        d="M12 3v6m0 6v6M3 12h6m6 0h6m-3.5-5.5L15 9m-6 6-2.5 2.5m0-11L9 9m6 6 2.5 2.5"
        stroke="currentColor"
        strokeLinecap="round"
        strokeWidth="1.8"
      />
    </svg>
  );
}

function PrimaryButton({ href, children, secondary = false }) {
  return (
    <a
      href={href}
      className={
        secondary
          ? "glass-button"
          : "emerald-button"
      }
    >
      {children}
    </a>
  );
}

function ShowcaseBadge({ tone = "neutral", children }) {
  return (
    <span className={`showcase-badge showcase-badge--${tone}`}>{children}</span>
  );
}

export default function App() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div id="top" className="min-h-screen bg-white text-[var(--ink)]">
      <section className="hero-shell">
        <AuroraBackdrop />

        <header className="relative z-20 px-4 pt-8 sm:px-6 lg:px-8">
          <div className="mx-auto flex max-w-[1280px] items-center justify-between gap-4 rounded-full border border-white/10 bg-white/5 px-5 py-3.5 backdrop-blur-xl sm:px-6">
            <LogoMark />

            <nav className="hidden items-center gap-8 lg:flex">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="text-sm font-extralight text-white/70 transition hover:text-white"
                >
                  {link.label}
                </a>
              ))}
            </nav>

            <div className="hidden items-center gap-3 lg:flex">
              <PrimaryButton href="#features" secondary>
                Log in
              </PrimaryButton>
              <PrimaryButton href="#about">Get Started</PrimaryButton>
            </div>

            <button
              type="button"
              className="inline-flex rounded-full border border-white/10 px-4 py-2 text-sm font-medium text-white lg:hidden"
              onClick={() => setMenuOpen((current) => !current)}
              aria-label="Toggle menu"
              aria-expanded={menuOpen}
            >
              Menu
            </button>
          </div>

          {menuOpen && (
            <div className="mx-auto mt-3 grid max-w-[1280px] gap-3 rounded-[1.5rem] border border-white/10 bg-[rgba(5,13,10,0.82)] p-4 backdrop-blur-xl lg:hidden">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="rounded-full border border-white/10 px-4 py-3 text-sm font-medium text-white/80"
                >
                  {link.label}
                </a>
              ))}
            </div>
          )}
        </header>

        <div className="relative z-20 mx-auto flex min-h-[640px] max-w-[940px] flex-col items-center justify-center px-6 pb-20 pt-28 text-center lg:min-h-[700px] lg:pb-24 lg:pt-28">
          <span className="hero-pill reveal" style={{ "--delay": "0.05s" }}>
            M-Pesa escrow for everyday work
          </span>

          <h1
            className="reveal mt-7 text-[clamp(3.2rem,7vw,6rem)] font-extrabold leading-[0.95] tracking-[-0.07em] text-white"
            style={{ "--delay": "0.12s" }}
          >
            Secure the money before
            <br />
            the work begins.
          </h1>

          <p
            className="reveal mt-7 max-w-[660px] text-base font-extralight leading-8 text-white/70 sm:text-lg"
            style={{ "--delay": "0.2s" }}
          >
            KaziPay gives clients and workers a calmer starting point: deposit
            through M-Pesa, track the job clearly, and release the payout only
            when the task is completed the right way.
          </p>

          <div
            className="reveal mt-11 flex flex-col gap-4 sm:flex-row"
            style={{ "--delay": "0.28s" }}
          >
            <PrimaryButton href="#features">Explore features</PrimaryButton>
            <PrimaryButton href="#trust" secondary>
              See why it works
            </PrimaryButton>
          </div>

          <div
            className="reveal mt-12 flex flex-wrap items-center justify-center gap-x-8 gap-y-4"
            style={{ "--delay": "0.36s" }}
          >
            {quickPoints.map((point) => (
              <div key={point} className="inline-flex items-center gap-2 text-sm text-white/85">
                <span className="grid h-5 w-5 place-items-center rounded-full bg-white/10 text-[var(--emerald)]">
                  <CheckIcon />
                </span>
                <span className="font-extralight">{point}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="relative z-20 border-t border-white/10 px-6 pb-12">
          <div className="mx-auto max-w-[1021px] pt-10 text-center">
            <p className="text-sm font-extralight text-white/80">
              Built for the way real jobs already move across Kenya
            </p>
            <div className="mt-7 flex flex-wrap justify-center gap-3">
              {sectors.map((sector) => (
                <span key={sector} className="sector-pill">
                  {sector}
                </span>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="about" className="bg-white px-4 py-24 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-[1280px]">
          <div className="max-w-[695px]">
            <p className="text-sm font-medium uppercase tracking-[0.22em] text-[var(--emerald)]">
              About KaziPay
            </p>
            <h2 className="mt-5 text-[clamp(2.4rem,5vw,4.5rem)] font-extrabold leading-[1.02] tracking-[-0.06em] text-[var(--ink)]">
              A calmer way to handle trust in Kenya&apos;s gig economy.
            </h2>
            <p className="mt-6 max-w-[695px] text-base font-extralight leading-8 text-[var(--muted)]">
              KaziPay is designed for the tension that sits between hiring and
              paying. It makes the payment real from the start, keeps job status
              visible while work is happening, and gives the client a clean
              release point when everything is done.
            </p>
          </div>

          <div id="features" className="mt-16 grid gap-6 lg:grid-cols-3">
            {featureCards.map((card, index) => (
              <article
                key={card.title}
                className="feature-card-light reveal"
                style={{ "--delay": `${0.08 * (index + 1)}s` }}
              >
                <div className="feature-icon">
                  <FeatureIcon type={card.icon} />
                </div>
                <div className="mt-16">
                  <h3 className="text-[1.55rem] font-bold tracking-[-0.04em] text-[var(--ink)]">
                    {card.title}
                  </h3>
                  <p className="mt-4 text-sm font-extralight leading-8 text-[var(--muted)]">
                    {card.text}
                  </p>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section id="showcase" className="bg-white px-4 pb-24 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-[1280px]">
          <div className="mx-auto max-w-[760px] text-center">
            <p className="text-sm font-medium uppercase tracking-[0.22em] text-[var(--emerald)]">
              Operations view
            </p>
            <h2 className="mt-5 text-[clamp(2.4rem,5vw,4.4rem)] font-extrabold leading-[1.02] tracking-[-0.06em] text-[var(--ink)]">
              One clean queue for funded jobs and releases.
            </h2>
            <p className="mt-6 text-base font-extralight leading-8 text-[var(--muted)]">
              This section only needs one clear workspace: a simple list that
              shows ownership, status, team, priority, and the latest activity
              without piling on extra feature blocks.
            </p>
          </div>

          <article
            className="showcase-card reveal mx-auto mt-16 max-w-[1120px]"
            style={{ "--delay": "0.08s" }}
          >
            <div className="max-w-[440px]">
              <div className="feature-icon">
                <FeatureIcon type="chart" />
              </div>
              <h3 className="mt-6 text-[1.95rem] font-bold leading-[1.02] tracking-[-0.05em] text-[var(--ink)]">
                Job command queue
              </h3>
              <p className="mt-4 text-sm font-extralight leading-7 text-[var(--muted)]">
                A single operating view for escrow-backed jobs moving from
                locked funds to review and final payout.
              </p>
            </div>

            <div className="showcase-table-shell mt-8">
              <div className="showcase-table-row showcase-table-row--header">
                <span>Job title</span>
                <span>Owner</span>
                <span>Status</span>
                <span>Team</span>
                <span>Priority</span>
                <span>Last activity</span>
              </div>

              {showcaseRows.map((row) => (
                <div key={row.title} className="showcase-table-row">
                  <span data-label="Job title">
                    <span className="showcase-title-cell">
                      <span className="showcase-checkbox" />
                      <span className="showcase-cell-title">{row.title}</span>
                    </span>
                  </span>
                  <span data-label="Owner">
                    <span className="showcase-owner-cell">
                      <span className="showcase-owner-avatar">{row.initials}</span>
                      <span className="showcase-cell-meta">{row.owner}</span>
                    </span>
                  </span>
                  <span data-label="Status">
                    <ShowcaseBadge tone={row.statusTone}>{row.status}</ShowcaseBadge>
                  </span>
                  <span className="showcase-cell-meta" data-label="Team">
                    {row.team}
                  </span>
                  <span data-label="Priority">
                    <ShowcaseBadge tone={row.priorityTone}>{row.priority}</ShowcaseBadge>
                  </span>
                  <span className="showcase-cell-meta" data-label="Last activity">
                    {row.updated}
                  </span>
                </div>
              ))}

              <div aria-hidden="true" className="showcase-table-fade" />
            </div>
          </article>
        </div>
      </section>

      <section id="trust" className="bg-[var(--paper)] px-4 py-24 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-[1280px]">
          <div className="mx-auto max-w-[695px] text-center">
            <p className="text-sm font-medium uppercase tracking-[0.22em] text-[var(--emerald)]">
              Trust signals
            </p>
            <h2 className="mt-5 text-[clamp(2.4rem,5vw,4.5rem)] font-extrabold leading-[1.02] tracking-[-0.06em] text-[var(--ink)]">
              What the product should make obvious at a glance.
            </h2>
            <p className="mt-6 text-base font-extralight leading-8 text-[var(--muted)]">
              The experience should immediately answer the questions that matter
              most to both sides: Is the money real? Who is in control? What
              happens next?
            </p>
          </div>

          <div className="mt-16 grid gap-6 lg:grid-cols-6">
            {trustCards.map((card, index) => (
              <article
                key={card.title}
                className={`trust-card reveal ${
                  card.size === "large" ? "lg:col-span-3" : "lg:col-span-2"
                }`}
                style={{ "--delay": `${0.08 * (index + 1)}s` }}
              >
                <p className="text-sm font-medium tracking-[-0.02em] text-black/35">
                  {card.eyebrow}
                </p>
                <div className="mt-12">
                  <h3 className="max-w-[560px] text-[1.6rem] font-bold leading-[1.12] tracking-[-0.04em] text-[var(--ink)]">
                    {card.title}
                  </h3>
                  <p className="mt-4 max-w-[560px] text-sm font-extralight leading-8 text-[var(--muted)]">
                    {card.text}
                  </p>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      <footer id="footer" className="footer-shell px-4 pt-24 sm:px-6 lg:px-8">
        <div aria-hidden="true" className="footer-backdrop" />

        <div className="relative z-10 mx-auto max-w-[1280px]">
          <div className="footer-cta mx-auto max-w-[910px] text-center">
            <p className="text-sm font-medium uppercase tracking-[0.22em] text-white/70">
              Ready to launch safer jobs?
            </p>
            <h2 className="mt-5 text-[clamp(2.8rem,6vw,5.6rem)] font-extrabold leading-[0.96] tracking-[-0.07em] text-white">
              Fund the work first.
              <br />
              Release it with confidence.
            </h2>
            <p className="mx-auto mt-6 max-w-[660px] text-base font-light leading-8 text-white">
              KaziPay keeps clients and workers aligned with upfront escrow,
              clean status tracking, and a release flow that feels fair to both
              sides.
            </p>

            <div className="mt-10 flex flex-col justify-center gap-4 sm:flex-row">
              <PrimaryButton href="#top">Get Started</PrimaryButton>
              <PrimaryButton href="#showcase" secondary>
                View operations
              </PrimaryButton>
            </div>
          </div>

          <div className="footer-divider mt-20" />

          <div className="grid gap-14 py-14 lg:grid-cols-[minmax(0,1.25fr)_minmax(0,0.85fr)_minmax(0,0.85fr)]">
            <div className="max-w-[320px]">
              <LogoMark />
              <p className="mt-5 text-sm font-light leading-7 text-white/90">
                Escrow-first payments for real work across Kenya&apos;s everyday
                service economy.
              </p>
            </div>

            {footerColumns.map((column) => (
              <div key={column.title}>
                <p className="footer-link-title">{column.title}</p>
                <div className="mt-5 grid gap-4">
                  {column.links.map((link) => (
                    <a key={link.label} href={link.href} className="footer-link">
                      {link.label}
                    </a>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="footer-divider" />

          <div className="flex flex-col gap-5 py-6 sm:flex-row sm:items-center sm:justify-between">
            <p className="text-sm font-light text-white/90">
              2026 KaziPay. Escrow-first payments for real work.
            </p>

            <div className="flex items-center gap-3">
              {footerSocials.map((social) => (
                <span key={social} className="footer-social-pill">
                  {social}
                </span>
              ))}
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
