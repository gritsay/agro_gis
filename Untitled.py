import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *

QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.6", True)
qgs = QgsApplication([], False)
qgs.initQgis()

i = 1
os.chdir("C:/Users/SHIF3R/Documents/agro_gis/source")
for file in os.listdir():
    if file.endswith(".tif"):
        myRaster = QgsRasterLayer(file, str(i))
        myRaster.loadNamedStyle("123.qml")
        QgsProject.instance().addMapLayer(myRaster)
        vlayer = QgsProject.instance().mapLayersByName(str(i))[0]
        options = QgsMapSettings()
        options.setLayers([vlayer])
        options.setBackgroundColor(QColor(255, 255, 255))
        options.setOutputSize(QSize(800, 600))
        options.setExtent(vlayer.extent())
        render = QgsMapRendererParallelJob(options)
        def finished():
            img = render.renderedImage()
            img.save("result//" + str(i) + ".png", "png")
        render.finished.connect(finished)
        render.start()
        render.waitForFinished()
        i = i + 1
qgs.exitQgis()