from osgeo import gdal, osr
driver = gdal.GetDriverByName("GTiff")
dataset = gdal.Open("/Users/mimela/Documents/Game/Naraka/Naraka_1_raw.jpg")

out_path = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw.tif"
# データセットに座標系を設定
dataset.SetProjection("EPSG:4326")

# 空間情報を作成する
srs = osr.SpatialReference()

srs.ImportFromEPSG(4326)  # 例えば、WGS 84のEPSGコードを指定

# 座標範囲を定義する
geo_transform = [90, xres, 0, ymax, 0, -yres]  # 例えば、xmin, xmax, ymin, ymax, xres, yresを指定

# GeoTIFFファイルに変換する
dst_ds = gdal.Translate(out_path, dataset, format='GTiff', outputSRS=srs, outputBounds=geo_transform)
