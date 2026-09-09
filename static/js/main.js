document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.navlinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var isOpen = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // Nav goes solid once the page scrolls past the transparent hero band
  var nav = document.querySelector('.topnav');
  if (nav) {
    var onScroll = function () {
      if (window.scrollY > 32) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Scroll-triggered reveal, progressively enhanced: elements only get
  // hidden once JS confirms it can observe and reveal them again.
  var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revealTargets = document.querySelectorAll('[data-reveal]');
  if (!prefersReduced && 'IntersectionObserver' in window && revealTargets.length) {
    revealTargets.forEach(function (el, index) {
      el.classList.add('reveal', 'reveal-' + ((index % 6) + 1));
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    revealTargets.forEach(function (el) {
      io.observe(el);
    });
  }
});
