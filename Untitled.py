import qgis.core, os
i = 1
os.chdir('C:/Projects/qgis/source') #рабочая директория
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
            img.save("result//" + str(i) + ".png", "png") #сохраняет в папку result
        render.finished.connect(finished)
        render.start()
        render.waitForFinished()
        i = i + 1