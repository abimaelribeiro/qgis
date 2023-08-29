import time

layersList = ["Sentinel 2017-07","Sentinel 2018-07","Sentinel 2019-07","Sentinel 2020-07","Sentinel 2022-07"]
layersComponent = []
x = 0

root = QgsProject.instance().layerTreeRoot()
mapThemesCollection = QgsProject.instance().mapThemeCollection()
mapThemes = mapThemesCollection.mapThemes()


for item in layersList:
    layersComponent.append(QgsProject.instance().mapLayersByName(item)[0])
    QgsProject.instance().layerTreeRoot().findLayer(layersComponent[x]).setItemVisibilityChecked(True)
    iface.setActiveLayer(layersComponent[x])
    layersComponent[x]
    time.sleep(2)
    
    mapThemeRecord = mapThemesCollection.createThemeFromCurrentState(
        QgsProject.instance().layerTreeRoot(),
        iface.layerTreeView().layerTreeModel()
    )
    mapThemesCollection.insert(item, mapThemeRecord)
    
    x += 1
    QgsProject.instance().layerTreeRoot().findLayer(layersComponent[x-1]).setItemVisibilityChecked(False)