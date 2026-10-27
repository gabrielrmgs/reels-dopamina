/*
 * Efeitos dopaminérgicos para composições HyperFrames + GSAP.
 * Tudo é determinístico (gerador com semente) e baseado na timeline, então qualquer quadro
 * renderizado isoladamente mostra o estado certo.
 *
 * Uso:
 *   const tl = gsap.timeline({ paused: true });
 *   const fx = createFx(tl, { seed: 7 });
 *   fx.splitWords();                 // monta os .kt[data-text]
 *   fx.progress(42);                 // barra de progresso do vídeo inteiro
 *   fx.words("#kt1", 1.2);
 */
(function () {
  const COLORS = ["#34d399", "#2563eb", "#fbbf24", "#f472b6", "#ffffff", "#60a5fa", "#a78bfa"];

  window.createFx = function createFx(tl, opts = {}) {
    let seed = opts.seed || 7;
    const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
    const $ = (id) => document.getElementById(id);
    const E = "expo.out";

    /* Texto cinético: *x* destaque, <b>x</b> vermelho, _x_ sublinhado (palavra inteira, com pontuação). */
    const splitWords = (root = document) => {
      root.querySelectorAll(".kt[data-text]").forEach((el) => {
        el.innerHTML = el.dataset.text.split(" ").map((raw) => {
          const bad = /^<b>.*<\/b>$/.test(raw), hl = /^\*.*\*$/.test(raw), ul = /^_.*_$/.test(raw);
          const word = bad ? raw.slice(3, -4) : hl || ul ? raw.slice(1, -1) : raw;
          const cls = `w${hl ? " hl" : ""}${bad ? " bad" : ""}${ul ? " ul" : ""}`;
          return `<span class="${cls}">${word}${ul ? '<i class="bar"></i>' : ""}</span>`;
        }).join(" ");
      });
    };

    const words = (sel, at, stagger = 0.08) => {
      tl.fromTo(`${sel} .w`, { opacity: 0, y: 50, filter: "blur(10px)" },
        { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.55, ease: E, stagger }, at);
      tl.fromTo(`${sel} .bar`, { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power2.out" }, at + 0.45);
    };
    const out = (sel, at) => tl.to(sel, { opacity: 0, y: -40, filter: "blur(8px)", duration: 0.3, ease: "power2.in" }, at);

    const popIn = (sel, at, from = {}) =>
      tl.fromTo(sel, { opacity: 0, scale: 0.7, y: 60, ...from },
        { opacity: 1, scale: 1, y: 0, x: 0, rotate: 0, duration: 0.7, ease: "back.out(1.6)" }, at);
    const punch = (sel, at, s = 1.1) =>
      tl.fromTo(sel, { scale: s }, { scale: 1, duration: 0.45, ease: "power3.out", immediateRender: false }, at);
    const stamp = (sel, at) => {
      tl.fromTo(sel, { opacity: 0, scale: 2.6 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.in" }, at);
      shake(sel, at + 0.2, 14, 6);
    };
    const checkIn = (sel, at) =>
      tl.fromTo(sel, { scale: 0, rotate: -90 }, { scale: 1, rotate: 0, duration: 0.45, ease: "back.out(2.4)" }, at);

    const flash = (at, o = 0.6, sel = "#fx-flash") =>
      tl.fromTo(sel, { opacity: o }, { opacity: 0, duration: 0.35, ease: "power2.out", immediateRender: false }, at);
    const progress = (total, sel = "#fx-progress") =>
      tl.fromTo(sel, { scaleX: 0 }, { scaleX: 1, duration: total, ease: "none" }, 0);
    const drift = (sel, at, dur, dy = -20, s = 1.03) =>
      tl.to(sel, { y: `+=${dy}`, scale: s, duration: dur, ease: "sine.inOut" }, at);

    /* Tremida determinística. */
    const shake = (sel, at, amp = 18, n = 8) => {
      const kf = [];
      for (let i = 0; i < n; i++) kf.push({ x: (i % 2 ? -1 : 1) * amp * (1 - i / n), y: ((i % 3) - 1) * amp * 0.5 * (1 - i / n), duration: 0.04 });
      kf.push({ x: 0, y: 0, duration: 0.04 });
      tl.to(sel, { keyframes: kf }, at);
    };

    /* Contador (dinheiro, km, quantidade). fmt recebe o número. */
    const brl = (v) => "R$ " + Math.round(v).toLocaleString("pt-BR");
    const count = (el, from, to, at, dur, fmt = brl) => {
      const s = { v: from };
      tl.fromTo(s, { v: from }, { v: to, duration: dur, ease: "power2.out", immediateRender: false,
        onUpdate() { el.textContent = fmt(s.v); } }, at);
    };

    /* Confete natural: nasce invisível no centro, sai em leque para cima já aparecendo,
       gira em 3D e cai com gravidade balançando de lado. boxId = div vazia dentro da cena. */
    const confetti = (boxId, at, cx, cy, n = 50, power = 1000) => {
      const box = $(boxId);
      for (let i = 0; i < n; i++) {
        const d = document.createElement("div");
        d.className = "conf";
        d.style.left = cx + "px"; d.style.top = cy + "px";
        d.style.background = COLORS[i % COLORS.length];
        if (i % 3 === 0) { d.style.width = "14px"; d.style.height = "14px"; d.style.borderRadius = "50%"; }
        box.appendChild(d);
        const ang = (-90 + (rnd() - 0.5) * 140) * Math.PI / 180;
        const v = power * (0.45 + rnd() * 0.55);
        const vx = Math.cos(ang) * v, vy = Math.sin(ang) * v;
        const t0 = at + rnd() * 0.12, peak = 0.45 + rnd() * 0.2, fall = 1.4 + rnd() * 0.8;
        const sway = 40 + rnd() * 70, spin = 360 + rnd() * 720;
        tl.set(d, { opacity: 0, scale: 0 }, 0);
        tl.to(d, { keyframes: [
          { x: vx * 0.35, y: vy * 0.35, opacity: 1, scale: 1, rotation: spin * 0.2, rotationX: 120, duration: peak * 0.35, ease: "power2.out" },
          { x: vx * 0.6, y: vy * 0.55, rotation: spin * 0.4, rotationX: 300, duration: peak * 0.65, ease: "power1.out" },
          { x: vx * 0.6 + sway, y: vy * 0.55 + 380, rotation: spin * 0.7, rotationX: 520, rotationY: 180, duration: fall * 0.35, ease: "sine.in" },
          { x: vx * 0.6 - sway * 0.6, y: vy * 0.55 + 820, rotation: spin * 0.9, rotationX: 720, rotationY: 360, duration: fall * 0.35, ease: "sine.inOut" },
          { x: vx * 0.6 + sway * 0.3, y: vy * 0.55 + 1250, rotation: spin, rotationX: 900, opacity: 0, duration: fall * 0.3, ease: "sine.in" },
        ] }, t0);
      }
    };

    /* Raios de luz radiais. boxId = div vazia dentro da cena. */
    const rays = (boxId, at, n = 18, dur = 1.2, spin = 0, cx = 540, cy = 960) => {
      const box = $(boxId);
      for (let i = 0; i < n; i++) {
        const r = document.createElement("div");
        r.className = "ray";
        r.style.left = cx + "px"; r.style.top = cy + "px";
        r.style.transform = `rotate(${(360 / n) * i}deg)`;
        box.appendChild(r);
        tl.fromTo(r, { opacity: 0, scaleX: 0.2 }, { opacity: 1, scaleX: 1, duration: 0.3, ease: "power2.out" }, at);
        tl.to(r, { opacity: 0, rotate: `+=${spin}`, duration: dur, ease: "power1.in" }, at + 0.3);
      }
    };

    /* Chuva de emojis caindo (dinheiro, corações). */
    const rain = (boxId, at, glyphs = ["💰", "💵"], n = 12) => {
      const box = $(boxId);
      for (let i = 0; i < n; i++) {
        const c = document.createElement("div");
        c.className = "rain"; c.textContent = glyphs[i % glyphs.length];
        c.style.left = 60 + ((i * 89) % 920) + "px"; c.style.top = "-140px";
        box.appendChild(c);
        tl.fromTo(c, { opacity: 0, y: 0, rotate: 0 },
          { opacity: 1, y: 2100 + rnd() * 300, rotate: (rnd() - 0.5) * 720, duration: 1.5 + rnd() * 0.5, ease: "power1.in" }, at + i * 0.07);
      }
    };

    /* Transições fluidas entre cenas (seletores das <section>). */
    const zoomThrough = (outSel, inSel, at, dur = 0.45) => {
      tl.to(outSel, { scale: 1.6, opacity: 0, duration: dur, ease: "power3.in" }, at);
      tl.fromTo(inSel, { scale: 0.7, opacity: 0 }, { scale: 1, opacity: 1, duration: dur + 0.1, ease: E }, at);
    };
    const circleIn = (inSel, at, x = "50%", y = "50%", dur = 0.55) =>
      tl.fromTo(inSel, { clipPath: `circle(0% at ${x} ${y})` }, { clipPath: `circle(150% at ${x} ${y})`, duration: dur, ease: "power3.inOut" }, at);
    const curtain = (inSel, at, fromBottom = false, dur = 0.5) =>
      tl.fromTo(inSel, { clipPath: fromBottom ? "inset(100% 0 0 0)" : "inset(0 0 100% 0)" }, { clipPath: "inset(0% 0 0% 0)", duration: dur, ease: "power3.inOut" }, at);
    const wipe = (panelSel, at, dur = 0.6) =>
      tl.fromTo(panelSel, { x: -2600 }, { x: 0, duration: dur, ease: "power4.inOut" }, at);

    /* Lista que se reorganiza: layout[i] = slot do item i (-1 esconde). Itens absolutos com top = base + i*step. */
    const relayout = (ids, layout, at, step = 170, dur = 0.6) => layout.forEach((slot, i) => {
      if (slot < 0) tl.to(ids[i], { opacity: 0, scale: 0.85, x: -80, duration: dur * 0.6, ease: "power2.in" }, at);
      else tl.to(ids[i], { opacity: 1, scale: 1, x: 0, y: (slot - i) * step, duration: dur, ease: E }, at + 0.05 + slot * 0.04);
    });

    return { rnd, splitWords, words, out, popIn, punch, stamp, checkIn, flash, progress, drift, shake, brl, count,
      confetti, rays, rain, zoomThrough, circleIn, curtain, wipe, relayout };
  };
})();
