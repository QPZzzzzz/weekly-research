#!/usr/bin/env python3
"""
Incredibuild 行业调研流水线
- Phase 1: 多轮搜索（中英文多平台覆盖）→ DeepSeek 结构化分析 → JSON
- Phase 2: JSON → DeepSeek 报告生成 → Markdown + Memory
"""

import os, sys, json, glob, requests
from datetime import datetime

# Config from env
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY", "")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
RAW_DIR = os.environ.get("RAW_DIR", "raw_sources")
MEMORY_DIR = os.environ.get("MEMORY_DIR", "memory")
REPORT_DIR = os.environ.get("REPORT_DIR", "reports")

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

DATE = datetime.now().strftime("%Y-%m-%d")

# 多维度搜索查询（覆盖中英文 + 不同平台视角）
SEARCH_QUERIES = [
    # 中文
    "Incredibuild 分布式编译 2025 2026",
    "Incredibuild 编译加速 C++ 游戏开发",
    "分布式编译 工具 对比 distcc nocc fastbuild 2025",
    "C++ 编译加速 行业方案 Incredibuild",
    # 英文
    "Incredibuild distributed compilation 2025 2026 news",
    "C++ build acceleration tools comparison Incredibuild alternatives",
    "distributed compilation game development UE Unity 2025 2026",
    "build cache optimization CI pipeline acceleration 2025",
    # 竞品
    "Nocc FASTBuild EngFlow Incredibuild comparison 2025",
    "mold linker sccache ccache distributed build C++ 2025",
]


def deepseek(system: str, user: str) -> str:
    """调用 DeepSeek API"""
    if not DEEPSEEK_API_KEY:
        print("  ❌ DEEPSEEK_API_KEY 未设置")
        sys.exit(1)
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


def tavily_search(query: str, max_results: int = 6) -> list:
    """调用 Tavily 搜索"""
    if not TAVILY_API_KEY:
        print("  ❌ TAVILY_API_KEY 未设置")
        sys.exit(1)
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


def read_memory() -> str:
    """读取历史趋势记忆"""
    path = f"{MEMORY_DIR}/incredibuild.md"
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""


def write_memory(content: str):
    """更新趋势记忆"""
    path = f"{MEMORY_DIR}/incredibuild.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Incredibuild - Research Memory\n\n")
        f.write(f"最后更新: {DATE}\n\n")
        f.write(content)


def find_prev_raw() -> dict | None:
    """查找上一次的原始数据"""
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    for f in files:
        if "incredibuild" in f:
            with open(f, encoding="utf-8") as pf:
                return json.load(pf)
    return None


# ── Phase 1 ────────────────────────────────────────────────

def phase1():
    print(f"[Phase 1] 多轮搜索开始 — {DATE}")
    memory = read_memory()
    all_results = []
    seen_urls = set()

    for query in SEARCH_QUERIES:
        print(f"  🔍 搜索: {query}")
        try:
            results = tavily_search(query)
            for r in results:
                if r.get("url") and r["url"] not in seen_urls:
                    seen_urls.add(r["url"])
                    all_results.append(r)
            print(f"     → 新增 {len(results)} 条，累计 {len(all_results)} 条")
        except Exception as e:
            print(f"     ⚠️ 搜索失败: {e}")

    print(f"  共采集 {len(all_results)} 条独立结果")

    if not all_results:
        print("  ⚠️ 无搜索结果，使用空数据占位")
        all_results = [{"title": "无结果", "url": "", "content": "", "score": 0}]

    context = json.dumps(
        [
            {
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "content": r.get("content", "")[:500],
            }
            for r in all_results
        ],
        ensure_ascii=False,
    )

    # DeepSeek 结构化分析
    raw_json_str = deepseek(
        "你是一个产业信息分析师。只输出 JSON，不要 markdown 代码块，不要额外说明。",
        f"""
分析以下关于 Incredibuild 行业的所有搜索结果，提取结构化信息。

历史记忆（已知道的信息，避免重复）：
{memory}

搜索结果：
{context}

输出 JSON 格式（严格）：
{{
  "topic": "Incredibuild 行业调研",
  "date": "{DATE}",
  "total_sources": {len(all_results)},
  "sources": [
    {{"title": "标题", "url": "链接", "platform": "来源平台", "summary": "一句话摘要", "relevance": "high/medium/low", "tags": ["标签"]}}
  ],
  "signals": [
    {{"signal": "值得关注的信号", "direction": "up/down/new/stable", "evidence": "支撑依据", "category": "产品/竞品/行业/技术"}}
  ],
  "trends": [
    {{"trend": "趋势描述", "evidence": "证据", "momentum": "rising/stable/declining"}}
  ],
  "companies_mentioned": ["公司名"],
  "hot_topics": ["热点话题"]
}}""",
    )

    raw_json_str = raw_json_str.strip()
    if raw_json_str.startswith("```"):
        raw_json_str = "\n".join(raw_json_str.split("\n")[1:-1])

    raw = json.loads(raw_json_str)

    filepath = f"{RAW_DIR}/{DATE}-incredibuild.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 原始数据已保存: {filepath}")


# ── Phase 2 ────────────────────────────────────────────────

def phase2():
    print(f"[Phase 2] 生成报告 — {DATE}")

    # 找最新的 JSON
    files = sorted(glob.glob(f"{RAW_DIR}/incredibuild*.json"), reverse=True)
    if not files:
        print("  ⚠️ 找不到原始数据")
        return

    with open(files[0], encoding="utf-8") as f:
        raw_data = json.load(f)

    memory = read_memory()
    prev_data = find_prev_raw() if len(files) > 1 else None

    sources = json.dumps(raw_data.get("sources", []), ensure_ascii=False, indent=2)
    signals = json.dumps(raw_data.get("signals", []), ensure_ascii=False, indent=2)
    trends = json.dumps(raw_data.get("trends", []), ensure_ascii=False, indent=2)
    companies = json.dumps(raw_data.get("companies_mentioned", []), ensure_ascii=False)
    hot_topics = json.dumps(raw_data.get("hot_topics", []), ensure_ascii=False)

    prev_sources = json.dumps(prev_data.get("sources", []) if prev_data else [], ensure_ascii=False, indent=2)
    prev_signals = json.dumps(prev_data.get("signals", []) if prev_data else [], ensure_ascii=False, indent=2)
    prev_trends = json.dumps(prev_data.get("trends", []) if prev_data else [], ensure_ascii=False, indent=2)

    report = deepseek(
        "你是一个产业调研报告撰写师。用中文撰写，使用 Markdown 格式。",
        f"""
基于以下原始数据，撰写一份全面的 Incredibuild 行业调研报告。

## 本期数据
来源数: {raw_data.get('total_sources', 0)}
涉及公司: {companies}
热点话题: {hot_topics}

来源详情:
{sources}

信号:
{signals}

趋势:
{trends}

## 上期数据（用于对比）
来源:
{prev_sources}

信号:
{prev_signals}

趋势:
{prev_trends}

## 历史记忆
{memory}

## 报告结构

### 本期核心发现
每条：**发现** + 来源依据

### 多维搜索摘要（覆盖 Google / 知乎 / Twitter / 技术社区 / 百度等）
- 按来源/语言分类列出关键信息

### 趋势变化分析（对比上期）
- 新出现的信号 vs 已消退的信号
- 热度变化方向
- 值得关注的早期信号

### 竞品与行业格局
- 新产品/项目动态
- 竞品对比变化

### 数据来源
所有参考链接列表""",
    )

    # 写入报告（文件名: YYYY-MM-DD-incredibuild-行业报告.md）
    report_file = f"{REPORT_DIR}/{DATE}-incredibuild-行业报告.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# Incredibuild 行业调研报告\n\n")
        f.write(f"**调研日期：** {DATE}\n")
        f.write(f"**搜索覆盖：** Google · 百度 · 知乎 · Twitter · 小红书 · 技术社区\n")
        f.write(f"**来源数：** {raw_data.get('total_sources', 0)}\n\n")
        f.write("---\n\n")
        f.write(report)
    print(f"  ✅ 报告已生成: {report_file}")

    # 更新 memory
    memory_content = deepseek(
        "你是一个信息提取器。输出简洁 Markdown。",
        f"""从以下报告和信号中提取关键记忆点，供下次调研参考：
- 涉及的公司/产品/项目
- 重要趋势信号
- 值得长期跟踪的话题
- 竞品动态

报告：
{report}

原始信号：
{signals}""",
    )
    write_memory(memory_content)
    print(f"  ✅ Memory 已更新")


# ── Entry ──────────────────────────────────────────────────

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "phase1":
        phase1()
    elif mode == "phase2":
        phase2()
    else:
        print("Usage: python research.py phase1|phase2")
        sys.exit(1)
