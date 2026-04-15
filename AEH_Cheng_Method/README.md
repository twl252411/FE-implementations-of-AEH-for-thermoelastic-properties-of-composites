# AEH_Cheng_Method

## English
This folder implements the 3-stage Cheng scheme in the AEH framework for homogenizing:
- Elastic stiffness (`Elastic`)
- Coefficient of thermal expansion (`CTE`)
- Effective thermal conductivity (`ETC`)

Main script groups:
- Input preprocessing: `AEH_Inp_Preprocessing_*_Cheng_s1/s2/s3.py`
- Postprocessing: `AEH_Postprocessing_*_Cheng_s1/s2/s3.py`

Recommended workflow:
1. Prepare baseline `.inp` (elastic/cte/etc).
2. Run stage `s1` preprocessing -> Abaqus -> stage `s1` postprocessing.
3. Run stage `s2` preprocessing -> Abaqus -> stage `s2` postprocessing.
4. Run stage `s3` preprocessing -> Abaqus -> stage `s3` postprocessing.
5. Read final homogenized outputs in `.txt` files.

Notes:
- Keep `satin_num`, `job_name`, and file prefixes consistent across scripts.
- ODB-reading postprocessing scripts require Abaqus Python (`odbAccess`).
- CTE scripts depend on the stiffness output produced by the elastic chain.

## 简体中文
- 请参考英文部分。
- 保持文件命名一致。
- 需在 Abaqus Python 环境运行 ODB 后处理。
