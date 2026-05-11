# Weekly Research Report

GitHub Actions 定时调研系统。搜索互联网 → DeepSeek 分析 → 结构化报告 → 同步 Obsidian。

## 使用方式

1. 将本项目所有文件上传到 `https://github.com/QPZzzzzz/weekly-research`
2. 在仓库 Settings → Secrets 中添加以下密钥
3. 等待定时触发，或手动运行 Actions

## 所需 Secrets

| Secret 名称 | 说明 |
|------------|------|
| `TAVILY_API_KEY` | https://tavily.com 注册获取（免费 1000 次/月）|
| `DEEPSEEK_API_KEY` | DeepSeek API Key |
| `GH_PAT` | GitHub Personal Access Token（`contents: write` 权限）|
