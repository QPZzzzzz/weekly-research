# incredibuild — Research Memory

最后更新: 2026-09-05

## 关键记忆点

- **Incredibuild**：mindshare 1.0%→1.3%（PeerSpot 2026.8-9），专业分布式编译厂商蚕食通用CI/CD平台份额
- **TeamCity**：mindshare 6.8%→4.8%；**GitLab**：12.8%→6.1%（同期大幅下滑）
- **EngFlow**：mindshare 0.3%→0.8%，但评分仅1/5，短期不构成实质威胁
- **FASTBuild**：SourceForge列为Incredibuild直接替代品（宣称10倍加速），中文社区（博客园）教程持续出现
- **腾讯yadcc**：开源分布式编译工具，日产出300万+目标文件，对中长尾客户构成系统性替代压力
- **Islo AI沙盒 + 免费CI加速（8倍）**：Incredibuild双引擎战略，官网/博客/资源页/新闻页四大渠道统一主推"AI时代的构建加速平台"
- **Build Cache功能**：Windows 10.37.0（2026.8.19）新增，对标Bazel/Nx等现代构建系统的缓存复用能力；目前仅限Windows，Linux跟进时间待观察
- **Unity Shader编译**：Incredibuild游戏行业垂直深耕新切入点，叠加Epic MegaGrants合作，游戏行业具"灯塔效应"
- **Buildkite**：被Incredibuild官方博客指缺乏缓存和分发能力，竞争边界扩展至云原生CI工具
- **AOSP 17支持**：Linux 4.29.0新增，标志向移动开发渗透
- **龙智**：Incredibuild中国授权合作伙伴，举办线下沙龙但中文社区热度不高
- **美团技术博客**：C++编译优化实践，使用Distcc/Dmucs方案，大厂自研倾向明显
- **BuildXL vs IncrediBuild**（Stack Overflow）：确认支持MSBuild/CMake/Make/Ninja/GCC等多种构建系统
- **mindshare领先收入6-12个月**（历史记忆已验证）：Incredibuild未来两季度有望看到实质性收入增长

## 重要趋势信号

- **专业工具蚕食通用CI/CD平台份额**：方向：专业分布式编译厂商mindshare上升，通用平台下滑；强度：high
- **"AI沙盒+免费CI加速"双引擎战略**：方向：AI开发场景与构建加速绑定为同一价值主张；强度：high
- **开源替代品威胁持续升级**：方向：FASTBuild/yadcc在中文社区加速渗透，对价格敏感客户形成替代压力；强度：high
- **Build Cache补齐缓存复用短板**：方向：从纯分布式并行向"分布式+缓存智能复用"演进；强度：high
- **游戏行业垂直深耕**：方向：Unity Shader编译切入，头部工作室辐射效应；强度：high
- **EngFlow竞争力回升**：方向：mindshare上升但绝对数值低，需连续多期观察；强度：low→medium
- **中国渠道活跃度低**：方向：大厂自研倾向明显，商业产品渗透有限；强度：low

## 值得长期跟踪的技术方向/话题

- **分布式编译 vs 现代构建系统（Bazel/Nx）的缓存机制竞争**：Build Cache功能补齐后的Linux版本跟进时间
- **AI编程助手普及对构建加速需求的拉动**：AI生成代码快速验证场景
- **开源分布式编译工具（FASTBuild/yadcc）对商业产品的替代边界**：中长尾客户分层分析
- **中国互联网大厂自研编译加速工具趋势**：美团Distcc/Dmucs为典型案例
- **mindshare变化向收入增长的转化验证**：6-12个月验证期

## 竞品动态

- **Incredibuild**：Windows 10.37.0新增Build Cache；Linux 4.29.2更新Apache至2.4.68（安全）；Linux 4.29.0新增AOSP 17支持；发布Unity Shader编译专题文章；官方博客发布CI/CD工具Top 10分析（2026）
- **Buildkite**：被指缺乏缓存和分发能力，成为Incredibuild差异化切入点
- **FASTBuild**：SourceForge列为直接替代品，中文社区教程持续出现
- **EngFlow**：宣称C++构建21倍加速（Reddit/The New Stack），mindshare上升但评分低
- **腾讯yadcc**：开源分布式编译工具，日产出300万+目标文件
- **龙智**：作为Incredibuild中国授权合作伙伴，提供咨询/销售/实施/培训服务