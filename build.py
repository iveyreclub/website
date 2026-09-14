#!/usr/bin/env python3
"""Builds the IREC static site into ./site — plain HTML out, no runtime deps."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

NAV = [
    ("about.html", "About"),
    ("events.html", "Events"),
    ("team.html", "Team"),
    ("partners.html", "Partners"),
]

APP_CLOSE = "2026-09-25T23:59:00"
APPLY_URL = "https://forms.gle/v6hqvXNeYxCrPAKw6"


def shell(page, title, description, body, status=True):
    nav_links = "\n".join(
        '        <a href="{href}"{cls}>{label}</a>'.format(
            href=href,
            label=label,
            cls=' class="is-active"' if href == page else "",
        )
        for href, label in NAV
    )

    status_bar = ""
    if status:
        status_bar = f"""  <div class="status" data-countdown="{APP_CLOSE}">
    <div class="wrap status__inner">
      <span class="status__dot" aria-hidden="true"></span>
      <span class="status__text" data-countdown-text>Analyst and Director applications for 2026/27 are open until September&nbsp;25.</span>
      <a href="join.html">Apply to IREC</a>
    </div>
  </div>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/photos/dob-group.jpg">
<meta name="theme-color" content="#034638">
<link rel="icon" href="assets/logos/irec.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=EB+Garamond:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="header">
  <div class="wrap header__inner">
    <a class="brand" href="index.html">
      <img src="assets/logos/irec.png" alt="">
      <span class="brand__name">Ivey Real Estate Club
        <span class="brand__sub">Ivey Business School</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="site-nav" aria-label="Main">
{nav_links}
      <a class="btn btn--solid" href="join.html">Join IREC</a>
    </nav>
  </div>
</header>
{status_bar}
<main id="main">
{body}
</main>

<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/logos/irec-white.png" alt="Ivey Real Estate Club">
        <p>Ivey Business School's student-led commercial real estate community. Founded 2014.</p>
      </div>
      <div>
        <h4>Club</h4>
        <ul>
          <li><a href="about.html">About IREC</a></li>
          <li><a href="team.html">Executive team</a></li>
          <li><a href="events.html">Events</a></li>
          <li><a href="join.html">Join the club</a></li>
        </ul>
      </div>
      <div>
        <h4>Industry</h4>
        <ul>
          <li><a href="partners.html">Partner with us</a></li>
          <li><a href="events.html#day-on-bay">Day on Bay</a></li>
          <li><a href="mailto:jdale.hba2027@ivey.ca">Sponsorship enquiries</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:jdale.hba2027@ivey.ca">jdale.hba2027@ivey.ca</a></li>
          <li><a href="mailto:echan.hba2027@ivey.ca">echan.hba2027@ivey.ca</a></li>
          <li><a href="https://www.instagram.com/iveyrealestateclub/" rel="noopener">Instagram</a></li>
          <li><a href="https://ca.linkedin.com/company/iveyrealestateclub" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__base">
      <span>&copy; 2026 Ivey Real Estate Club. 1255 Western Road, London, Ontario.</span>
      <span>A student organisation at the Ivey Business School, Western University.</span>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""


# --------------------------------------------------------------------------
# shared content
# --------------------------------------------------------------------------

FIRMS = [
    "BMO Capital Markets", "Oxford Properties", "CBRE", "QuadReal", "Hines",
    "KingSett Capital", "CIBC", "Eastdil Secured", "Colliers", "Fitzrovia",
    "Tricon Residential", "Harrison Street", "Wells Fargo", "RBC Capital Markets",
    "TD Securities", "Blackstone", "Crestpoint", "Cadillac Fairview",
    "Ontario Teachers'",
    "Choice Properties", "Welltower", "Beedie", "Nicola Wealth", "Opus",
    "First Capital", "Cresa", "Desjardins", "Harbour Equity",
    "North American Development Group", "Lee Chow Group", "Epic Investment Services",
]

TEAM = [
    ("erica-chan", "Erica Chan", "Co-President", "echan.hba2027@ivey.ca"),
    ("jesse-dale", "Jesse Dale", "Co-President", "jdale.hba2027@ivey.ca"),
    ("maia-lucchese", "Maia Lucchese", "VP Internal", ""),
    ("nicole-reeve", "Nicole Reeve", "VP Education", ""),
    ("nikola-petkovski", "Nikola Petkovski", "VP External", "npetkovski.hba2027@ivey.ca"),
    ("paul-prangikos", "Paul Prangikos", "VP External", "pprangikos.hba2027@ivey.ca"),
    ("gianmarco-bruni", "Gianmarco Bruni", "VP Events", ""),
    ("brooke-mirabella", "Brooke Mirabella", "VP Finance", ""),
    ("lina-deyrmenjian", "Lina Deyrmenjian", "VP Communications", ""),
    ("justin-lang", "Justin Lang", "Head Analyst", ""),
    ("elena-vlitas", "Elena Vlitas", "Head Analyst", ""),
    ("ashlee-wittlin", "Ashlee Wittlin", "Head Analyst", ""),
]

PANEL = [
    ("Michael Cooper", "President &amp; Chief Responsible Officer", "Dream"),
    ("Rob Kumer", "Chief Executive Officer", "KingSett Capital"),
    ("Janice Lin", "Managing Director, Head of Canadian Real Estate", "Blackstone"),
    ("Stephen Price", "President &amp; Chief Executive Officer", "Graywood"),
    ("Benjamin Tal", "Managing Director &amp; Deputy Chief Economist", "CIBC"),
    ("Andy Gibbons", "Partner &amp; Co-Head, Real Estate (moderator)", "Torys LLP"),
]


def people_html(team):
    out = []
    for slug, name, role, mail in team:
        mail_html = (
            f'\n      <a class="person__mail" href="mailto:{mail}">{mail}</a>' if mail else ""
        )
        out.append(
            f"""    <div class="person">
      <img src="assets/team/{slug}.jpg" alt="{name}" loading="lazy" width="560" height="560">
      <p class="person__name">{name}</p>
      <p class="person__role">{role}</p>{mail_html}
    </div>"""
        )
    return "\n".join(out)


def wall_html():
    return "\n".join(f"      <span>{f}</span>" for f in FIRMS)


def panel_html():
    return "\n".join(
        f"""      <div class="panelist">
        <strong>{n}</strong>
        <span>{r}</span>
        <em>{f}</em>
      </div>"""
        for n, r, f in PANEL
    )


CTA = """<section class="cta">
  <div class="wrap cta__inner">
    <div>
      <h2>Real estate is a relationship business.</h2>
      <p style="margin-bottom:0">IREC exists so Ivey students start building those relationships before they graduate — through the people in the room, not a job board.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn--light" href="join.html">Join the club</a>
      <a class="btn btn--outline-light" href="partners.html">Partner with IREC</a>
    </div>
  </div>
</section>"""


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------

home = f"""<section class="hero">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__copy">
        <p class="hero__eyebrow">Student-led at the Ivey Business School since 2014</p>
        <h1 class="h1--long">Connecting Ivey HBA Students to the Commercial Real Estate Industry</h1>
        <p>We prepare students for careers in commercial real estate — technical workshops, live transaction analysis, and interview preparation — and connect them directly to the firms hiring, in Toronto, New York, London, and beyond.</p>
        <div class="btn-row">
          <a class="btn btn--light" href="join.html">Join IREC</a>
          <a class="btn btn--outline-light" href="events.html#day-on-bay">See Day on Bay</a>
        </div>
      </div>
      <div class="hero__media">
        <img src="assets/photos/ivey-building-dusk.jpg" alt="The Ivey Business School building at dusk" width="1600" height="1067">
      </div>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="stat__n">150+</div><div class="stat__l">Active members</div></div>
      <div class="stat"><div class="stat__n">700+</div><div class="stat__l">Alumni across the industry</div></div>
      <div class="stat"><div class="stat__n">15+</div><div class="stat__l">Firm partners</div></div>
      <div class="stat"><div class="stat__n">10+</div><div class="stat__l">Events each year</div></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">What we do</span>
        <h2>The Three Pillars</h2>
      </div>
      <div class="grid" style="gap:36px">
        <div class="pillar">
          <h3>Connect</h3>
          <p>Firm visits, speaker events, and a flagship day on Bay Street. Our members meet CEOs, partners, and analysts who were sitting in the same seats five years ago.</p>
        </div>
        <div class="pillar">
          <h3>Educate</h3>
          <p>Technical workshops run by practitioners — development models, valuation, and the interview prep that decides who gets the offer.</p>
        </div>
        <div class="pillar">
          <h3>Engage</h3>
          <p>A community of students who care about the same industry, and an alumni network that keeps answering emails long after graduation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="feature" id="day-on-bay">
  <div class="feature__media">
    <img src="assets/photos/dob-panel-2.jpg" alt="Senior real estate leaders on the Day on Bay panel" loading="lazy">
  </div>
  <div class="feature__body">
    <div class="wrap" style="padding:0;max-width:520px;margin:0">
      <span class="kicker">Flagship event</span>
      <h2>Day on Bay</h2>
      <p>One day, a bus from London, and the calendars of the people who run Canadian real estate. Members visit leading firms in the morning and afternoon, then sit down for a senior leaders panel and a networking reception.</p>
      <p>Last year's panel brought together Dream, KingSett Capital, Blackstone, Graywood, and CIBC, moderated by Torys LLP — who also hosted the day.</p>
      <a class="textlink" href="events.html#day-on-bay">How the day runs</a>
    </div>
  </div>
</section>

<section class="section section--forest">
  <div class="wrap">
    <span class="kicker">Where our members end up</span>
    <h2 style="max-width:18ch">Our alumni sit across every corner of the industry.</h2>
    <div class="wall" style="margin-top:38px">
{wall_html()}
    </div>
    <p style="margin-top:32px;font-size:.95rem">Full-time and internship placements held by IREC members and alumni in investment banking, investment management, development, brokerage, and asset management.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">Recruiting now</span>
        <h2>Applications are open.</h2>
        <p class="lede">We're hiring HBA1 and HBA2 Analysts and three Director roles for 2026/27. Applications close September&nbsp;25.</p>
        <div class="btn-row">
          <a class="btn btn--solid" href="join.html">See the roles</a>
          <a class="btn btn--ghost" href="{APPLY_URL}" rel="noopener">Apply now</a>
        </div>
      </div>
      <div class="note">
        <p><strong>Not selected? You're still in the club.</strong></p>
        <p>Interest in real estate at Ivey has grown faster than the number of seats on the team. General membership is open to every HBA student, and the programming — speaker events, workshops, Day on Bay — is built for the whole club, not just the executive.</p>
      </div>
    </div>
  </div>
</section>

{CTA}"""


about = f"""<section class="pagehead">
  <div class="wrap">
    <h1>About IREC</h1>
    <p>Ivey Business School's official student-led real estate community, connecting HBA students to the commercial real estate industry since 2014.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">Who we are</span>
        <h2>Built on relationships, not job boards.</h2>
      </div>
      <div>
        <p class="lede">Founded in 2014, IREC has grown quickly alongside student interest in real estate and adjacent careers. What started as a small group of interested students is now one of Ivey's largest professional clubs.</p>
        <p>IREC prides itself on its ability to foster relationships, and holds one of the strongest alumni networks of any student organisation in Canada — with past members and mentors working across Toronto, New York, London, and other major finance hubs.</p>
        <p>Analysts, Directors, and general members immerse themselves in every part of the commercial real estate industry: networking events, technical and interview workshops, case competitions, and the club's flagship Day on Bay.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest section--tight">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><div class="stat__n">2014</div><div class="stat__l">Founded</div></div>
      <div class="stat"><div class="stat__n">150+</div><div class="stat__l">Active members</div></div>
      <div class="stat"><div class="stat__n">700+</div><div class="stat__l">Alumni across the industry</div></div>
      <div class="stat"><div class="stat__n">15+</div><div class="stat__l">Firm partners</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="kicker">Our programming</span>
    <h2 style="max-width:20ch">What membership actually gets you.</h2>
    <div class="grid grid--3" style="margin-top:48px">
      <div class="pillar">
        <h3>Connect</h3>
        <p>IREC's primary objective is to bridge the gap between students and industry professionals. Real estate is a relationship-driven industry, and IREC gives students the chance to build those relationships early.</p>
      </div>
      <div class="pillar">
        <h3>Educate</h3>
        <p>We help students prepare for technical interviews and succeed on the job through workshops, technical training, and practical exposure to real estate concepts — building both confidence and skill.</p>
      </div>
      <div class="pillar">
        <h3>Engage</h3>
        <p>A strong social community where members build relationships with peers who share an interest in real estate, and become part of a network that extends well beyond their time at Ivey.</p>
      </div>
    </div>
  </div>
</section>

<section class="feature feature--flip">
  <div class="feature__media">
    <img src="assets/photos/quadreal-panel.jpg" alt="Students at an IREC information session" loading="lazy">
  </div>
  <div class="feature__body">
    <div style="max-width:520px">
      <span class="kicker">How we're organised</span>
      <h2>A small executive, a deep bench.</h2>
      <p>IREC is run by two Co-Presidents and seven portfolio VPs covering internal, education, external, events, finance, and communications. Each portfolio carries Directors, and the analyst stream — three Head Analysts and twelve HBA1 and HBA2 Analysts — reports through VP Internal.</p>
      <p>Analysts publish weekly market reports and quarterly sector deep dives, and represent Ivey at external case competitions.</p>
      <a class="textlink" href="team.html">Meet the 2026/27 team</a>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="quote">
      <p>Every Ivey student interested in real estate should leave with technical skill, industry contacts, and a clear view of the career in front of them.</p>
    </div>
  </div>
</section>

{CTA}"""


events = f"""<section class="pagehead">
  <div class="wrap">
    <h1>Events</h1>
    <p>Panels, firm visits, technical workshops, and case competitions — programming built to put members in the room with the industry.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="kicker">Upcoming</span>
    <h2>This semester</h2>
    <div class="dates" style="margin-top:34px">
      <div class="date-row">
        <div class="date-row__when">Sept 11</div>
        <div class="date-row__what"><strong>Harrison Street information &amp; networking session</strong><span>On campus, with the Ivey Career Management team</span></div>
        <div class="date-row__tag">Meet the Firm</div>
      </div>
      <div class="date-row">
        <div class="date-row__when">Sept 14&ndash;18</div>
        <div class="date-row__what"><strong>Clubs Fair</strong><span>Come find the IREC table and meet the executive team</span></div>
        <div class="date-row__tag">Recruiting</div>
      </div>
      <div class="date-row">
        <div class="date-row__when">Sept 22</div>
        <div class="date-row__what"><strong>Annual General Meeting</strong><span>In person — the full picture of what IREC runs this year</span></div>
        <div class="date-row__tag">Recruiting</div>
      </div>
      <div class="date-row">
        <div class="date-row__when">Oct 6</div>
        <div class="date-row__what"><strong>Day on Bay</strong><span>Firm visits, senior leaders panel, and networking reception in Toronto</span></div>
        <div class="date-row__tag">Flagship</div>
      </div>
    </div>
  </div>
</section>

<section class="section section--forest" id="day-on-bay">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">Flagship event</span>
        <h2>Day on Bay</h2>
      </div>
      <div>
        <p class="lede" style="color:rgba(255,255,255,.88)">A bus leaves Ivey in the morning and returns that night. In between: visits to leading real estate firms, a panel with senior executives, and a networking reception.</p>
        <p>Day on Bay is the one day a year when the whole club is on Bay Street at once. Members see how different corners of the industry actually operate — investment management, development, brokerage, law — and leave with contacts rather than a brochure.</p>
      </div>
    </div>

    <h3 style="margin-top:72px;margin-bottom:32px">Last year's panel</h3>
    <div class="panelists">
{panel_html()}
    </div>
    <p style="margin-top:34px;font-size:.95rem">Hosted at the offices of Torys LLP, our 2025/26 venue sponsor.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="kicker">Recurring programming</span>
    <h2 style="max-width:22ch">What runs through the rest of the year.</h2>
    <div class="grid grid--2" style="margin-top:52px">
      <div class="pillar">
        <h3>Meet the Firm</h3>
        <p>Run with the Ivey Career Management team, these on-campus sessions give students a direct look at a firm's business, culture, and hiring. Presentations from senior leaders, insight from recent alumni, and Q&amp;A with recruiters. Recent guests include Harrison Street Asset Management and QuadReal.</p>
      </div>
      <div class="pillar">
        <h3>CRE Learning Sessions</h3>
        <p>Technical workshops that build practical skill. Liam Sauro (Partner) and Emily Forster (VP, Asset Management) of Lee Chow Group walked members through a full development model — the analytical side of the industry, taught by people who do it daily.</p>
      </div>
      <div class="pillar">
        <h3>Case competitions</h3>
        <p>IREC teams represent Ivey at leading real estate case competitions. At the 2026 Expand Your Empire competition hosted by TMU, the IREC team took First Place and the Most Feasible Design Award.</p>
      </div>
      <div class="pillar">
        <h3>Senior Leaders Panel</h3>
        <p>An on-campus panel on leadership, market conditions, and career paths — most recently with Ali Damji (Forum Asset Management), Adrian Rocca (Fitzrovia), and Kevin Leon (Crestpoint), followed by an open Q&amp;A.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="grid grid--2" style="gap:24px">
      <img src="assets/photos/dob-group.jpg" alt="IREC members at Day on Bay" loading="lazy">
      <img src="assets/photos/dob-networking.jpg" alt="Members networking with industry professionals" loading="lazy">
    </div>
  </div>
</section>

{CTA}"""


team = f"""<section class="pagehead">
  <div class="wrap">
    <h1>2026/27 Executive Team</h1>
    <p>Twelve students running the club this year — two Co-Presidents, seven portfolio VPs, and three Head Analysts.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="people">
{people_html(TEAM)}
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">Get in touch</span>
        <h2>Who to email.</h2>
      </div>
      <div>
        <p>For anything about membership, events, or the club generally, write to either Co-President. For sponsorship, partnerships, and firm relationships, reach our VP External team directly.</p>
        <p>Sponsorship and partnership arrangements apply to the 2026/27 school year.</p>
        <div class="btn-row">
          <a class="btn btn--solid" href="mailto:jdale.hba2027@ivey.ca">Email the Co-Presidents</a>
          <a class="btn btn--ghost" href="partners.html">Partnership information</a>
        </div>
      </div>
    </div>
  </div>
</section>

{CTA}"""


partners = f"""<section class="pagehead">
  <div class="wrap">
    <h1>Partners</h1>
    <p>The firms whose support makes IREC's programming possible — and who get first access to the students building careers in this industry.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">Why partner</span>
        <h2>Talent, earlier.</h2>
      </div>
      <div>
        <p class="lede">IREC members are the Ivey students who have already decided real estate is the career. They apply, they show up, and they recruit hard.</p>
        <p>Partnership puts your firm in front of that group directly: an on-campus information session, a technical workshop taught by your team, a Day on Bay office visit, or a panel seat. Our partners consistently tell us the calibre of question in the room is the reason they come back.</p>
        <div class="btn-row">
          <a class="btn btn--solid" href="mailto:jdale.hba2027@ivey.ca">Start a conversation</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <span class="kicker">2025/26 partners</span>
    <h2 style="margin-bottom:56px">Thank you to the firms who backed us last year.</h2>

    <div class="tier">
      <div class="tier__label"><h3>Title sponsor</h3><span class="rule-grow"></span></div>
      <div class="logos logos--single">
        <div class="logo-cell"><img src="assets/logos/oakbank.png" alt="Oakbank" loading="lazy"></div>
      </div>
    </div>

    <div class="tier">
      <div class="tier__label"><h3>Supporting sponsors</h3><span class="rule-grow"></span></div>
      <div class="logos">
        <div class="logo-cell"><img src="assets/logos/peakhill.png" alt="Peakhill Capital" loading="lazy"></div>
        <div class="logo-cell"><img src="assets/logos/lee-chow.png" alt="Lee Chow Group" loading="lazy"></div>
        <div class="logo-cell"><img src="assets/logos/balmoral.png" alt="Balmoral Capital" loading="lazy"></div>
        <div class="logo-cell"><img src="assets/logos/quadreal.png" alt="QuadReal" loading="lazy"></div>
        <div class="logo-cell"><img src="assets/logos/kipling.png" alt="Kipling" loading="lazy"></div>
        <div class="logo-cell"><img src="assets/logos/harrison-street.png" alt="Harrison Street" loading="lazy"></div>
      </div>
    </div>

    <div class="tier" style="margin-bottom:0">
      <div class="tier__label"><h3>Day on Bay venue host</h3><span class="rule-grow"></span></div>
      <div class="logos logos--single">
        <div class="logo-cell"><img src="assets/logos/torys.png" alt="Torys LLP" loading="lazy"></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="kicker">Ways to work with us</span>
    <h2 style="max-width:20ch">Four formats that actually work.</h2>
    <div class="grid grid--2" style="margin-top:52px">
      <div class="pillar">
        <h3>Venue host, Day on Bay</h3>
        <p>Host the panel and reception at your offices for roughly 120 students and guests. Venue hosts are recognised as a sponsor across the event and may nominate a moderator for the panel.</p>
      </div>
      <div class="pillar">
        <h3>Information session</h3>
        <p>An on-campus session run with Ivey Career Management — your business, your culture, your hiring process, in front of the students who will apply.</p>
      </div>
      <div class="pillar">
        <h3>Technical workshop</h3>
        <p>Your team teaches the skill. Past workshops have walked members line by line through a live development model.</p>
      </div>
      <div class="pillar">
        <h3>Firm visit</h3>
        <p>Open your office for a morning or afternoon during Day on Bay, or host a smaller group through the year.</p>
      </div>
    </div>
    <div class="note" style="margin-top:52px">
      <p>Sponsorship and partnership arrangements are set annually and currently apply to the 2026/27 school year. To discuss a package, email Jesse Dale and Erica Chan, Co-Presidents, at <a href="mailto:jdale.hba2027@ivey.ca">jdale.hba2027@ivey.ca</a>.</p>
    </div>
  </div>
</section>

{CTA}"""


join = f"""<section class="pagehead">
  <div class="wrap">
    <h1>Join IREC</h1>
    <p>Analyst and Director applications for 2026/27 are open to HBA1 and HBA2 students. General membership is open to everyone.</p>
    <div class="btn-row">
      <a class="btn btn--light" href="{APPLY_URL}" rel="noopener">Start your application</a>
      <a class="btn btn--outline-light" href="#roles">Read the roles first</a>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="offer">
      <div>
        <span class="kicker">Membership</span>
        <h2 style="margin-bottom:.35em">Become a member for 2026/27</h2>
        <p style="margin-bottom:0">Club membership is open to every HBA student, whatever year you're in and whether or not you apply for a role on the team. Members get access to IREC's full programming calendar for the year.</p>
      </div>
      <div class="offer__action">
        <span class="btn btn--disabled" aria-disabled="true" role="link">Coming soon</span>
        <p class="offer__note">The membership purchase link goes live shortly. Watch IREC's Instagram for the announcement.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="roles">
  <div class="wrap">
    <span class="kicker">Open roles</span>
    <h2 style="margin-bottom:38px">Four roles, four different jobs.</h2>

    <div class="tabs" role="tablist" aria-label="Open roles">
      <button class="tab" role="tab" id="tab-analyst" aria-controls="panel-analyst" aria-selected="true" tabindex="0">Analyst</button>
      <button class="tab" role="tab" id="tab-external" aria-controls="panel-external" aria-selected="false" tabindex="-1">Director &mdash; External</button>
      <button class="tab" role="tab" id="tab-events" aria-controls="panel-events" aria-selected="false" tabindex="-1">Director &mdash; Events</button>
      <button class="tab" role="tab" id="tab-comms" aria-controls="panel-comms" aria-selected="false" tabindex="-1">Director &mdash; Communications</button>
    </div>

    <div class="panel is-active" role="tabpanel" id="panel-analyst" aria-labelledby="tab-analyst">
      <div class="role">
        <div class="role__meta">
          <dl>
            <dt>Role</dt><dd>HBA1 / HBA2 Analyst</dd>
            <dt>Seats</dt><dd>8 HBA1 + 4 HBA2</dd>
            <dt>Commitment</dt><dd>4&ndash;5 hrs / week</dd>
            <dt>Reports to</dt><dd>Head Analysts</dd>
            <dt>Portfolio VP</dt><dd>Maia Lucchese, VP Internal</dd>
          </dl>
        </div>
        <div>
          <p class="lede">Build your real estate knowledge through market research, transaction analysis, and hands-on projects.</p>
          <div class="role__cols" style="margin-top:32px">
            <div>
              <h4>What you'll do</h4>
              <ul class="ticks">
                <li>Write weekly market reports combining transaction and market research with your own view and takeaways</li>
                <li>Contribute to quarterly deep dives on sectors, transactions, or emerging themes</li>
                <li>Take part in internal and external case competitions, technical workshops, and recruiting prep</li>
              </ul>
            </div>
            <div>
              <h4>What you'll get</h4>
              <ul class="ticks">
                <li>Stronger investment judgement — what drives value, risk, and transaction decisions</li>
                <li>Practical market knowledge across asset classes, capital markets, and live transactions</li>
                <li>Direct feedback and mentorship from HBA2s, alumni, and industry professionals</li>
                <li>A collaborative team focused on setting each other up for success</li>
              </ul>
            </div>
          </div>
          <div class="note" style="margin-top:30px">
            <p><strong>Ideal candidate.</strong> Intellectually curious and eager to learn about the industry. Strong analysts are reliable, detail-oriented, and willing to think critically — comfortable forming their own opinions and defending them.</p>
          </div>
        </div>
      </div>
    </div>

    <div class="panel" role="tabpanel" id="panel-external" aria-labelledby="tab-external">
      <div class="role">
        <div class="role__meta">
          <dl>
            <dt>Role</dt><dd>Director &mdash; External</dd>
            <dt>Seats</dt><dd>2 open</dd>
            <dt>Commitment</dt><dd>1&ndash;2 hrs / week</dd>
            <dt>Reports to</dt><dd>VP External</dd>
            <dt>Portfolio VPs</dt><dd>Nikola Petkovski &amp; Paul Prangikos</dd>
          </dl>
        </div>
        <div>
          <p class="lede">For the member who wants to own the club's relationships with the industry.</p>
          <div class="role__cols" style="margin-top:32px">
            <div>
              <h4>What you'll own</h4>
              <ul class="ticks">
                <li>Research prospective sponsors, speakers, and industry contacts for club initiatives</li>
                <li>Support the VPs with drafting and sending professional outreach and follow-up communications</li>
                <li>Maintain organised contact lists and track outreach status, responses, and next steps</li>
                <li>Assist with speaker, sponsor, and firm coordination leading up to events</li>
              </ul>
            </div>
            <div>
              <h4>What you'll get</h4>
              <ul class="ticks">
                <li>Direct exposure to professionals and firms across the real estate industry</li>
                <li>Experience writing professional outreach and managing external communication with senior people</li>
                <li>Insight into how sponsorships, speaker engagements, and industry partnerships are built</li>
                <li>Opportunities to expand your own network</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="panel" role="tabpanel" id="panel-events" aria-labelledby="tab-events">
      <div class="role">
        <div class="role__meta">
          <dl>
            <dt>Role</dt><dd>Director &mdash; Events</dd>
            <dt>Seats</dt><dd>2 open</dd>
            <dt>Commitment</dt><dd>1&ndash;2 hrs / week</dd>
            <dt>Reports to</dt><dd>VP Events</dd>
            <dt>Portfolio VP</dt><dd>Gianmarco Bruni</dd>
          </dl>
        </div>
        <div>
          <p class="lede">For the member who wants the room to run right — and to know why it did.</p>
          <div class="role__cols" style="margin-top:32px">
            <div>
              <h4>What you'll own</h4>
              <ul class="ticks">
                <li>Support planning and logistics for club events, from workshops through to Day on Bay</li>
                <li>Coordinate logistics: rooms, catering, transport, materials, and run-of-show</li>
                <li>Help run events on the day — setup, registration, and speaker support</li>
                <li>Gather member feedback and help improve how the next event runs</li>
              </ul>
            </div>
            <div>
              <h4>What you'll get</h4>
              <ul class="ticks">
                <li>Hands-on experience running events that matter to the club's reputation</li>
                <li>Work directly alongside the executive team and industry guests</li>
                <li>Project management reps you can point to in an interview</li>
                <li>A mentored path toward VP Events next year</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="panel" role="tabpanel" id="panel-comms" aria-labelledby="tab-comms">
      <div class="role">
        <div class="role__meta">
          <dl>
            <dt>Role</dt><dd>Director &mdash; Communications</dd>
            <dt>Seats</dt><dd>1 open</dd>
            <dt>Commitment</dt><dd>1&ndash;2 hrs / week</dd>
            <dt>Reports to</dt><dd>VP Communications</dd>
            <dt>Portfolio VP</dt><dd>Lina Deyrmenjian</dd>
          </dl>
        </div>
        <div>
          <p class="lede">For the member who wants IREC's voice to reach further than the room.</p>
          <div class="role__cols" style="margin-top:32px">
            <div>
              <h4>What you'll own</h4>
              <ul class="ticks">
                <li>IREC's public voice across Instagram, LinkedIn, and the member newsletter</li>
                <li>Build and run the semester content calendar around flagship events and recruiting</li>
                <li>Produce event graphics, decks, and collateral within the IREC brand system</li>
                <li>Report reach and engagement to the board, and adjust what isn't landing</li>
              </ul>
            </div>
            <div>
              <h4>What you'll get</h4>
              <ul class="ticks">
                <li>A real portfolio: audience numbers, brand work, and campaigns you led</li>
                <li>Direct exposure to the board and to every flagship initiative</li>
                <li>Hands-on reps in design, copywriting, and audience analytics</li>
                <li>A mentored path toward VP Communications next year</li>
              </ul>
            </div>
          </div>
          <div class="note" style="margin-top:30px">
            <p><strong>Ideal candidate.</strong> A sharp eye for design and tight copy, comfortable shipping on a deadline. Curious about how a brand earns credibility with members, sponsors, and alumni.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="wrap">
    <div class="grid grid--split">
      <div>
        <span class="kicker">How to apply</span>
        <h2>Five steps.</h2>
        <p>Applications close September&nbsp;25 — a hard cut-off. We strongly encourage applying early.</p>
      </div>
      <div class="steps">
        <div class="step">
          <div class="step__n">1</div>
          <div><h4>Attend the information session</h4><p>Held September 6. If you missed it, come find us at the Clubs Fair.</p></div>
        </div>
        <div class="step">
          <div class="step__n">2</div>
          <div><h4>Attend the AGM</h4><p>Our Annual General Meeting is held in person on September 22.</p></div>
        </div>
        <div class="step">
          <div class="step__n">3</div>
          <div><h4>Apply</h4><p>Applications opened September 10 and are submitted through our application form.</p></div>
        </div>
        <div class="step">
          <div class="step__n">4</div>
          <div><h4>Interview</h4><p>Both Analyst and Director roles include an interview, held September 28 to October 2.</p></div>
        </div>
        <div class="step">
          <div class="step__n">5</div>
          <div><h4>Decision</h4><p>Final decisions are released by Ivey email in early October. Programming starts immediately.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="note">
      <p><strong>If you're not selected, stay in the club.</strong></p>
      <p>Interest in IREC and in real estate generally has grown sharply in recent years, and there are more strong applicants than seats. We're committed to making general membership better than it has ever been — if you aren't selected for an Analyst or Director position, we strongly encourage you to stay active and take part in everything the club runs.</p>
    </div>
    <div class="btn-row">
      <a class="btn btn--solid" href="{APPLY_URL}" rel="noopener">Start your application</a>
      <a class="btn btn--ghost" href="mailto:jdale.hba2027@ivey.ca">Ask a question</a>
    </div>
  </div>
</section>"""


PAGES = [
    ("index.html", "Ivey Real Estate Club — Ivey Business School", "IREC is Ivey Business School's student-led commercial real estate community, connecting HBA students to the industry through Day on Bay, firm visits, technical workshops, and one of Canada's strongest student alumni networks.", home),
    ("about.html", "About — Ivey Real Estate Club", "Founded in 2014, IREC connects Ivey HBA students to the commercial real estate industry through connection, education, and community.", about),
    ("events.html", "Events — Ivey Real Estate Club", "Day on Bay, Meet the Firm sessions, CRE technical workshops, case competitions, and senior leaders panels hosted by the Ivey Real Estate Club.", events),
    ("team.html", "Team — Ivey Real Estate Club", "The 2026/27 IREC executive team: Co-Presidents, portfolio VPs, and Head Analysts.", team),
    ("partners.html", "Partners — Ivey Real Estate Club", "Partner with the Ivey Real Estate Club: Day on Bay venue hosting, information sessions, technical workshops, and firm visits.", partners),
    ("join.html", "Join — Ivey Real Estate Club", "Analyst and Director applications for 2026/27, role descriptions, the application process, and key dates.", join),
]

if __name__ == "__main__":
    for filename, title, desc, body in PAGES:
        html = shell(filename, title, desc, body)
        with open(os.path.join(OUT, filename), "w", encoding="utf-8") as fh:
            fh.write(html)
        print("wrote", filename, len(html), "bytes")
