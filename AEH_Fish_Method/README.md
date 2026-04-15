# AEH_Fish_Method

## English
This folder contains the Fish-scheme AEH workflow (currently focused on elastic homogenization).

Key files:
- `AEH_Inp_Periodic_BCs_Elastic_Fish.py`: builds periodic boundary-condition node sets and equations.
- `AEH_Postprocessing_Elastic_Fish.py`: extracts ODB results and computes homogenized stiffness.
- `UEXPAN.for`: optional Abaqus user subroutine example.

Workflow:
1. Prepare baseline input: `Job_woven{satin_num}_AEH2_elastic.inp`.
2. Run `AEH_Inp_Periodic_BCs_Elastic_Fish.py` -> generate `..._1.inp`.
3. Run Abaqus on `..._1.inp`.
4. Run `AEH_Postprocessing_Elastic_Fish.py`.
5. Read `Woven{satin_num}_Homogenized_Stiffness_AEH2.txt`.

Notes:
- Match script parameters and file prefixes before running.
- Postprocessing requires Abaqus Python environment.

## 简体中文
- 请参考英文部分。
- 保持文件命名一致。
