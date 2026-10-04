import json
from pathlib import Path

ROOT = Path('/Users/sym/Code/dark-souls-3-lore')
OUT_DIR = ROOT / 'compositions'
OUT_DIR.mkdir(exist_ok=True)

# Common CSS & styling for Dark Souls 3 gothic aesthetic
COMMON_CSS = """
  @font-face {
    font-family: LabChinese;
    src: url('assets/PingFang.ttc');
  }
  * { box-sizing: border-box; }
  #root {
    position: absolute;
    inset: 0;
    background: #06080d;
    color: #f1f5f9;
    font-family: LabChinese, -apple-system, sans-serif;
    overflow: hidden;
  }
  .bg-wrap {
    position: absolute;
    inset: 0;
    overflow: hidden;
  }
  .bg-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.38;
    filter: brightness(0.78) contrast(1.2) saturate(1.1);
  }
  .bg-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 35%, rgba(6,8,13,0.3) 0%, rgba(5,6,9,0.92) 80%);
  }
  .ember-glow {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 90%, rgba(245, 158, 11, 0.12) 0%, transparent 60%);
    pointer-events: none;
  }

  /* Global Timeline Rail */
  .timeline-rail {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 36px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 15;
  }
  .timeline-steps {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .timeline-node {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 1px;
    background: rgba(255, 255, 255, 0.05);
    color: #64748b;
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
  .timeline-node.active {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
    border-color: rgba(245, 158, 11, 0.6);
    box-shadow: 0 0 15px rgba(245, 158, 11, 0.25);
  }
  .timeline-arrow {
    color: #475569;
    font-size: 14px;
  }
  .topic-tag {
    font-size: 18px;
    color: #94a3b8;
    letter-spacing: 2px;
    font-weight: 600;
  }

  /* Hero Title Area */
  .title-area {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 96px;
    z-index: 10;
  }
  .main-title {
    font-size: 54px;
    font-weight: 900;
    line-height: 1.15;
    margin: 0;
    letter-spacing: 2px;
    background: linear-gradient(135deg, #ffffff 20%, #fde68a 55%, #f59e0b 85%, #d97706 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 15px rgba(0,0,0,0.8));
  }
  .sub-tagline {
    font-size: 22px;
    color: #e2e8f0;
    margin-top: 8px;
    font-weight: 500;
    letter-spacing: 1.5px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .tagline-badge {
    padding: 3px 10px;
    border-radius: 6px;
    background: rgba(239, 68, 68, 0.2);
    border: 1px solid rgba(239, 68, 68, 0.45);
    color: #fca5a5;
    font-size: 15px;
    font-weight: 700;
  }

  /* Split Layout Container */
  .content-split {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 225px;
    bottom: 125px;
    display: flex;
    gap: 36px;
    z-index: 10;
  }

  /* Left Flow / Logic Column */
  .logic-column {
    flex: 1.15;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 16px;
  }
  .logic-box {
    background: linear-gradient(145deg, rgba(17, 24, 39, 0.85) 0%, rgba(9, 13, 22, 0.92) 100%);
    border: 1.5px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 20px 24px;
    position: relative;
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
  }
  .logic-box.highlight {
    border-color: rgba(245, 158, 11, 0.5);
    box-shadow: 0 10px 30px rgba(0,0,0,0.6), 0 0 25px rgba(245, 158, 11, 0.15);
  }
  .logic-box.danger {
    border-color: rgba(239, 68, 68, 0.5);
    box-shadow: 0 10px 30px rgba(0,0,0,0.6), 0 0 25px rgba(239, 68, 68, 0.15);
  }
  .box-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 10px;
  }
  .box-pill {
    font-size: 14px;
    font-weight: 800;
    padding: 3px 10px;
    border-radius: 6px;
    letter-spacing: 1px;
  }
  .box-pill.gold {
    background: rgba(245, 158, 11, 0.25);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.4);
  }
  .box-pill.red {
    background: rgba(239, 68, 68, 0.25);
    color: #fca5a5;
    border: 1px solid rgba(239, 68, 68, 0.4);
  }
  .box-pill.blue {
    background: rgba(59, 130, 246, 0.25);
    color: #93c5fd;
    border: 1px solid rgba(59, 130, 246, 0.4);
  }
  .box-title {
    font-size: 24px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: 1px;
  }
  .box-bullets {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .bullet-item {
    font-size: 18px;
    line-height: 1.45;
    color: #cbd5e1;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }
  .bullet-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #f59e0b;
    margin-top: 10px;
    flex-shrink: 0;
  }
  .bullet-item b {
    color: #fbbf24;
  }
  .bullet-item.alert b {
    color: #f87171;
  }

  /* Right Art Card Column */
  .art-column {
    flex: 0.85;
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    border: 2px solid rgba(245, 158, 11, 0.35);
    background: #0d111a;
    box-shadow: 0 20px 45px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.15);
  }
  .art-img-wrap {
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
  }
  .art-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
  }
  .art-gradient-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(6,8,13,0.1) 40%, rgba(6,8,13,0.95) 100%);
  }
  .art-info-overlay {
    position: absolute;
    left: 24px;
    right: 24px;
    bottom: 24px;
    z-index: 5;
  }
  .art-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 700;
    background: rgba(245, 158, 11, 0.25);
    border: 1px solid rgba(245, 158, 11, 0.5);
    color: #fbbf24;
    margin-bottom: 8px;
  }
  .art-name {
    font-size: 34px;
    font-weight: 900;
    color: #ffffff;
    margin: 0 0 6px 0;
    letter-spacing: 1.5px;
    text-shadow: 0 3px 10px rgba(0,0,0,0.8);
  }
  .art-desc {
    font-size: 17px;
    color: #cbd5e1;
    line-height: 1.4;
    margin: 0;
  }

  /* Bottom Floating Subtitle (No Progress Bar!) */
  .caption-container {
    position: absolute;
    left: 80px;
    right: 80px;
    bottom: 28px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 25;
  }
  .caption-box {
    position: absolute;
    background: rgba(8, 11, 18, 0.94);
    backdrop-filter: blur(16px);
    border: 1.5px solid rgba(245, 158, 11, 0.45);
    padding: 14px 44px;
    border-radius: 40px;
    font-size: 30px;
    font-weight: 700;
    color: #ffffff;
    box-shadow: 0 10px 30px rgba(0,0,0,0.85), 0 0 25px rgba(245, 158, 11, 0.2);
    text-align: center;
    white-space: nowrap;
    letter-spacing: 1px;
  }

  /* Special Grid for Scene 3 (4 Lords) */
  .grid-4-lords {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 220px;
    bottom: 125px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    z-index: 10;
  }
  .lord-card {
    background: linear-gradient(160deg, rgba(20, 26, 40, 0.88) 0%, rgba(10, 13, 20, 0.95) 100%);
    border: 1.5px solid rgba(255, 255, 255, 0.12);
    border-radius: 18px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    backdrop-filter: blur(14px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.7);
    position: relative;
  }
  .lord-card.active-glow {
    border-color: rgba(245, 158, 11, 0.6);
    box-shadow: 0 15px 35px rgba(0,0,0,0.8), 0 0 25px rgba(245, 158, 11, 0.2);
  }
  .lord-card-img-wrap {
    height: 230px;
    width: 100%;
    position: relative;
    overflow: hidden;
  }
  .lord-card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .lord-card-content {
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: space-between;
  }
  .lord-card-title {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 6px 0;
  }
  .lord-card-badge {
    display: inline-block;
    font-size: 13px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 5px;
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.35);
    margin-bottom: 10px;
  }
  .lord-card-bullets {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .lord-bullet {
    font-size: 15px;
    line-height: 1.4;
    color: #cbd5e1;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  .lord-bullet-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #f59e0b;
    margin-top: 7px;
    flex-shrink: 0;
  }
  .lord-bullet b {
    color: #fbbf24;
  }
"""

def generate_scene_01():
    # Dur: 25.5s
    # Audio: 23.95s (start 0.5s)
    # Nano art: nano_gwyn.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-01" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-01-bg" class="bg-img" src="assets/images/scene01_awakening.jpg" data-layout-allow-overflow data-duration="25.5" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node active">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">06 灭火破晓</div>
    </div>
    <div class="topic-tag">前因后果 · 宇宙级诅咒诞生</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">起源与前因 · 葛温的万年诅咒</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">万恶之源</span>
      <span>并不是为了救世，而是神权为了永恒特权的自我献祭！</span>
    </div>
  </div>

  <div class="content-split">
    <!-- Left Logic Flow -->
    <div class="logic-column">
      <div id="node-01-1" class="logic-box highlight">
        <div class="box-header">
          <span class="box-pill gold">起因 · 初火衰退</span>
          <span class="box-title">统治危机：火熄则神权覆灭</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>初火诞生孕育了巨人和众神，<b>太阳王葛温</b>建立起至高统治。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>然而初火终有寿命，一旦熄灭，属于<b>人类与深渊的黑暗时代</b>必将来临。</span></div>
        </div>
      </div>

      <div id="node-01-2" class="logic-box danger">
        <div class="box-header">
          <span class="box-pill red">转折 · 以身饲火</span>
          <span class="box-title">葛温投火：违背自然的极端血祭</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>因极度恐惧黑暗，葛温率领骑士前往初始火炉，<b>强行将自身神魂当柴烧</b>！</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>初代薪王诞生，初火强行续命，但<b>自然生死法则自此彻底崩坏</b>！</span></div>
        </div>
      </div>

      <div id="node-01-3" class="logic-box">
        <div class="box-header">
          <span class="box-pill blue">后果 · 诅咒套牢</span>
          <span class="box-title">定下铁律：每隔千年必须献祭王者</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>初火每隔千年就会再次熄灭，必须抓捕最强王者<b>周而复始地自焚献祭</b>。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>人类被烙上不死人诅咒，世间生灵永受折磨——这正是<b>黑魂3危机的真正根源</b>！</span></div>
        </div>
      </div>
    </div>

    <!-- Right Art Card (Nano Gwyn Art) -->
    <div id="art-01" class="art-column">
      <div class="art-img-wrap" data-layout-allow-overflow>
        <img id="nano-gwyn-img" class="art-img" src="assets/images/nano_gwyn.jpg" data-layout-allow-overflow data-duration="25.5" />
        <div class="art-gradient-overlay"></div>
        <div class="art-info-overlay">
          <div class="art-badge">初代薪王 / 始作俑者</div>
          <h2 class="art-name">太阳王 · 葛温</h2>
          <p class="art-desc">
            "为了维系神族的黄金幻象，他强行点燃了自身，却把整个世界拖入了永无止境的炼狱与枯竭！"
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-01-1" class="caption-box" style="opacity: 0;">很多朋友看黑魂总觉得看不懂，其实黑魂三底层逻辑极其硬核！</div>
    <div id="c-01-2" class="caption-box" style="opacity: 0;">一切前因回到最初：神王葛温为维系神权，强行以身投火开启诅咒！</div>
    <div id="c-01-3" class="caption-box" style="opacity: 0;">从此天地定下规矩：初火每隔千年熄灭，必须献祭强者给世界续命！</div>
    <div id="c-01-4" class="caption-box" style="opacity: 0;">这一场违背自然规律的万年循环，彻底拉开了黑魂三的残酷大幕！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-01-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -25, duration: 25.5, ease: "none" }}, 0);
  tl.fromTo("#nano-gwyn-img", {{ scale: 1.05 }}, {{ scale: 1.15, duration: 25.5, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);
  tl.fromTo("#art-01", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.9, ease: "power2.out" }}, 0.6);

  // Nodes Sequence
  tl.fromTo("#node-01-1", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.8);
  tl.fromTo("#node-01-2", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 5.5);
  tl.fromTo("#node-01-3", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 13.0);

  // Captions
  tl.set("#c-01-1", {{ opacity: 1 }}, 0.50).set("#c-01-1", {{ opacity: 0 }}, 5.30);
  tl.set("#c-01-2", {{ opacity: 1 }}, 5.50).set("#c-01-2", {{ opacity: 0 }}, 12.80);
  tl.set("#c-01-3", {{ opacity: 1 }}, 13.00).set("#c-01-3", {{ opacity: 0 }}, 18.80);
  tl.set("#c-01-4", {{ opacity: 1 }}, 19.00).set("#c-01-4", {{ opacity: 0 }}, 24.50);

  window.__timelines["scene-01"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-01.html').write_text(html)

def generate_scene_02():
    # Dur: 27.0s
    # Audio: 25.54s (start 0.5s)
    # Nano art: nano_twin_princes.jpg / scene02_firelink.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-02" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-02-bg" class="bg-img" src="assets/images/scene02_firelink.jpg" data-layout-allow-overflow data-duration="27.0" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node active">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">06 灭火破晓</div>
    </div>
    <div class="topic-tag">黑魂3危机 · 体系全面暴雷</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">黑魂3危机 · 薪王集体罢工跑路</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">系统崩溃</span>
      <span>初火油尽灯枯！现任拒绝接盘，老将从坟里叫醒后全体撂挑子！</span>
    </div>
  </div>

  <div class="content-split">
    <!-- Left Logic Flow -->
    <div class="logic-column">
      <div id="node-02-1" class="logic-box danger">
        <div class="box-header">
          <span class="box-pill red">危机爆发 · 现任拒传</span>
          <span class="box-title">双王子摆烂：我们不做神权耗材</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>初火被榨取万年已连渣都不剩，世界即将彻底断电。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>现任法定继承人<b>洛斯里克双王子</b>看透骗局，<b>坚决拒绝传火</b>！</span></div>
        </div>
      </div>

      <div id="node-02-2" class="logic-box highlight">
        <div class="box-header">
          <span class="box-pill gold">应急机制 · 掘墓返工</span>
          <span class="box-title">钟声敲响：强行唤醒四大往昔薪王</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>传火祭祀场拉响最高警报，敲响荒原无主古钟。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>将历史上曾经自焚过一次的<b>四位大能薪王从棺椁中硬拉起来</b>！</span></div>
        </div>
      </div>

      <div id="node-02-3" class="logic-box">
        <div class="box-header">
          <span class="box-pill blue">全面瘫痪 · 各自跑路</span>
          <span class="box-title">大佬震怒：老子早就烧过一次，滚！</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item alert"><div class="bullet-dot"></div><span><b>深渊监视者</b>回法兰互砍，<b>尤姆</b>回罪都封刀，<b>埃尔德里奇</b>去食神！</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>四大王座彻底空悬，世界灭绝进入最后倒计时！</span></div>
        </div>
      </div>
    </div>

    <!-- Right Art Card (Nano Twin Princes) -->
    <div id="art-02" class="art-column">
      <div class="art-img-wrap" data-layout-allow-overflow>
        <img id="nano-princes-img" class="art-img" src="assets/images/nano_twin_princes.jpg" data-layout-allow-overflow data-duration="27.0" />
        <div class="art-gradient-overlay"></div>
        <div class="art-info-overlay">
          <div class="art-badge">罢工领头人 / 现任王子</div>
          <h2 class="art-name">洛斯里克 & 洛里安</h2>
          <p class="art-desc">
            "王位是可悲的诅咒，传火不过是谎言。我们选择在城堡最深处，静静注视火的熄灭！"
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-02-1" class="caption-box" style="opacity: 0;">到了黑魂三的时代，初火已经被榨得连渣都不剩了！</div>
    <div id="c-02-2" class="caption-box" style="opacity: 0;">现任王室双王子直接摆烂，看透骗局拒绝传火！</div>
    <div id="c-02-3" class="caption-box" style="opacity: 0;">祭祀场敲响古钟拉响最高警报，强行掘墓叫醒四个老薪王返工！</div>
    <div id="c-02-4" class="caption-box" style="opacity: 0;">结果薪王们集体罢工：老子早就烧过一次，绝不回炉当柴！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-02-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.07, y: -20, duration: 27.0, ease: "none" }}, 0);
  tl.fromTo("#nano-princes-img", {{ scale: 1.05 }}, {{ scale: 1.14, duration: 27.0, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);
  tl.fromTo("#art-02", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.9, ease: "power2.out" }}, 0.6);

  // Nodes Sequence
  tl.fromTo("#node-02-1", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.8);
  tl.fromTo("#node-02-2", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 11.2);
  tl.fromTo("#node-02-3", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 18.5);

  // Captions
  tl.set("#c-02-1", {{ opacity: 1 }}, 0.50).set("#c-02-1", {{ opacity: 0 }}, 5.60);
  tl.set("#c-02-2", {{ opacity: 1 }}, 5.80).set("#c-02-2", {{ opacity: 0 }}, 11.00);
  tl.set("#c-02-3", {{ opacity: 1 }}, 11.20).set("#c-02-3", {{ opacity: 0 }}, 18.20);
  tl.set("#c-02-4", {{ opacity: 1 }}, 18.50).set("#c-02-4", {{ opacity: 0 }}, 26.00);

  window.__timelines["scene-02"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-02.html').write_text(html)

def generate_scene_03():
    # Dur: 31.0s
    # Audio: 29.57s (start 0.5s)
    # Nano art: nano_abyss_watchers.jpg, nano_yhorm.jpg, nano_aldrich.jpg, nano_twin_princes.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-03" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-03-bg" class="bg-img" src="assets/images/scene03_lords.jpg" data-layout-allow-overflow data-duration="31.0" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node active">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">06 灭火破晓</div>
    </div>
    <div class="topic-tag">深层机理 · 四大薪王档案</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">四大薪王档案 · 为何宁死不回王座</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">血泪教训</span>
      <span>他们每一个都曾全力以赴，换来的却是毁灭、背叛与永恒痛苦！</span>
    </div>
  </div>

  <!-- 4 Columns Grid showcasing Nano Arts -->
  <div class="grid-4-lords">
    <!-- Lord 1: Abyss Watchers -->
    <div id="lord-card-1" class="lord-card">
      <div class="lord-card-img-wrap" data-layout-allow-overflow>
        <img class="lord-card-img" src="assets/images/nano_abyss_watchers.jpg" data-layout-allow-overflow data-duration="31.0" />
      </div>
      <div class="lord-card-content">
        <div>
          <span class="lord-card-badge">法兰要塞</span>
          <h3 class="lord-card-title">法兰不死队</h3>
          <div class="lord-card-bullets">
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>饮狼血立誓<b>诛灭深渊</b></span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>自身却反遭深渊恶兆污染</span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>在老巢陷入<b>永恒同门互砍</b></span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Lord 2: Yhorm the Giant -->
    <div id="lord-card-2" class="lord-card">
      <div class="lord-card-img-wrap" data-layout-allow-overflow>
        <img class="lord-card-img" src="assets/images/nano_yhorm.jpg" data-layout-allow-overflow data-duration="31.0" />
      </div>
      <div class="lord-card-content">
        <div>
          <span class="lord-card-badge">罪业之都</span>
          <h3 class="lord-card-title">巨人尤姆</h3>
          <div class="lord-card-bullets">
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>以异族之躯<b>守护人族臣民</b></span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>舍身传火试图平息罪火暴动</span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>归来满城百姓<b>全部烧成黑炭</b></span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Lord 3: Aldrich -->
    <div id="lord-card-3" class="lord-card">
      <div class="lord-card-img-wrap" data-layout-allow-overflow>
        <img class="lord-card-img" src="assets/images/nano_aldrich.jpg" data-layout-allow-overflow data-duration="31.0" />
      </div>
      <div class="lord-card-content">
        <div>
          <span class="lord-card-badge">幽邃教堂</span>
          <h3 class="lord-card-title">噬神者·埃尔德里奇</h3>
          <div class="lord-card-bullets">
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>预见初火必熄，<b>深海时代</b>降临</span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>彻底抛弃传火神圣幻象</span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>直接攻入王城<b>吞噬葛温幺子</b></span></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Lord 4: Twin Princes -->
    <div id="lord-card-4" class="lord-card">
      <div class="lord-card-img-wrap" data-layout-allow-overflow>
        <img class="lord-card-img" src="assets/images/nano_twin_princes.jpg" data-layout-allow-overflow data-duration="31.0" />
      </div>
      <div class="lord-card-content">
        <div>
          <span class="lord-card-badge">大书库顶层</span>
          <h3 class="lord-card-title">洛斯里克双王子</h3>
          <div class="lord-card-bullets">
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>自幼受尽王室配种<b>血脉折磨</b></span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span>看透神权血祭的荒谬虚妄</span></div>
            <div class="lord-bullet"><div class="lord-bullet-dot"></div><span><b>誓不当柴</b>，冷眼坐看火灭</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-03-1" class="caption-box" style="opacity: 0;">为什么薪王宁可去死也不回王座？因为全都是血泪教训！</div>
    <div id="c-03-2" class="caption-box" style="opacity: 0;">法兰不死队饮狼血斩深渊反遭侵蚀，陷入永恒同门自残！</div>
    <div id="c-03-3" class="caption-box" style="opacity: 0;">巨人尤姆为臣民传火，归来却见满城化为黑炭，万念俱灰！</div>
    <div id="c-03-4" class="caption-box" style="opacity: 0;">埃尔德里奇预见深海时代，叛变吞食神明寻求蜕变！</div>
    <div id="c-03-5" class="caption-box" style="opacity: 0;">双王子自幼受尽血脉诅咒，看透神权谎言，誓死拒当耗材！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-03-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -25, duration: 31.0, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);

  // Cards Sequence
  tl.fromTo("#lord-card-1", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power2.out" }}, 0.8);
  tl.fromTo("#lord-card-2", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power2.out" }}, 1.2);
  tl.fromTo("#lord-card-3", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power2.out" }}, 1.6);
  tl.fromTo("#lord-card-4", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.7, ease: "power2.out" }}, 2.0);

  // Highlighting active lord according to voiceover
  tl.to("#lord-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 0 35px rgba(245, 158, 11, 0.4)", duration: 0.4 }}, 5.5)
    .to("#lord-card-1", {{ borderColor: "rgba(255, 255, 255, 0.12)", boxShadow: "0 15px 35px rgba(0,0,0,0.7)", duration: 0.4 }}, 12.5);

  tl.to("#lord-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 0 35px rgba(245, 158, 11, 0.4)", duration: 0.4 }}, 12.5)
    .to("#lord-card-2", {{ borderColor: "rgba(255, 255, 255, 0.12)", boxShadow: "0 15px 35px rgba(0,0,0,0.7)", duration: 0.4 }}, 19.0);

  tl.to("#lord-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 0 35px rgba(245, 158, 11, 0.4)", duration: 0.4 }}, 19.0)
    .to("#lord-card-3", {{ borderColor: "rgba(255, 255, 255, 0.12)", boxShadow: "0 15px 35px rgba(0,0,0,0.7)", duration: 0.4 }}, 25.0);

  tl.to("#lord-card-4", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 0 35px rgba(245, 158, 11, 0.4)", duration: 0.4 }}, 25.0);

  // Captions
  tl.set("#c-03-1", {{ opacity: 1 }}, 0.50).set("#c-03-1", {{ opacity: 0 }}, 5.30);
  tl.set("#c-03-2", {{ opacity: 1 }}, 5.50).set("#c-03-2", {{ opacity: 0 }}, 12.30);
  tl.set("#c-03-3", {{ opacity: 1 }}, 12.50).set("#c-03-3", {{ opacity: 0 }}, 18.80);
  tl.set("#c-03-4", {{ opacity: 1 }}, 19.00).set("#c-03-4", {{ opacity: 0 }}, 24.80);
  tl.set("#c-03-5", {{ opacity: 1 }}, 25.00).set("#c-03-5", {{ opacity: 0 }}, 30.20);

  window.__timelines["scene-03"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-03.html').write_text(html)

def generate_scene_04():
    # Dur: 29.5s
    # Audio: 27.70s (start 0.5s)
    # Nano art: scene04_ritual.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-04" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-04-bg" class="bg-img" src="assets/images/scene01_awakening.jpg" data-layout-allow-overflow data-duration="29.5" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node active">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">06 灭火破晓</div>
    </div>
    <div class="topic-tag">执行机制 · 终极保底清道夫</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">保底机制 · 叫醒灰烬强制催债</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">物理执法</span>
      <span>薪王不肯自己走回王座？那就踏遍世界，把他们的柴薪全部按回原位！</span>
    </div>
  </div>

  <div class="content-split">
    <!-- Left Logic Flow -->
    <div class="logic-column">
      <div id="node-04-1" class="logic-box">
        <div class="box-header">
          <span class="box-pill gold">应急机制 · 唤醒灰烬</span>
          <span class="box-title">谁是余灰？连当柴资格都没有的淘汰者</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>曾经尝试传火但神魂不够强大、直接烧成<b>残渣飞灰的失败者</b>。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>无欲无求，拥有<b>无限次死而复生</b>的绝对本能！</span></div>
        </div>
      </div>

      <div id="node-04-2" class="logic-box danger">
        <div class="box-header">
          <span class="box-pill red">催债使命 · 物理斩杀</span>
          <span class="box-title">强行执行：不回王座就斩首拖回</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item alert"><div class="bullet-dot"></div><span>踏平洛斯里克高墙、深入法兰沼泽、荡平冷冽谷与罪业之都！</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span><b>将叛逃薪王逐一斩杀</b>，割下柴薪与头颅带回祭祀场！</span></div>
        </div>
      </div>

      <div id="node-04-3" class="logic-box highlight">
        <div class="box-header">
          <span class="box-pill blue">柴薪共鸣 · 通道开启</span>
          <span class="box-title">四王归位：轰然打开最初火炉之门</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>当四大柴薪在王座上重燃，古老的传火能量彻底汇聚。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>营火共鸣，打通通往世界尽头<b>最初火炉</b>的传送大门！</span></div>
        </div>
      </div>
    </div>

    <!-- Right Art Card (Ritual) -->
    <div id="art-04" class="art-column">
      <div class="art-img-wrap" data-layout-allow-overflow>
        <img id="ritual-img" class="art-img" src="assets/images/scene04_ritual.jpg" data-layout-allow-overflow data-duration="29.5" />
        <div class="art-gradient-overlay"></div>
        <div class="art-info-overlay">
          <div class="art-badge">终极执行官 / 无火余灰</div>
          <h2 class="art-name">灰烬归位仪式</h2>
          <p class="art-desc">
            "若王者不归，余灰便跨越千难万险，将他们的遗骸按上冰冷的石座！"
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-04-1" class="caption-box" style="opacity: 0;">薪王全跑路怎么办？传火体制启动终极应急预案：唤醒无火余灰！</div>
    <div id="c-04-2" class="caption-box" style="opacity: 0;">余灰是当年连当柴资格都没有、直接烧成飞灰的淘汰者！</div>
    <div id="c-04-3" class="caption-box" style="opacity: 0;">余灰目标极其纯粹：薪王不肯主动返工，那就全部砍翻按回王座！</div>
    <div id="c-04-4" class="caption-box" style="opacity: 0;">当四大柴薪在祭祀场集齐共鸣，通往最初火炉的道路轰然开启！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-04-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -25, duration: 29.5, ease: "none" }}, 0);
  tl.fromTo("#ritual-img", {{ scale: 1.05 }}, {{ scale: 1.15, duration: 29.5, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);
  tl.fromTo("#art-04", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.9, ease: "power2.out" }}, 0.6);

  // Nodes Sequence
  tl.fromTo("#node-04-1", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.8);
  tl.fromTo("#node-04-2", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 12.5);
  tl.fromTo("#node-04-3", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 20.5);

  // Captions
  tl.set("#c-04-1", {{ opacity: 1 }}, 0.50).set("#c-04-1", {{ opacity: 0 }}, 5.80);
  tl.set("#c-04-2", {{ opacity: 1 }}, 6.00).set("#c-04-2", {{ opacity: 0 }}, 12.20);
  tl.set("#c-04-3", {{ opacity: 1 }}, 12.50).set("#c-04-3", {{ opacity: 0 }}, 20.20);
  tl.set("#c-04-4", {{ opacity: 1 }}, 20.50).set("#c-04-4", {{ opacity: 0 }}, 28.50);

  window.__timelines["scene-04"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-04.html').write_text(html)

def generate_scene_05():
    # Dur: 28.0s
    # Audio: 26.02s (start 0.5s)
    # Nano art: scene05_kiln.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-05" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-05-bg" class="bg-img" src="assets/images/scene02_firelink.jpg" data-layout-allow-overflow data-duration="28.0" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node active">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">06 灭火破晓</div>
    </div>
    <div class="topic-tag">决战舞台 · 千万年执念具象</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">终极决战 · 薪王化身与流血暗日</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">宿命之战</span>
      <span>击败他，不是为了延续神话，而是亲手斩断千万年强加于世的枷锁！</span>
    </div>
  </div>

  <div class="content-split">
    <!-- Left Logic Flow -->
    <div class="logic-column">
      <div id="node-05-1" class="logic-box danger">
        <div class="box-header">
          <span class="box-pill red">末日异象 · 时空坍缩</span>
          <span class="box-title">初始火炉：流血的黑暗之环日蚀</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>世间时空彻底错乱聚拢，历代王朝废墟在此崩塌凝固。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>苍穹悬挂着淌血的<b>黑暗之环日蚀</b>，整部传火史的苍凉在此定格！</span></div>
        </div>
      </div>

      <div id="node-05-2" class="logic-box">
        <div class="box-header">
          <span class="box-pill gold">终极守门 · 历代化身</span>
          <span class="box-title">薪王化身：千千万万传火者的聚合体</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>初代葛温与千万代传火英雄的<b>残存执念凝为一体</b>。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>他会使用历代玩家与英雄的所有武器技艺，守卫最后残焰！</span></div>
        </div>
      </div>

      <div id="node-05-3" class="logic-box highlight">
        <div class="box-header">
          <span class="box-pill blue">灵魂悲歌 · 葛温复苏</span>
          <span class="box-title">钢琴三连音：始作俑者的宿命悲叹</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>二阶段<b>哀伤的钢琴三连音（Plin Plin Plon）</b>轰然响起。</span></div>
          <div class="bullet-item alert"><div class="bullet-dot"></div><span>击败他，正是<b>彻底终结葛温万年前亲手犯下的原罪</b>！</span></div>
        </div>
      </div>
    </div>

    <!-- Right Art Card (Kiln / Soul of Cinder) -->
    <div id="art-05" class="art-column">
      <div class="art-img-wrap" data-layout-allow-overflow>
        <img id="kiln-img" class="art-img" src="assets/images/scene05_kiln.jpg" data-layout-allow-overflow data-duration="28.0" />
        <div class="art-gradient-overlay"></div>
        <div class="art-info-overlay">
          <div class="art-badge">最终守门人 / 执念集合体</div>
          <h2 class="art-name">薪王们的化身</h2>
          <p class="art-desc">
            "他是千万代英雄壮烈献身的丰碑，也是神权万年谎言最悲凉的守墓人！"
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-05-1" class="caption-box" style="opacity: 0;">来到世界尽头的初始火炉，天上挂着流血的黑暗之环日蚀！</div>
    <div id="c-05-2" class="caption-box" style="opacity: 0;">最后守门人薪王化身，是初代葛温与千万代英雄执念的集合体！</div>
    <div id="c-05-3" class="caption-box" style="opacity: 0;">击败化身，就是战胜过去千万年来强加于世界的传火枷锁！</div>
    <div id="c-05-4" class="caption-box" style="opacity: 0;">当二阶段哀伤的钢琴三连音响起，无数宿命的悲壮在此彻底引爆！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-05-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -25, duration: 28.0, ease: "none" }}, 0);
  tl.fromTo("#kiln-img", {{ scale: 1.05 }}, {{ scale: 1.15, duration: 28.0, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);
  tl.fromTo("#art-05", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.9, ease: "power2.out" }}, 0.6);

  // Nodes Sequence
  tl.fromTo("#node-05-1", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.8);
  tl.fromTo("#node-05-2", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 6.5);
  tl.fromTo("#node-05-3", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 13.5);

  // Captions
  tl.set("#c-05-1", {{ opacity: 1 }}, 0.50).set("#c-05-1", {{ opacity: 0 }}, 6.30);
  tl.set("#c-05-2", {{ opacity: 1 }}, 6.50).set("#c-05-2", {{ opacity: 0 }}, 13.20);
  tl.set("#c-05-3", {{ opacity: 1 }}, 13.50).set("#c-05-3", {{ opacity: 0 }}, 19.50);
  tl.set("#c-05-4", {{ opacity: 1 }}, 19.80).set("#c-05-4", {{ opacity: 0 }}, 27.00);

  window.__timelines["scene-05"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-05.html').write_text(html)

def generate_scene_06():
    # Dur: 30.5s
    # Audio: 28.06s (start 0.5s)
    # Nano art: scene06_firekeeper.jpg
    html = f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-06" data-width="1920" data-height="1080" style="width:1920px;height:1080px;position:relative;overflow:hidden;">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-06-bg" class="bg-img" src="assets/images/scene01_awakening.jpg" data-layout-allow-overflow data-duration="30.5" />
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="timeline-rail">
    <div class="timeline-steps">
      <div class="timeline-node">01 葛温源头</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">02 薪王罢工</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">03 叛逃真相</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">04 余灰催债</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node">05 终局决战</div>
      <div class="timeline-arrow">➔</div>
      <div class="timeline-node active">06 灭火破晓</div>
    </div>
    <div class="topic-tag">终局抉择 · 挣脱枷锁破晓新生</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">终局抉择 · 熄灭初火与破晓新生</h1>
    <div class="sub-tagline">
      <span class="tagline-badge">破局新生</span>
      <span>放下对初火的盲目执念，让病态的万年诅咒归于宁静的长夜！</span>
    </div>
  </div>

  <div class="content-split">
    <!-- Left Logic Flow -->
    <div class="logic-column">
      <div id="node-06-1" class="logic-box danger">
        <div class="box-header">
          <span class="box-pill red">虚妄结局 · 强行传火</span>
          <span class="box-title">油尽灯枯：毫无意义的苟延残喘</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>初火早已被榨干，哪怕你全身坐上去，也只能冒出几颗凄凉火星。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>盲目传火只会让世界在扭曲畸变中继续受罪，<b>毫无解脱可言</b>！</span></div>
        </div>
      </div>

      <div id="node-06-2" class="logic-box highlight">
        <div class="box-header">
          <span class="box-pill gold">真正解脱 · 托付初火</span>
          <span class="box-title">灭火结局：召唤防火女捧起微光</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>将残存的初火交予<b>防火女</b>双手中，让初火自然熄灭。</span></div>
          <div class="bullet-item"><div class="bullet-dot"></div><span>烧了几万年的病态诅咒彻底斩断，天地归于<b>深邃宁静的黑夜</b>。</span></div>
        </div>
      </div>

      <div id="node-06-3" class="logic-box">
        <div class="box-header">
          <span class="box-pill blue">未来希望 · 静待破晓</span>
          <span class="box-title">黑夜之后：清澈的新火必将复生</span>
        </div>
        <div class="box-bullets">
          <div class="bullet-item"><div class="bullet-dot"></div><span>黑暗并不代表灭亡，而是万物休养生息的自然节律。</span></div>
          <div class="bullet-item alert"><div class="bullet-dot"></div><span>正如防火女最后的轻语：<b>在漫长黑暗尽头，微小的火苗必将重新诞生！</b></span></div>
        </div>
      </div>
    </div>

    <!-- Right Art Card (Firekeeper) -->
    <div id="art-06" class="art-column">
      <div class="art-img-wrap" data-layout-allow-overflow>
        <img id="firekeeper-img" class="art-img" src="assets/images/scene06_firekeeper.jpg" data-layout-allow-overflow data-duration="30.5" />
        <div class="art-gradient-overlay"></div>
        <div class="art-info-overlay">
          <div class="art-badge">长夜伴侣 / 真正解脱</div>
          <h2 class="art-name">防火女 · 灭火之伴</h2>
          <p class="art-desc">
            "余灰大人，您还能听到我的声音吗……火已熄灭，但请别害怕，黑夜的尽头终有破晓！"
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Captions -->
  <div class="caption-container">
    <div id="c-06-1" class="caption-box" style="opacity: 0;">击败薪王化身后，整个世界的命运终于交到了你的手中！</div>
    <div id="c-06-2" class="caption-box" style="opacity: 0;">继续传火？初火早已油尽灯枯，坐上去只能冒几点残星，毫无意义！</div>
    <div id="c-06-3" class="caption-box" style="opacity: 0;">真正的解脱是把初火交给防火女：让烧了几万年的病态诅咒彻底熄灭！</div>
    <div id="c-06-4" class="caption-box" style="opacity: 0;">世界迎来宁静长夜：在漫长的黑暗尽头，终有一日，微小的火苗会重获新生！</div>
  </div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Pan
  tl.fromTo("#scene-06-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -25, duration: 30.5, ease: "none" }}, 0);
  tl.fromTo("#firekeeper-img", {{ scale: 1.05 }}, {{ scale: 1.15, duration: 30.5, ease: "none" }}, 0);

  // Layout In
  tl.fromTo(".timeline-rail", {{ opacity: 0, y: -15 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8 }}, 0.4);
  tl.fromTo("#art-06", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.9, ease: "power2.out" }}, 0.6);

  // Nodes Sequence
  tl.fromTo("#node-06-1", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 0.8);
  tl.fromTo("#node-06-2", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 5.8);
  tl.fromTo("#node-06-3", {{ opacity: 0, y: 25 }}, {{ opacity: 1, y: 0, duration: 0.6 }}, 12.8);

  // Captions
  tl.set("#c-06-1", {{ opacity: 1 }}, 0.50).set("#c-06-1", {{ opacity: 0 }}, 5.60);
  tl.set("#c-06-2", {{ opacity: 1 }}, 5.80).set("#c-06-2", {{ opacity: 0 }}, 12.50);
  tl.set("#c-06-3", {{ opacity: 1 }}, 12.80).set("#c-06-3", {{ opacity: 0 }}, 20.20);
  tl.set("#c-06-4", {{ opacity: 1 }}, 20.50).set("#c-06-4", {{ opacity: 0 }}, 29.50);

  window.__timelines["scene-06"] = tl;
}}
</script>
</template>
</body>
</html>
"""
    (OUT_DIR / 'scene-06.html').write_text(html)

def main():
    print("Generating scene-01.html...")
    generate_scene_01()
    print("Generating scene-02.html...")
    generate_scene_02()
    print("Generating scene-03.html...")
    generate_scene_03()
    print("Generating scene-04.html...")
    generate_scene_04()
    print("Generating scene-05.html...")
    generate_scene_05()
    print("Generating scene-06.html...")
    generate_scene_06()
    print("All scenes generated successfully!")

if __name__ == '__main__':
    main()
