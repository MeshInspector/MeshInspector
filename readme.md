# MeshInspector releases

This repository holds public MeshInspector releases.

MeshInspector is an application for geometry processing based on [MeshLib](https://github.com/MeshInspector/MeshLib). 
Find more in [Slides](https://docs.google.com/presentation/d/1D0Ry6SE2J25PBtO_G9ZIp1cavoX2wyyY8jgvtjeayC4/edit?usp=sharing).

![image](https://user-images.githubusercontent.com/3136125/153055383-a86e9e4f-f260-476c-af5e-c5e28e7a1632.png)

[Check out web version of MeshInspector](https://demo.meshinspector.com/)
> This is still in work, tested on Chrome and Firefox browsers

[Report an issue anonymously](https://MeshInspector.github.io/ReportIssue/)

### Technology
 - OpenGL v4 by default, v3 for a compatibility
### Performance
 - Fast drawing up to 20+M triangles,
 - Hardware-accelerated object picker (finding triangle or point under the cursor).
### Viewport camera modes
 - Perspective and Orthographic,
 - Renderable objects
   - Cloud points,
   - Meshes,
   - Lines,
   - Voxels
   - DistanceMaps
### Color and textures 
 - Vertices color map,
 - Triangles color map,
 - Static textures.
### Order independed transparency

Perfect and fast visualization of many transparent objects with complex geometry using OpenGL 4:
![image](https://user-images.githubusercontent.com/3136125/168789144-ee83ca11-4ca1-4dd0-97fc-e138500d9b10.png)

### Convenient for mesh algorithms debugging, showing mesh edges, boundaries
### Computed-tomography reconstruction
An ability to reconstruct voxel object from a set of projection images (radiographs) and known cone-beam CT scanner geometry parameters. Nvidia GPU is utilized via CUDA technology for the best reconstruction performance.
