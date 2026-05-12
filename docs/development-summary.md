# Weekly Research Pipeline — 开发过程总结

**项目：** `QPZzzzzz/weekly-research`
**最后更新：** 2026-05-12
**本地路径：** `~/Desktop/weekly-research`

---

## 项目概述

基于 GitHub Actions 的自动化行业调研系统。每周一/三/五/日北京时间 09:00 自动运行，通过 Tavily Search API 进行多轮搜索，DeepSeek 结构化分析与报告生成，最终将报告推送到 Obsidian 私有仓库。

### 三个调研方向

| Label | 主题 | Obsidian 路径 |
|-------|------|--------------|
| `ai-sdlc-tools` | SDLC 中的 AI 工具（Cursor/Copilot/代码生成/CI自动化） | `学习/行业信息/{DATE}/ai-sdlc-tools.md` |
| `build-acceleration` | 编译加速行业动态（分布式编译/build cache/C++工具链） | `学习/行业信息/{DATE}/build-acceleration.md` |
| `incredibuild` | Incredibuild 及其竞品（产品动态/竞品对比/行业格局） | `学习/行业信息/{DATE}/incredibuild.md` |

### 报告结构

每份报告包含四个章节：
1. **本周核心发现** — 每条发现 + 依据 + 来源链接
2. **各平台摘要** — 按来源/语言分类（Google / 知乎 / 技术社区等）
3. **趋势变化分析** — 对上期：新信号 vs 消退信号 + 热度方向
4. **数据来源** — 所有参考链接

---

## 架构

```
GitHub Actions (cron: 周一/三/五/日 09:00 北京时间)

Phase 1: Matrix 并行搜索 (3 jobs, fail-fast: false)
├── Collect: ai-sdlc-tools       → raw_sources/{DATE}-ai-sdlc-tools.json
├── Collect: build-acceleration   → raw_sources/{DATE}-build-acceleration.json
└── Collect: incredibuild         → raw_sources/{DATE}-incredibuild.json

Phase 2: 串行报告生成 (1 job, 依赖 Phase 1 全部成功)
└── 遍历所有 label，各自:
    1. 读取 raw JSON + 历史 Memory
    2. DeepSeek 生成报告
    3. 更新 Memory (per label)
    4. 输出 reports/{DATE}-{label}.md

Phase 3: 推送到 Obsidian (1 job, 依赖 Phase 2)
└── 复制 reports/*.md → obsidian-vault/学习/行业信息/{DATE}/
    推送到 QPZzzzzz/obsidian-data 仓库（通过 GH_PAT）
```

### 关键设计决策

- **Matrix 并行** — 三个 topic 各自独立搜索，`fail-fast: false` 确保一个失败不影响其他
- **Per-label Memory** — 每个 topic 独立维护历史趋势记忆（`memory/{label}.md`），保证趋势分析的连贯性
- **按日期分组** — 同一次运行的三份报告放在 `学习/行业信息/{DATE}/` 目录下，Obsidian 中按日期浏览
- **动态日期注入** — 搜索查询中的年份/月份在运行时计算（`CURRENT_YEAR`/`CURRENT_MONTH`），不再硬编码
- **Tavily `days=7` 过滤** — API 层面限制只返回最近 7 天的数据，确保时效性

---

## 文件结构

```
weekly-research/
├── .github/workflows/weekly-research.yml  # CI/CD 工作流
├── scripts/research.py                    # 核心流水线脚本
├── README.md                              # 使用说明
└── docs/superpowers/
    ├── specs/2026-05-11-weekly-research-redesign.md  # 设计文档
    └── plans/2026-05-11-weekly-research-redesign.md  # 实现计划
```

---

## Git 提交历史（按时间倒序）

| Commit | 描述 |
|--------|------|
| `ff08e04` | **fix:** Tavily 搜索缺少 `days` 时间过滤 + 查询细化到月份（"2026年5月"）|
| `57c19a4` | **refactor:** Matrix 并行架构 + `学习/行业信息/{DATE}` 按日期分组 |
| `a6cc443` | **fix:** Phase 2 label 解析 bug（日期中的横线导致错误拆分）+ batch 错误处理 |
| `68e81aa` | **refactor:** 恢复 Matrix 多主题架构 + 动态日期 + v1 报告结构 |
| `10db0fa` | **docs:** implementation plan for weekly research pipeline redesign |
| `9ff9f8f` | **docs:** weekly research pipeline 重构设计 spec |
| `894aca3` | **fix:** Phase 2 glob 匹配不上 Phase 1 日期前缀文件名 |
| `97bd251` | **fix:** 修复 collect 失败时 push 报 artifact not found |
| `cb7a15b` | **update:** 重组搜索为三个维度（Incredibuild最新/行业/竞品）|
| `ad218b4` | **update:** 单 topic 聚焦 Incredibuild, 多轮搜索, 一周四跑 |
| `1972b96` | **fix:** make Tavily API key optional for Phase 2 |
| `27cb4cc` | **init:** weekly research pipeline |

---

## 已修复的 Bug 清单

### 1. Phase 2 glob 匹配失败（`894aca3`）
- **问题：** Phase 1 保存文件名为 `{DATE}-{label}.json`，Phase 2 搜索 `{label}*.json`，日期前缀导致无法匹配
- **修复：** glob 改为 `*-{label}.json`

### 2. Artifact not found（`97bd251`）
- **问题：** `generate` 设了 `if: always()`，collect 失败后仍运行，无报告 artifact 时 push 报错
- **修复：** 改为 `if: success()` + `continue-on-error` + 报告数量守卫

### 3. Label 解析错误（`a6cc443`）
- **问题：** 用 `split("-", 1)` 解析 `YYYY-MM-DD-{label}.json`，日期中的横线导致 label 被截断
- **修复：** 跳过前 11 个字符（`YYYY-MM-DD-`）直接取 label

### 4. 搜索时间范围失效（`ff08e04`）
- **问题：** 查询中只有年份 "2026"，Tavily API 无 `days` 参数，返回 2025 年 12 月旧数据
- **修复：** API 增加 `days=7` + 查询细化到月份 "2026年5月"

---

## 所需 GitHub Secrets

| Secret | 说明 |
|--------|------|
| `TAVILY_API_KEY` | Tavily Search API Key（免费 1000 次/月）|
| `DEEPSEEK_API_KEY` | DeepSeek API Key |
| `GH_PAT` | GitHub Personal Access Token（`contents: write` 权限，用于推送 Obsidian 仓库）|

---

## 触发方式

- **自动：** 每周一/三/五/日 UTC 01:00（北京时间 09:00）
- **手动：** [Actions 页面](https://github.com/QPZzzzzz/weekly-research/actions/workflows/weekly-research.yml) → "Run workflow"
