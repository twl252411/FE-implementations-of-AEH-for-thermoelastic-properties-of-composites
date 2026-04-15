# Yarn_Properties

## English
This folder converts yarn/material parameters into Abaqus-ready text data
for elastic stiffness, CTE, and thermal conductivity.

Main script:
- `Yarn_Properties_For_Abaqus.py`

Typical outputs:
- `*_abaqus_elastic_stiff_*.txt`
- `*_abaqus_alpha_*.txt`
- `*_abaqus_kappa_*.txt`

Dependencies:
- `numpy`
- `scipy`
- `pytransform3d`

Usage:
```bash
python Yarn_Properties_For_Abaqus.py
```

## 简体中文
- 请参考英文部分。
- 保持文件命名一致。
