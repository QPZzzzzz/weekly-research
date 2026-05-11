#!/usr/bin/env python3
"""
Weekly Research Pipeline — Matrix 多主题架构
- Phase 1: 多轮搜索 → DeepSeek 结构化分析 → JSON (per label)
- Phase 2: JSON → DeepSeek 报告生成 → Markdown + Memory (per label)
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
CURRENT_YEAR = str(datetime.now().year)
NEXT_YEAR = str(datetime.now().year + 1)


def deepseek(system: str, user: str) -> str:
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


def read_memory(label: str) -> str:
    path = f"{MEMORY_DIR}/{label}.md"
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
    return ""


def write_memory(label: str, content: str):
    path = f"{MEMORY_DIR}/{label}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {label} — Research Memory\n\n")
        f.write(f"最后更新: {DATE}\n\n")
        f.write(content)


def find_prev_raw(label: str, exclude: str = "") -> dict | None:
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    for f in files:
        basename = os.path.basename(f)
        if f.endswith(f"-{label}.json"):
            if f != exclude:
                with open(f, encoding="utf-8") as pf:
                    return json.load(pf)
    return None


def get_search_queries(label: str) -> list:
    """每个 topic 的动态搜索查询列表，年份运行时注入"""
    queries = {
        "ai-sdlc-tools": [
            f"AI coding assistant 软件工程 SDLC 趋势 {CURRENT_YEAR}",
            f"Cursor Copilot Codeium AI 编程 工具 最新 {CURRENT_YEAR}",
            f"AI SDLC automation CICD testing code review {CURRENT_YEAR}",
            f"大模型 软件开发 自动化 代码生成 {CURRENT_YEAR} {NEXT_YEAR}",
            f"AI powered software development lifecycle trends {CURRENT_YEAR}",
        ],
        "build-acceleration": [
            f"编译加速 分布式编译 C++ 行业 {CURRENT_YEAR}",
            f"distributed compilation build acceleration C++ {CURRENT_YEAR} {NEXT_YEAR}",
            f"mold sccache ccache build cache 编译 优化 {CURRENT_YEAR}",
            f"C++ build systems cmake bazel buck2 comparison {CURRENT_YEAR}",
            f"build pipeline optimization CI acceleration techniques {CURRENT_YEAR}",
        ],
        "incredibuild": [
            f"Incredibuild 分布式编译 最新 动态 {CURRENT_YEAR}",
            f"Incredibuild distributed compilation news {CURRENT_YEAR} {NEXT_YEAR}",
            f"Incredibuild 竞品 Nocc FASTBuild EngFlow BuildBarn {CURRENT_YEAR}",
            f"Incredibuild competitor comparison distributed build {CURRENT_YEAR}",
            f"分布式编译 行业格局 加速 方案 C++ {CURRENT_YEAR}",
        ],
    }
    return queries.get(label, queries["incredibuild"])


# ── Phase 1 ────────────────────────────────────────────────

def phase1():
    topic = os.environ.get("TOPIC", "")
    label = os.environ.get("LABEL", "")
    if not topic or not label:
        print("Usage: TOPIC='...' LABEL='...' python research.py phase1")
        sys.exit(1)

    print(f"[Phase 1] {label} — {DATE}")
    print(f"  动态年份: {CURRENT_YEAR} / {NEXT_YEAR}")

    memory = read_memory(label)
    queries = get_search_queries(label)
    all_results = []
    seen_urls = set()

    for query in queries:
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

    raw_json_str = deepseek(
        "你是一个产业信息分析师。只输出 JSON，不要 markdown 代码块，不要额外说明。",
        f"""分析以下关于「{topic}」的搜索结果，提取结构化信息。

历史记忆（已知道的信息，避免重复）：
{memory}

搜索结果：
{context}

输出 JSON 格式（严格）：
{{
  "topic": "{topic}",
  "label": "{label}",
  "date": "{DATE}",
  "total_sources": {len(all_results)},
  "sources": [
    {{"title": "标题", "url": "链接", "platform": "来源平台", "summary": "一句话摘要", "relevance": "high/medium/low", "tags": ["标签"]}}
  ],
  "signals": [
    {{"signal": "值得关注的信号", "direction": "up/down/new/stable", "evidence": "支撑依据", "category": "产品/技术/行业/竞品"}}
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

    filepath = f"{RAW_DIR}/{DATE}-{label}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)
    print(f"  ✅ 原始数据已保存: {filepath}")


# ── Phase 2 ────────────────────────────────────────────────

def phase2(label: str = ""):
    print(f"[Phase 2] 生成报告 — {DATE}")

    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    target = None
    for f in files:
        if f.endswith(f"-{label}.json"):
            target = f
            break

    if not target:
        print(f"  ⚠️ 找不到 {label} 的原始数据，搜索 *-{label}.json")
        return

    with open(target, encoding="utf-8") as f:
        raw_data = json.load(f)

    topic = raw_data.get("topic", label)
    memory = read_memory(label)
    prev_data = find_prev_raw(label, exclude=target)

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
        f"""基于以下原始数据，撰写「{topic}」调研报告。

## 本周数据
来源数: {raw_data.get('total_sources', 0)}
涉及公司: {companies}
热点话题: {hot_topics}

来源详情:
{sources}

信号:
{signals}

趋势:
{trends}

## 上期数据（用于对比。首次运行此项为空，请标注"首期，暂无对比"）
来源:
{prev_sources}

信号:
{prev_signals}

趋势:
{prev_trends}

## 历史记忆
{memory}

## 报告结构（严格按此输出）

### 本周核心发现
每条：**发现** + 依据（附来源链接）

### 各平台摘要
按来源/语言分类列出关键信息（Google / 知乎 / 技术社区 / 百度 等）

### 趋势变化分析（对比上期）
- 新出现的信号 vs 已消退的信号
- 热度变化方向（上升/下降/平稳）
- 值得关注的早期信号

### 数据来源
所有参考链接列表（Markdown 链接格式）""",
    )

    report_file = f"{REPORT_DIR}/{DATE}-{label}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(f"**调研日期：** {DATE}\n")
        f.write(f"**来源数：** {raw_data.get('total_sources', 0)}\n\n")
        f.write("---\n\n")
        f.write(report)
    print(f"  ✅ 报告已生成: {report_file}")

    # 更新 memory
    memory_content = deepseek(
        "你是一个信息提取器。输出简洁 Markdown。",
        f"""从以下报告和信号中提取关键记忆点，供下次调研参考：
- 涉及的公司/产品/项目名称
- 重要趋势信号（方向 + 描述）
- 值得长期跟踪的话题
- 竞品动态

报告：
{report}

原始信号：
{signals}""",
    )
    write_memory(label, memory_content)
    print(f"  ✅ Memory 已更新: {MEMORY_DIR}/{label}.md")


# ── Entry ──────────────────────────────────────────────────

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""

    if mode == "phase1":
        phase1()

    elif mode == "phase2":
        arg = sys.argv[2] if len(sys.argv) > 2 else ""
        if arg:
            phase2(arg)
        else:
            # 无参数时遍历所有 label
            labels = set()
            for f in sorted(glob.glob(f"{RAW_DIR}/*.json")):
                basename = os.path.basename(f)
                parts = basename.replace(".json", "").split("-", 1)
                if len(parts) > 1:
                    labels.add(parts[1])
            if not labels:
                print("  ⚠️ 没有找到任何 raw JSON 文件")
            for label in sorted(labels):
                phase2(label)

    else:
        print("Usage: python research.py phase1          (needs TOPIC + LABEL env)")
        print("       python research.py phase2 [label]  (omit label to process all)")
        sys.exit(1)
