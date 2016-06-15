# ExtractAltiumSTEPModels
This is a Proof of Concept (PoC) on how we can extract the 3D components models from an Altium PCB Project file (.PcbDoc file)

The .PcbDoc is not more than a ZIP file we can extract normally how another common zlib file. After that, you can find many folders and one off this is the MODELS folder where we can found the STEP models but in a binary format.

With this little PoC python script, you can extract that binary data in a clear text format (ASCII STEP file) to import for example in FreeCAD.

In this little example you can see a 3D model for a LED component. The 0.dat file is the one Altium project has in the MODELS folder and the 0.step file contain the ASCII STEP format you can use in FreeCAD or another 3D software.
