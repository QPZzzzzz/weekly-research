# Weekly Research Pipeline — 重构设计

**日期:** 2026-05-11
**状态:** 已确认

## 概述

恢复 v1 Matrix 并行架构，三个调研方向独立搜索、独立报告。修复三个已知问题：搜索日期写死、Obsidian 路径错误、报告结构偏离 v1。

## 调研方向

| Label | 搜索主题 | Obsidian 目标 |
|-------|---------|--------------|
| `ai-sdlc-tools` | SDLC 中的 AI 工具（Cursor/Copilot/自动化等） | `学习/行业信息/{DATE}/ai-sdlc-tools.md` |
| `build-acceleration` | 编译加速行业动态（C++ build tools/分布式编译等） | `学习/行业信息/{DATE}/build-acceleration.md` |
| `incredibuild` | Incredibuild 及其竞品（产品动态/竞品对比/行业格局） | `学习/行业信息/{DATE}/incredibuild.md` |

三份报告放入同一个日期文件夹，例如 `学习/行业信息/2026-05-11/`。

## 修复项

### 1. 日期 Bug
- **问题:** 搜索查询中硬编码 `2025 2026`，API 返回过期数据
- **修复:** 查询中动态注入 `datetime.now().year` 和次年，确保始终搜索最新数据

### 2. Obsidian 路径
- **问题:** 推送到 `行业信息/incredibuild`，缺少 `学习/` 前缀，且不支持多 topic
- **修复:** 改为 `学习/行业信息/{DATE}/`，按日期分组存放

### 3. 报告结构
- **问题:** 当前五段式（Incredibuild 最新动态/行业动态/竞品情报/趋势对比/数据来源）
- **修复:** 恢复 v1 三段式：
  - **本周核心发现** — 每条发现 + 依据
  - **各平台摘要** — 按来源/平台分类
  - **趋势变化分析（对比上期）** — 新信号 vs 消退信号 + 热度方向
  - **数据来源** — 所有参考链接

## 架构

```
GitHub Actions
├── Phase 1: Matrix 并行搜索 (3 jobs)
│   ├── ai-sdlc-tools      → raw_sources/{DATE}-ai-sdlc-tools.json
│   ├── build-acceleration  → raw_sources/{DATE}-build-acceleration.json
│   └── incredibuild        → raw_sources/{DATE}-incredibuild.json
│
├── Phase 2: 串行报告生成 (1 job, 依赖 Phase 1)
│   └── 遍历三个 label，各自:
│       1. 读取 raw JSON
│       2. DeepSeek 生成报告 (v1 结构)
│       3. 更新 Memory (per label)
│       4. 输出到 reports/{DATE}-{label}.md
│
└── Phase 3: 推送到 Obsidian (1 job, 依赖 Phase 2)
    └── 将 reports/*.md 复制到 obsidian-vault/学习/行业信息/{DATE}/
```

## 搜索查询设计

每个 topic 5 条多角度查询，中英文覆盖：

### ai-sdlc-tools
- AI coding assistant 软件工程 SDLC 趋势 {year}
- Cursor Copilot Codeium AI 编程 工具 最新 {year}
- AI SDLC automation CICD testing code review {year}
- 大模型 软件开发 自动化 代码生成 {year} {year+1}
- AI powered software development lifecycle trends {year}

### build-acceleration
- 编译加速 分布式编译 C++ 行业 {year}
- distributed compilation build acceleration C++ {year} {year+1}
- mold sccache ccache build cache 编译 优化 {year}
- C++ build systems cmake bazel buck2 comparison {year}
- build pipeline optimization CI acceleration techniques {year}

### incredibuild
- Incredibuild 分布式编译 最新 动态 {year}
- Incredibuild distributed compilation news {year} {year+1}
- Incredibuild 竞品 Nocc FASTBuild EngFlow BuildBarn {year}
- Incredibuild competitor comparison distributed build {year}
- 分布式编译 行业格局 加速 方案 C++ {year}

## 关键约束

- Phase 2 只在 Phase 1 全部成功后运行（`if: success()`）
- Phase 3 在 Phase 2 成功后运行，如无报告文件则优雅跳过
- Memory 文件按 label 独立维护（`memory/ai-sdlc-tools.md` 等），保持趋势分析的连贯性
- 回退兼容：首次运行时无上期数据，趋势对比部分标注"首期"

## 自测计划

1. **日期动态化验证:** 确认搜索查询中注入的是当前年份
2. **路径验证:** 确认 Obsidian 推送目标为 `学习/行业信息/{DATE}/{label}.md`
3. **报告结构验证:** 确认生成的报告包含 本周核心发现/各平台摘要/趋势变化分析/数据来源 四个章节
4. **端到端:** 本地 `python scripts/research.py phase1` + `python scripts/research.py phase2` 模拟运行
