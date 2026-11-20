'use strict';

const root = document.documentElement;
const motionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');
const themeButton = document.querySelector('.theme-toggle');
function syncThemeButton() {
  const dark = root.dataset.theme === 'dark';
  themeButton.setAttribute('aria-pressed', String(dark));
  themeButton.setAttribute('aria-label', dark ? 'Activer le thème clair' : 'Activer le thème sombre');
  document.querySelector('meta[name="theme-color"]').content = dark ? '#191b18' : '#f4f2eb';
}
syncThemeButton();
themeButton.addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem('az-theme', root.dataset.theme); } catch (_) { /* Storage is optional. */ }
  syncThemeButton();
});

const menuButton = document.querySelector('.menu-toggle');
const mobileNav = document.querySelector('.mobile-nav');
function setMenu(open) {
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  mobileNav.hidden = !open;
}
menuButton.addEventListener('click', () => setMenu(mobileNav.hidden));
mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && !mobileNav.hidden) { setMenu(false); menuButton.focus(); }
});
window.matchMedia('(min-width: 601px)').addEventListener('change', event => { if (event.matches) setMenu(false); });

const projectCards = [...document.querySelectorAll('.pgrid .card')];
const filters = [...document.querySelectorAll('[data-filter]')];
filters.forEach(button => button.addEventListener('click', () => {
  const filter = button.dataset.filter;
  filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  let count = 0;
  projectCards.forEach(card => {
    const visible = filter === 'all' || card.dataset.cat.split(' ').includes(filter);
    card.hidden = !visible;
    card.classList.remove('filter-enter');
    if (visible) {
      count++;
      if (!motionPreference.matches) {
        void card.offsetWidth;
        card.classList.add('filter-enter');
      }
    }
  });
  document.getElementById('project-count').textContent = `${count} projet${count > 1 ? 's' : ''} à explorer`;
}));

const copyButton = document.getElementById('copy-email');
const copyStatus = document.getElementById('copy-status');
let statusTimer;
copyButton.addEventListener('click', async () => {
  clearTimeout(statusTimer);
  try {
    await navigator.clipboard.writeText('zemouli.hamouda@gmail.com');
    copyStatus.textContent = 'Adresse copiée !';
  } catch (_) {
    copyStatus.textContent = 'Sélectionnez l’adresse pour la copier.';
  }
  statusTimer = setTimeout(() => { copyStatus.textContent = ''; }, 4500);
});
document.getElementById('year').textContent = new Date().getFullYear();

if ('IntersectionObserver' in window) {
  const reveals = [...document.querySelectorAll('.reveal')];
  const revealObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.remove('is-pending');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.06 });
  if (!motionPreference.matches) {
    reveals.forEach(element => { element.classList.add('is-pending'); revealObserver.observe(element); });
  }
  motionPreference.addEventListener('change', () => {
    if (motionPreference.matches) {
      reveals.forEach(element => element.classList.remove('is-pending'));
      revealObserver.disconnect();
    }
  });

  const navLinks = [...document.querySelectorAll('.desktop-nav a')];
  const navObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => {
          if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'true');
          else link.removeAttribute('aria-current');
        });
      }
    });
  }, { rootMargin: '-15% 0px -65% 0px' });
  document.querySelectorAll('main > section[id]').forEach(section => navObserver.observe(section));
}

const progress = document.querySelector('.progress');
let framePending = false;
function updateProgress() {
  const scrollable = root.scrollHeight - innerHeight;
  progress.style.transform = `scaleX(${scrollable > 0 ? Math.min(1, Math.max(0, scrollY / scrollable)) : 0})`;
  framePending = false;
}
addEventListener('scroll', () => {
  if (!framePending) { framePending = true; requestAnimationFrame(updateProgress); }
}, { passive: true });
addEventListener('resize', updateProgress);
updateProgress();
