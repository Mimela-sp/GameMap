import streamlit as st
# import leafmap.foliumap as leafmap
from folium import TileLayer
import leafmap

# ファイルのアップロード
# file = st.file_uploader("GeoJSONファイルを選択してください", type=["json"])
file = ""
if file is not None:
    # LeafMapのMapオブジェクトを作成
    m = leafmap.Map()

    # GeoJSONファイルの読み込み
    # m.add_geojson(file.name, data=file)

    # カスタムの背景画像を追加
    # image_url = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw_cog.tif"  # カスタムの画像URLを指定
    # m.add_cog_layer(image_url, name='Untitled', attribution='.', opacity=1.0, shown=True, bands=3, titiler_endpoint=None)
    # m.add_raster(image_url, palette="terrain", layer_name="Local COG")
    # m.add_cog_layer(image_url, palette="gist_earth", name="Remote COG")
    # m.add_image(image_url, position=(0, 90))
    # leafmap.plot_raster(image_url,  figsize=(1092, 1091))
    # m.add_raster(image_url,  bands=[0], layer_name='test')
    # 地図の表示
    # m.to_streamlit()