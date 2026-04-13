import json

with open('card_data.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

cards_json = json.dumps(cards, ensure_ascii=False, separators=(',', ':'))

html_parts = []

html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pokemall — Japanese Scarlet &amp; Violet 151 Price Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0a0f;
  --surface:#12121a;
  --surface2:#1a1a26;
  --surface3:#22223a;
  --accent:#FFDE00;
  --accent2:#CC0000;
  --text:#ffffff;
  --text2:#a0a0b0;
  --text3:#606080;
  --border:#2a2a3a;
  --radius:12px;
  --tr:0.2s ease;
}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;min-height:100vh;overflow-x:hidden;opacity:0;transition:opacity 0.5s ease}
body.loaded{opacity:1}
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--surface3);border-radius:3px}

/* NAVBAR */
.navbar{position:sticky;top:0;z-index:100;background:rgba(10,10,15,0.85);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:0 24px;height:64px;display:flex;align-items:center;gap:20px;transition:background var(--tr)}
.navbar.scrolled{background:rgba(10,10,15,0.97)}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0}
.nav-logo-text{font-family:'Rajdhani',sans-serif;font-size:28px;font-weight:700;color:var(--accent);letter-spacing:1px;text-shadow:0 0 20px rgba(255,222,0,0.4)}
.pb{width:28px;height:28px;border-radius:50%;border:2.5px solid #fff;position:relative;overflow:hidden;flex-shrink:0}
.pb::before{content:'';position:absolute;top:0;left:0;width:100%;height:50%;background:var(--accent2)}
.pb::after{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:8px;height:8px;background:#fff;border-radius:50%;border:2px solid #333;z-index:2}
.pb .belt{position:absolute;top:calc(50% - 1.5px);left:0;width:100%;height:3px;background:#333;z-index:1}
.nav-search{flex:1;max-width:480px;position:relative}
.nav-search input{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:9px 16px 9px 42px;font-size:14px;font-family:'Inter',sans-serif;outline:none;transition:border-color var(--tr),box-shadow var(--tr)}
.nav-search input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,222,0,0.12)}
.nav-search input::placeholder{color:var(--text3)}
.nav-search svg{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--text3);pointer-events:none}
.nav-stats{margin-left:auto;font-size:13px;color:var(--text2);white-space:nowrap;font-weight:500}
.nav-stats span{color:var(--accent)}

/* HERO */
.hero-wrap{max-width:1400px;margin:0 auto}
.hero{background:linear-gradient(135deg,var(--bg) 0%,#0d0d1a 50%,#0a0a12 100%);padding:60px 24px 40px;display:flex;align-items:center;gap:48px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-80px;right:160px;width:400px;height:400px;background:radial-gradient(circle,rgba(255,222,0,0.06) 0%,transparent 70%);pointer-events:none}
.hero-text{flex:1;min-width:0}
.hero-tag{display:inline-flex;align-items:center;gap:6px;background:rgba(255,222,0,0.1);border:1px solid rgba(255,222,0,0.3);border-radius:20px;padding:4px 14px;font-size:13px;color:var(--accent);font-weight:600;margin-bottom:20px;letter-spacing:0.5px}
.hero-title{font-family:'Rajdhani',sans-serif;font-size:72px;font-weight:700;color:var(--accent);line-height:1;text-shadow:0 0 40px rgba(255,222,0,0.3);margin-bottom:12px}
.hero-sub{font-size:20px;color:var(--text2);font-weight:400;margin-bottom:10px;line-height:1.4}
.hero-meta{font-size:14px;color:var(--text3);font-weight:500}
.hero-meta strong{color:var(--accent);font-weight:600}
.hero-img-wrap{flex-shrink:0;position:relative}
.hero-img-wrap img{width:220px;height:280px;object-fit:cover;object-position:top center;border-radius:16px;position:relative;z-index:1;filter:drop-shadow(0 0 30px rgba(255,222,0,0.25))}
.hero-glow{position:absolute;inset:-12px;border-radius:20px;background:linear-gradient(135deg,rgba(255,222,0,0.2),rgba(255,165,0,0.1));filter:blur(16px);z-index:0}
.hero-stats{display:flex;gap:16px;padding:0 24px 32px;flex-wrap:wrap}
.hstat{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px 24px;flex:1;min-width:180px;position:relative;overflow:hidden;transition:border-color var(--tr),transform var(--tr)}
.hstat:hover{border-color:var(--accent);transform:translateY(-2px)}
.hstat::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#FFD700,#FFA500)}
.hstat-label{font-size:12px;color:var(--text3);font-weight:500;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.hstat-val{font-family:'Rajdhani',sans-serif;font-size:28px;font-weight:700;color:var(--accent)}
.hstat-sub{font-size:12px;color:var(--text3);margin-top:2px}

/* FILTER BAR */
.filter-bar{max-width:1400px;margin:0 auto;padding:0 24px 20px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.filter-btns{display:flex;gap:8px;flex-wrap:wrap;flex:1}
.fb{background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text2);padding:8px 16px;font-size:13px;font-weight:500;cursor:pointer;transition:all var(--tr);font-family:'Inter',sans-serif;white-space:nowrap}
.fb:hover{border-color:rgba(255,222,0,0.5);color:var(--text)}
.fb.active{background:rgba(255,222,0,0.12);border-color:var(--accent);color:var(--accent)}
.sort-sel{background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:8px 12px;font-size:13px;cursor:pointer;outline:none;font-family:'Inter',sans-serif;transition:border-color var(--tr)}
.sort-sel:focus{border-color:var(--accent)}
.rc-wrap{max-width:1400px;margin:0 auto;width:100%;padding:0 24px 12px;font-size:13px;color:var(--text3)}
.rc-wrap span{color:var(--accent);font-weight:600}

/* CARD GRID */
.card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px;max-width:1400px;margin:0 auto;padding:0 24px 40px}
@media(max-width:768px){
  .card-grid{grid-template-columns:repeat(2,1fr);gap:12px;padding:0 12px 32px}
  .hero{flex-direction:column;padding:40px 16px 24px;gap:24px;text-align:center}
  .hero-title{font-size:48px}
  .hero-sub{font-size:16px}
  .hero-img-wrap img{width:160px;height:200px}
  .hero-stats{padding:0 12px 24px}
  .filter-bar{padding:0 12px 16px}
  .navbar{padding:0 16px}
  .nav-stats{display:none}
}
@media(max-width:480px){.card-grid{grid-template-columns:1fr}.hero-title{font-size:40px}}
@media(min-width:1200px){.card-grid{grid-template-columns:repeat(5,1fr)}}
@media(min-width:900px) and (max-width:1199px){.card-grid{grid-template-columns:repeat(4,1fr)}}
@media(min-width:640px) and (max-width:899px){.card-grid{grid-template-columns:repeat(3,1fr)}}

/* POKEMON CARD */
.poke-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px;position:relative;cursor:pointer;transition:transform var(--tr),border-color var(--tr),box-shadow var(--tr);overflow:hidden}
.poke-card:hover{transform:translateY(-4px);border-color:var(--accent);box-shadow:0 8px 32px rgba(255,222,0,0.12)}
.poke-card.r-special-art{background:linear-gradient(135deg,#1a1228,#12121a);border-color:#3d2d5a}
.poke-card.r-special-art:hover{border-color:#764ba2;box-shadow:0 8px 32px rgba(102,126,234,0.2)}
.poke-card.r-ultra-rare{background:linear-gradient(135deg,#1e1a0a,#12121a);border-color:#3d3000}
.poke-card.r-ultra-rare:hover{border-color:#FFD700;box-shadow:0 8px 32px rgba(255,215,0,0.2)}
.poke-card.r-holo-rare,.poke-card.r-rare-holo{background:linear-gradient(135deg,#0d1826,#12121a);border-color:#1a2d4a}
.shimmer{position:absolute;inset:0;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,0.03) 50%,transparent 60%);background-size:200% 100%;animation:shimmer 3s infinite linear;pointer-events:none}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.feat-badge{position:absolute;top:0;right:0;background:linear-gradient(135deg,#FFD700,#FFA500);color:#000;font-size:10px;font-weight:700;padding:4px 10px;border-radius:0 var(--radius) 0 var(--radius);letter-spacing:.5px;text-transform:uppercase}
.cnum{font-size:11px;color:var(--text3);font-weight:600;letter-spacing:1px;margin-bottom:4px;font-family:'Rajdhani',sans-serif}
.cimg{width:100%;aspect-ratio:3/4;border-radius:8px;overflow:hidden;margin-bottom:12px;background:var(--surface2);display:flex;align-items:center;justify-content:center}
.cimg img{width:100%;height:100%;object-fit:cover;transition:transform .3s ease}
.poke-card:hover .cimg img{transform:scale(1.04)}
.cname{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:700;color:var(--text);margin-bottom:6px;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rbadge{display:inline-flex;align-items:center;border-radius:4px;padding:2px 8px;font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-bottom:12px}
.b-common{background:rgba(120,120,140,.2);color:#888;border:1px solid rgba(120,120,140,.3)}
.b-uncommon{background:rgba(0,200,100,.15);color:#4CAF50;border:1px solid rgba(0,200,100,.3)}
.b-rare{background:rgba(0,120,255,.15);color:#5b9cf6;border:1px solid rgba(0,120,255,.3)}
.b-rare-holo{background:rgba(147,51,234,.15);color:#a855f7;border:1px solid rgba(147,51,234,.3)}
.b-holo-rare{background:rgba(102,126,234,.2);color:#818cf8;border:1px solid rgba(102,126,234,.4)}
.b-ultra-rare{background:linear-gradient(135deg,rgba(255,215,0,.2),rgba(255,165,0,.2));color:#FFD700;border:1px solid rgba(255,215,0,.5)}
.b-special-art{background:linear-gradient(135deg,rgba(240,147,251,.2),rgba(245,87,108,.2));color:#f093fb;border:1px solid rgba(240,147,251,.4)}
.b-special{background:rgba(200,200,200,.1);color:#aaa;border:1px solid rgba(200,200,200,.2)}
.cdiv{height:1px;background:var(--border);margin-bottom:10px}
.prow{display:flex;align-items:center;justify-content:space-between;padding:3px 0}
.plabel{font-size:11px;color:var(--text3);font-weight:500}
.pval{font-family:'Rajdhani',sans-serif;font-size:15px;font-weight:700;color:var(--text)}
.pval.hl{color:var(--accent)}
.pval.gr{color:#a855f7}
.pval.ps{color:#f093fb}
.no-results{grid-column:1/-1;text-align:center;padding:80px 20px;color:var(--text3)}
.no-results h3{font-family:'Rajdhani',sans-serif;font-size:24px;color:var(--text2);margin-bottom:8px}

/* STATS SECTION */
.stats-sec{background:var(--surface);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:48px 24px;margin:20px 0}
.stats-inner{max-width:1400px;margin:0 auto}
.sec-title{font-family:'Rajdhani',sans-serif;font-size:28px;font-weight:700;color:var(--text);margin-bottom:32px;display:flex;align-items:center;gap:12px}
.sec-title::after{content:'';flex:1;height:1px;background:var(--border)}
.sgrid{display:grid;grid-template-columns:1fr 1fr;gap:24px}
@media(max-width:768px){.sgrid{grid-template-columns:1fr}}
.panel-title{font-family:'Rajdhani',sans-serif;font-size:18px;font-weight:700;color:var(--text);margin-bottom:16px}
.t10-item{display:flex;align-items:center;gap:12px;padding:10px 16px;border-radius:8px;transition:background var(--tr);margin-bottom:4px;cursor:pointer}
.t10-item:hover{background:var(--surface2)}
.t10-rank{font-family:'Rajdhani',sans-serif;font-size:18px;font-weight:700;width:28px;color:var(--text3);flex-shrink:0}
.t10-rank.gold{color:var(--accent)}
.t10-name{flex:1;font-size:14px;font-weight:500;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.t10-price{font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:700;color:var(--accent);flex-shrink:0}
.bar-chart{display:flex;flex-direction:column;gap:10px}
.bar-label{display:flex;justify-content:space-between;font-size:12px;color:var(--text2);margin-bottom:4px}
.bar-track{background:var(--surface3);border-radius:4px;height:10px;overflow:hidden}
.bar-fill{height:100%;border-radius:4px;width:0;transition:width 1s ease}
.sum-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px}
@media(max-width:600px){.sum-cards{grid-template-columns:1fr}}
.scard{background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:16px;text-align:center}
.scard-label{font-size:11px;color:var(--text3);text-transform:uppercase;letter-spacing:1px;margin-bottom:6px}
.scard-val{font-family:'Rajdhani',sans-serif;font-size:22px;font-weight:700;color:var(--accent)}

/* FOOTER */
footer{background:var(--surface);border-top:1px solid var(--border);padding:32px 24px;text-align:center}
.footer-logo{font-family:'Rajdhani',sans-serif;font-size:32px;font-weight:700;color:var(--accent);margin-bottom:8px}
.footer-tag{font-size:14px;color:var(--text3);margin-bottom:16px}
.pb-spin{width:32px;height:32px;border-radius:50%;border:3px solid #fff;position:relative;overflow:hidden;display:inline-block;animation:spin 4s linear infinite;margin-bottom:12px}
.pb-spin::before{content:'';position:absolute;top:0;left:0;width:100%;height:50%;background:var(--accent2)}
.pb-spin::after{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:9px;height:9px;background:#fff;border-radius:50%;border:2px solid #333;z-index:2}
.pb-spin .belt2{position:absolute;top:calc(50% - 2px);left:0;width:100%;height:4px;background:#333;z-index:1}
@keyframes spin{100%{transform:rotate(360deg)}}
.footer-copy{font-size:12px;color:var(--text3)}

/* SCAN FAB */
.scan-fab{position:fixed;bottom:28px;right:28px;z-index:200;background:var(--accent);color:#000;border:none;border-radius:50px;padding:14px 20px;display:flex;align-items:center;gap:10px;font-family:'Rajdhani',sans-serif;font-size:15px;font-weight:700;letter-spacing:.5px;cursor:pointer;box-shadow:0 4px 24px rgba(255,222,0,0.35);transition:transform var(--tr),box-shadow var(--tr)}
.scan-fab:hover{transform:translateY(-2px) scale(1.03);box-shadow:0 6px 32px rgba(255,222,0,0.5)}
.fab-pb{width:22px;height:22px;border-radius:50%;border:2px solid rgba(0,0,0,.4);position:relative;overflow:hidden;flex-shrink:0}
.fab-pb::before{content:'';position:absolute;top:0;left:0;width:100%;height:50%;background:rgba(0,0,0,.3)}
.fab-pb::after{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:6px;height:6px;background:rgba(0,0,0,.5);border-radius:50%;border:1px solid rgba(0,0,0,.3);z-index:2}
.fab-belt{position:absolute;top:calc(50% - 1px);left:0;width:100%;height:2px;background:rgba(0,0,0,.3);z-index:1}

/* MODAL */
.modal-ov{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.85);display:flex;align-items:center;justify-content:center;padding:16px;opacity:0;pointer-events:none;transition:opacity .2s ease;backdrop-filter:blur(4px)}
.modal-ov.open{opacity:1;pointer-events:auto}
.modal{background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:24px;width:100%;max-width:460px;max-height:90vh;overflow-y:auto;position:relative;transform:scale(.95);transition:transform .2s ease}
.modal-ov.open .modal{transform:scale(1)}
@media(max-width:600px){.modal-ov{padding:0;align-items:flex-end}.modal{border-radius:20px 20px 0 0;max-height:95vh}}
.modal-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:20px}
.modal-ttl{font-family:'Rajdhani',sans-serif;font-size:22px;font-weight:700;color:var(--accent)}
.modal-cls{background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text2);width:36px;height:36px;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px;transition:all var(--tr)}
.modal-cls:hover{border-color:var(--accent2);color:var(--accent2)}
.cam-wrap{position:relative;border-radius:12px;overflow:hidden;border:2px solid var(--accent);background:#000;aspect-ratio:4/3;margin-bottom:16px}
#camFeed{width:100%;height:100%;object-fit:cover;display:block}
.sf{position:absolute;inset:0;pointer-events:none}
.sc{position:absolute;width:28px;height:28px;border-color:var(--accent);border-style:solid;border-width:0}
.sc.tl{top:12px;left:12px;border-top-width:3px;border-left-width:3px;border-radius:4px 0 0 0}
.sc.tr{top:12px;right:12px;border-top-width:3px;border-right-width:3px;border-radius:0 4px 0 0}
.sc.bl{bottom:12px;left:12px;border-bottom-width:3px;border-left-width:3px;border-radius:0 0 0 4px}
.sc.br{bottom:12px;right:12px;border-bottom-width:3px;border-right-width:3px;border-radius:0 0 4px 0}
.sl{position:absolute;left:12px;right:12px;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);animation:scanMove 2s ease-in-out infinite;box-shadow:0 0 8px var(--accent)}
@keyframes scanMove{0%,100%{top:15%}50%{top:80%}}
.flash-ov{position:absolute;inset:0;background:#fff;opacity:0;pointer-events:none;transition:opacity .1s}
.flash-ov.flash{opacity:.8}
.api-sec{margin-bottom:16px}
.api-sec label{font-size:12px;color:var(--text3);display:block;margin-bottom:6px;font-weight:500}
.api-inp{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:8px;color:var(--text);padding:9px 12px;font-size:13px;font-family:'Inter',sans-serif;outline:none;transition:border-color var(--tr)}
.api-inp:focus{border-color:var(--accent)}
.mbtn{width:100%;background:var(--accent);color:#000;border:none;border-radius:10px;padding:12px;font-family:'Rajdhani',sans-serif;font-size:17px;font-weight:700;cursor:pointer;transition:all var(--tr);display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:8px}
.mbtn:hover{background:#ffe840;box-shadow:0 4px 16px rgba(255,222,0,.3)}
.mbtn:disabled{background:var(--surface3);color:var(--text3);cursor:not-allowed;box-shadow:none}
.mbtn-sec{width:100%;background:var(--surface2);color:var(--text2);border:1px solid var(--border);border-radius:10px;padding:11px;font-family:'Rajdhani',sans-serif;font-size:16px;font-weight:600;cursor:pointer;transition:all var(--tr)}
.mbtn-sec:hover{border-color:var(--accent);color:var(--accent)}
.scan-st{text-align:center;padding:12px;font-size:14px;color:var(--text2);display:none}
.spinner{display:inline-block;width:20px;height:20px;border:2px solid var(--surface3);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite;margin-right:8px;vertical-align:middle}
.scan-res{display:none;margin-top:16px}
.res-found{background:linear-gradient(135deg,rgba(0,200,100,.1),rgba(0,150,80,.1));border:1px solid rgba(0,200,100,.3);border-radius:12px;padding:20px;margin-bottom:12px}
.res-nf{background:rgba(204,0,0,.1);border:1px solid rgba(204,0,0,.3);border-radius:12px;padding:20px;text-align:center}
.res-name{font-family:'Rajdhani',sans-serif;font-size:24px;font-weight:700;color:var(--text);margin-bottom:4px}
.res-num{font-size:13px;color:var(--text3);margin-bottom:12px}
.res-prices{display:flex;flex-direction:column;gap:6px;margin-bottom:12px}
.res-prow{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.05)}
.res-plabel{font-size:13px;color:var(--text3)}
.res-pval{font-family:'Rajdhani',sans-serif;font-size:18px;font-weight:700;color:var(--accent)}
.cam-err{background:rgba(204,0,0,.1);border:1px solid rgba(204,0,0,.3);border-radius:12px;padding:20px;text-align:center;display:none}
.cam-err p{color:var(--text2);font-size:14px;line-height:1.6}
#scanCanvas{display:none}
</style>
</head>
<body>

<nav class="navbar" id="navbar">
  <a class="nav-logo" href="#">
    <div class="pb"><div class="belt"></div></div>
    <span class="nav-logo-text">Pokemall</span>
  </a>
  <div class="nav-search">
    <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="search" id="searchInput" placeholder="Search cards by name..." autocomplete="off">
  </div>
  <div class="nav-stats"><span>518</span> Cards &nbsp;•&nbsp; Scarlet &amp; Violet 151</div>
</nav>

<div class="hero-wrap">
  <div class="hero">
    <div class="hero-text">
      <div class="hero-tag">&#127942; Expert Curator</div>
      <h1 class="hero-title">Pokemall</h1>
      <p class="hero-sub">Japanese Scarlet &amp; Violet 151<br>&mdash; Complete Price Guide</p>
      <p class="hero-meta">Curated by <strong>Kemal</strong> &nbsp;&bull;&nbsp; 518 Cards &nbsp;&bull;&nbsp; Real Market Prices</p>
    </div>
    <div class="hero-img-wrap">
      <div class="hero-glow"></div>
      <img src="kemal.jpg" alt="Kemal" onerror="this.style.display='none'">
    </div>
  </div>
</div>
<div class="hero-wrap">
  <div class="hero-stats">
    <div class="hstat">
      <div class="hstat-label">Total Cards</div>
      <div class="hstat-val">518</div>
      <div class="hstat-sub">Including all variants</div>
    </div>
    <div class="hstat">
      <div class="hstat-label">Avg Price</div>
      <div class="hstat-val">$10.16</div>
      <div class="hstat-sub">Ungraded market value</div>
    </div>
    <div class="hstat">
      <div class="hstat-label">Most Valuable</div>
      <div class="hstat-val">$390.00</div>
      <div class="hstat-sub">Gengar [Master Ball] #94</div>
    </div>
    <div class="hstat">
      <div class="hstat-label">Collection Value</div>
      <div class="hstat-val">$5,261</div>
      <div class="hstat-sub">Total ungraded sum</div>
    </div>
  </div>
</div>

<div class="filter-bar">
  <div class="filter-btns">
    <button class="fb active" data-f="all">All Cards</button>
    <button class="fb" data-f="holo">Holo</button>
    <button class="fb" data-f="rare">Rare</button>
    <button class="fb" data-f="ultra">Ultra Rare</button>
    <button class="fb" data-f="special">Special Art</button>
    <button class="fb" data-f="under5">Under $5</button>
    <button class="fb" data-f="under20">Under $20</button>
    <button class="fb" data-f="over20">$20+</button>
  </div>
  <select class="sort-sel" id="sortSel">
    <option value="default">Featured</option>
    <option value="priceHigh">Price: High to Low</option>
    <option value="priceLow">Price: Low to High</option>
    <option value="cardNum">Card Number</option>
    <option value="nameAZ">Name A-Z</option>
  </select>
</div>
<div class="rc-wrap">Showing <span id="rc">518</span> cards</div>

<div class="card-grid" id="cardGrid"></div>

<div class="stats-sec">
  <div class="stats-inner">
    <div class="sec-title">Collection Analytics</div>
    <div class="sgrid">
      <div>
        <div class="panel-title">&#127942; Top 10 Most Valuable</div>
        <div id="top10"></div>
      </div>
      <div>
        <div class="panel-title">&#128202; Price Distribution by Rarity</div>
        <div class="bar-chart" id="rarityChart"></div>
        <div class="sum-cards">
          <div class="scard"><div class="scard-label">Avg Ungraded</div><div class="scard-val">$10.16</div></div>
          <div class="scard"><div class="scard-label">Total Value</div><div class="scard-val">$5,261</div></div>
          <div class="scard"><div class="scard-label">Cards w/ PSA</div><div class="scard-val" id="gradedCnt">-</div></div>
        </div>
      </div>
    </div>
  </div>
</div>

<footer>
  <div class="footer-logo">Pokemall</div>
  <div class="pb-spin"><div class="belt2"></div></div>
  <div class="footer-tag">Powered by Kemal&#39;s Collection</div>
  <div class="footer-copy">Data sourced from original price guide &nbsp;&bull;&nbsp; Japanese Scarlet &amp; Violet 151</div>
</footer>

<button class="scan-fab" id="scanFab">
  <div class="fab-pb"><div class="fab-belt"></div></div>
  Scan Card
</button>

<div class="modal-ov" id="scanModal">
  <div class="modal">
    <div class="modal-hdr">
      <div class="modal-ttl">&#128247; Card Scanner</div>
      <button class="modal-cls" id="mClose">&#x2715;</button>
    </div>
    <div class="api-sec">
      <label>Anthropic API Key (saved locally in browser)</label>
      <input type="password" class="api-inp" id="apiKey" placeholder="sk-ant-...">
    </div>
    <div id="camSec">
      <div class="cam-wrap">
        <video id="camFeed" autoplay playsinline muted></video>
        <div class="sf">
          <div class="sc tl"></div><div class="sc tr"></div>
          <div class="sc bl"></div><div class="sc br"></div>
          <div class="sl"></div>
        </div>
        <div class="flash-ov" id="flashOv"></div>
      </div>
      <button class="mbtn" id="scanBtn">
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>
        Scan Card
      </button>
    </div>
    <div class="cam-err" id="camErr">
      <p>&#9888;&#65039; Camera access denied or unavailable.<br>Please allow camera permissions and try again.</p>
    </div>
    <div class="scan-st" id="scanSt"><span class="spinner"></span>Analyzing card with AI...</div>
    <div class="scan-res" id="scanRes"></div>
    <canvas id="scanCanvas"></canvas>
  </div>
</div>

<script>
""")

html_parts.append("const CARDS = ")
html_parts.append(cards_json)
html_parts.append(""";

const RC = {
  'Common':'r-common','Uncommon':'r-uncommon','Rare':'r-rare',
  'Rare Holo':'r-rare-holo','Holo Rare':'r-holo-rare',
  'Ultra Rare':'r-ultra-rare','Special Art':'r-special-art','Special':'r-special'
};
const BC = {
  'Common':'b-common','Uncommon':'b-uncommon','Rare':'b-rare',
  'Rare Holo':'b-rare-holo','Holo Rare':'b-holo-rare',
  'Ultra Rare':'b-ultra-rare','Special Art':'b-special-art','Special':'b-special'
};
const IMG_DIR = "imgs/";

const parseP = v => v ? parseFloat(v.replace(/[$,]/g,'')) : 0;
const byPrice = [...CARDS].sort((a,b) => parseP(b.ungraded) - parseP(a.ungraded));
const top5 = new Set(byPrice.slice(0,5).map(c=>c.id));

let curFilter='all', curSort='default', curSearch='';

function cardHTML(c) {
  const isHolo = ['Holo Rare','Rare Holo','Special Art','Ultra Rare'].includes(c.rarity);
  const num = c.number.padStart(3,'0');
  const rc = RC[c.rarity]||'r-common';
  const bc = BC[c.rarity]||'b-common';
  return `<div class="poke-card ${rc}" id="card-${c.id}" data-id="${c.id}">
    ${isHolo?'<div class="shimmer"></div>':''}
    ${top5.has(c.id)?'<div class="feat-badge">&#11088; Featured</div>':''}
    <div class="cnum">#${num}</div>
    <div class="cimg">
      ${c.img
        ? `<img src="${IMG_DIR}${c.img}" alt="${c.name}" loading="lazy" onerror="this.style.display='none'">`
        : `<svg width="60" height="60" viewBox="0 0 80 80" fill="none"><circle cx="40" cy="40" r="36" stroke="#3a3a5a" stroke-width="3"/><circle cx="40" cy="40" r="10" fill="#3a3a5a"/><path d="M4 40h72M40 4v72" stroke="#3a3a5a" stroke-width="2"/></svg>`
      }
    </div>
    <div class="cname" title="${c.name}">${c.name}</div>
    <span class="rbadge ${bc}">${c.rarity}</span>
    <div class="cdiv"></div>
    <div class="prow"><span class="plabel">Ungraded</span><span class="pval hl">${c.ungraded||'—'}</span></div>
    ${c.grade9?`<div class="prow"><span class="plabel">Grade 9</span><span class="pval gr">${c.grade9}</span></div>`:''}
    ${c.psa10?`<div class="prow"><span class="plabel">PSA 10</span><span class="pval ps">${c.psa10}</span></div>`:''}
  </div>`;
}

function getFiltered() {
  let list = [...CARDS];
  if (curSearch) {
    const q = curSearch.toLowerCase();
    list = list.filter(c => c.name.toLowerCase().includes(q)||c.fullTitle.toLowerCase().includes(q)||c.number.includes(q));
  }
  switch(curFilter) {
    case 'holo': list=list.filter(c=>['Holo Rare','Rare Holo'].includes(c.rarity)); break;
    case 'rare': list=list.filter(c=>c.rarity==='Rare'); break;
    case 'ultra': list=list.filter(c=>c.rarity==='Ultra Rare'); break;
    case 'special': list=list.filter(c=>c.rarity==='Special Art'); break;
    case 'under5': list=list.filter(c=>parseP(c.ungraded)<5); break;
    case 'under20': list=list.filter(c=>parseP(c.ungraded)<20); break;
    case 'over20': list=list.filter(c=>parseP(c.ungraded)>=20); break;
  }
  switch(curSort) {
    case 'priceHigh': list.sort((a,b)=>parseP(b.ungraded)-parseP(a.ungraded)); break;
    case 'priceLow': list.sort((a,b)=>parseP(a.ungraded)-parseP(b.ungraded)); break;
    case 'cardNum': list.sort((a,b)=>parseInt(a.number||0)-parseInt(b.number||0)); break;
    case 'nameAZ': list.sort((a,b)=>a.name.localeCompare(b.name)); break;
  }
  return list;
}

function renderCards() {
  const grid = document.getElementById('cardGrid');
  const list = getFiltered();
  document.getElementById('rc').textContent = list.length;
  if (!list.length) {
    grid.innerHTML = '<div class="no-results"><h3>No cards found</h3><p>Try adjusting your search or filters</p></div>';
    return;
  }
  grid.innerHTML = list.map(cardHTML).join('');
}

document.getElementById('searchInput').addEventListener('input', e => {
  curSearch = e.target.value.trim();
  renderCards();
});
document.querySelectorAll('.fb').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.fb').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    curFilter = btn.dataset.f;
    renderCards();
  });
});
document.getElementById('sortSel').addEventListener('change', e => {
  curSort = e.target.value;
  renderCards();
});
window.addEventListener('scroll', () => {
  document.getElementById('navbar').classList.toggle('scrolled', scrollY > 20);
});

function scrollToCard(id) {
  curFilter='all'; curSearch=''; curSort='default';
  document.querySelectorAll('.fb').forEach(b=>b.classList.remove('active'));
  document.querySelector('[data-f="all"]').classList.add('active');
  document.getElementById('searchInput').value='';
  document.getElementById('sortSel').value='default';
  renderCards();
  setTimeout(()=>{
    const el = document.getElementById('card-'+id);
    if(el) el.scrollIntoView({behavior:'smooth',block:'center'});
  },100);
}

function buildTop10() {
  document.getElementById('top10').innerHTML = byPrice.slice(0,10).map((c,i) =>
    `<div class="t10-item" onclick="scrollToCard(${c.id})">
      <span class="t10-rank ${i<3?'gold':''}">&#35;${i+1}</span>
      <span class="t10-name">${c.name} <span style="color:var(--text3);font-size:11px">#${c.number}</span></span>
      <span class="t10-price">${c.ungraded}</span>
    </div>`
  ).join('');
}

function buildChart() {
  const avg={}, cnt={};
  CARDS.forEach(c=>{
    if(!avg[c.rarity]){avg[c.rarity]=0;cnt[c.rarity]=0;}
    avg[c.rarity]+=parseP(c.ungraded); cnt[c.rarity]++;
  });
  const data = Object.entries(avg).map(([r,s])=>({r,avg:s/cnt[r],count:cnt[r]})).sort((a,b)=>b.avg-a.avg);
  const maxA = Math.max(...data.map(d=>d.avg));
  const cols = {
    'Ultra Rare':'linear-gradient(90deg,#FFD700,#FFA500)',
    'Special Art':'linear-gradient(90deg,#f093fb,#f5576c)',
    'Holo Rare':'linear-gradient(90deg,#667eea,#764ba2)',
    'Rare Holo':'linear-gradient(90deg,#818cf8,#5b9cf6)',
    'Rare':'linear-gradient(90deg,#5b9cf6,#3b82f6)',
    'Uncommon':'linear-gradient(90deg,#4CAF50,#2e7d32)',
    'Common':'linear-gradient(90deg,#888,#555)',
    'Special':'linear-gradient(90deg,#aaa,#666)'
  };
  document.getElementById('rarityChart').innerHTML = data.map(d=>`
    <div>
      <div class="bar-label">
        <span>${d.r} <span style="color:var(--text3);font-size:11px">(${d.count})</span></span>
        <span>avg $${d.avg.toFixed(2)}</span>
      </div>
      <div class="bar-track">
        <div class="bar-fill" data-w="${(d.avg/maxA*100).toFixed(1)}" style="background:${cols[d.r]||'linear-gradient(90deg,#888,#555)'}"></div>
      </div>
    </div>`).join('');
  setTimeout(()=>{
    document.querySelectorAll('.bar-fill').forEach(b=>{ b.style.width=b.dataset.w+'%'; });
  },300);
  document.getElementById('gradedCnt').textContent = CARDS.filter(c=>c.grade9||c.psa10).length;
}

// SCANNER
let stream = null;
document.getElementById('scanFab').addEventListener('click', openScan);
document.getElementById('mClose').addEventListener('click', closeScan);
document.getElementById('scanModal').addEventListener('click', e=>{ if(e.target.id==='scanModal') closeScan(); });

document.getElementById('apiKey').addEventListener('change', e => {
  localStorage.setItem('pmall_key', e.target.value);
});

async function openScan() {
  document.getElementById('scanModal').classList.add('open');
  const saved = localStorage.getItem('pmall_key');
  if(saved) document.getElementById('apiKey').value = saved;
  document.getElementById('scanRes').style.display='none';
  document.getElementById('scanSt').style.display='none';
  document.getElementById('camErr').style.display='none';
  document.getElementById('camSec').style.display='block';
  try {
    stream = await navigator.mediaDevices.getUserMedia({video:{facingMode:'environment',width:{ideal:1280},height:{ideal:960}}});
    document.getElementById('camFeed').srcObject = stream;
  } catch(e) {
    document.getElementById('camSec').style.display='none';
    document.getElementById('camErr').style.display='block';
  }
}
function closeScan() {
  document.getElementById('scanModal').classList.remove('open');
  if(stream){stream.getTracks().forEach(t=>t.stop());stream=null;}
}

document.getElementById('scanBtn').addEventListener('click', async () => {
  const apiKey = document.getElementById('apiKey').value.trim();
  if(!apiKey){alert('Please enter your Anthropic API key first.');return;}
  localStorage.setItem('pmall_key', apiKey);
  const video = document.getElementById('camFeed');
  const canvas = document.getElementById('scanCanvas');
  const ctx = canvas.getContext('2d');
  const flash = document.getElementById('flashOv');
  flash.classList.add('flash');
  setTimeout(()=>flash.classList.remove('flash'),200);
  canvas.width = video.videoWidth||640;
  canvas.height = video.videoHeight||480;
  ctx.drawImage(video,0,0,canvas.width,canvas.height);
  const b64 = canvas.toDataURL('image/jpeg',0.8).replace(/^data:image\/jpeg;base64,/,'');
  document.getElementById('scanBtn').disabled=true;
  document.getElementById('scanSt').style.display='block';
  document.getElementById('scanRes').style.display='none';
  const cardList = CARDS.map(c=>({name:c.name,number:c.number,rarity:c.rarity,ungraded:c.ungraded,grade9:c.grade9,psa10:c.psa10}));
  try {
    const res = await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json','x-api-key':apiKey,'anthropic-version':'2023-06-01','anthropic-dangerous-direct-browser-access':'true'},
      body:JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:500,
        messages:[{
          role:'user',
          content:[
            {type:'image',source:{type:'base64',media_type:'image/jpeg',data:b64}},
            {type:'text',text:`Bu bir Pokemon kart fotografi. Kartin adini ve numarasini tespit et. Elimdeki kart listesi: ${JSON.stringify(cardList.slice(0,200))}. Listede eslesen karti bul ve SADECE su formatta JSON dondur (baska hicbir sey yazma): {"found":true,"cardName":"kart adi","cardNumber":"001","normalPrice":"$X.XX","holoPrice":null,"gradedPrice":null,"rarity":"rarity tipi","confidence":"high","notes":"aciklama"}`}
          ]
        }]
      })
    });
    const data = await res.json();
    document.getElementById('scanSt').style.display='none';
    document.getElementById('scanBtn').disabled=false;
    if(data.error) throw new Error(data.error.message);
    const txt = data.content[0].text;
    let result;
    try {
      const m = txt.match(/\{[\s\S]*\}/);
      result = JSON.parse(m?m[0]:txt);
    } catch(e){ throw new Error('Could not parse AI response'); }
    showResult(result);
  } catch(err) {
    document.getElementById('scanSt').style.display='none';
    document.getElementById('scanBtn').disabled=false;
    document.getElementById('scanRes').style.display='block';
    document.getElementById('scanRes').innerHTML=`<div class="res-nf"><p style="color:var(--accent2);font-size:16px;font-weight:600;margin-bottom:8px">&#9888;&#65039; Error</p><p style="color:var(--text2);font-size:13px">${err.message}</p></div>`;
  }
});

function showResult(r) {
  const el = document.getElementById('scanRes');
  el.style.display='block';
  if(!r.found){
    el.innerHTML=`<div class="res-nf"><p style="color:var(--text2);font-size:15px;font-weight:600;margin-bottom:6px">Card not found in collection</p><p style="color:var(--text3);font-size:13px">Try scanning again or check the lighting</p></div><button class="mbtn-sec" onclick="document.getElementById('scanRes').style.display='none'">Scan Again</button>`;
    return;
  }
  const match = CARDS.find(c=>c.number===r.cardNumber||c.name.toLowerCase()===r.cardName.toLowerCase());
  const confColor = {high:'#4CAF50',medium:'#FFA500',low:'#CC0000'}[r.confidence]||'#aaa';
  el.innerHTML=`<div class="res-found">
    <p style="font-size:13px;color:#4CAF50;margin-bottom:8px;font-weight:600">&#10003; Card Identified!</p>
    <div class="res-name">${r.cardName}</div>
    <div class="res-num">#${r.cardNumber} &bull; ${r.rarity||'Unknown'}</div>
    <div class="res-prices">
      <div class="res-prow"><span class="res-plabel">Ungraded</span><span class="res-pval">${r.normalPrice||'—'}</span></div>
      ${r.holoPrice?`<div class="res-prow"><span class="res-plabel">Grade 9</span><span class="res-pval" style="color:#a855f7">${r.holoPrice}</span></div>`:''}
      ${r.gradedPrice?`<div class="res-prow"><span class="res-plabel">PSA 10 &#9733;</span><span class="res-pval" style="color:#f093fb">${r.gradedPrice}</span></div>`:''}
    </div>
    <p style="font-size:12px;color:var(--text3)">Confidence: <span style="color:${confColor};font-weight:600">${(r.confidence||'').toUpperCase()}</span>${r.notes?` &bull; ${r.notes}`:''}</p>
  </div>
  <div style="display:flex;gap:8px;margin-top:0">
    ${match?`<button class="mbtn" style="flex:1" onclick="closeScan();scrollToCard(${match.id})">View in Collection</button>`:'<button class="mbtn" style="flex:1;opacity:.5" disabled>View in Collection</button>'}
    <button class="mbtn-sec" style="flex:0.6" onclick="document.getElementById('scanRes').style.display='none'">Scan Again</button>
  </div>`;
}

document.addEventListener('DOMContentLoaded', () => {
  renderCards();
  buildTop10();
  buildChart();
  document.body.classList.add('loaded');
  console.log('[Pokemall] Cards loaded:', CARDS.length);
});
</script>
</body>
</html>""")

html = ''.join(html_parts)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done! File size: {len(html):,} bytes ({len(html)//1024} KB)')
