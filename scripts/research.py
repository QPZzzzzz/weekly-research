#!/usr/bin/env python3
"""
Weekly Research Pipeline
- Phase 1: Tavily 搜索 → DeepSeek 结构化分析 → JSON
- Phase 2: JSON → DeepSeek 报告生成 → Markdown + Memory
"""

import os, sys, json, glob, requests
from datetime import datetime

# Config from env
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
DEEPSEEK_API_KEY = os.environ["DEEPSEEK_API_KEY"]
RAW_DIR = os.environ.get("RAW_DIR", "raw_sources")
MEMORY_DIR = os.environ.get("MEMORY_DIR", "memory")
REPORT_DIR = os.environ.get("REPORT_DIR", "reports")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

DATE = datetime.now().strftime("%Y-%m-%d")


def deepseek(system: str, user: str) -> str:
    resp = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.3,
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def tavily_search(query: str, max_results: int = 8) -> list:
    resp = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "include_answer": False,
            "max_results": max_results,
        },
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("results", [])


def read_memory(label: str) -> str:
    path = f"{MEMORY_DIR}/{label}.md"
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""


def write_memory(label: str, content: str):
    path = f"{MEMORY_DIR}/{label}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {label} - Research Memory\n\n")
        f.write(f"最后更新: {DATE}\n\n")
        f.write(content)


def find_prev_raw(label: str, exclude: str = "") -> dict | None:
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    for f in files:
        if label in f and f != exclude:
            with open(f, encoding="utf-8") as pf:
                return json.load(pf)
    return None


# ── Phase 1 ────────────────────────────────────────────────

def phase1(topic: str, label: str):
    print(f"[Phase 1] {topic}")

    memory = read_memory(label)
    results = tavily_search(topic)

    if not results:
        print("  ⚠️ 无搜索结果，使用空数据")
        results = []

    context = json.dumps(
        [
            {"title": r["title"], "url": r["url"], "content": r.get("content", "")[:500]}
            for r in results
        ],
        ensure_ascii=False,
    )

    raw_json_str = deepseek(
        "你是一个产业信息分析师。只输出 JSON，不要 markdown 代码块，不要额外说明。",
        f"""分析以下搜索结果，提取结构化信息。

话题：{topic}

历史记忆（已知道的信息，避免重复）：
{memory}

搜索结果：
{context}

输出 JSON 格式（严格）：
{{
  "topic": "{topic}",
  "date": "{DATE}",
  "sources": [
    {{"title": "文章标题", "url": "链接", "platform": "来源平台", "summary": "一句话摘要", "relevance": "high/medium/low", "tags": ["标签"]}}
  ],
  "signals": [
    {{"signal": "值得关注的信号", "direction": "up/down/new/stable", "evidence": "支撑依据"}}
  ]
}}""",
    )

    # 清理可能的 markdown 标记
    raw_json_str = raw_json_str.strip()
    if raw_json_str.startswith("```"):
        raw_json_str = "\n".join(raw_json_str.split("\n")[1:-1])

    raw = json.loads(raw_json_str)

    filepath = f"{RAW_DIR}/{DATE}-{label}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 已保存: {filepath}")


# ── Phase 2 ────────────────────────────────────────────────

def phase2(label: str):
    print(f"[Phase 2] {label}")

    # 找最新的 raw JSON
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    target = next((f for f in files if label in f), None)
    if not target:
        print(f"  ⚠️ 找不到 {label} 的原始数据")
        return

    with open(target, encoding="utf-8") as f:
        raw_data = json.load(f)

    topic = raw_data.get("topic", label)
    memory = read_memory(label)
    prev_data = find_prev_raw(label, exclude=target)

    sources = json.dumps(raw_data.get("sources", []), ensure_ascii=False, indent=2)
    signals = json.dumps(raw_data.get("signals", []), ensure_ascii=False, indent=2)
    prev_sources = json.dumps(prev_data.get("sources", []) if prev_data else [], ensure_ascii=False, indent=2)

    # 生成报告
    report = deepseek(
        "你是一个产业调研报告撰写师。用中文和 Markdown 格式输出。",
        f"""基于以下原始数据撰写调研报告。

话题：{topic}

本周数据：
{sources}

本周信号：
{signals}

上周数据（用于趋势对比，空的表示首次）：
{prev_sources}

历史记忆（已跟踪的长期趋势）：
{memory}

报告结构如下，使用 ## 和 ### 标题层级：

### 本周核心发现
每条：**发现** + 依据

### 各平台摘要
按来源分类

### 趋势变化分析
- 新出现的主题 vs 已消退的主题
- 热度上升/下降的趋势
- 值得关注的早期信号

### 数据来源
链接列表""",
    )

    # 保存报告
    report_file = f"{REPORT_DIR}/{DATE}-{label}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(f"**调研日期：** {DATE}\n\n")
        f.write(report)
    print(f"  ✅ 报告已生成: {report_file}")

    # 更新 memory
    memory_content = deepseek(
        "你是一个信息提取器。输出简洁的 Markdown 格式。",
        f"""从以下报告和原始数据中提取关键记忆点：
- 涉及的公司/产品/项目名称
- 趋势信号（方向 + 描述）
- 值得长期跟踪的话题

报告：
{report}

原始信号：
{signals}""",
    )
    write_memory(label, memory_content)
    print(f"  ✅ Memory 已更新")


# ── Entry ──────────────────────────────────────────────────

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""

    if mode == "phase1":
        phase1(os.environ["TOPIC"], os.environ["LABEL"])
    elif mode == "phase2":
        label = sys.argv[2] if len(sys.argv) > 2 else ""
        if label:
            phase2(label)
        else:
            # 为所有 label 执行 phase2
            for f in sorted(glob.glob(f"{RAW_DIR}/*.json")):
                name = os.path.basename(f).replace(".json", "")
                parts = name.split("-", 1)
                if len(parts) > 1:
                    phase2(parts[1])
    else:
        print("Usage: python research.py phase1|phase2 [label]")
        sys.exit(1)
