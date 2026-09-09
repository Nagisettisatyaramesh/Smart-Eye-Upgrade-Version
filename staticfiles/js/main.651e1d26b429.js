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
    var onNavScroll = function () {
      if (window.scrollY > 32) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    onNavScroll();
    window.addEventListener('scroll', onNavScroll, { passive: true });
  }

  var prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll-triggered reveal, progressively enhanced: elements only get
  // hidden once JS confirms it can observe and reveal them again.
  // data-reveal="up" (default) | "left" | "right" | "scale"
  var revealTargets = document.querySelectorAll('[data-reveal]');
  if (!prefersReduced && 'IntersectionObserver' in window && revealTargets.length) {
    revealTargets.forEach(function (el, index) {
      var variant = el.getAttribute('data-reveal');
      el.classList.add('reveal', 'reveal-' + ((index % 6) + 1));
      if (variant && variant !== 'up' && variant !== '') {
        el.classList.add('reveal-' + variant);
      }
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

  // Gentle parallax on decorative layers only - never on content that
  // carries text a reader needs to track while it moves.
  var parallaxTargets = Array.prototype.slice.call(document.querySelectorAll('[data-parallax]'));
  if (!prefersReduced && parallaxTargets.length && 'IntersectionObserver' in window) {
    var active = [];
    var parallaxIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          if (active.indexOf(entry.target) === -1) active.push(entry.target);
        } else {
          var idx = active.indexOf(entry.target);
          if (idx !== -1) active.splice(idx, 1);
        }
      });
    }, { threshold: 0 });
    parallaxTargets.forEach(function (el) { parallaxIo.observe(el); });

    var ticking = false;
    var applyParallax = function () {
      ticking = false;
      var vh = window.innerHeight;
      active.forEach(function (el) {
        var factor = parseFloat(el.getAttribute('data-parallax')) || 0.12;
        var rect = el.getBoundingClientRect();
        var centerOffset = (rect.top + rect.height / 2) - vh / 2;
        var shift = Math.max(-60, Math.min(60, -centerOffset * factor));
        el.style.transform = 'translate3d(0,' + shift.toFixed(1) + 'px,0)';
      });
    };
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(applyParallax);
        ticking = true;
      }
    }, { passive: true });
    applyParallax();
  }
});
