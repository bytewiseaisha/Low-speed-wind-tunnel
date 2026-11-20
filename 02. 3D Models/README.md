# 02. 3D Models

CAD models of the wind tunnel, designed in Autodesk Fusion.

## Files

| Path | Description |
|---|---|
| `Contraction_Diffuser/Tunnel Model.f3d` | Fusion source file: contraction, diffuser and construction planes |
| `Contraction_Diffuser/Tunnel Model.step` | Neutral CAD format |
| `Contraction_Diffuser/Tunnel Model.stl` | Mesh for 3D printing |
| `Fan Mount/Fan Mount.step` | Fan mount, neutral CAD format |
| `Fan Mount/Fan Mount.stl` | Fan mount, mesh for 3D printing |
| `Renders/` | Images of the components and the full tunnel |

## Components

| Component | Description | Manufacture |
|---|---|---|
| Contraction | Cosine wall profile, 125 mm → 95 mm square, 234.247 mm long | 3D printed (PETG), split into two parts |
| Diffuser | Cosine wall profile, 95 mm → 125 mm square, 233.928 mm long | 3D printed (PETG), split into two parts |
| Fan mount | Square frame holding the axial fan at the contraction inlet | 3D printed (PETG) |
| Test section | 95 × 95 × 310 mm bore, 4 mm walls | Hand-cut 4 mm cast acrylic (not modelled before assembly) |
| CFD test section | 92 × 92 × 376.667 mm, modelled later for the CFD only | Not manufactured |

Construction planes in the model mark the start and end of the test section, so the printed parts line up with it.

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
| Contraction ratio | 1.738 | 1.8535 |

This mismatch changes the CFD results by about 25% relative to a model of the physical tunnel. To keep the verification fair, the analytical model was also run on the CFD geometry (see `01. analytical-model`).

## Air block

For the CFD, the tunnel's internal volume was extracted in Fusion as a single solid (`Body4`) and exported as a STEP file. See `03. CFD Model/Wind Tunnel Air Block.step`.
