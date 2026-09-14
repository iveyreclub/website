/* IREC — site behaviour
   Everything here is progressive: the pages are fully readable without JS. */

(function () {
  'use strict';

  /* ---- mobile navigation ---- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A' && window.innerWidth <= 900) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* ---- header border once the page scrolls ---- */
  var header = document.querySelector('.header');
  if (header) {
    var setStuck = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    setStuck();
    window.addEventListener('scroll', setStuck, { passive: true });
  }

  /* ---- role tabs (Join page) ---- */
  var tablist = document.querySelector('[role="tablist"]');
  if (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));

    var select = function (tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.setAttribute('tabindex', on ? '0' : '-1');
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.classList.toggle('is-active', on);
      });
    };

    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab); });
      tab.addEventListener('keydown', function (e) {
        var next = null;
        if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
        if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
        if (next) { e.preventDefault(); select(next); next.focus(); }
      });
    });
  }

  /* ---- application countdown ----
     Update APPLICATION_CLOSE each recruiting cycle. When the date passes,
     the banner switches to the closed message on its own.              */
  var banner = document.querySelector('[data-countdown]');
  if (banner) {
    var close = new Date(banner.getAttribute('data-countdown'));
    var days = Math.ceil((close - new Date()) / 86400000);
    var target = banner.querySelector('[data-countdown-text]');

    if (target) {
      if (days > 1) {
        target.innerHTML = 'Analyst and Director applications are open — <strong>' +
          days + ' days left</strong> to apply.';
      } else if (days === 1) {
        target.innerHTML = 'Applications close <strong>tomorrow</strong>.';
      } else if (days === 0) {
        target.innerHTML = 'Applications close <strong>today</strong>.';
      } else {
        target.innerHTML = 'Applications for 2026/27 are now closed. ' +
          'General membership stays open to every HBA student.';
        var dot = banner.querySelector('.status__dot');
        if (dot) dot.style.background = '#AFC4BC';
      }
    }
  }
})();
