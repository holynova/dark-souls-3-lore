import json
from pathlib import Path

ROOT = Path('/Users/sym/Code/dark-souls-3-lore')
meta = json.loads((ROOT / 'scenes_meta.json').read_text())

# Common CSS & styling for Dark Souls 3 gothic aesthetic
DS3_COMMON_CSS = """
  @font-face {
    font-family: LabChinese;
    src: url('assets/PingFang.ttc');
  }
  * { box-sizing: border-box; }
  #root {
    position: absolute;
    inset: 0;
    background: #08090d;
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
    opacity: 0.42;
    filter: brightness(0.85) contrast(1.15) saturate(1.1);
  }
  .bg-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 40%, rgba(8,9,13,0.3) 0%, rgba(6,7,10,0.92) 80%);
  }
  .ember-glow {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 85%, rgba(245, 158, 11, 0.12) 0%, transparent 60%);
    pointer-events: none;
  }

  /* Top Navigation */
  .header {
    position: absolute;
    left: 80px;
    top: 48px;
    right: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
  }
  .badge-chapter {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 8px 22px;
    border-radius: 30px;
    background: rgba(245, 158, 11, 0.16);
    border: 1.5px solid rgba(245, 158, 11, 0.45);
    color: #fbbf24;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 2px;
    box-shadow: 0 0 20px rgba(245, 158, 11, 0.2);
  }
  .topic-tag {
    font-size: 22px;
    color: #94a3b8;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 500;
  }

  /* Hero Title Area */
  .title-area {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 120px;
    text-align: center;
    z-index: 10;
  }
  .main-title {
    font-size: 64px;
    font-weight: 900;
    line-height: 1.2;
    margin: 0;
    letter-spacing: 3px;
    background: linear-gradient(135deg, #ffffff 15%, #fde68a 50%, #f59e0b 85%, #d97706 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 6px 20px rgba(0,0,0,0.8));
  }
  .sub-title {
    font-size: 26px;
    color: #cbd5e1;
    margin-top: 12px;
    font-weight: 400;
    letter-spacing: 3px;
  }

  /* Cards Container */
  .cards-grid {
    position: absolute;
    left: 80px;
    right: 80px;
    top: 275px;
    height: 590px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 32px;
    z-index: 10;
  }
  .card-item {
    flex: 1;
    height: 100%;
    border-radius: 20px;
    padding: 32px 30px;
    background: linear-gradient(160deg, rgba(22, 27, 38, 0.82) 0%, rgba(10, 12, 18, 0.94) 100%);
    border: 1.5px solid rgba(245, 158, 11, 0.3);
    box-shadow: 0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1);
    backdrop-filter: blur(16px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
  }
  .card-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, transparent, #f59e0b, transparent);
  }

  .card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }
  .card-icon-title {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .card-icon {
    font-size: 32px;
  }
  .card-heading {
    font-size: 28px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: 1px;
  }
  .card-badge {
    font-size: 16px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 12px;
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.4);
    letter-spacing: 1px;
  }

  .card-quote {
    font-size: 19px;
    color: #fbbf24;
    font-style: italic;
    line-height: 1.4;
    margin: 10px 0 14px 0;
    padding-left: 14px;
    border-left: 3px solid #f59e0b;
  }

  .card-details {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-top: 10px;
  }
  .detail-row {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    font-size: 19px;
    line-height: 1.5;
    color: #cbd5e1;
  }
  .detail-bullet {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #f59e0b;
    box-shadow: 0 0 8px #f59e0b;
    margin-top: 10px;
    flex-shrink: 0;
  }

  .card-footer {
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 17px;
    color: #94a3b8;
  }
  .footer-highlight {
    color: #f59e0b;
    font-weight: 600;
  }

  /* Bottom Captions & Progress */
  .caption-container {
    position: absolute;
    left: 100px;
    right: 100px;
    bottom: 35px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 20;
  }
  .caption-box {
    position: absolute;
    background: rgba(10, 13, 20, 0.92);
    backdrop-filter: blur(14px);
    border: 1.5px solid rgba(245, 158, 11, 0.4);
    padding: 12px 42px;
    border-radius: 40px;
    font-size: 32px;
    font-weight: 600;
    color: #ffffff;
    box-shadow: 0 10px 35px rgba(0,0,0,0.8), 0 0 25px rgba(245, 158, 11, 0.15);
    text-align: center;
    white-space: nowrap;
  }
  .progress-track {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 5px;
    background: rgba(255,255,255,0.08);
    z-index: 30;
  }
  .progress-bar {
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, #ea580c, #f59e0b, #fbbf24);
    box-shadow: 0 0 10px #f59e0b;
    transform-origin: left;
  }
"""

def generate_scene_01(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-01" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-01-bg" class="bg-img" src="assets/images/scene01_awakening.jpg" alt="Cemetery of Ash" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter">🔥 PROLOGUE · 灰烬墓地</div>
    <div class="topic-tag">DARK SOULS III · 传火史诗</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">火渐熄 · 王不见王</h1>
    <div class="sub-title">昔日初火衰微停滞，沉睡千年的无火余灰破棺而起</div>
  </div>

  <div class="cards-grid">
    <div id="scene-01-card-1" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🕯️</span>
            <span class="card-heading">初火濒临熄灭</span>
          </div>
          <span class="card-badge">世界崩坏</span>
        </div>
        <div class="card-quote">“当火光渐熄，唯有黑暗笼罩一切。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>传火轮回历经千万载，初火衰竭殆尽</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>时空在洛斯里克汇聚挤压，世界趋向停滞</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>古老的钟声敲响，宣告世界末日的降临</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>天地异象</span>
        <span class="footer-highlight">终末钟声鸣响</span>
      </div>
    </div>

    <div id="scene-01-card-2" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">⚔️</span>
            <span class="card-heading">无火的余灰</span>
          </div>
          <span class="card-badge">主角身份</span>
        </div>
        <div class="card-quote">“连薪柴都不够资格燃烧的灰烬之躯。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>曾经尝试传火却化为灰烬的不死人</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>不具柴薪资格，却对余火有着无尽渴望</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>被赋予最后猎王与挽救宿命的艰难重任</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>宿命烙印</span>
        <span class="footer-highlight">追寻余火的灰烬</span>
      </div>
    </div>

    <div id="scene-01-card-3" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🏰</span>
            <span class="card-heading">洛斯里克高墙</span>
          </div>
          <span class="card-badge">王土沉沦</span>
        </div>
        <div class="card-quote">“漂泊王土的交汇处，通往火炉的险阻。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>巍峨高墙自大地隆起，隔绝了诸王故地</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>骑士化为游魂，羽翼恶魔徘徊城头</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>灰烬走出墓地，踏上凶险莫测的征程</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>初始征途</span>
        <span class="footer-highlight">踏出墓地之门</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-01-1" class="caption-box" style="opacity: 0;">火渐熄，王不见王。</div>
    <div id="c-01-2" class="caption-box" style="opacity: 0;">当最初的薪火再次衰微，洛斯里克的钟声响彻荒原。</div>
    <div id="c-01-3" class="caption-box" style="opacity: 0;">那些曾经为了传火燃烧自身、却力有不逮化为尘埃的无火余灰，</div>
    <div id="c-01-4" class="caption-box" style="opacity: 0;">自沉睡千年的墓穴中再次苏醒。</div>
  </div>

  <div class="progress-track"><div id="p-01" class="progress-bar"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-01-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -20, duration: {dur}, ease: "none" }}, 0);
  
  // Title & Header In
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-01-card-1", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-01-card-2", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.2);
  tl.fromTo("#scene-01-card-3", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.6);
  tl.to("#scene-01-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 0.8)
    .to("#scene-01-card-1", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 8.5)
    .to("#scene-01-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 8.5)
    .to("#scene-01-card-2", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 13.8)
    .to("#scene-01-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 13.8);

  // Captions
  tl.set("#c-01-1", {{ opacity: 1 }}, 0.50).set("#c-01-1", {{ opacity: 0 }}, 3.80);
  tl.set("#c-01-2", {{ opacity: 1 }}, 3.80).set("#c-01-2", {{ opacity: 0 }}, 8.50);
  tl.set("#c-01-3", {{ opacity: 1 }}, 8.50).set("#c-01-3", {{ opacity: 0 }}, 13.80);
  tl.set("#c-01-4", {{ opacity: 1 }}, 13.80).set("#c-01-4", {{ opacity: 0 }}, 17.50);

  // Progress Bar
  tl.fromTo("#p-01", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-01"] = tl;
}}
</script>
</template>
</body>
</html>"""

def generate_scene_02(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-02" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-02-bg" class="bg-img" src="assets/images/scene02_firelink.jpg" alt="Firelink Shrine" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter">🔥 CHAPTER I · 传火祭祀场</div>
    <div class="topic-tag">DARK SOULS III · 避难所与王座</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">王座空悬 · 诸王背誓</h1>
    <div class="sub-title">昔日传火诸王弃座而逃，唯有鲁道斯与盲眼防火女静候灰烬</div>
  </div>

  <div class="cards-grid">
    <div id="scene-02-card-1" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🪑</span>
            <span class="card-heading">宏伟的石质王座</span>
          </div>
          <span class="card-badge">五座王座</span>
        </div>
        <div class="card-quote">“刻着伟大薪王名号的宝座，如今尽是虚无。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>环形祭祀场中立着五位薪王的石制王座</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>本应履行传火重责的诸王，纷纷潜逃故地</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>空旷的殿堂在微光中诉说着绝望与苍凉</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>祭祀场异象</span>
        <span class="footer-highlight">王不见王</span>
      </div>
    </div>

    <div id="scene-02-card-2" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">👑</span>
            <span class="card-heading">放逐者鲁道斯</span>
          </div>
          <span class="card-badge">唯一留守</span>
        </div>
        <div class="card-quote">“即使身材矮小，我亦是实实在在的薪王。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>唯有库尔兰的鲁道斯独自端坐于王座之上</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>精通灵魂炼成技艺，洞悉火之时代的残酷</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>自愿再次化为柴薪，等待最后的一刻</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>坚定意志</span>
        <span class="footer-highlight">静待薪尽火灭</span>
      </div>
    </div>

    <div id="scene-02-card-3" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">👁️</span>
            <span class="card-heading">盲眼防火女</span>
          </div>
          <span class="card-badge">营火侍从</span>
        </div>
        <div class="card-quote">“愿余火引导灰烬大人的道路。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>眼蒙银质冠冕，守护螺旋剑插落的篝火</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>将游离无主的灵魂转化为灰烬力量的源泉</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>默默见证无数灰烬的出发、沉沦与新生</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>神圣契约</span>
        <span class="footer-highlight">守候营火余温</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-02-1" class="caption-box" style="opacity: 0;">传火祭祀场中，高耸的五座王座如今大多空空如也。</div>
    <div id="c-02-2" class="caption-box" style="opacity: 0;">为了维系濒临崩溃的世界，昔日薪王被钟声唤醒，</div>
    <div id="c-02-3" class="caption-box" style="opacity: 0;">然而他们却选择背弃宿命，逃离传火的使命，回到了各自荒芜的故土。</div>
  </div>

  <div class="progress-track"><div id="p-02" class="progress-bar"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-02-bg", {{ scale: 1.0, x: 0 }}, {{ scale: 1.07, x: -15, duration: {dur}, ease: "none" }}, 0);
  
  // Headers
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-02-card-1", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-02-card-2", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.2);
  tl.fromTo("#scene-02-card-3", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.6);
  tl.to("#scene-02-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 0.8)
    .to("#scene-02-card-1", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 4.8)
    .to("#scene-02-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 4.8)
    .to("#scene-02-card-2", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 10.2)
    .to("#scene-02-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 10.2);

  // Captions
  tl.set("#c-02-1", {{ opacity: 1 }}, 0.50).set("#c-02-1", {{ opacity: 0 }}, 4.80);
  tl.set("#c-02-2", {{ opacity: 1 }}, 4.80).set("#c-02-2", {{ opacity: 0 }}, 10.20);
  tl.set("#c-02-3", {{ opacity: 1 }}, 10.20).set("#c-02-3", {{ opacity: 0 }}, 16.80);

  // Progress Bar
  tl.fromTo("#p-02", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-02"] = tl;
}}
</script>
</template>
</body>
</html>"""

def generate_scene_03(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
  .cards-grid-4 {{
    position: absolute;
    left: 80px;
    right: 80px;
    top: 275px;
    height: 590px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    z-index: 10;
  }}
</style>
<div id="root" data-composition-id="scene-03" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-03-bg" class="bg-img" src="assets/images/scene03_lords.jpg" alt="Lords of Cinder" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter">🔥 CHAPTER II · 诸王悲歌</div>
    <div class="topic-tag">DARK SOULS III · 叛离的四大薪王</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">诸王悲歌 · 逃离传火宿命</h1>
    <div class="sub-title">深渊侵蚀、保护落空、追逐暗潮与厌弃轮回——每位薪王皆有拒绝的绝望</div>
  </div>

  <div class="cards-grid-4">
    <div id="scene-03-card-1" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🐺</span>
            <span class="card-heading">法兰不死队</span>
          </div>
        </div>
        <span class="card-badge">深渊监视者</span>
        <div class="card-quote">“饮下狼血誓言，终困深渊泥潭。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>以法兰狼血维系誓约，监视深渊迹象</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>体内血液终遭深渊污染，灵柩前骨肉相残</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>不死之身陷入无休止的内耗互杀地狱</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>悲剧结局</span>
        <span class="footer-highlight">永恒自残</span>
      </div>
    </div>

    <div id="scene-03-card-2" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🛡️</span>
            <span class="card-heading">巨人尤姆</span>
          </div>
        </div>
        <span class="card-badge">孤独守护者</span>
        <div class="card-quote">“为了守护子民传火，归来唯余焦土。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>身为异族巨人，却誓死庇护罪业之都人类</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>投身传火欲压制罪业火焰，却引发焚城浩劫</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>孤坐尸山王座，舍弃大盾心如死灰</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>昔日友人</span>
        <span class="footer-highlight">洋葱骑士的约定</span>
      </div>
    </div>

    <div id="scene-03-card-3" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🌊</span>
            <span class="card-heading">埃尔德里奇</span>
          </div>
        </div>
        <span class="card-badge">吞噬神明者</span>
        <div class="card-quote">“预见火熄深海，吞噬神体追寻暗潮。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>幽邃教堂圣职，因噬人恶习化为污秽泥泞</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>梦见火熄之后的“深海时代”，抛弃初火信仰</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>进军废弃王城亚诺尔隆德，残忍吞噬暗月之神</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>狂热狂信</span>
        <span class="footer-highlight">深海幽邃时代</span>
      </div>
    </div>

    <div id="scene-03-card-4" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">👑</span>
            <span class="card-heading">双王子</span>
          </div>
        </div>
        <span class="card-badge">王室血脉</span>
        <div class="card-quote">“传火不过是诅咒，请容我们在此安睡。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>洛斯里克王室为制造完美柴薪不择手段</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>王子双双残疾受咒，看透神权虚伪谎言</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>誓死拒绝登上薪王宝座，静待初火自灭</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>决然反抗</span>
        <span class="footer-highlight">断绝传火血脉</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-03-1" class="caption-box" style="opacity: 0;">法兰不死队在深渊的侵蚀中刀剑相向、自相残杀；</div>
    <div id="c-03-2" class="caption-box" style="opacity: 0;">巨人尤姆在罪业之都的废墟中独守空亡与悲愿；</div>
    <div id="c-03-3" class="caption-box" style="opacity: 0;">吞噬神明的埃尔德里奇狂热地追寻深海时代；</div>
    <div id="c-03-4" class="caption-box" style="opacity: 0;">而洛斯里克双王子，则彻底厌倦了神权的诅咒与传火的荒诞轮回。</div>
  </div>

  <div class="progress-track"><div id="p-03" class="progress-bar"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-03-bg", {{ scale: 1.05, y: 0 }}, {{ scale: 1.0, y: 15, duration: {dur}, ease: "none" }}, 0);
  
  // Headers
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-03-card-1", {{ opacity: 0, y: 40, scale: 0.95 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" }}, 0.5);
  tl.fromTo("#scene-03-card-2", {{ opacity: 0, y: 40, scale: 0.95 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-03-card-3", {{ opacity: 0, y: 40, scale: 0.95 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" }}, 1.1);
  tl.fromTo("#scene-03-card-4", {{ opacity: 0, y: 40, scale: 0.95 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.6, ease: "back.out(1.2)" }}, 1.4);
  tl.to("#scene-03-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 0.5)
    .to("#scene-03-card-1", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 5.5)
    .to("#scene-03-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 5.5)
    .to("#scene-03-card-2", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 10.8)
    .to("#scene-03-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 10.8)
    .to("#scene-03-card-3", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 15.2)
    .to("#scene-03-card-4", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 15.2);

  // Captions
  tl.set("#c-03-1", {{ opacity: 1 }}, 0.50).set("#c-03-1", {{ opacity: 0 }}, 5.50);
  tl.set("#c-03-2", {{ opacity: 1 }}, 5.50).set("#c-03-2", {{ opacity: 0 }}, 10.80);
  tl.set("#c-03-3", {{ opacity: 1 }}, 10.80).set("#c-03-3", {{ opacity: 0 }}, 15.20);
  tl.set("#c-03-4", {{ opacity: 1 }}, 15.20).set("#c-03-4", {{ opacity: 0 }}, 20.90);

  // Progress Bar
  tl.fromTo("#p-03", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-03"] = tl;
}}
</script>
</template>
</body>
</html>"""

def generate_scene_04(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-04" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-04-bg" class="bg-img" src="assets/images/scene04_ritual.jpg" alt="Ritual of Cinders" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter">🔥 CHAPTER III · 薪柴归座</div>
    <div class="topic-tag">DARK SOULS III · 猎王誓约与火炉启封</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">猎王之誓 · 柴薪共鸣</h1>
    <div class="sub-title">无火余灰踏平诸神，四大薪王柴薪归位，点燃通往最初火炉的通天烈焰</div>
  </div>

  <div class="cards-grid">
    <div id="scene-04-card-1" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">⚔️</span>
            <span class="card-heading">灰烬的猎王征途</span>
          </div>
          <span class="card-badge">凡躯弑神</span>
        </div>
        <div class="card-quote">“虽为卑微余灰，却斩下了王者的头颅。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>踏遍冷冽谷、地下监牢、罪业之都与洛斯里克</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>以凡人之躯接连斩杀传奇薪王与古老神明</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>将四位薪王的柴薪遗蜕强行带回传火祭祀场</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>征伐印记</span>
        <span class="footer-highlight">余火的觉醒</span>
      </div>
    </div>

    <div id="scene-04-card-2" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🔥</span>
            <span class="card-heading">王座共鸣仪式</span>
          </div>
          <span class="card-badge">柴薪聚首</span>
        </div>
        <div class="card-quote">“当柴薪齐聚，王座将化作通往世界尽头的桥梁。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>四王柴薪安放于空悬王座，鲁道斯自燃为引</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>五道冲天金焰与古老符文在大理石地面交织</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>千万代积攒的余火之力汇聚于余灰一身体内</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>仪轨圆满</span>
        <span class="footer-highlight">烈火燃透圣所</span>
      </div>
    </div>

    <div id="scene-04-card-3" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🌀</span>
            <span class="card-heading">最初火炉之门</span>
          </div>
          <span class="card-badge">时空尽头</span>
        </div>
        <div class="card-quote">“时空倾覆碎裂，通往世界一切宿命的终局。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>传火祭祀场营火爆发出穿梭时空的引力</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>余灰被传送至坍塌倾斜的“初始火炉”</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>世界的尽头，一切历史与王国在这里挤压成废墟</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>彼岸归宿</span>
        <span class="footer-highlight">叩响终局之门</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-04-1" class="caption-box" style="opacity: 0;">余灰虽被世人鄙夷为无火无光之物，却唯有他们踏上猎王之路。</div>
    <div id="c-04-2" class="caption-box" style="opacity: 0;">斩杀薪王，集齐四大柴薪，置于祭祀场的王座之上。</div>
    <div id="c-04-3" class="caption-box" style="opacity: 0;">当余火再度激荡，通往最初火炉的道路轰然开启。</div>
  </div>

  <div class="progress-track"><div id="p-04" class="progress-bar"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-04-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -20, duration: {dur}, ease: "none" }}, 0);
  
  // Headers
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-04-card-1", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-04-card-2", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.2);
  tl.fromTo("#scene-04-card-3", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.6);
  tl.to("#scene-04-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 0.8)
    .to("#scene-04-card-1", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 5.2)
    .to("#scene-04-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 5.2)
    .to("#scene-04-card-2", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 10.6)
    .to("#scene-04-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 10.6);

  // Captions
  tl.set("#c-04-1", {{ opacity: 1 }}, 0.50).set("#c-04-1", {{ opacity: 0 }}, 5.20);
  tl.set("#c-04-2", {{ opacity: 1 }}, 5.20).set("#c-04-2", {{ opacity: 0 }}, 10.60);
  tl.set("#c-04-3", {{ opacity: 1 }}, 10.60).set("#c-04-3", {{ opacity: 0 }}, 16.80);

  // Progress Bar
  tl.fromTo("#p-04", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-04"] = tl;
}}
</script>
</template>
</body>
</html>"""

def generate_scene_05(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
</style>
<div id="root" data-composition-id="scene-05" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-05-bg" class="bg-img" src="assets/images/scene05_kiln.jpg" alt="Soul of Cinder" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter">🔥 CHAPTER IV · 最初火炉</div>
    <div class="topic-tag">DARK SOULS III · 宿命的最终守门人</div>
  </div>

  <div class="title-area">
    <h1 class="main-title">终局之战 · 薪王化身</h1>
    <div class="sub-title">暗日流血的世界尽头，万千前代传火者灵魂的聚合体与悲壮对决</div>
  </div>

  <div class="cards-grid">
    <div id="scene-05-card-1" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🌑</span>
            <span class="card-heading">滴血的黑暗之环</span>
          </div>
          <span class="card-badge">灭世异象</span>
        </div>
        <div class="card-quote">“太阳化作淌血的黑洞，初火再难维系。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>天空中挂着渗出暗红淤血的黑暗之环（Darksign）</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>历代王朝建筑如同破碎的浪潮扭曲堆叠</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>这不仅是火炉，更是整部传火史的苍凉墓冢</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>世界尽头</span>
        <span class="footer-highlight">倾颓的天空</span>
      </div>
    </div>

    <div id="scene-05-card-2" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">⚔️</span>
            <span class="card-heading">薪王们的化身</span>
          </div>
          <span class="card-badge">千万灵魂</span>
        </div>
        <div class="card-quote">“它是你，是他，是一切曾为初火献身的英雄。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>初代薪王葛温与无数玩家、历代传火者的聚合体</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>手握螺旋剑，随意切换法术、奇迹、弯刀与长枪</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>它是传火意志的最后具象，守卫着残火的尊严</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>终极考验</span>
        <span class="footer-highlight">战胜过去的自己</span>
      </div>
    </div>

    <div id="scene-05-card-3" class="card-item">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🎹</span>
            <span class="card-heading">葛温的钢琴三连音</span>
          </div>
          <span class="card-badge">传世哀歌</span>
        </div>
        <div class="card-quote">“当熟悉的旋律响起，一代史诗在此落幕。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet"></span><span>进入二阶段，化身燃起金色雷电与阳光奇迹</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>背景音乐突变，一代葛温钢琴主题悠然响起</span></div>
          <div class="detail-row"><span class="detail-bullet"></span><span>那并非胜利的狂想，而是一曲跨越千年的安魂绝唱</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>落幕之音</span>
        <span class="footer-highlight">三连音的叹息</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-05-1" class="caption-box" style="opacity: 0;">在世界的尽头，天空悬挂着流淌着暗色余晖的暗黑之环。</div>
    <div id="c-05-2" class="caption-box" style="opacity: 0;">最后的守门人——薪王们的化身，是千百年来所有传火者灵魂的聚合体。</div>
    <div id="c-05-3" class="caption-box" style="opacity: 0;">当凄凉的钢琴三连音响起，无数宿命的悲壮在此刻交织碰撞。</div>
  </div>

  <div class="progress-track"><div id="p-05" class="progress-bar"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-05-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.08, y: -20, duration: {dur}, ease: "none" }}, 0);
  
  // Headers
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-05-card-1", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-05-card-2", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.2);
  tl.fromTo("#scene-05-card-3", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.6);
  tl.to("#scene-05-card-1", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 0.8)
    .to("#scene-05-card-1", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 5.5)
    .to("#scene-05-card-2", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 5.5)
    .to("#scene-05-card-2", {{ borderColor: "rgba(245, 158, 11, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.7), 0 0 25px rgba(245, 158, 11, 0.1)", duration: 0.5 }}, 11.2)
    .to("#scene-05-card-3", {{ borderColor: "rgba(245, 158, 11, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(245, 158, 11, 0.35)", duration: 0.5 }}, 11.2);

  // Captions
  tl.set("#c-05-1", {{ opacity: 1 }}, 0.50).set("#c-05-1", {{ opacity: 0 }}, 5.50);
  tl.set("#c-05-2", {{ opacity: 1 }}, 5.50).set("#c-05-2", {{ opacity: 0 }}, 11.20);
  tl.set("#c-05-3", {{ opacity: 1 }}, 11.20).set("#c-05-3", {{ opacity: 0 }}, 19.00);

  // Progress Bar
  tl.fromTo("#p-05", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-05"] = tl;
}}
</script>
</template>
</body>
</html>"""

def generate_scene_06(dur):
    return f"""<!doctype html>
<html lang="zh-CN">
<head><meta charset="UTF-8"></head>
<body>
<template>
<style>
{DS3_COMMON_CSS}
  .card-item-serene {{
    background: linear-gradient(160deg, rgba(16, 20, 30, 0.85) 0%, rgba(5, 7, 12, 0.95) 100%);
    border: 1.5px solid rgba(125, 211, 252, 0.3);
    box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 25px rgba(125, 211, 252, 0.1);
  }}
  .card-item-serene::before {{
    background: linear-gradient(90deg, transparent, #7dd3fc, transparent);
  }}
  .badge-serene {{
    background: rgba(125, 211, 252, 0.15) !important;
    border: 1px solid rgba(125, 211, 252, 0.4) !important;
    color: #7dd3fc !important;
  }}
  .quote-serene {{
    color: #bae6fd !important;
    border-left-color: #38bdf8 !important;
  }}
  .bullet-serene {{
    background: #38bdf8 !important;
    box-shadow: 0 0 8px #38bdf8 !important;
  }}
</style>
<div id="root" data-composition-id="scene-06" data-width="1920" data-height="1080">
  <div class="bg-wrap" data-layout-allow-overflow>
    <img id="scene-06-bg" class="bg-img" src="assets/images/scene06_firekeeper.jpg" alt="The End of Fire" data-layout-allow-overflow data-start="0" data-duration="{dur}">
    <div class="bg-overlay"></div>
    <div class="ember-glow"></div>
  </div>

  <div class="header">
    <div class="badge-chapter" style="background: rgba(125, 211, 252, 0.15); border-color: rgba(125, 211, 252, 0.45); color: #bae6fd;">✨ EPILOGUE · 传火终局</div>
    <div class="topic-tag">DARK SOULS III · 熄火与破晓的余愿</div>
  </div>

  <div class="title-area">
    <h1 class="main-title" style="background: linear-gradient(135deg, #ffffff 20%, #bae6fd 60%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">火的归宿 · 熄灭初火</h1>
    <div class="sub-title">当微弱的余烬在掌心熄灭，世界终归于宁静深邃的安眠与微小的未来</div>
  </div>

  <div class="cards-grid">
    <div id="scene-06-card-1" class="card-item card-item-serene">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🕯️</span>
            <span class="card-heading">初火终归熄灭</span>
          </div>
          <span class="card-badge badge-serene">打破轮回</span>
        </div>
        <div class="card-quote quote-serene">“传火不是永恒的救赎，而是一场逆天命的延期。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>四代结局中最为诗意深邃的抉择：灭火（End of Fire）</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>盲眼防火女双手承接初火，任由火光渐次黯淡</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>强行延续千百年的传火诅咒，在此刻终于宣告结束</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>宿命解脱</span>
        <span class="footer-highlight" style="color: #38bdf8;">火之时代的终焉</span>
      </div>
    </div>

    <div id="scene-06-card-2" class="card-item card-item-serene">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">🌌</span>
            <span class="card-heading">宁谧深邃的黑暗</span>
          </div>
          <span class="card-badge badge-serene">世界本真</span>
        </div>
        <div class="card-quote quote-serene">“黑暗并非灾难，而是世界应有的安歇。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>天地陷于纯净的静默，游魂与人类归于平静</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>褪去狂热的薪柴献祭，大地得以修养生息</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>黑暗中的低语：“灰烬大人，您还听得到我的声音吗？”</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>静默守护</span>
        <span class="footer-highlight" style="color: #38bdf8;">听觉的相伴</span>
      </div>
    </div>

    <div id="scene-06-card-3" class="card-item card-item-serene">
      <div>
        <div class="card-top">
          <div class="card-icon-title">
            <span class="card-icon">✨</span>
            <span class="card-heading">微火终将新生</span>
          </div>
          <span class="card-badge badge-serene">未来的希望</span>
        </div>
        <div class="card-quote quote-serene">“在很久以后的黑暗尽头，定会有微小的火苗重新诞生。”</div>
        <div class="card-details">
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>毁灭不是终点，而是孕育新纪元的必经之路</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>自然律动不可阻挡，火与暗终有下一次潮起潮落</span></div>
          <div class="detail-row"><span class="detail-bullet bullet-serene"></span><span>黑魂三部曲在此画上唯美、深邃且充满余韵的句点</span></div>
        </div>
      </div>
      <div class="card-footer">
        <span>微弱微光</span>
        <span class="footer-highlight" style="color: #38bdf8;">破晓的预兆</span>
      </div>
    </div>
  </div>

  <div class="caption-container">
    <div id="c-06-1" class="caption-box" style="opacity: 0;">初火终有熄灭的一天。</div>
    <div id="c-06-2" class="caption-box" style="opacity: 0;">当防火女轻轻捧起那微弱如萤火的余烬，世界终于迎来了静谧的黑暗。</div>
    <div id="c-06-3" class="caption-box" style="opacity: 0;">但正如她所言：在极其漫长的黑暗尽头，终会有一日，微小的火苗会再度诞生。</div>
  </div>

  <div class="progress-track"><div id="p-06" class="progress-bar" style="background: linear-gradient(90deg, #0284c7, #38bdf8, #bae6fd); box-shadow: 0 0 10px #38bdf8;"></div></div>
</div>
<script>
{{
  const tl = gsap.timeline({{ paused: true }});
  
  // Background Ken Burns
  tl.fromTo("#scene-06-bg", {{ scale: 1.0, y: 0 }}, {{ scale: 1.07, y: -15, duration: {dur}, ease: "none" }}, 0);
  
  // Headers
  tl.fromTo(".header", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.8, ease: "power2.out" }}, 0.2);
  tl.fromTo(".title-area", {{ opacity: 0, y: -25 }}, {{ opacity: 1, y: 0, duration: 1.0, ease: "power2.out" }}, 0.4);
  
  // Cards Stagger In
  tl.fromTo("#scene-06-card-1", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 0.8);
  tl.fromTo("#scene-06-card-2", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.2);
  tl.fromTo("#scene-06-card-3", {{ opacity: 0, y: 40, scale: 0.96 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "back.out(1.2)" }}, 1.6);
  tl.to("#scene-06-card-1", {{ borderColor: "rgba(125, 211, 252, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(125, 211, 252, 0.4)", duration: 0.5 }}, 0.8)
    .to("#scene-06-card-1", {{ borderColor: "rgba(125, 211, 252, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 25px rgba(125, 211, 252, 0.1)", duration: 0.5 }}, 3.8)
    .to("#scene-06-card-2", {{ borderColor: "rgba(125, 211, 252, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(125, 211, 252, 0.4)", duration: 0.5 }}, 3.8)
    .to("#scene-06-card-2", {{ borderColor: "rgba(125, 211, 252, 0.3)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 25px rgba(125, 211, 252, 0.1)", duration: 0.5 }}, 9.8)
    .to("#scene-06-card-3", {{ borderColor: "rgba(125, 211, 252, 0.9)", boxShadow: "0 15px 40px rgba(0,0,0,0.8), 0 0 35px rgba(125, 211, 252, 0.4)", duration: 0.5 }}, 9.8);

  // Captions
  tl.set("#c-06-1", {{ opacity: 1 }}, 0.50).set("#c-06-1", {{ opacity: 0 }}, 3.80);
  tl.set("#c-06-2", {{ opacity: 1 }}, 3.80).set("#c-06-2", {{ opacity: 0 }}, 9.80);
  tl.set("#c-06-3", {{ opacity: 1 }}, 9.80).set("#c-06-3", {{ opacity: 0 }}, 17.70);

  // Progress Bar
  tl.fromTo("#p-06", {{ scaleX: 0 }}, {{ scaleX: 1, duration: {dur}, ease: "none" }}, 0);

  window.__timelines["scene-06"] = tl;
}}
</script>
</template>
</body>
</html>"""

def build_all():
    compositions_dir = ROOT / 'compositions'
    compositions_dir.mkdir(parents=True, exist_ok=True)
    
    scene_durations = [18.5, 18.0, 22.0, 18.0, 20.5, 21.0]
    
    generators = [
        generate_scene_01,
        generate_scene_02,
        generate_scene_03,
        generate_scene_04,
        generate_scene_05,
        generate_scene_06
    ]
    
    for idx, (gen, dur) in enumerate(zip(generators, scene_durations), 1):
        target = compositions_dir / f"scene-0{idx}.html"
        content = gen(dur)
        target.write_text(content, encoding='utf-8')
        print(f"Generated {target.name} (duration: {dur}s)")

if __name__ == '__main__':
    build_all()
