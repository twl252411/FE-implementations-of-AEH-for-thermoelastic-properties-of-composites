# AEH_UEL_Method

## English
This folder implements AEH with UEL (user element) workflows for:
- Elastic
- CTE
- ETC

### Current Script Structure
- PBC input generation:
  - `AEH_Inp_Periodic_BCs_Elastic_UEL.py`
  - `AEH_Inp_Periodic_BCs_CTE_UEL.py`
  - `AEH_Inp_Periodic_BCs_ETC_UEL.py`
- UEL input modification:
  - `UEL_Inp_Modification_Elastic_UEL.py`
  - `UEL_Inp_Modification_CTE_UEL.py`
  - `UEL_Inp_Modification_ETC_UEL.py`
- DAT processing:
  - `DatFile_Processing_Elastic_UEL.py`
  - `DatFile_Processing_CTE_UEL.py`
  - `DatFile_Processing_ETC_UEL.py`
- Final postprocessing:
  - `AEH_Postprocessing_Elastic_UEL.py`
  - `AEH_Postprocessing_CTE.py`
  - `AEH_Postprocessing_ETC_UEL.py`
- Shared utility module:
  - `pbc_matching_utils.py`
- User subroutines:
  - `UEL_LinearP_Elastic.for`
  - `UEL_Thermal_Expansion.for`
  - `UEL_Thermal_Conductivity.for`

### Refactor Status (Latest)
- `AEH_Inp_Periodic_BCs_CTE_UEL.py` and `AEH_Inp_Periodic_BCs_ETC_UEL.py`
  now call `build_periodic_set_lines(...)` from `pbc_matching_utils.py`.
- This reduces duplicated pairing code while preserving matching behavior.

### Workflow
1. Start from baseline `Job_woven{satin_num}_AEH1_{type}.inp`.
2. Generate PBC-enabled input (`..._1.inp`).
3. Convert to UEL-ready input (`..._2.inp`).
4. Run Abaqus with the corresponding `.for` subroutine -> produce `.dat`.
5. Process `.dat` -> `..._3.dat`.
6. Run final postprocessing scripts for homogenized outputs.

### Notes
- For CTE, run elastic chain first (stiffness dependency).
- Ensure Fortran compiler and Abaqus UEL toolchain are configured.
- ODB-related scripts must run in Abaqus Python environment.

## 简体中文
本目录提供 AEH + UEL 的完整流程，覆盖弹性、热膨胀、导热三类分析。

### 当前程序结构
- 周期边界输入生成脚本（Elastic/CTE/ETC）
- UEL 输入改写脚本
- DAT 解析脚本
- 最终后处理脚本
- 公共工具模块：`pbc_matching_utils.py`

### 最新重构说明
- `AEH_Inp_Periodic_BCs_CTE_UEL.py` 与 `AEH_Inp_Periodic_BCs_ETC_UEL.py`
  已统一调用 `build_periodic_set_lines(...)`。
- 改造目标是结构简化与去重，功能保持不变。

### 注意事项
- CTE 流程依赖弹性刚度结果，建议先运行弹性链路。
- 请确保 Fortran 编译器与 Abaqus UEL 环境已正确配置。
