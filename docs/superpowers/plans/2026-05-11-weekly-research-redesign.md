# Weekly Research Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore v1 Matrix parallel architecture with three independent research topics, dynamic date injection, corrected Obsidian path, and v1 report structure.

**Architecture:** Matrix-based parallel search (3 topic jobs) → serial report generation (1 job iterating labels) → push to Obsidian under `学习/行业信息/{DATE}/`. Each topic has its own 5-query search list with runtime-computed year keywords.

**Tech Stack:** Python 3.12, requests, Tavily Search API, DeepSeek Chat API, GitHub Actions

**Spec:** `docs/superpowers/specs/2026-05-11-weekly-research-redesign.md`

---

### Task 1: Rewrite `scripts/research.py` — multi-topic, dynamic dates, v1 reports

**Files:**
- Overwrite: `scripts/research.py` (complete rewrite)

The current script is single-topic (hardcoded Incredibuild) with hardcoded year strings. Rewrite to accept `TOPIC`/`LABEL` env vars in Phase 1 and `label` argument in Phase 2, restoring the v1 multi-topic pattern.

- [ ] **Step 1: Write the new `scripts/research.py`**

Replace the entire file with:

```python
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
        if f"*-{label}.json" in f or f.endswith(f"-{label}.json"):
            if f != exclude:
                with open(f, encoding="utf-8") as pf:
                    return json.load(pf)
    return None


def get_search_queries(label: str) -> list:
    """每个 topic 的动态搜索查询列表，{year}/{next_year} 运行时注入"""
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

    # 找最新的 JSON
    files = sorted(glob.glob(f"{RAW_DIR}/*.json"), reverse=True)
    target = None
    for f in files:
        basename = os.path.basename(f)
        if f"-{label}.json" in basename or basename.endswith(f"-{label}.json"):
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

## 上期数据（用于对比。首次运行此项为空，需标注"首期，暂无对比"）
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
```

- [ ] **Step 2: Verify syntax**

```bash
python3 -m py_compile /Users/chenwen/Desktop/weekly-research/scripts/research.py
```

Expected: silent output (no errors).

- [ ] **Step 3: Commit**

```bash
git -C /Users/chenwen/Desktop/weekly-research add scripts/research.py
git -C /Users/chenwen/Desktop/weekly-research commit -m "refactor: 恢复 Matrix 多主题架构 + 动态日期 + v1 报告结构"
```

---

### Task 2: Rewrite `.github/workflows/weekly-research.yml` — Matrix strategy + corrected paths

**Files:**
- Overwrite: `.github/workflows/weekly-research.yml`

Restore the Matrix strategy for Phase 1 (3 parallel topic jobs), download all artifacts in Phase 2, push to `学习/行业信息/{DATE}/` in Phase 3.

- [ ] **Step 1: Write the new workflow file**

Replace the entire file with:

```yaml
name: Weekly Research Report

on:
  schedule:
    # 周一、三、五、日 UTC 01:00（北京时间 09:00）
    - cron: '0 1 * * 1,3,5,0'
  workflow_dispatch:

env:
  RAW_DIR: raw_sources
  MEMORY_DIR: memory
  REPORT_DIR: reports
  OBSIDIAN_REPO: QPZzzzzz/obsidian-data
  OBSIDIAN_BASE_DIR: 学习/行业信息

jobs:
  # ═══════════════════════════════════════════════════════════
  # Phase 1: Matrix 并行搜索 + 结构化采集
  # ═══════════════════════════════════════════════════════════
  collect:
    name: "Collect - ${{ matrix.label }}"
    strategy:
      matrix:
        include:
          - topic: 'SDLC 中的 AI 工具 Cursor Copilot 代码生成 自动化 CICD'
            label: 'ai-sdlc-tools'
          - topic: '编译加速 分布式编译 C++ 行业 build cache 趋势'
            label: 'build-acceleration'
          - topic: 'Incredibuild 分布式编译 竞品对比 行业格局'
            label: 'incredibuild'
      fail-fast: false
    runs-on: ubuntu-latest
    timeout-minutes: 20

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install requests

      - name: Phase 1 - Multi-source search & analysis
        env:
          TAVILY_API_KEY: ${{ secrets.TAVILY_API_KEY }}
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
          TOPIC: ${{ matrix.topic }}
          LABEL: ${{ matrix.label }}
        run: python scripts/research.py phase1

      - name: Upload raw data
        uses: actions/upload-artifact@v4
        with:
          name: raw-${{ matrix.label }}
          path: raw_sources/

  # ═══════════════════════════════════════════════════════════
  # Phase 2: 报告生成（串行，遍历所有 label）
  # ═══════════════════════════════════════════════════════════
  generate:
    name: Generate Reports
    needs: collect
    if: success()
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install requests

      - name: Download all raw data
        uses: actions/download-artifact@v4
        with:
          pattern: raw-*
          path: raw_sources/
          merge-multiple: true

      - name: Phase 2 - Generate reports for all labels
        env:
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
        run: python scripts/research.py phase2

      - name: Upload reports
        uses: actions/upload-artifact@v4
        with:
          name: reports
          path: reports/

  # ═══════════════════════════════════════════════════════════
  # Phase 3: 推送报告到 Obsidian
  # ═══════════════════════════════════════════════════════════
  push:
    name: Sync to Obsidian
    needs: generate
    if: success()
    runs-on: ubuntu-latest

    steps:
      - name: Download reports
        uses: actions/download-artifact@v4
        with:
          name: reports
          path: reports/
        continue-on-error: true

      - name: Push to Obsidian vault
        run: |
          REPORT_COUNT=$(ls reports/*.md 2>/dev/null | wc -l)
          if [ "$REPORT_COUNT" -eq 0 ]; then
            echo "ℹ️ 没有报告文件，跳过同步"
            exit 0
          fi

          DATE=$(date +%Y-%m-%d)

          git clone https://x-access-token:${{ secrets.GH_PAT }}@github.com/${{ env.OBSIDIAN_REPO }}.git obsidian-vault

          TARGET="obsidian-vault/${{ env.OBSIDIAN_BASE_DIR }}/${DATE}"
          mkdir -p "$TARGET"

          for f in reports/*.md; do
            [ ! -f "$f" ] && continue
            cp "$f" "$TARGET/"
            echo "  📄 $(basename "$f") → ${{ env.OBSIDIAN_BASE_DIR }}/${DATE}/"
          done

          cd obsidian-vault
          git config user.name "weekly-research-bot"
          git config user.email "bot@weekly-research"
          git add "${{ env.OBSIDIAN_BASE_DIR }}/${DATE}/"
          if git diff --cached --quiet; then
            echo "ℹ️ 没有新内容需要同步"
          else
            git commit -m "weekly-research: ${DATE} 调研报告"
            git push
            echo "✅ 已同步到 Obsidian: ${{ env.OBSIDIAN_BASE_DIR }}/${DATE}/"
          fi
```

- [ ] **Step 2: Verify YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('/Users/chenwen/Desktop/weekly-research/.github/workflows/weekly-research.yml'))" && echo "OK"
```

Expected: `OK` (no parse errors). If `yaml` module not installed, `pip install pyyaml` first.

- [ ] **Step 3: Commit**

```bash
git -C /Users/chenwen/Desktop/weekly-research add .github/workflows/weekly-research.yml
git -C /Users/chenwen/Desktop/weekly-research commit -m "refactor: Matrix 并行架构 + 学习/行业信息/{DATE} 按日期分组"
```

---

### Task 3: Local end-to-end dry-run validation

**Files:** None modified — validation only.

Run Phase 1 and Phase 2 locally (without API keys) to verify the code handles missing keys gracefully, the date injection produces correct year strings, and the label/file matching logic works.

- [ ] **Step 1: Validate dynamic date injection**

```bash
cd /Users/chenwen/Desktop/weekly-research
python3 -c "
from datetime import datetime
y = datetime.now().year
print(f'当前年份: {y}')
print(f'次年: {y+1}')
# Verify queries contain dynamic years
import scripts.research as r
for label in ['ai-sdlc-tools', 'build-acceleration', 'incredibuild']:
    queries = r.get_search_queries(label)
    print(f'\n{label}: {len(queries)} queries')
    for q in queries:
        assert str(y) in q or str(y+1) in q, f'Missing year in: {q}'
        print(f'  OK: {q[:60]}...')
print('\n✅ All queries contain dynamic year')
"
```

Expected: all queries contain current year, no hardcoded `2025`.

- [ ] **Step 2: Verify Phase 1/Phase 2 entry points and label matching**

```bash
cd /Users/chenwen/Desktop/weekly-research
mkdir -p raw_sources reports memory

# Create a mock raw JSON to test Phase 2 label matching
DATE=$(date +%Y-%m-%d)
cat > "raw_sources/${DATE}-ai-sdlc-tools.json" << 'JSONEOF'
{
  "topic": "SDLC 中的 AI 工具",
  "label": "ai-sdlc-tools",
  "date": "DATE_PLACEHOLDER",
  "total_sources": 3,
  "sources": [
    {"title": "Test article", "url": "https://example.com/1", "platform": "技术博客", "summary": "Test summary", "relevance": "high", "tags": ["AI", "SDLC"]}
  ],
  "signals": [
    {"signal": "Test signal", "direction": "up", "evidence": "Test evidence", "category": "产品"}
  ],
  "trends": [
    {"trend": "Test trend", "evidence": "Test", "momentum": "rising"}
  ],
  "companies_mentioned": ["TestCorp"],
  "hot_topics": ["AI Testing"]
}
JSONEOF
sed -i '' "s/DATE_PLACEHOLDER/${DATE}/g" "raw_sources/${DATE}-ai-sdlc-tools.json"

echo "  ✅ Mock raw JSON created: raw_sources/${DATE}-ai-sdlc-tools.json"
echo "  Files in raw_sources/:"
ls raw_sources/
```

Expected: one file `{today}-ai-sdlc-tools.json` exists.

- [ ] **Step 3: Verify Phase 2 label detection (without API call)**

```bash
cd /Users/chenwen/Desktop/weekly-research
# Test label detection logic
python3 -c "
import glob, os
RAW_DIR = 'raw_sources'
files = sorted(glob.glob(f'{RAW_DIR}/*.json'), reverse=True)
labels = set()
for f in files:
    basename = os.path.basename(f)
    parts = basename.replace('.json', '').split('-', 1)
    if len(parts) > 1:
        labels.add(parts[1])
print(f'Detected labels: {labels}')
assert 'ai-sdlc-tools' in labels, 'Should detect ai-sdlc-tools'
print('✅ Label detection works')
"
```

Expected: `ai-sdlc-tools` detected.

- [ ] **Step 4: Clean up mock data**

```bash
cd /Users/chenwen/Desktop/weekly-research
rm -rf raw_sources reports memory
echo "✅ Mock data cleaned"
```

- [ ] **Step 5: Validate workflow YAML syntax**

```bash
python3 -c "import yaml; yaml.safe_load(open('/Users/chenwen/Desktop/weekly-research/.github/workflows/weekly-research.yml')); print('✅ Workflow YAML valid')"
```

If `pyyaml` is not installed, install it first: `pip3 install pyyaml`

- [ ] **Step 6: Commit validation scripts (if any) and push**

The validation was read-only, no files to commit from this task. If any test fixtures were accidentally left behind, clean them up.

```bash
cd /Users/chenwen/Desktop/weekly-research
rm -rf raw_sources reports memory 2>/dev/null
git status  # should be clean
```

---

### Task 4: Push all commits and trigger manual run

**Files:** None modified.

- [ ] **Step 1: Push all commits**

```bash
git -C /Users/chenwen/Desktop/weekly-research push origin main
```

- [ ] **Step 2: Inform user to manually trigger**

Done in the final message. User triggers via [Actions page](https://github.com/QPZzzzzz/weekly-research/actions/workflows/weekly-research.yml) → "Run workflow".

---

### Summary of Changes

| File | Change |
|------|--------|
| `scripts/research.py` | Complete rewrite: multi-topic (`TOPIC`/`LABEL` env), dynamic year injection via `CURRENT_YEAR`/`NEXT_YEAR`, per-label memory, 5 queries per topic, v1 report structure (本周核心发现/各平台摘要/趋势变化分析/数据来源) |
| `.github/workflows/weekly-research.yml` | Complete rewrite: Matrix strategy (3 parallel collect jobs), `pattern: raw-*` with `merge-multiple: true`, Phase 3 path `学习/行业信息/{DATE}/` |
