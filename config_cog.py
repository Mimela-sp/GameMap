from osgeo import gdal

# ファイルパスを指定
file_path = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw_cog.tif"

# ファイルを開く
dataset = gdal.Open(file_path, gdal.GA_Update)

# バンド数を取得
band_count = dataset.RasterCount

# バンドごとにメタデータを追加
for i in range(band_count):
    band = dataset.GetRasterBand(i + 1)
    band.SetMetadata({'description': 'band ' + str(i + 1)})