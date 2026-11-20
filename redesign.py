from pathlib import Path
import re

old = Path('index.original.html').read_text(encoding='utf-8')
projects = re.search(r'<ul class="pgrid">(.*?)</ul>\s*<p class="gh-cta">', old, re.S).group(1)
projects = re.sub(r'href="#" data-repo="([^"]+)"', r'href="https://github.com/AhmedAbdelMoukim/\1" target="_blank" rel="noopener noreferrer"', projects)
projects = projects.replace('Voir le code</a>', 'Explorer le code <span aria-hidden="true">↗</span></a>')
skills = re.search(r'<div class="skills">(.*?)\n  </div>\n</section>', old, re.S).group(1)
timeline = re.search(r'<div class="two">(.*?)\n  </div>\n</section>', old, re.S).group(1)

html = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ahmed Zemouli — Développeur logiciel · IA & Vision</title>
  <meta name="description" content="Ahmed Zemouli, développeur logiciel à Moncton. Découvrez mes projets en intelligence artificielle, vision par ordinateur et développement web.">
  <meta name="theme-color" content="#f4f2eb">
  <meta property="og:title" content="Ahmed Zemouli — Du code. De l’impact.">
  <meta property="og:description" content="Développement logiciel, intelligence artificielle et vision par ordinateur. Moncton, Canada. Mobile pour travailler.">
  <meta property="og:type" content="website">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;450;500;550;600;650;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <script>try{if(localStorage.getItem('az-theme')==='dark')document.documentElement.dataset.theme='dark'}catch(e){}</script>
  <script src="script.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Aller au contenu</a>
<div class="progress" aria-hidden="true"></div>
<header class="site-header">
  <div class="wrap nav-bar">
    <a class="brand" href="#top" aria-label="Ahmed Zemouli, accueil">az<span class="brand-dot">.</span><span class="brand-name">AHMED<br>ZEMOULI</span></a>
    <nav class="desktop-nav" aria-label="Navigation principale"><a href="#projets">Projets <span>01</span></a><a href="#apropos">À propos <span>02</span></a><a href="#parcours">Parcours <span>03</span></a></nav>
    <div class="nav-actions"><button class="theme-toggle" type="button" aria-label="Activer le thème sombre" aria-pressed="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 13.2A8.5 8.5 0 0 1 10.8 3.5 8.5 8.5 0 1 0 20.5 13.2Z"/></svg></button><a class="nav-contact" href="#contact">Discutons <span aria-hidden="true">↗</span></a><button class="menu-toggle" aria-expanded="false" aria-controls="mobile-nav" aria-label="Ouvrir le menu"><span></span><span></span></button></div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Navigation mobile" hidden><a href="#projets">01 — Projets</a><a href="#apropos">02 — À propos</a><a href="#parcours">03 — Parcours</a><a href="#contact">04 — Contact</a></nav>
</header>
<main id="main">
<section class="hero wrap" id="top" aria-labelledby="hero-title">
  <div class="hero-topline"><span class="eyebrow"><span class="live-dot"></span> DISPONIBLE POUR DE NOUVEAUX DÉFIS</span><span class="location">MONCTON, CANADA <span aria-hidden="true">↗</span></span></div>
  <div class="hero-grid">
    <div class="hero-copy">
      <p class="hello">Bonjour, moi c’est Ahmed <span aria-hidden="true">✳</span></p>
      <h1 id="hero-title"><span class="title-line">Du code.</span><span class="title-line">De <em>l’impact.</em></span></h1>
      <p class="hero-role">Développeur logiciel <span>/</span> IA & vision</p>
      <p class="hero-description">Je transforme des problèmes complexes en solutions concrètes. Basé à Moncton, au Canada, je suis mobile pour de nouvelles opportunités.</p>
      <div class="hero-cta"><a class="button button-dark" href="#projets">Découvrir mes projets <span aria-hidden="true">↗</span></a><a class="text-link" href="https://github.com/AhmedAbdelMoukim" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 19c-4 1.2-4-2-6-2m12 5v-3.4c0-1 .1-1.5-.5-2 3-.3 6.2-1.5 6.2-6.8a5.3 5.3 0 0 0-1.4-3.7 4.9 4.9 0 0 0-.1-3.7s-1.2-.4-4 1.4a13.8 13.8 0 0 0-7.3 0c-2.8-1.8-4-1.4-4-1.4a5 5 0 0 0-.1 3.7 5.3 5.3 0 0 0-1.4 3.7c0 5.3 3.2 6.5 6.2 6.8-.5.5-.7 1.2-.6 2V22"/></svg>GitHub <span aria-hidden="true">↗</span></a></div>
      <div class="hero-note"><span class="tiny-star" aria-hidden="true">✳</span><span>La curiosité comme moteur.<br>Le code comme langage.</span></div>
    </div>
    <div class="portrait-composition">
      <div class="portrait-card">
        <div class="portrait-grid" aria-hidden="true"></div><span class="portrait-label">L’HUMAIN DERRIÈRE LE CODE</span>
        <img class="portrait" src="photo.jpg" width="460" height="460" alt="Ahmed Zemouli, souriant, avec des lunettes et un appareil photo" fetchpriority="high">
        <div class="vision-frame" aria-hidden="true"><i></i><i></i><i></i><i></i><span>hello_world.py</span></div>
        <div class="portrait-caption"><span>Ahmed Zemouli<small>DÉVELOPPEUR · EXPLORATEUR</small></span><span class="portrait-plus" aria-hidden="true">+</span></div>
      </div>
      <div class="orbit-stamp" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="stamp-circle" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs><text><textPath href="#stamp-circle">TOUJOURS CURIEUX · TOUJOURS EN MOUVEMENT · </textPath></text></svg><span>✳</span></div>
      <span class="portrait-index">FIG. 01 — CRÉATIVITÉ × TECHNOLOGIE</span>
    </div>
  </div>
  <div class="hero-bottom"><span>LOGICIEL BIEN PENSÉ. IMPACT BIEN RÉEL.</span><a href="#projets">EXPLORER <span aria-hidden="true">↓</span></a></div>
</section>
<div class="tech-ribbon" aria-label="Technologies : Python, TensorFlow, React, OpenCV, CUDA, TypeScript"><div class="ribbon-track"><div>PYTHON <span>✳</span> TENSORFLOW <span>✳</span> REACT <span>✳</span> OPENCV <span>✳</span> CUDA <span>✳</span> TYPESCRIPT <span>✳</span></div><div aria-hidden="true">PYTHON <span>✳</span> TENSORFLOW <span>✳</span> REACT <span>✳</span> OPENCV <span>✳</span> CUDA <span>✳</span> TYPESCRIPT <span>✳</span></div></div></div>
<section class="section wrap" id="projets">
  <div class="section-heading reveal"><div><p class="eyebrow">01 / PROJETS SÉLECTIONNÉS</p><h2>Des idées.<br>Du concret<span class="accent">.</span></h2></div><p>Des applications utiles aux expériences en IA.<br>Une sélection de ce que j’aime construire.</p></div>
  <article class="featured-project reveal">
    <a class="project-art hope-art" href="https://github.com/AhmedAbdelMoukim/Hopelink-final-version" target="_blank" rel="noopener noreferrer" aria-label="Explorer le code de Hope Link sur GitHub">
      <span class="art-caption">CONNECTER LES RESSOURCES. CRÉER DU LIEN.</span>
      <div class="hope-network" aria-hidden="true"><div class="network-orbit orbit-one"></div><div class="network-orbit orbit-two"></div><div class="network-line line-one"></div><div class="network-line line-two"></div><div class="network-line line-three"></div><div class="network-center">h<span>↗</span></div><div class="network-node node-one">♡<small>DONNER</small></div><div class="network-node node-two">⌂<small>RECEVOIR</small></div><div class="network-node node-three">↔<small>CONNECTER</small></div></div>
      <span class="art-wordmark">hope<span>link</span><sup>®</sup></span><span class="art-footnote">ILLUSTRATION DU CONCEPT</span><span class="art-open" aria-hidden="true">↗</span>
    </a>
    <div class="project-info"><div class="project-meta"><span>01 — APPLICATION WEB</span><span class="project-badge">HACK4CHANGE · 2026</span></div><h3>Hope Link</h3><p>Faire le lien entre ceux qui donnent et ceux qui en ont besoin. Une plateforme pour coordonner les dons, rendre les besoins visibles et réduire le gaspillage.</p><ul class="tags"><li>TypeScript</li><li>React</li><li>Impact social</li></ul><a class="project-link" href="https://github.com/AhmedAbdelMoukim/Hopelink-final-version" target="_blank" rel="noopener noreferrer">Explorer le projet <span aria-hidden="true">↗</span></a></div>
  </article>
  <div class="project-pair">
    <article class="project-small reveal"><div class="project-art recommendation-art"><span class="art-caption">L’INTELLIGENCE AU SERVICE DU BON MATCH.</span><div class="match-visual" aria-hidden="true"><div class="match-person">u<span>utilisateur</span></div><div class="match-path"><i></i><i></i><i></i></div><div class="match-brain">✳</div><div class="match-path"><i></i><i></i><i></i></div><div class="match-person">r<span>recommandation</span></div></div><span class="art-wordmark">neural<span class="accent">.</span></span><span class="art-footnote">ILLUSTRATION DU CONCEPT</span></div><div class="project-meta"><span>02 — INTELLIGENCE ARTIFICIELLE</span><span>RECOMMANDATION</span></div><h3>Système de recommandation par réseau de neurones</h3><p>Un système de recommandation fondé sur un réseau de neurones profond pour proposer des correspondances personnalisées.</p><div class="project-small-bottom"><ul class="tags"><li>Python</li><li>TensorFlow</li></ul><span class="private-label">Code privé <span aria-hidden="true">↗</span></span></div></article>
    <article class="project-small reveal"><div class="project-art naftal-art"><span class="art-caption">DE LA COMPLEXITÉ À LA FLUIDITÉ.</span><div class="route-visual" aria-hidden="true"><svg viewBox="0 0 500 210"><path class="route-base" d="M70 160V85Q70 65 90 65H235Q255 65 255 85V130Q255 150 275 150H410V45"/><path class="route-moving" d="M70 160V85Q70 65 90 65H235Q255 65 255 85V130Q255 150 275 150H410V45"/><circle cx="70" cy="160" r="10"/><circle cx="255" cy="105" r="10"/><circle cx="410" cy="45" r="10"/></svg><span class="route-tag route-tag-one">01 / PLANIFIER</span><span class="route-tag route-tag-two">02 / CONNECTER</span><span class="route-tag route-tag-three">03 / LIVRER</span></div><span class="art-wordmark">naftal<span> / logistique</span></span><span class="art-footnote">ILLUSTRATION DU CONCEPT</span></div><div class="project-meta"><span>03 — DÉVELOPPEMENT WEB</span><span>STAGE · 2023</span></div><h3>La logistique, simplifiée.</h3><p>Une application web de gestion logistique, conçue au sein de Naftal pendant mon stage de génie logiciel.</p><div class="project-small-bottom"><ul class="tags"><li>Application web</li><li>Logistique</li></ul><span class="private-label">Projet interne <span aria-hidden="true">↗</span></span></div></article>
  </div>
  <div class="lab-heading reveal"><div><span class="eyebrow">LE LABORATOIRE</span><h3>Explorer. Apprendre. Construire.</h3></div><a class="text-link" href="https://github.com/AhmedAbdelMoukim" target="_blank" rel="noopener noreferrer">Tout sur GitHub <span aria-hidden="true">↗</span></a></div>
  <div class="filters" role="group" aria-label="Filtrer les projets"><button type="button" data-filter="all" aria-pressed="true">Tous <span>09</span></button><button type="button" data-filter="ia" aria-pressed="false">Intelligence artificielle</button><button type="button" data-filter="vision" aria-pressed="false">Vision</button><button type="button" data-filter="systemes" aria-pressed="false">Systèmes & GPU</button><button type="button" data-filter="algo" aria-pressed="false">Algorithmes</button></div>
  <p class="project-count" id="project-count" role="status" aria-live="polite">9 projets à explorer</p>
  <ul class="pgrid">''' + projects + '''</ul>
</section>
<section class="about-section" id="apropos"><div class="wrap about-grid"><div class="about-intro reveal"><p class="eyebrow">02 / L’HUMAIN DERRIÈRE LE CODE</p><h2>Curieux par nature.<br>Développeur<br>par passion<span class="accent">.</span></h2><div class="about-coordinate"><span aria-hidden="true">↗</span><span>ALGER → MONCTON<br><small>Deux cultures. Une même curiosité.</small></span></div></div><div class="about-copy reveal"><p class="about-lead">J’aime comprendre comment les choses fonctionnent. Et imaginer comment elles pourraient mieux fonctionner.</p><p>Mon parcours m’a mené du génie logiciel en Algérie à l’informatique appliquée au Canada, avec un intérêt particulier pour l’apprentissage automatique, la vision par ordinateur et le calcul sur GPU.</p><p>À la Place Resurgo, je suis aussi guide-interprète du patrimoine. Expliquer des sujets complexes à des publics variés nourrit ma façon de documenter, de collaborer et de présenter mon code.</p><div class="about-facts"><div><strong>03</strong><span>langues pour échanger<br>Français · Arabe · Anglais</span></div><div><strong>02</strong><span>universités, un parcours<br>USTHB · Université de Moncton</span></div></div></div></div>
<div class="wrap toolkit"><div class="toolkit-heading reveal"><h3>Les outils derrière les idées.</h3><span class="eyebrow">MA BOÎTE À OUTILS</span></div><div class="skills">''' + skills + '''</div></div></section>
<section class="section wrap" id="parcours"><div class="section-heading reveal"><div><p class="eyebrow">03 / PARCOURS</p><h2>Toujours en<br>mouvement<span class="accent">.</span></h2></div><p>Apprendre en construisant.<br>Grandir à chaque expérience.</p></div><div class="two">''' + timeline + '''</div></section>
<section class="contact-section" id="contact"><div class="wrap"><div class="contact-top"><p class="eyebrow">04 / ET SI ON CONSTRUISAIT LA SUITE ?</p><span class="availability"><span class="live-dot"></span> OUVERT AUX OPPORTUNITÉS</span></div><a class="contact-title" href="mailto:zemouli.hamouda@gmail.com">Une idée ?<br>Parlons-en<span aria-hidden="true">↗</span></a><div class="contact-bottom"><p>Basé à Moncton, au Canada, et prêt à déménager pour travailler.<br>Discutons de vos projets, où que vous soyez.</p><div class="email-actions"><a href="mailto:zemouli.hamouda@gmail.com">zemouli.hamouda@gmail.com</a><button id="copy-email" type="button" aria-label="Copier l’adresse courriel"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V4H4v12h4"/></svg></button><span id="copy-status" role="status" aria-live="polite"></span></div></div></div></section>
</main>
<footer class="wrap"><a class="brand" href="#top" aria-label="Retour en haut">az<span class="brand-dot">.</span></a><p>© <span id="year">2026</span> Ahmed Abdel Moukim Zemouli</p><a href="https://github.com/AhmedAbdelMoukim" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="#top">Retour en haut ↑</a></footer>
</body>
</html>'''
Path('index.html').write_text(html, encoding='utf-8')
