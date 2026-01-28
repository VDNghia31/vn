"""
Script để tạo mastergrid từ shapefile Census2019_All_of_Vietnam.shp
"""
import geopandas as gpd
from pypoprf.utils.vector import rasterize

print("=" * 60)
print("Tạo mastergrid từ shapefile Census 2019")
print("=" * 60)

# Đường dẫn
shp_path = "my_project/data/admin/Census2019_All_of_Vietnam.shp"
output_path = "my_project/data/mastergrid_census2019.tif"
template_path = "my_project/data/VNM_covariate_2019/vnm_built_S_GHS_U_wFGW_100m_v1_2019.tif"

# Đọc shapefile
print(f"\n1. Đọc shapefile: {shp_path}")
gdf = gpd.read_file(shp_path)
print(f"   - Số lượng features: {len(gdf)}")
print(f"   - CRS: {gdf.crs}")
print(f"   - Sử dụng cột 'OBJECTID' làm giá trị zone")

# Rasterize với template
print(f"\n2. Rasterize shapefile thành mastergrid...")
print(f"   - Template: {template_path}")
print(f"   - Output: {output_path}")
print(f"   - Resolution: 100m")

rasterize(
    source=gdf,
    outfile=output_path,
    template=template_path,
    column='OBJECTID',
    dtype='int32',
    by_block=True,
    max_workers=4,
    show_progress=True,
    block_size=(512, 512)
)

print(f"\n✓ Hoàn thành! Mastergrid đã được tạo tại: {output_path}")
print("=" * 60)
