from osgeo import gdal
driver = gdal.GetDriverByName("GTiff")
dataset = gdal.Open("/Users/mimela/Documents/Game/Naraka/Naraka_1_raw.jpg")

out_path = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw.tif"
# データセットに座標系を設定
dataset.SetProjection("EPSG:4326")

dst_ds = gdal.Translate(out_path, dataset)