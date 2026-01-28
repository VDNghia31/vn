import geopandas as gpd

# Đọc shapefile
shp_path = r"my_project/data/admin/Census2019_All_of_Vietnam.shp"
gdf = gpd.read_file(shp_path)

print("Các cột trong shapefile:")
print(list(gdf.columns))
print("\n3 dòng đầu tiên:")
print(gdf.head(3))
print(f"\nTổng số features: {len(gdf)}")
print(f"CRS: {gdf.crs}")
