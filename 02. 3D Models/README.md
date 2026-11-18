# 02. 3D Models

CAD models of the wind tunnel, designed in Autodesk Fusion.

## Components

| Component | Description | Manufacture |
|---|---|---|
| Contraction | Smooth wall profile, 125 mm → 95 mm square, 234.2 mm long | 3D printed (PETG), split into two parts |
| Diffuser | Smooth wall profile, 95 mm → 125 mm square, 233.9 mm long | 3D printed (PETG), split into two parts |
| Fan mount | Square frame holding the axial fan at the contraction inlet | 3D printed (PETG) |
| Test section | 95 × 95 × 310 mm bore, 4 mm walls | Hand-cut 4 mm cast acrylic (not modelled before assembly) |
| CFD test section | 92 × 92 × 376.7 mm, modelled later for the CFD only | Not manufactured |

## Printing

| Setting | Value |
|---|---|
| Printer | Flashforge Adventurer 5M Pro |
| Material | Creality CR-PETG, 1.75 mm, black |
| Nozzle / bed temperature | 245 °C / 80 °C |
| Nozzle diameter | 0.6 mm |

The contraction and diffuser were too large for the build plate, so each was split in the slicer and the halves bonded after printing.

## Note on the test section

The physical test section was assembled by hand from acrylic before any CAD model of it existed. The test section in the CFD model was drawn afterwards and differs slightly in size:

| | Physical | CFD model |
|---|---|---|
| Inner bore | 95 × 95 mm | 92 × 92 mm |
| Outer size | 103 × 103 mm | 100 × 100 mm |
| Length | 310 mm | 376.667 mm |
| Contraction ratio | 1.738 | 1.853 |

This mismatch is one of the sources of difference discussed in the comparison.

## Air block

For the CFD, the tunnel's internal volume was extracted in Fusion as a single solid (`Body4`) and exported as a STEP file. See `03. CFD Model/wind_tunnel_air_block.step`.
