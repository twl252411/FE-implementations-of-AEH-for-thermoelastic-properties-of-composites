FEH_Method (English / 简体中文)

[English]
General FEH workflow:
1) Generate baseline FE input.
2) Run FEH_Inp_Periodic_BCs_Type.py (Type = Elastic/ETC/CTE1/CTE2).
3) Run Abaqus FE analysis.
4) Run FEH_Postprocessing_Type.py.

Latest structure update:
- CTE1/CTE2/ETC PBC scripts now share `pbc_matching_utils.py`
  via `build_periodic_set_lines(...)`.
- Refactor goal: simplify structure and remove duplication without changing behavior.

[简体中文]
FEH 通用流程：
1）生成基础有限元输入。
2）运行 FEH_Inp_Periodic_BCs_Type.py（Type = Elastic/ETC/CTE1/CTE2）。
3）运行 Abaqus 有限元求解。
4）运行 FEH_Postprocessing_Type.py。

最新结构更新：
- CTE1/CTE2/ETC 的 PBC 脚本已统一调用 `pbc_matching_utils.py`。
- 重构目标：简化结构、减少重复，同时保持功能不变。
