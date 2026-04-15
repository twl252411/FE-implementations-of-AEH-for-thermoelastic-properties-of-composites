# FE Implementations of AEH for Thermoelastic Properties of Composites

## English

### Overview
This repository provides finite-element implementations for homogenizing thermo-mechanical properties of composite materials under a unified AEH/FEH-oriented workflow. It includes geometry generation, material preprocessing, periodic boundary condition (PBC) input construction, UEL-based and non-UEL-based homogenization pipelines, and postprocessing scripts.

Target effective properties include:
- Elastic stiffness
- Coefficient of thermal expansion (CTE)
- Thermal conductivity (ETC)

### Repository Structure
- `RVE_Generation/`: Build representative volume element (RVE) geometry models.
- `Yarn_Properties/`: Convert yarn/material parameters into Abaqus-ready data files.
- `Preprocessing_AEH_FEH/`: Unified preprocessing of `.cae` models and export of analysis `.inp` files.
- `FEH_Method/`: FEH workflows for Elastic, CTE1/CTE2, and ETC.
- `AEH_UEL_Method/`: AEH workflows based on UEL, including input modification and DAT processing.
- `AEH_Fish_Method/`: AEH Fish-scheme scripts (mainly elastic case).
- `AEH_Cheng_Method/`: AEH Cheng 3-stage workflows for elastic/CTE/ETC.

Each folder contains its own bilingual README for detailed per-script usage.

### Recommended End-to-End Workflow
1. Prepare material/yarn property files in `Yarn_Properties/`.
2. Generate an RVE model in `RVE_Generation/`.
3. Run `Preprocessing_AEH_FEH/Preprocessing_AEH_FEH.py` to export baseline `.inp` files.
4. Choose one homogenization route:
- FEH route: run scripts in `FEH_Method/`.
- AEH UEL route: run scripts in `AEH_UEL_Method/`.
- AEH Fish / Cheng routes: run scripts in corresponding folders.
5. Run Abaqus jobs for generated `.inp` files.
6. Run corresponding postprocessing scripts to obtain homogenized outputs (`.txt`).

### Environment
- Abaqus Python environment for preprocessing and ODB-related postprocessing.
- Anaconda/Conda environment is recommended for standalone syntax checks and Python dependency management.
- Common dependencies in script subsets include `numpy`, `scipy`, and `pytransform3d`.

### Current Refactor Notes (Behavior-Preserving)
To reduce duplication and improve maintainability, repeated periodic-node matching logic has been extracted into shared helper modules:
- `FEH_Method/pbc_matching_utils.py`
- `AEH_UEL_Method/pbc_matching_utils.py`

CTE/ETC-related scripts in these folders now call `build_periodic_set_lines(...)` while preserving original behavior.

### Typical Outputs
Depending on the selected workflow, outputs include:
- Modified Abaqus input files (`*_1.inp`, etc.)
- Homogenized property reports (`Woven*_Homogenized_*.txt`)
- Intermediate UEL/DAT processing artifacts (UEL pipeline)

## 中文（简体）

### 项目概述
本仓库提供复合材料热-力学等效性质的有限元实现，围绕 AEH/FEH 的统一思路组织，覆盖几何建模、材料预处理、周期边界条件（PBC）构建、UEL 与非 UEL 流程以及后处理。

支持的等效性质主要包括：
- 等效弹性刚度
- 线膨胀系数（CTE）
- 等效导热系数（ETC）

### 仓库结构
- `RVE_Generation/`：生成代表体元（RVE）几何模型。
- `Yarn_Properties/`：将纱线/材料参数转换为 Abaqus 可用数据文件。
- `Preprocessing_AEH_FEH/`：统一处理 `.cae` 并导出分析用 `.inp`。
- `FEH_Method/`：FEH 路线（Elastic、CTE1/CTE2、ETC）。
- `AEH_UEL_Method/`：基于 UEL 的 AEH 路线（含输入修改与 DAT 处理）。
- `AEH_Fish_Method/`：AEH Fish 方案脚本（当前以弹性为主）。
- `AEH_Cheng_Method/`：AEH Cheng 三阶段流程（elastic/CTE/ETC）。

各子目录均提供双语 README，说明该目录内脚本的详细用法。

### 推荐完整流程
1. 在 `Yarn_Properties/` 准备材料/纱线参数文件。
2. 在 `RVE_Generation/` 生成 RVE 几何模型。
3. 运行 `Preprocessing_AEH_FEH/Preprocessing_AEH_FEH.py` 导出基础 `.inp`。
4. 选择一种等效化路线：
- FEH：运行 `FEH_Method/` 下脚本。
- AEH UEL：运行 `AEH_UEL_Method/` 下脚本。
- AEH Fish / Cheng：运行对应目录脚本。
5. 在 Abaqus 中执行生成的 `.inp` 任务。
6. 运行对应后处理脚本，得到等效性质结果（`.txt`）。

### 运行环境
- 预处理与 ODB 后处理建议在 Abaqus Python 环境执行。
- 建议使用 Anaconda/Conda 进行独立语法检查和依赖管理。
- 相关脚本常见依赖包括 `numpy`、`scipy`、`pytransform3d`。

### 当前重构说明（功能保持不变）
为减少重复代码并降低维护成本，周期节点匹配逻辑已抽取为共享模块：
- `FEH_Method/pbc_matching_utils.py`
- `AEH_UEL_Method/pbc_matching_utils.py`

上述目录下 CTE/ETC 同类脚本已统一调用 `build_periodic_set_lines(...)`，并保持原有行为一致。

### 常见输出
根据所选流程，典型输出包括：
- 修改后的 Abaqus 输入文件（`*_1.inp` 等）
- 等效性质结果文件（`Woven*_Homogenized_*.txt`）
- UEL 流程中的中间 DAT/修改文件

## Citation / 引用
If this program is helpful to your research, please cite the following paper:

如果本程序对您的研究有帮助，请引用下述论文：

Wenlong Tian, Xujiang Chao, Lehua Qi, *Finite element implementations of asymptotic expansion homogenization for thermo-mechanical composites: unified formulation and discrete consistency*, Review of Materials Research, 2026, Revision.
