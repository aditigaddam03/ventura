const navToggle = document.querySelector('.nav-toggle');
const siteNav = document.querySelector('#site-nav');
const navLinks = siteNav ? siteNav.querySelectorAll('a') : [];
const yearTarget = document.querySelector('#current-year');

function closeMenu() {
  if (!navToggle || !siteNav) {
	return;
  }

  navToggle.setAttribute('aria-expanded', 'false');
  siteNav.classList.remove('is-open');
}

if (navToggle && siteNav) {
  navToggle.addEventListener('click', () => {
	const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
	navToggle.setAttribute('aria-expanded', String(!isExpanded));
	siteNav.classList.toggle('is-open', !isExpanded);
  });

  navLinks.forEach((link) => {
	link.addEventListener('click', closeMenu);
  });

  window.addEventListener('keydown', (event) => {
	if (event.key === 'Escape') {
	  closeMenu();
	}
  });

  window.addEventListener('resize', () => {
	if (window.innerWidth > 780) {
	  closeMenu();
	}
  });
}

if (yearTarget) {
  yearTarget.textContent = new Date().getFullYear().toString();
}

