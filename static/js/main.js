/* ===== NAVBAR SCROLL ===== */
(function () {
  const nav = document.getElementById('mainNav');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });
})();

/* ===== PROFICIENCY BARS ANIMATION ===== */
(function () {
  const fills = document.querySelectorAll('.prof-fill');
  if (!fills.length) return;

  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = el.style.width;
        el.style.width = '0';
        requestAnimationFrame(() => {
          requestAnimationFrame(() => {
            el.style.width = target;
          });
        });
        io.unobserve(el);
      }
    });
  }, { threshold: 0.3 });

  fills.forEach(el => io.observe(el));
})();

/* ===== SCROLL REVEAL ===== */
(function () {
  const style = document.createElement('style');
  style.textContent = `
    .reveal { opacity: 0; transform: translateY(24px); transition: opacity .55s ease, transform .55s ease; }
    .reveal.visible { opacity: 1; transform: none; }
  `;
  document.head.appendChild(style);

  const cards = document.querySelectorAll(
    '.project-card, .value-card, .cert-card, .skill-category-card, .timeline-card, .edu-card'
  );

  cards.forEach(el => el.classList.add('reveal'));

  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 60);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(el => io.observe(el));
})();

/* ===== SMOOTH SCROLL FOR ANCHOR LINKS ===== */
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    const offset = 80;
    const top = target.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  });
});

/* ===== ALERT AUTO-DISMISS ===== */
setTimeout(() => {
  document.querySelectorAll('.alert').forEach(el => {
    const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
    if (bsAlert) bsAlert.close();
  });
}, 6000);
