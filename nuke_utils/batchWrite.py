import os
import nuke
for n in nuke.selectedNodes():
    path = n['file'].getValue().replace('\\', '/')
    baseName = os.path.splitext(os.path.basename(path))[0]
    dirName = os.path.dirname(path)
    outName = os.path.join(dirName, f'{baseName}.png').replace('\\', '/')
    node = nuke.nodes.Write(file=outName, inputs=[n])
    nuke.execute(node, 1, 1)
