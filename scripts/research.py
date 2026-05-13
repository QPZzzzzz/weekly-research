#!/usr/bin/env python3
"""
Weekly Research Pipeline — Matrix 多主题架构 + Multi-Agent
- Phase 1: 多轮搜索 → DeepSeek 结构化分析 → JSON (per label)
- Phase 2: Multi-Agent 协作
    Agent 1 (Trend Agent):   本期信号 vs 上期信号 → 结构化 diff
    Agent 2 (Writer Agent):  信号 + diff + memory → Markdown 报告
    Agent 3 (Memory Agent):  报告 → 历史记忆提取
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
CURRENT_MONTH = datetime.now().strftime("%Y年%-m月")  # e.g. "2026年5月"


def deepseek(system: str, user: str) -> str:
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY 未设置")
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


def deepseek_json(system: str, user: str) -> dict:
    """Call DeepSeek and parse JSON response, with cleanup"""
    raw = deepseek(system, user)
    raw = raw.strip()
    if raw.startswith("```"):
        raw = "\n".join(raw.split("\n")[1:-1])
    return json.loads(raw)


def tavily_search(query: str, max_results: int = 6) -> list:
    if not TAVILY_API_KEY:
        raise RuntimeError("TAVILY_API_KEY 未设置")
    resp = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "include_answer": False,
            "max_results": max_results,
            "days": 7,
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
    """每个 topic 的动态搜索查询列表，日期运行时注入"""
    queries = {
        "ai-sdlc-tools": [
            f"AI coding assistant 软件工程 SDLC {CURRENT_MONTH}",
            f"Cursor Copilot Codeium AI 编程 工具 {CURRENT_MONTH}",
            f"AI SDLC automation CICD testing code review {CURRENT_MONTH}",
            f"大模型 软件开发 自动化 代码生成 {CURRENT_YEAR} {NEXT_YEAR}",
            f"AI powered software development lifecycle trends {CURRENT_MONTH}",
        ],
        "build-acceleration": [
            f"编译加速 分布式编译 C++ {CURRENT_MONTH}",
            f"distributed compilation build acceleration C++ {CURRENT_MONTH}",
            f"mold sccache ccache build cache 编译 优化 {CURRENT_MONTH}",
            f"C++ build systems cmake bazel buck2 {CURRENT_MONTH}",
            f"build pipeline optimization CI acceleration {CURRENT_MONTH}",
        ],
        "incredibuild": [
            f"Incredibuild 分布式编译 动态 {CURRENT_MONTH}",
            f"Incredibuild distributed compilation news {CURRENT_MONTH}",
            f"Incredibuild 竞品 Nocc FASTBuild EngFlow BuildBarn {CURRENT_MONTH}",
            f"Incredibuild competitor comparison distributed build {CURRENT_MONTH}",
            f"分布式编译 行业格局 加速 方案 C++ {CURRENT_MONTH}",
        ],
    }
    return queries.get(label, queries["incredibuild"])


# ── Multi-Agent Functions (Phase 2) ──────────────────────────


def trend_agent(label, current_signals, current_trends,
                prev_signals, prev_trends, memory) -> dict:
    """Agent 1: 跨期趋势对比。结构化 diff 本期 vs 上期信号"""
    if not prev_signals and not prev_trends:
        return {"is_first_run": True, "note": "首期运行，暂无对比数据"}

    curr_sig = json.dumps(current_signals, ensure_ascii=False, indent=2)
    curr_tr = json.dumps(current_trends, ensure_ascii=False, indent=2)
    prev_sig = json.dumps(prev_signals, ensure_ascii=False, indent=2)
    prev_tr = json.dumps(prev_trends, ensure_ascii=False, indent=2)

    try:
        result = deepseek_json(
            "你是一个产业趋势对比分析师。只输出 JSON，不要 markdown 代码块，不要额外说明。严格基于给定数据，不要编造。",
            f"""对比本期和上期的产业信号与趋势，执行结构化 diff。

历史记忆：
{memory}

本期信号：
{curr_sig}

本期趋势：
{curr_tr}

上期信号：
{prev_sig}

上期趋势：
{prev_tr}

输出 JSON：
{{
  "is_first_run": false,
  "new_signals": [
    {{"name": "新出现信号", "significance": "high/medium/low",
      "category": "产品/技术/行业/竞品", "what_changed": "具体变化描述"}}
  ],
  "disappeared_signals": [
    {{"name": "已消退信号", "likely_reason": "可能原因",
      "was_significance": "上期级别 high/medium/low"}}
  ],
  "strengthened": [
    {{"name": "信号名", "from": "上期强度 high/medium/low",
      "to": "本期强度 high/medium/low", "evidence": "强化证据"}}
  ],
  "weakened": [
    {{"name": "信号名", "from": "上期强度", "to": "本期强度",
      "evidence": "弱化证据"}}
  ],
  "hotness_shift": "整体热度变化：升温/降温/持平，一句话总结",
  "early_signals_to_watch": ["描述1", "描述2"]
}}

要求：
- 如果某项确实无变化，用空列表 []
- 信号强度必须基于实际数据判断
- 不要为了凑数编造变化"""
        )
        return result
    except Exception as e:
        print(f"  ⚠️ Trend Agent 失败: {e}，回退到无对比模式")
        return {"is_first_run": True, "note": f"趋势对比暂不可用 ({e})"}


def writer_agent(topic: str, raw_data: dict, trend: dict, memory: str) -> str:
    """Agent 2: 报告撰写。整合信号、趋势 diff、历史记忆 → Markdown"""
    sources = json.dumps(raw_data.get("sources", []), ensure_ascii=False, indent=2)
    signals = json.dumps(raw_data.get("signals", []), ensure_ascii=False, indent=2)
    trends_raw = json.dumps(raw_data.get("trends", []), ensure_ascii=False, indent=2)
    companies = json.dumps(raw_data.get("companies_mentioned", []), ensure_ascii=False)
    hot_topics = json.dumps(raw_data.get("hot_topics", []), ensure_ascii=False)
    trend_analysis = json.dumps(trend, ensure_ascii=False, indent=2)

    # Build the trend section prompt based on whether we have comparison data
    if trend.get("is_first_run"):
        trend_section_prompt = "#### 趋势变化分析\n标注\"首期运行，暂无对比数据\"，说明将在下期报告中提供趋势变化分析。"
    else:
        trend_section_prompt = f"""#### 趋势变化分析（严格基于以下结构化 diff，不要重新分析原始数据）

结构化趋势 diff：
{trend_analysis}

在此章节中：
1. 列出**新出现的信号**（按 significance 排序），每条说明为什么值得关注
2. 列出**已消退的信号**，分析可能原因
3. 列出**信号强度变化**（strengthened / weakened），用 → 符号清晰标注变化方向
4. 总结**整体热度变化**，引用 early_signals_to_watch"""

    return deepseek(
        "你是一个产业调研报告撰写师。用中文撰写，使用 Markdown 格式。报告要有洞察力，数据驱动的结论。",
        f"""撰写关于「{topic}」的产业调研报告。

## 本期数据概览
来源数: {raw_data.get('total_sources', 0)}
涉及公司: {companies}
热点话题: {hot_topics}

## 本期结构化信号
{signals}

## 本期趋势
{trends_raw}

## 历史记忆
{memory}

## 来源详情
{sources}

## 报告结构（严格按此输出）

### 本周核心发现
每条：**发现** + 依据 + 来源链接。按重要性排序，挑最有价值的 3-5 条。

### 各平台摘要
按来源/语言分类列出关键信息（Google / 知乎 / 技术社区 / 百度 / GitHub / Reddit 等）

{trend_section_prompt}

### 数据来源
所有参考链接列表（Markdown 链接格式，按 relevance 排序）
"""
    )


def memory_agent(report: str, signals: list) -> str:
    """Agent 3: 记忆提取。从报告中提取关键点，供下次调研参考"""
    sig_json = json.dumps(signals, ensure_ascii=False, indent=2)
    return deepseek(
        "你是一个信息提取器。输出简洁 Markdown，每条一行。",
        f"""从以下报告和信号中提取关键记忆点，供下次调研参考：

- 涉及的公司/产品/项目名称
- 重要趋势信号（方向 + 描述 + 强度 high/medium/low）
- 值得长期跟踪的技术方向或话题
- 竞品动态（新产品、融资、合作、技术突破）

报告：
{report}

信号：
{sig_json}"""
    )


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
    print(f"\n{'='*60}")
    print(f"[Phase 2] {label} — Multi-Agent 协作")
    print(f"{'='*60}")

    # ── 加载数据 ──
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    target = None
    for f in files:
        if f.endswith(f"-{label}.json"):
            target = f
            break

    if not target:
        print(f"  ⚠️ 找不到 {label} 的原始数据 (搜索 *-{label}.json)")
        return

    with open(target, encoding="utf-8") as f:
        raw_data = json.load(f)

    topic = raw_data.get("topic", label)
    memory = read_memory(label)
    prev_data = find_prev_raw(label, exclude=target)

    current_signals = raw_data.get("signals", [])
    current_trends = raw_data.get("trends", [])
    prev_signals = prev_data.get("signals", []) if prev_data else []
    prev_trends = prev_data.get("trends", []) if prev_data else []

    # ── Agent 1: Trend Analysis ──
    print(f"  🧠 Agent 1/3 (Trend Agent): 跨期信号对比...")
    trend = trend_agent(label, current_signals, current_trends,
                        prev_signals, prev_trends, memory)
    if trend.get("is_first_run"):
        print(f"     📝 {trend.get('note', '首期运行')}")
    else:
        new_n = len(trend.get("new_signals", []))
        gone_n = len(trend.get("disappeared_signals", []))
        up_n = len(trend.get("strengthened", []))
        down_n = len(trend.get("weakened", []))
        print(f"     📊 新信号:{new_n}  消退:{gone_n}  强化:{up_n}  弱化:{down_n}  |  热度:{trend.get('hotness_shift', 'N/A')}")

    # ── Agent 2: Report Writing ──
    print(f"  ✍️  Agent 2/3 (Writer Agent): 报告撰写...")
    try:
        report = writer_agent(topic, raw_data, trend, memory)
    except RuntimeError as e:
        print(f"  ❌ Writer Agent 失败: {e}")
        return

    report_file = f"{REPORT_DIR}/{DATE}-{label}.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(f"**调研日期：** {DATE}\n")
        f.write(f"**来源数：** {raw_data.get('total_sources', 0)}\n\n")
        f.write("---\n\n")
        f.write(report)
    print(f"  ✅ 报告已生成: {report_file}")

    # ── Agent 3: Memory Update ──
    print(f"  🗄️  Agent 3/3 (Memory Agent): 记忆提取...")
    try:
        memory_content = memory_agent(report, current_signals)
        write_memory(label, memory_content)
        print(f"  ✅ Memory 已更新: {MEMORY_DIR}/{label}.md")
    except RuntimeError as e:
        print(f"  ⚠️ Memory 更新失败（非致命）: {e}")


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
                name = basename.replace(".json", "")
                # Filename format: YYYY-MM-DD-{label}.json — first 11 chars are date + dash
                if len(name) > 11 and name[4] == "-" and name[7] == "-":
                    labels.add(name[11:])
            if not labels:
                print("  ⚠️ 没有找到任何 raw JSON 文件")
            for label in sorted(labels):
                phase2(label)

    else:
        print("Usage: python research.py phase1          (needs TOPIC + LABEL env)")
        print("       python research.py phase2 [label]  (omit label to process all)")
        sys.exit(1)
