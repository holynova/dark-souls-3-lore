# 《黑暗之魂3：万年传火因果与终局破晓》视频工程

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Online-orange)](https://holynova.github.io/dark-souls-3-lore/)
[![Resolution](https://img.shields.io/badge/Resolution-1080P%20Full%20HD-blue)](https://holynova.github.io/dark-souls-3-lore/)
[![Duration](https://img.shields.io/badge/Duration-2m%2051s%20(5145%20Frames)-green)](https://holynova.github.io/dark-souls-3-lore/)
[![Engine](https://img.shields.io/badge/Engine-Hyperframe%20%2B%20GSAP-red)](https://github.com/heygen-com/hyperframes)

使用 **Hyperframe** 视听动效引擎与 Nano 级 AI 概念美术深度打造的《黑暗之魂3》底层剧情逻辑解析视频。

彻底抛弃故弄玄虚的黑话，采用通俗直接的硬核语言与因果时间线，慷慨激昂地解析万年传火骗局的前因后果：从神王葛温的私欲投火，到黑魂3初火枯竭、薪王集体罢工跑路，再到体制叫醒淘汰者无火余灰物理催债，直至世界尽头决战化身与熄灭初火迎来真正新生。

- **在线网页播放**：[https://holynova.github.io/dark-souls-3-lore/](https://holynova.github.io/dark-souls-3-lore/)
- **本地渲染成品**：[`dark_souls_3_lore.mp4`](dark_souls_3_lore.mp4) (1080P 30FPS · 2分51秒 · 76.6MB)

---

## 📽️ 因果时间线分幕章节

| 章节 | 时间轴 | 主题 | 核心因果逻辑 | Nano 概念原画 |
| :--- | :--- | :--- | :--- | :--- |
| **01 · 起源前因** | 00:00 – 00:25 | 葛温投火 · 宇宙级诅咒诞生 | **【因】** 为维系神权统治，神王以身投火建立千年献祭铁律，给全人类套上不死人诅咒 | `nano_gwyn.jpg` |
| **02 · 体系暴雷** | 00:25 – 00:52 | 初火油尽 · 薪王集体撂挑子 | **【转】** 初火枯竭，双王子摆烂拒传！祭祀场敲钟掘墓，昔日老薪王全体罢工逃回老家 | `nano_twin_princes.jpg` |
| **03 · 诸王档案** | 00:52 – 01:23 | 四大薪王 · 宁死不当耗材 | **【析】** 不死队同门自残、尤姆臣民全灭、埃尔德里奇深海食神、双王子誓死拒当柴 | `nano_abyss_watchers.jpg`<br>`nano_yhorm.jpg`<br>`nano_aldrich.jpg` |
| **04 · 终极保底** | 01:23 – 01:53 | 无火余灰 · 叫醒淘汰者物理催债 | **【机】** 启动终极应急预案唤醒未成灰残渣，踏遍天下将逃跑薪王全部斩首按回王座 | `scene04_ritual.jpg` |
| **05 · 宿命决战** | 01:53 – 02:21 | 初始火炉 · 薪王化身与流血暗日 | **【决】** 流血暗日坍缩世界，战胜历代千万英雄执念集合体，钢琴三连音斩断万年原罪 | `scene05_kiln.jpg` |
| **06 · 终局破晓** | 02:21 – 02:51 | 灭火归真 · 斩断诅咒静待破晓 | **【果】** 拒绝残火苟延，托付初火给防火女彻底熄火，深邃长夜尽头静待清澈新生火苗 | `scene06_firekeeper.jpg` |

---

## 🎨 视听设计与工程亮点

1. **零进度条沉浸设计**：彻底移除画面底部的进度条干扰，保证画面如电影级纪录片般干净纯粹；
2. **极简逻辑排版**：杜绝大段长篇文字堆砌，采用大号醒目标题、因果方块（`【起因】`、`【转折】`、`【后果】`）与高密度要点 Bullets；
3. **Nano 概念原画精制**：为太阳王葛温、洛斯里克双王子、法兰不死队、巨人尤姆、噬神者埃尔德里奇生成专属 4K 构图插画；
4. **慷慨激昂云健配音**：采用高亢、宏大、充满激情的音色与快节奏叙事，彻底说人话；
5. **暗黑管弦与钢琴混音**：大提琴低沉低鸣、青铜古钟远鸣与二阶段葛温钢琴三连音（Plin Plin Plon）四轨混音；
6. **响应式 GitHub Pages 影院**：支持毫秒级时间跳转、双语/旁白字幕实时高亮跟读、剧情逻辑拓扑图谱及原画灯箱。

---

## 🚀 本地开发与二次渲染

```bash
# 生成语音与时间戳元数据
python3 generate_audio.py

# 生成背景音乐与音效
python3 generate_bgm.py

# 构建分幕 HTML 模板
python3 build_scenes.py

# 本地渲染生成完整 MP4 视频
npx hyperframes render -o dark_souls_3_lore.mp4 --workers 1
```
