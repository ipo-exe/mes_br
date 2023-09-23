from osgeo import gdal
import geopandas as gpd
import pandas as pd
import numpy as np
import processing
import shutil
import os

# -----------------------------------------------------------------------------
# FUNCTIONS

def get_blank_raster(file_input, file_output, blank_value=0):
    """
    get a blank raster copy from other raster
    :param file_input: path to input raster file
    :type file_input: str
    :param file_output: path to output raster file
    :type file_output: str
    :param blank_value: value for constant blank raster
    :type blank_value: int
    :return: none
    :rtype:
    """
    # -------------------------------------------------------------------------
    # LOAD

    # Open the raster file using gdal
    raster_input = gdal.Open(file_input)

    # Get the raster band
    band_input = raster_input.GetRasterBand(1)

    # Read the raster data as a numpy array
    grid_input = band_input.ReadAsArray()

    # truncate to byte integer
    grid_input = grid_input.astype(np.uint8)

    # -- Collect useful metadata

    raster_x_size = raster_input.RasterXSize
    raster_y_size = raster_input.RasterYSize
    raster_projection = raster_input.GetProjection()
    raster_geotransform = raster_input.GetGeoTransform()

    # -- Close the raster
    raster_input = None

    # -------------------------------------------------------------------------
    # PROCESS
    grid_output = grid_input * blank_value

    # -------------------------------------------------------------------------
    # EXPORT RASTER FILE
    # Get the driver to create the new raster
    driver = gdal.GetDriverByName('GTiff')

    # Create a new raster with the same dimensions as the original
    raster_output = driver.Create(
        file_output,
        raster_x_size,
        raster_y_size,
        1,
        gdal.GDT_Byte
    )

    # Set the projection and geotransform of the new raster to match the original
    raster_output.SetProjection(raster_projection)
    raster_output.SetGeoTransform(raster_geotransform)

    # Write the new data to the new raster
    raster_output.GetRasterBand(1).WriteArray(grid_output)

    # Close
    raster_output = None


def get_lulc_hq(file_mapbiomas, file_osm, file_biomes, file_table, file_style, output_folder, output_name="lulc_hq"):
    # -------------------------------------------------------------------------
    # LOAD TABLE

    df_table = pd.read_csv(file_table, sep=",")


    # -------------------------------------------------------------------------
    # LOAD MAPBIOMAS

    # Open the raster file using gdal
    raster_mapbiomas = gdal.Open(file_mapbiomas)

    # Get the raster band
    band_mapbiomas = raster_mapbiomas.GetRasterBand(1)

    # Read the raster data as a numpy array
    grid_mapbiomas = band_mapbiomas.ReadAsArray()

    # truncate to byte integer
    grid_mapbiomas = grid_mapbiomas.astype(np.uint8)

    # -- Collect useful metadata

    raster_x_size = raster_mapbiomas.RasterXSize
    raster_y_size = raster_mapbiomas.RasterYSize
    raster_projection = raster_mapbiomas.GetProjection()
    raster_geotransform = raster_mapbiomas.GetGeoTransform()

    # -- Close the raster
    raster_mapbiomas = None

    del band_mapbiomas
    # -------------------------------------------------------------------------
    # LOAD OSM
    # Open the raster file using gdal
    raster_osm = gdal.Open(file_osm)

    # Get the raster band
    band_osm = raster_osm.GetRasterBand(1)

    # Read the raster data as a numpy array
    grid_osm = band_osm.ReadAsArray()

    # truncate to byte integer
    grid_osm = grid_osm.astype(np.uint8)

    # -- Close the raster
    raster_osm = None

    del band_osm

    # -------------------------------------------------------------------------
    # LOAD BIOMES
    # Open the raster file using gdal
    raster_biomes = gdal.Open(file_biomes)

    # Get the raster band
    band_biomes = raster_biomes.GetRasterBand(1)

    # Read the raster data as a numpy array
    grid_biomes = band_biomes.ReadAsArray()

    # truncate to byte integer
    grid_biomes = grid_biomes.astype(np.uint8)

    # -- Close the raster
    raster_biomes = None

    del band_biomes

    # -------------------------------------------------------------------------
    # PROCESS
    grid_output = grid_mapbiomas

    # -------------------------------------------------------------------------
    # EXPORT RASTER FILE
    # Get the driver to create the new raster
    driver = gdal.GetDriverByName('GTiff')

    # Create a new raster with the same dimensions as the original
    raster_output = driver.Create(
        file_output,
        raster_x_size,
        raster_y_size,
        1,
        gdal.GDT_Byte
    )

    # Set the projection and geotransform of the new raster to match the original
    raster_output.SetProjection(raster_projection)
    raster_output.SetGeoTransform(raster_geotransform)

    # Write the new data to the new raster
    raster_output.GetRasterBand(1).WriteArray(grid_output)

    # Close
    raster_output = None


    print("hi")
# -----------------------------------------------------------------------------
# SET DATASETS FILEPATHS

# output dir
s_root = "C:/gis/_projects_/invest_br"

# mes geopackage dataset
s_file_db = "C:/Users/Ipo/PycharmProjects/mes_br/mes_br_db.gpkg"

# styles files
s_file_qml_biomes = "C:/Users/Ipo/PycharmProjects/mes_br/biomes.qml"
s_file_qml_osm = "C:/Users/Ipo/PycharmProjects/mes_br/osm.qml"

# osm geopackage
s_file_osm = "C:/gis/osm/osm_br_2022/osm_br_2022.gpkg"

# mapbiomas dataset
s_folder_mapbiomas = "C:/gis/mapbiomas/Mapbiomas_landsat_30m/collection_08"
s_file_style_mapbiomas = "C:/gis/mapbiomas/Mapbiomas_landsat_30m/style_c8.qml"


# -----------------------------------------------------------------------------
# SET PARAMETERS
# set grid size
grid_deg = 2

# set tiles ids
lst_tile_ids = [271]

# set lulc years
lst_years = [2020, 2021, 2022]

# create folder
s_folder_grid = "{}/grid_{}deg".format(s_root, grid_deg)
if os.path.exists(s_folder_grid):
    pass
else:
    os.mkdir(s_folder_grid)

# read the tiles dataset
gdf_tiles = gpd.read_file(s_file_db, layer="grid_br_{}deg".format(grid_deg))
# Filter the DataFrame based on the 'id' column
gdf_tiles = gdf_tiles[gdf_tiles['id'].isin(lst_tile_ids)]

# -----------------------------------------------------------------------------
# AUX VARIABLES
# define projections
dct_projs = {
    'UTM 18N': 'EPSG:31972, SIRGAS 2000 / UTM zone 18N',
    'UTM 19N': 'EPSG:31973, SIRGAS 2000 / UTM zone 19N',
    'UTM 20N': 'EPSG:31974, SIRGAS 2000 / UTM zone 20N',
    'UTM 21N': 'EPSG:31975, SIRGAS 2000 / UTM zone 21N',
    'UTM 22N': 'EPSG:31976, SIRGAS 2000 / UTM zone 22N',
    'UTM 18S': 'EPSG:31978, SIRGAS 2000 / UTM zone 18S',
    'UTM 19S': 'EPSG:31979, SIRGAS 2000 / UTM zone 19S',
    'UTM 20S': 'EPSG:31980, SIRGAS 2000 / UTM zone 20S',
    'UTM 21S': 'EPSG:31981, SIRGAS 2000 / UTM zone 21S',
    'UTM 22S': 'EPSG:31982, SIRGAS 2000 / UTM zone 22S',
    'UTM 23S': 'EPSG:31983, SIRGAS 2000 / UTM zone 23S',
    'UTM 24S': 'EPSG:31984, SIRGAS 2000 / UTM zone 24S',
    'UTM 25S': 'EPSG:31985, SIRGAS 2000 / UTM zone 25S',
}
dct_hem = {
    "S": "south",
    "N": "north"
}

# -----------------------------------------------------------------------------
# loop in all tiles
for i in range(len(gdf_tiles)):
    # get tile id
    tile_id = gdf_tiles["id"].values[i]

    # -------------------------------------------------------------------------
    # run tile

    print("\n\n>>> tile {}".format(tile_id))

    # create folder
    s_folder_tile = "{}/tile_{}".format(s_folder_grid, tile_id)
    if os.path.exists(s_folder_tile):
        pass
    else:
        os.mkdir(s_folder_tile)

    # -------------------------------------------------------------------------
    # GET TILE ATTRIBUTES
    # get list of regions
    lst_grid_regioes = gdf_tiles["regiao"].values[i].split(",")

    # get window projection
    tile_proj = dct_projs[gdf_tiles["Fuso UTM"].values[i]]
    tile_zone = tile_proj[-3:-1]
    tile_hem = dct_hem[tile_proj[-1:]]

    # get extent
    min_x = gdf_tiles['left'].values[i]  # -39.85121,
    max_y = gdf_tiles['top'].values[i]  # -14.36413
    max_x = gdf_tiles['right'].values[i]  # -39.19078,
    min_y = gdf_tiles['bottom'].values[i]  # -15.03517
    grid_extent = '{},{},{},{} [EPSG:4326]'.format(min_x, max_x, min_y, max_y)

    # -------------------------------------------------------------------------
    # GET VECTORS
    print(">>> tile {} :: processing vectors...".format(tile_id))
    # set lists
    lst_latlong_layers = list()

    s_file_vectors_db = '{}/vectors.gpkg'.format(s_folder_tile)

    # biomes
    print(">>> tile {} ::  vector --biomes".format(tile_id))
    s_layer = "biomes_latlong"
    lst_latlong_layers.append(s_layer)
    # clip by extent
    processing.run(
        "native:extractbyextent",
        {
            'INPUT': '{}|layername=biomas'.format(s_file_db),
            'EXTENT': grid_extent,
            'CLIP': True,
            'OUTPUT': 'ogr:dbname=\'{}\' table="{}" (geom)'.format(s_file_vectors_db, s_layer)
        }
    )

    # get all regions osm
    for region in lst_grid_regioes:
        print(">>> tile {} ::  vector --osm at {}".format(tile_id, region))
        # roads
        s_layer = "osm_roads_{}_latlong".format(region)
        lst_latlong_layers.append(s_layer)

        # clip by extent
        processing.run(
            "native:extractbyextent",
            {
                'INPUT': '{}|layername=gis_osm_roads_free_1_{}'.format(s_file_osm, region),
                'EXTENT': grid_extent,
                'CLIP': True,
                'OUTPUT': 'ogr:dbname=\'{}\' table="{}" (geom)'.format(s_file_vectors_db, s_layer)
            }
        )

        # railways
        s_layer = "osm_rails_{}_latlong".format(region)
        lst_latlong_layers.append(s_layer)
        # clip by extent
        processing.run(
            "native:extractbyextent",
            {
                'INPUT': '{}|layername=gis_osm_railways_free_1_{}'.format(s_file_osm, region),
                'EXTENT': grid_extent,
                'CLIP': True,
                'OUTPUT': 'ogr:dbname=\'{}\' table="{}" (geom)'.format(s_file_vectors_db, s_layer)
            }
        )

    lst_osm_layers = list()
    # reproject all latlong layers to UTM
    for lyr in lst_latlong_layers:
        new_lyr = lyr[:-8] + "_utm"
        if "osm" in new_lyr:
            lst_osm_layers.append(new_lyr)
        # reproject
        processing.run(
            "native:reprojectlayer",
            {
                'INPUT': '{}|layername={}'.format(s_file_vectors_db, lyr),
                'TARGET_CRS': QgsCoordinateReferenceSystem(tile_proj.split(",")[0]),
                'OPERATION': '+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=utm +zone={} +{} +ellps=GRS80'.format(tile_zone, tile_hem),
                'OUTPUT': 'ogr:dbname=\'{}\' table="{}" (geom)'.format(s_file_vectors_db, new_lyr)
            }
        )

    # -------------------------------------------------------------------------
    # RUN YEARS
    print(">>> tile {} :: processing rasters...".format(tile_id))
    for year in lst_years:
        print(">>> tile {} :: raster --year {}".format(tile_id, year))

        # ---------------------------------------------------------------------
        # create folder
        s_folder_year = "{}/lulc_{}".format(s_folder_tile, year)
        if os.path.exists(s_folder_year):
            pass
        else:
            os.mkdir(s_folder_year)

        # ---------------------------------------------------------------------
        # clip and warp mapbiomas
        s_file_mapbiomas = "{}/brasil_coverage_{}.tif".format(s_folder_mapbiomas, year)
        s_file_mapbiomas_output_name = "{}/mapbiomas".format(s_folder_year)

        # copy style file
        shutil.copy(s_file_style_mapbiomas, s_file_mapbiomas_output_name + ".qml")

        # run warp
        s_file_mapbiomas_output = s_file_mapbiomas_output_name + ".tif"
        processing.run(
            "gdal:warpreproject",
            {
                'INPUT': s_file_mapbiomas,
                'SOURCE_CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
                'TARGET_CRS': QgsCoordinateReferenceSystem(tile_proj.split(",")[0]),
                'RESAMPLING': 0,
                'NODATA': 255,
                'TARGET_RESOLUTION': 30,
                'OPTIONS': '',
                'DATA_TYPE': 0,
                'TARGET_EXTENT': grid_extent,
                'TARGET_EXTENT_CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
                'MULTITHREADING': False,
                'EXTRA': '',
                'OUTPUT': s_file_mapbiomas_output
            }
        )

        # ---------------------------------------------------------------------
        # make blank copies for OSM and Biomes rasterization
        # biomes
        s_file_biomes_output = "{}/biomes.tif".format(s_folder_year)
        get_blank_raster(
            file_input=s_file_mapbiomas_output,
            file_output=s_file_biomes_output,
            blank_value=0
        )
        # copy qml file
        shutil.copy(src=s_file_qml_biomes, dst="{}/biomes.qml".format(s_folder_year))

        # OSM
        s_file_osm_output = "{}/osm.tif".format(s_folder_year)
        get_blank_raster(
            file_input=s_file_mapbiomas_output,
            file_output=s_file_osm_output,
            blank_value=0
        )
        # copy qml file
        shutil.copy(src=s_file_qml_osm, dst="{}/osm.qml".format(s_folder_year))

        # ---------------------------------------------------------------------
        # rasterize vectors

        # biomes
        processing.run(
            "gdal:rasterize_over",
            {
                'INPUT': '{}|layername=biomes_utm'.format(s_file_vectors_db),
                'INPUT_RASTER': s_file_biomes_output,
                'FIELD': 'Id_Bioma',
                'ADD': False,
                'EXTRA': ''
            }
        )
        # osm
        for lyr in lst_osm_layers:
            # Read the GeoPackage layer
            osm_gdf = gpd.read_file(s_file_vectors_db, layer=lyr)
            # Add a new field
            osm_gdf["Id_OSM"] = 0

            # rail
            if "osm_rails" in lyr:
                osm_gdf["Id_OSM"] = 104

            # roads
            else:
                # conversion
                osm_gdf["Id_OSM"] = 100
                dct_conversion = {
                    "motorway": 103,
                    "motorway_link": 103,
                    "primary": 102,
                    "primary_link": 102,
                    "secondary": 101,
                    "secondary_link": 101,
                    "residential": 24,
                }
                for f in range(len(osm_gdf)):
                    s_class = osm_gdf["fclass"].values[f]
                    if s_class in list(dct_conversion.keys()):
                        osm_gdf["Id_OSM"].values[f] = dct_conversion[s_class]

            # Save the modified GeoDataFrame back to the same GeoPackage layer
            osm_gdf.to_file(s_file_vectors_db, layer=lyr, driver="GPKG")

            # rasterize
            processing.run(
                "gdal:rasterize_over",
                {
                    'INPUT': '{}|layername={}'.format(s_file_vectors_db, lyr),
                    'INPUT_RASTER': s_file_osm_output,
                    'FIELD': 'Id_OSM',
                    'ADD': False,
                    'EXTRA': ''
                }
            )

        # ---------------------------------------------------------------------
        # compute lulc for habitat quality model







