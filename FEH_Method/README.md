# FEH_Method

## English
This folder contains FEH workflows for:
- Elastic homogenization
- Thermal expansion homogenization (`CTE1`, `CTE2`)
- Thermal conductivity homogenization (`ETC`)

### Current Script Structure
- PBC input scripts:
  - `FEH_Inp_Periodic_BCs_Elastic.py`
  - `FEH_Inp_Periodic_BCs_CTE1.py`
  - `FEH_Inp_Periodic_BCs_CTE2.py`
  - `FEH_Inp_Periodic_BCs_ETC.py`
- Postprocessing scripts:
  - `FEH_Postprocessing_Elastic.py`
  - `FEH_Postprocessing_CTE1.py`
  - `FEH_Postprocessing_CTE2.py`
  - `FEH_Postprocessing_ETC.py`
- Shared utility module:
  - `pbc_matching_utils.py`

### Refactor Status (Latest)
- `FEH_Inp_Periodic_BCs_CTE1.py`, `FEH_Inp_Periodic_BCs_CTE2.py`, and `FEH_Inp_Periodic_BCs_ETC.py`
  now call `build_periodic_set_lines(...)` from `pbc_matching_utils.py`.
- This refactor removes duplicated node-pairing code while preserving behavior
  (tolerant matching + neighbor-bucket search + linear fallback).

### Recommended Workflow
1. Generate baseline FE input.
2. Run corresponding `FEH_Inp_Periodic_BCs_*.py`.
3. Run Abaqus analysis.
4. Run corresponding `FEH_Postprocessing_*.py`.

### Notes
- `CTE2` postprocessing depends on `Woven{satin_num}_Homogenized_Stiffness_FEH.txt`.
- Keep `satin_num`, `job_name`, and file prefixes consistent across scripts.
- ODB-based postprocessing must run in Abaqus Python environment.

## 简体中文
本目录提供 FEH 的三类均匀化流程：
- 弹性（Elastic）
- 热膨胀（CTE1，CTE2）
- 导热（ETC）

### 当前程序结构
- 周期边界输入脚本：
  - `FEH_Inp_Periodic_BCs_Elastic.py`
  - `FEH_Inp_Periodic_BCs_CTE1.py`
  - `FEH_Inp_Periodic_BCs_CTE2.py`
  - `FEH_Inp_Periodic_BCs_ETC.py`
- 后处理脚本：
  - `FEH_Postprocessing_Elastic.py`
  - `FEH_Postprocessing_CTE1.py`
  - `FEH_Postprocessing_CTE2.py`
  - `FEH_Postprocessing_ETC.py`
- 公共工具模块：
  - `pbc_matching_utils.py`

### 最新重构说明
- `CTE1/CTE2/ETC` 三个 PBC 输入脚本已统一调用
  `pbc_matching_utils.py` 中的 `build_periodic_set_lines(...)`。
- 该改造仅做结构简化与去重，不改变功能与匹配规则。

### 建议流程
1. 先生成基础输入文件。
2. 运行对应的 `FEH_Inp_Periodic_BCs_*.py`。
3. 用 Abaqus 求解。
4. 运行对应的 `FEH_Postprocessing_*.py`。

### 注意事项
- `CTE2` 后处理依赖弹性刚度结果文件。
- `satin_num`、`job_name`、文件前缀必须全流程一致。
- 读取 ODB 的后处理脚本需在 Abaqus Python 环境执行。
