# build-acceleration — Research Memory

最后更新: 2026-08-18

## 关键记忆点

### 核心公司/产品
- **微软**：VS 2026集成GitHub Copilot AI构建优化代理（Agent Mode），IDE内置路线
- **IncrediBuild**：推出Islo AI沙箱+免费8倍加速CI runners，独立工具链路线，面向管理层输出"构建速度=业务竞争力"
- **sccache**：Google Android官方采用（C/C++、Rust、CUDA），成为编译缓存事实标准
- **腾讯yadcc**：开源，定位"提高吞吐而非降低单文件编译耗时"
- **美团**：分享C++编译优化实践（分布式编译+PCH+ccache综合方案）
- **NativeLink**：与CMake集成方案受关注
- **Coralogix**：入局CI/CD可观测性

### 重要趋势信号
- **AI构建优化产品化爆发**（high）：微软IDE内置 vs IncrediBuild独立工具链，12个月内明朗
- **"CMake + RE服务"组合兴起**（high）：挑战"分布式编译必须绑定Bazel"认知，降低接入门槛
- **CI/CD构建加速升级为管理KPI**（high）：采购决策链延伸至高管，预算升级为基础设施投资
- **Bazel热度明确下降**（down）：讨论从"下一代"转向质疑，CMake低迁移成本优势凸显
- **国内大厂工具外输**（medium）：从使用者变提供者，加剧中小型企业市场竞争

### 值得长期跟踪
- **sccache vs ccache迁移**：Google背书效应扩散，多语言+云存储+分布式组合优势
- **腾讯yadcc社区运营**：GitHub Star、文档完善度、Issue响应速度
- **sccache与mold兼容性修复**：完善"编译缓存+高速链接"链路
- **RE服务+CMake生态**：企业采用案例、NativeLink社区活跃度
- **distcc实践数据**：10台机器112核，编译时间30分钟→8分半

### 竞品动态
- **微软**：MSVC Build Tools v14.52预览更新（C++模块、ARM64改进）
- **IncrediBuild**：从"编译加速工具"升级为"构建效能全栈平台"，内容营销密集
- **Google Pigweed**：Bazel为主构建系统，GN进入维护模式，CMake继续支持
- **ccache**：4.13.6版本，社区关注度平稳
- **Buck2**：Hacker News讨论提及与CMake集成问题