# Preprocessing_AEH_FEH

## English
This folder contains the unified preprocessing entry script:
- `Preprocessing_AEH_FEH.py`

It opens an existing RVE `.cae`, assigns materials/sections, creates analysis steps,
meshes the model, and exports analysis `.inp` files for FEH/AEH workflows.

Typical run (Abaqus environment):
```bash
abaqus cae noGUI=Preprocessing_AEH_FEH.py
```

Inputs usually include:
- RVE `.cae` from `RVE_Generation`
- Yarn/material text files from `Yarn_Properties` (woven/braided cases)

Notes:
- Keep `composite_type`, `analysis_type`, `job_name`, and referenced file names consistent.
- Ensure `periodic_meshes` module is available in the Abaqus Python path.

## 简体中文
- 请参考英文部分。
- 保持文件命名一致。
