[![Latest release](https://img.shields.io/github/v/release/MeshInspector/MeshInspector?label=latest%20release)](https://meshinspector.com/download/)
[![Platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20Web-blue)](https://meshinspector.com/download/)

# MeshInspector — Scan to Mesh. Mesh to Production.

**STL editor, viewer and mesh repair application for 3D scans and 3D printing.** Prepare watertight, print-ready models with defined tolerances and QA reports, handle 50M+ point clouds without stalling, and drive the whole thing from Python or an AI agent.

[**Get started for free →**](https://app.meshinspector.com/sign-up) · [**Download for Windows / macOS / Linux**](https://meshinspector.com/download/) · [Website](https://meshinspector.com/) · [Features](https://meshinspector.com/features/) · [Knowledge base](https://meshinspector.com/knowledge-base/) · [Report an issue](https://MeshInspector.github.io/ReportIssue/)

> **Get MeshInspector from [meshinspector.com/download](https://meshinspector.com/download/)** — installers for Windows, macOS and Linux. Or skip installing entirely and [open the web app](https://app.meshinspector.com/sign-up).

![MeshInspector — STL editor and mesh repair application](https://user-images.githubusercontent.com/3136125/153055383-a86e9e4f-f260-476c-af5e-c5e28e7a1632.png)

## What you can do with it

- **Repair broken meshes.** Fill holes, remove self-intersections and degeneracies, and make models watertight and printable — the `Mesh Healer` tools, including one-click `Auto Repair Mesh`. ([2-minute walkthrough](https://www.youtube.com/watch?v=9TykB8fzmoE))
- **Edit STL files.** Cut, select, transform, subtract and combine geometry with `Mesh Boolean` — without converting to another format first.
- **Turn 3D scans into printable models.** Triangulate point clouds, clean scanner noise with `Reduce Noise`, and export a manifold, watertight mesh ready for slicing and 3D printing.
- **Prove the result is correct.** `Surface Deviation` for scan-vs-reference comparison, `Measure Thickness`, `Measure Distance`, `Measure Angle`, `Collision Detection`, and a one-click `Quality Control Report` — measurable proof instead of a visual eyeball check.
- **Work at scale.** 10–50M+ triangle meshes, 50–100M+ point clouds and large CBCT datasets, with hardware-accelerated picking and order-independent transparency.
- **Open and convert formats.** Meshes (STL, OBJ, PLY, 3MF, GLTF, CTM, OFF, DXF), point clouds (E57, LAS/LAZ, ASC, PTS, XYZ), CT volumes (DICOM, TIFF, VDB) and polylines — plus CAD (STEP/STP) and G-code (GCODE/NC) **import**, converted to mesh on load. [Full format table, with import/export per format](https://meshinspector.com/knowledge-base/import-export/supported-file-formats/).

## Automate it — including with AI agents

Batch repetitive work with in-app Python, or let an AI agent drive MeshInspector over **MCP**. It works with Claude Code, Claude Desktop, Cursor, GitHub Copilot, Windsurf, Cline, OpenAI Codex, Gemini CLI and any MCP-compatible assistant.

- [MCP configuration instructions](https://meshinspector.com/knowledge-base/automation/mcp-configuration-instruction-for-meshinspector-users/)
- [Controlling the UI with Python](https://meshinspector.com/knowledge-base/automation/how-to-start-using-python-in-meshinspector/)
- [Advanced automation with MeshInspector and MeshLib](https://meshinspector.com/knowledge-base/automation/advanced-automation-with-meshinspector-and-meshlib/)

## Where it is used

3D printing and additive manufacturing · scan-to-print workflows · digital dentistry · medical imaging and surgical planning · metrology and quality inspection · GIS and BIM as-built modelling.

> *"It's the fastest program I've used so far, and I can now do 150 scans in just 2 days instead of 1.5 weeks."*
> — Susteni AS

## Run it anywhere

| | |
|---|---|
| **Web** | [app.meshinspector.com](https://app.meshinspector.com/sign-up) — the full application in a browser tab, nothing to install. |
| **Desktop** | Windows, macOS and Linux (Ubuntu/Debian, Fedora/RHEL) — [download from meshinspector.com](https://meshinspector.com/download/). |
| **Scripted** | Embedded Python for batch jobs, plus MCP for agent-driven workflows. |

## Built on MeshLib

MeshInspector is powered by [**MeshLib**](https://github.com/MeshInspector/MeshLib), our 3D mesh and point cloud processing SDK. Everything in this UI is available as an API for C++, C, C#, Python and JavaScript — so a workflow you prototype here can ship inside your own product.

Building an application rather than looking for one? Start at [meshlib.io](https://meshlib.io/) or try the [live SDK demo](https://demo.meshlib.io).

## Feedback and support

- **Bugs and feature requests** → [Report an issue](https://MeshInspector.github.io/ReportIssue/)
- **Questions, pricing and licensing** → [meshinspector.com](https://meshinspector.com/)
