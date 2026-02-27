import json
import datetime
import random

def generate_matches():
    """生成今日比赛数据（示例版，后续可替换为真实抓取）"""
    today = datetime.date.today()
    time_slots = ['19:35', '20:30', '22:00', '23:00', '01:00', '03:00']
    
    templates = [
        {"league": "英超", "home": "阿森纳", "away": "切尔西"},
        {"league": "英超", "home": "利物浦", "away": "曼联"},
        {"league": "西甲", "home": "皇马", "away": "巴萨"},
        {"league": "意甲", "home": "国米", "away": "米兰"},
        {"league": "德甲", "home": "拜仁", "away": "多特"},
        {"league": "中超", "home": "海港", "away": "泰山"}
    ]
    
    matches = []
    for i, t in enumerate(random.sample(templates, min(4, len(templates)))):
        matches.append({
            "id": int(datetime.datetime.now().timestamp()) + i,
            "league": t["league"],
            "home": t["home"],
            "away": t["away"],
            "time": f"{today} {time_slots[i]}",
            "homeRank": random.randint(1, 10),
            "awayRank": random.randint(8, 20),
            "homeForm": random.randint(8, 15),
            "awayForm": random.randint(4, 12),
            "homeGoals": random.randint(8, 15),
            "homeConceded": random.randint(3, 8),
            "awayGoals": random.randint(5, 12),
            "awayConceded": random.randint(6, 12),
            "status": "pending"
        })
    
    with open('matches.json', 'w', encoding='utf-8') as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(matches)} matches")

if __name__ == "__main__":
    generate_matches()
