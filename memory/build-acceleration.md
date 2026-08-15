# build-acceleration — Research Memory

最后更新: 2026-08-15

## 关键记忆点

### 公司/产品/项目
- **微软**：VS 2026 集成 Copilot AI 构建优化，接近完整支持 C++23，ARM64 ASan
- **IncrediBuild**：AI 沙箱 Islo，CI/CD 加速，定位转型为"构建效能全栈平台"
- **腾讯**：开源分布式编译系统 yadcc（国内大厂内部工具外输信号）
- **Google**：Android 官方采用 sccache 作为编译缓存工具
- **NativeLink**：RE 服务 + CMake 组合，可能颠覆分布式编译格局
- **sccache**（wasmerio）：确立主流编译缓存地位，支持 C/C++/Rust/CUDA + 云存储
- **ccache**：进入维护期（4.13.6），被 sccache 降维打击
- **Pigweed**：Bazel 设为主要构建系统，CMake 继续支持，GN 进入维护模式
- **美团**：C++ 编译优化实践（分布式编译、PCH、ccache）
- **FASTBuild**：分布式编译工具，热度有限

### 趋势信号
- **AI 驱动构建优化产品化**（up, high）：三大玩家同期布局，从概念进入交付
- **CI/CD 构建加速成为管理 KPI**（up, high）：采购决策链扩展至 VP/CTO 层级
- **RE 服务 + CMake 降低接入门槛**（up, medium）：从早期信号变为具体方案，最具颠覆性潜力
- **sccache 成为主流编译缓存**（up, high）：Google 背书是关键转折点，热度不再上升但地位确立
- **Bazel 热度下降，CMake 保持主流**（stable）：讨论从"下一代"转向质疑
- **分布式编译工具多样化**（new, medium）：腾讯 yadcc 开源，市场快速扩张期信号

### 长期跟踪方向
- **AI 构建优化两条路线竞争**：VS 内置（IDE 集成）vs IncrediBuild 独立工具链，12 个月内明朗
- **RE 服务 + CMake 实际落地案例**：是否真正降低中小团队接入门槛
- **sccache 与 mold 兼容性修复进展**：完善"编译缓存 + 高速链接"链路
- **腾讯 yadcc 能否在分布式编译市场占据一席之地**
- **构建加速作为业务指标**：IncrediBuild 教育市场将构建速度视为业务竞争力

### 竞品动态
- **IncrediBuild**：密集内容营销（3+ 份报告），面向管理层输出"构建速度 = 业务竞争力"叙事
- **腾讯 yadcc**：开源分布式编译，与 IncrediBuild 形成竞争
- **NativeLink + CMake**：挑战"分布式编译必须绑定 Bazel"的传统认知，威胁 IncrediBuild、华为云 CodeArts Build 等
- **sccache**：替代 distcc + ccache 组合，挤压 distcc 讨论空间