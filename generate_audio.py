import json
import os
from pathlib import Path
import subprocess

ROOT = Path('/Users/sym/Code/dark-souls-3-lore')

SCENES = [
    {
        "id": "scene-01",
        "title": "起源与前因 · 葛温的万年诅咒",
        "eyebrow": "TIMELINE 01 / ORIGIN OF THE CURSE",
        "image": "assets/images/nano_gwyn.jpg",
        "narration": "很多朋友看黑魂总觉得神神叨叨看不懂，其实黑魂三的底层逻辑极其硬核！一切前因都要回到最初：神王葛温为了维系神权统治，强行把自己当柴烧、开启了传火诅咒！从此天地定下规矩：初火每隔千年就会熄灭，必须找强大的王者献祭自身去给世界续命！"
    },
    {
        "id": "scene-02",
        "title": "黑魂3危机 · 薪王集体罢工跑路",
        "eyebrow": "TIMELINE 02 / THE CRISIS & DESERTION",
        "image": "assets/images/scene02_firelink.jpg",
        "narration": "到了黑魂三的时代，初火已经被榨得连渣都不剩了！现任王室双王子直接摆烂拒绝传火。祭祀场急得拉响最高警报，敲响古钟，把以前烧过一次的四个老薪王从坟墓里强行叫醒返工！结果这帮大佬一看：又想烧我？老子早就不干了！全体罢工，各自跑回老家！"
    },
    {
        "id": "scene-03",
        "title": "四大薪王档案 · 为何宁死不回王座",
        "eyebrow": "TIMELINE 03 / THE 4 LORDS DOSSIER",
        "image": "assets/images/scene03_lords.jpg",
        "narration": "为什么他们宁可去死也不回王座？因为全是血泪教训！法兰不死队为了斩深渊喝下狼血，结果自己被深渊污染，天天在老巢互砍；巨人尤姆为了保全臣民去传火，回来却发现满城百姓被烧成黑炭，心死如灰；埃尔德里奇预见火灭后是深海时代，直接叛变吞噬神明；而双王子更是看透了神权谎言，誓死不当耗材！"
    },
    {
        "id": "scene-04",
        "title": "保底机制 · 叫醒灰烬强制催债",
        "eyebrow": "TIMELINE 04 / ASHEN ONE AWAKENS",
        "image": "assets/images/scene04_ritual.jpg",
        "narration": "薪王全跑了怎么办？体制只能启动终极应急预案：唤醒无火余灰！余灰是什么？就是当年连当柴资格都没有、直接烧成飞灰的淘汰者！但余灰目标极其纯粹：既然薪王不肯自己走回王座，那就踏遍世界把他们全砍了，把柴薪强行按在王座上！当四大柴薪共鸣，通往最初火炉的道路轰然打开！"
    },
    {
        "id": "scene-05",
        "title": "终极决战 · 薪王化身与流血暗日",
        "eyebrow": "TIMELINE 05 / KILN & SOUL OF CINDER",
        "image": "assets/images/scene05_kiln.jpg",
        "narration": "来到世界尽头的初始火炉，天上挂着流血的黑暗之环日蚀，整部传火史的苍凉在此凝固！最后的守门人薪王们的化身，是初代葛温与千万代传火英雄执念的集合体！击败他，就是战胜过去千万年传火的执念！当二阶段哀伤的钢琴三连音响起，无数宿命的悲壮在此刻彻底引爆！"
    },
    {
        "id": "scene-06",
        "title": "终局抉择 · 熄灭初火与破晓新生",
        "eyebrow": "TIMELINE 06 / THE END OF FIRE",
        "image": "assets/images/scene06_firekeeper.jpg",
        "narration": "击败化身后，世界的命运交到你手中！继续传火？初火早已油尽灯枯，坐上去只能冒几点可怜的火星，毫无意义！真正的解脱是把初火交给防火女：让这烧了几万年的病态诅咒彻底熄灭！世界迎来宁静的黑夜，正如防火女所言：在漫长的黑暗尽头，终会有一日，微小的火苗会再度诞生！"
    }
]

def main():
    out_dir = ROOT / 'assets/audio'
    out_dir.mkdir(parents=True, exist_ok=True)
    
    durations = {}
    total_duration = 0.0
    # Impassioned, energetic, booming delivery
    voice = "zh-CN-YunjianNeural"

    for idx, scene in enumerate(SCENES, 1):
        filename_mp3 = out_dir / f"scene-0{idx}.mp3"
        filename_wav = out_dir / f"scene-0{idx}.wav"
        print(f"Generating audio for Scene {idx}: {scene['title']}...")
        
        cmd = [
            "edge-tts",
            "--voice", voice,
            "--rate=+2%",
            "--pitch=+0Hz",
            "--text", scene['narration'],
            "--write-media", str(filename_mp3)
        ]
        subprocess.run(cmd, check=True)
        
        subprocess.run([
            "ffmpeg", "-y", "-i", str(filename_mp3),
            "-ar", "44100", "-ac", "2", str(filename_wav)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        dur = float(subprocess.check_output([
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', str(filename_wav)
        ]).strip())
        
        durations[f"scene-0{idx}"] = round(dur, 2)
        total_duration += dur
        print(f"Scene {idx} completed: {dur:.2f}s")
        
        if filename_mp3.exists():
            filename_mp3.unlink()

    print(f"\nAll scenes generated! Total narration length: {total_duration:.2f}s")
    
    meta_path = ROOT / 'scenes_meta.json'
    meta_path.write_text(json.dumps({
        "scenes": SCENES,
        "durations": durations,
        "total_duration": round(total_duration, 2)
    }, indent=2, ensure_ascii=False))
    print(f"Metadata saved to {meta_path}")

if __name__ == '__main__':
    main()
