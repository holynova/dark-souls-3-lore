# 《黑暗之魂3：火的熄灭与宿命轮回》视频工程

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Online-orange)](https://holynova.github.io/dark-souls-3-lore/)
[![Resolution](https://img.shields.io/badge/Resolution-1080P%20Full%20HD-blue)](https://holynova.github.io/dark-souls-3-lore/)
[![Engine](https://img.shields.io/badge/Engine-Hyperframe%20%2B%20GSAP-red)](https://github.com/heygen-com/hyperframes)

使用 **Hyperframe** 视听动效引擎与 AI 概念美术创作的《黑暗之魂3》剧情解析视频。全景还原初火衰微、薪王悲歌、化身绝唱与熄火抉择。

- **在线网页播放**：[https://holynova.github.io/dark-souls-3-lore/](https://holynova.github.io/dark-souls-3-lore/)
- **本地渲染成品**：[`dark_souls_3_lore.mp4`](dark_souls_3_lore.mp4) (1080P 30FPS · 31.5MB)

---

## 📽️ 分幕章节

| 章节 | 时间轴 | 主题 | 核心内容 |
| :--- | :--- | :--- | :--- |
| **01 · 序章** | 00:00 – 00:18 | 火渐熄 · 王不见王 | 初火衰微，时空错位，钟声唤醒沉睡千年的无火余灰 |
| **02 · 第一章** | 00:18 – 00:36 | 王座空悬 · 诸王背誓 | 传火祭祀场五王座空悬，仅有放逐者鲁道斯与盲眼防火女 |
| **03 · 第二章** | 00:36 – 00:58 | 诸王悲歌 · 逃离宿命 | 法兰不死队、巨人尤姆、噬神者埃尔德里奇与双王子的绝望 |
| **04 · 第三章** | 00:58 – 01:16 | 猎王之誓 · 柴薪共鸣 | 灰烬斩灭诸王，四大柴薪归位，金色烈焰叩响初始火炉之门 |
| **05 · 第四章** | 01:16 – 01:37 | 终局之战 · 薪王化身 | 流血暗日（Dark Sign），万千传火者灵魂聚合体与葛温钢琴三连音 |
| **06 · 终章** | 01:37 – 01:58 | 火的归宿 · 熄灭初火 | 防火女轻捧微火，世界归于静谧黑暗，静候未来微光重燃 |

---

## 🛠️ 技术实现

1. **Hyperframe 渲染与动效**：基于 HTML5/CSS3 与 GSAP 3 时间线，实现亚秒级帧确定性与可寻道渲染；
2. **多轨声音设计**：
   - Track 0：视觉子合成图层（6 大独立 Composition）
   - Track 1：标准影视级纪录片解说旁白
   - Track 2：D 小调专属氛围底噪、远方钟鸣与葛温钢琴音
   - Track 3：电影级低音冲击（Impact Bass）与转场呼啸（Whoosh）
3. **WCAG AA 视觉验证**：全篇 124 处文本元素全部通过无障碍对比度合规测试。

---

## 🚀 本地开发与二次渲染

```bash
# 安装依赖
npm install

# 启动本地实时预览 Studio
npm run preview

# 检查合成契约与无障碍对比度
npm run check

# 本地渲染生成 MP4 视频
npm run render
```
