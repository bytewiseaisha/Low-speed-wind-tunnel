# 3D Models

This directory contains the CAD models and fabrication files developed for the low-speed wind tunnel project. The models support the physical construction of the tunnel and preparation of its geometry for computational analysis.

## Directory Structure

```text
02. 3D Models/
├── README.md
├── contraction_diffuser/
│   ├── contraction_diffuser.f3d
│   ├── contraction_diffuser.step
│   └── contraction_diffuser.stl
├── test_section/
│   ├── test_section.f3d
│   └── test_section.step
└── fan_mount/
    ├── fan_mount.step
    └── fan_mount.stl
```

## 1. Contraction and Diffuser

**CAD software:** Autodesk Fusion 360  
**Fabrication:** 3D printing

The contraction and diffuser were designed together in Fusion 360 and fabricated through 3D printing. These sections form the transitions into and out of the wind tunnel test section.

Files:
- `.f3d` — Native Fusion 360 design file.
- `.step` — Neutral CAD exchange format for sharing solid geometry with other engineering software.
- `.stl` — Mesh geometry for 3D printing.

## 2. Test Section

**CAD software:** Autodesk Fusion 360  
**Physical construction:** Acrylic

The test-section geometry was modelled in Fusion 360 after Physical assembly using Acrylic. This was done to define its dimensions and interfaces with the adjacent tunnel sections and provide the geometry for the planned computational fluid dynamics (CFD) analysis.

Files:
- `.f3d` — Native Fusion 360 design file.
- `.step` — Neutral CAD geometry for interoperability and downstream engineering workflows.

## 3. Fan Mount

**CAD software:** Onshape  
**Fabrication:** 3D printing

The fan mount was designed in Onshape and fabricated through 3D printing.

Files:
- `.step` — Neutral CAD exchange format for sharing the solid geometry.
- `.stl` — Mesh geometry used for 3D printing.

## File Formats

The native CAD files preserve the designs in their original software, while STEP files support geometry exchange across CAD applications and STL files provide mesh geometry for fabrication.

