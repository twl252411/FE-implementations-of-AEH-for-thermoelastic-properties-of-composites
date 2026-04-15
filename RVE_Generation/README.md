# RVE_Generation

## English
This folder generates composite RVE geometry models (`.cae`) for downstream FEH/AEH analysis.

Main scripts:
- `RVE_Particle_Composites.py`
- `RVE_Fiber_Composites.py`
- `RVE_Twill_Weave_Composites.py`
- `RVE_Braided_4D_Composites_Interior_Cell.py`
- `RVE_Braided_5D_Composites_Interior_Cell.py`

Supporting inputs:
- `points3d_particle.txt`
- `points3d_fiber.txt`
- `angles3d_fiber.txt`

Typical run:
```bash
abaqus cae noGUI=RVE_Twill_Weave_Composites.py
```

Notes:
- Verify point/angle file formats and units before running.
- Some scripts may need manual parameter checks for specific model branches.

## 简体中文
- 请参考英文部分。
- 保持文件命名一致。
