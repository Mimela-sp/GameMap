import leafmap

image_url = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw_geo.tif"  # カスタムの画像URLを指定

leafmap.cog_validate(image_url)

out_cog = "/Users/mimela/Documents/Game/Naraka/Naraka_1_raw_cog.tif"
leafmap.image_to_cog(image_url, out_cog)