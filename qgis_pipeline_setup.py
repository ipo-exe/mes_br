from osgeo import gdal
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    driver = gdal.GetDriverByName("GTiff")

    # Create a new raster with the same dimensions as the original
    raster_output = driver.Create(
        file_output, raster_x_size, raster_y_size, 1, gdal.GDT_Byte
    )

    # Set the projection and geotransform of the new raster to match the original
    raster_output.SetProjection(raster_projection)
    raster_output.SetGeoTransform(raster_geotransform)

    # Write the new data to the new raster
    raster_output.GetRasterBand(1).WriteArray(grid_output)

    # Close
    raster_output = None
    return None

def get_lulc_model(
    file_mapbiomas,
    file_osm,
    file_table,
    output_folder,
    output_name="lulc",
    habitat_quality=True,
    file_style_hq=None,
    plans3=True,
    file_style_plans3=None,
    mbc="MBC8",
):
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
    # raster_mapbiomas = None

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
    # plt.imshow(grid_osm)
    # plt.show()

    # -- Close the raster
    raster_osm = None

    del band_osm

    # -------------------------------------------------------------------------
    # PROCESS

    # set lulc mbc
    grid_osm_bool = 1 * (grid_osm > 0)
    grid_lulc_mbc = (grid_mapbiomas * (grid_osm_bool == 0)) + (grid_osm * grid_osm_bool)

    if habitat_quality:

        # -------------------------------------------------------------------------
        # EXPORT RASTER FILE
        # Get the driver to create the new raster
        driver = gdal.GetDriverByName("GTiff")

        # Create a new raster with the same dimensions as the original
        file_output_name = "{}/{}_hq".format(output_folder, output_name)
        file_output = file_output_name + ".tif"
        raster_output = driver.Create(
            file_output, raster_x_size, raster_y_size, 1, gdal.GDT_Byte
        )
        # Set the projection and geotransform of the new raster to match the original
        raster_output.SetProjection(raster_projection)
        raster_output.SetGeoTransform(raster_geotransform)

        # Write the new data to the new raster
        raster_output.GetRasterBand(1).WriteArray(grid_lulc_mbc)

        # Close
        raster_output = None

        # -------------------------------------------------------------------------
        # EXPORT STYLE
        if file_style_hq is None:
            pass
        else:
            shutil.copy(
                src=file_style_hq,
                dst="{}.qml".format(file_output_name)
            )

    if plans3:
        # PLANS lulc
        # set output grid
        grid_output = grid_lulc_mbc * 0
        # filter tables
        df_table_plans3 = df_table.drop_duplicates(subset="Alias_{}".format(mbc))

        # run all classes
        for i in range(len(df_table_plans3)):
            id_old_lulc = df_table_plans3["Id_{}".format(mbc)].values[i]
            id_new = df_table_plans3["Id_PLANS3"].values[i]
            grid_output = grid_output + (id_new * (grid_lulc_mbc == id_old_lulc))

        # -------------------------------------------------------------------------
        # EXPORT RASTER FILE
        # Get the driver to create the new raster
        driver = gdal.GetDriverByName("GTiff")

        # Create a new raster with the same dimensions as the original
        file_output_name = "{}/{}_plans3".format(output_folder, output_name)
        file_output = file_output_name + ".tif"
        raster_output = driver.Create(
            file_output, raster_x_size, raster_y_size, 1, gdal.GDT_Byte
        )
        # Set the projection and geotransform of the new raster to match the original
        raster_output.SetProjection(raster_projection)
        raster_output.SetGeoTransform(raster_geotransform)

        # Write the new data to the new raster
        raster_output.GetRasterBand(1).WriteArray(grid_output)

        # Close
        raster_output = None

        # -------------------------------------------------------------------------
        # EXPORT STYLE
        if file_style_plans3 is None:
            pass
        else:
            shutil.copy(
                src=file_style_plans3,
                dst="{}.qml".format(file_output_name)
            )
    return None

def get_threats(file_lulchq, file_table, output_folder):
    # -------------------------------------------------------------------------
    # Load table
    df_table = pd.read_csv(file_table, sep=",")
    df_table = df_table.query("Type_MBC8 != 'Natural cover'")

    # -------------------------------------------------------------------------
    # LOAD
    # Open the raster file using gdal
    raster_input = gdal.Open(file_lulchq)

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

    for i in range(len(df_table)):
        name_threat = df_table["Alias_HQ"].values[i]
        id_threat = df_table["Id_HQ"].values[i]
        if id_threat == 0:
            pass
        else:

            grid_output = 1 * (grid_input == id_threat)

            # -------------------------------------------------------------------------
            # EXPORT RASTER FILE
            # Get the driver to create the new raster
            driver = gdal.GetDriverByName("GTiff")

            # Create a new raster with the same dimensions as the original
            file_output = "{}/{}.tif".format(output_folder, name_threat.upper())
            raster_output = driver.Create(
                file_output, raster_x_size, raster_y_size, 1, gdal.GDT_Byte
            )
            # Set the projection and geotransform of the new raster to match the original
            raster_output.SetProjection(raster_projection)
            raster_output.SetGeoTransform(raster_geotransform)

            # Write the new data to the new raster
            raster_output.GetRasterBand(1).WriteArray(grid_output)

            # Close
            raster_output = None

# -----------------------------------------------------------------------------
# SET DATASETS FILEPATHS

# output dir
s_root = "C:/gis/_projects_/mes_br" # default: "C:/gis/_projects_/mes_br"

# mes geopackage dataset
s_src_folder = "C:/Users/Ipo/PycharmProjects/mes_br"
s_src_folder_tables = "C:/Users/Ipo/PycharmProjects/mes_br"
s_file_db = "{}/mes_br_db.gpkg".format(s_src_folder)
# mes lulc table
s_file_lulc_table = "{}/lulc_conversion_table.csv".format(s_src_folder)

# styles files
s_file_qml_biomes = "{}/biomes.qml".format(s_src_folder)
s_file_qml_osm = "{}/osm.qml".format(s_src_folder)
s_file_qml_lulchq = "{}/lulc_hq.qml".format(s_src_folder)
s_file_qml_plans3 = "{}/plans3.qml".format(s_src_folder)

# osm geopackage
s_file_osm = "C:/gis/osm/osm_br_2022/osm_br_2022.gpkg"

# mapbiomas dataset
s_folder_mapbiomas = "C:/gis/mapbiomas/Mapbiomas_sentinel_10m/collection_beta"
s_file_style_mapbiomas = "C:/gis/mapbiomas/Mapbiomas_landsat_30m/style_beta.qml"

# -----------------------------------------------------------------------------
# SET PARAMETERS
# set grid size
grid_deg = 1 # 2

# set tiles ids
lst_tile_ids = [1183]

# set lulc years
lst_years = [2016, 2017, 2018, 2019, 2020, 2021, 2022]

# create folder
s_folder_grid = "{}/grid_{}deg_10m".format(s_root, grid_deg)
if os.path.exists(s_folder_grid):
    pass
else:
    os.mkdir(s_folder_grid)

# read the tiles dataset
gdf_tiles = gpd.read_file(s_file_db, layer="grid_br_{}deg".format(grid_deg))
# Filter the DataFrame based on the 'id' column
gdf_tiles = gdf_tiles[gdf_tiles["id"].isin(lst_tile_ids)]

# -----------------------------------------------------------------------------
# AUX VARIABLES
# define projections
dct_projs = {
    "UTM 18N": "EPSG:31972, SIRGAS 2000 / UTM zone 18N",
    "UTM 19N": "EPSG:31973, SIRGAS 2000 / UTM zone 19N",
    "UTM 20N": "EPSG:31974, SIRGAS 2000 / UTM zone 20N",
    "UTM 21N": "EPSG:31975, SIRGAS 2000 / UTM zone 21N",
    "UTM 22N": "EPSG:31976, SIRGAS 2000 / UTM zone 22N",
    "UTM 18S": "EPSG:31978, SIRGAS 2000 / UTM zone 18S",
    "UTM 19S": "EPSG:31979, SIRGAS 2000 / UTM zone 19S",
    "UTM 20S": "EPSG:31980, SIRGAS 2000 / UTM zone 20S",
    "UTM 21S": "EPSG:31981, SIRGAS 2000 / UTM zone 21S",
    "UTM 22S": "EPSG:31982, SIRGAS 2000 / UTM zone 22S",
    "UTM 23S": "EPSG:31983, SIRGAS 2000 / UTM zone 23S",
    "UTM 24S": "EPSG:31984, SIRGAS 2000 / UTM zone 24S",
    "UTM 25S": "EPSG:31985, SIRGAS 2000 / UTM zone 25S",
}
dct_hem = {"S": "south", "N": "north"}

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
    # copy lulc tables
    shutil.copy(
        src="{}/lulc_mean.csv".format(s_src_folder_tables),
        dst="{}/lulc_mean.csv".format(s_folder_tile))
    shutil.copy(
        src="{}/lulc_p05.csv".format(s_src_folder_tables),
        dst="{}/lulc_p05.csv".format(s_folder_tile))
    shutil.copy(
        src="{}/lulc_p95.csv".format(s_src_folder_tables),
        dst="{}/lulc_p95.csv".format(s_folder_tile))

    # -------------------------------------------------------------------------
    # GET TILE ATTRIBUTES
    # get list of regions
    lst_grid_regioes = gdf_tiles["regiao"].values[i].split(",")

    # get window projection
    tile_proj = dct_projs[gdf_tiles["Fuso UTM"].values[i]]
    tile_zone = tile_proj[-3:-1]
    tile_hem = dct_hem[tile_proj[-1:]]

    # get extent
    min_x = gdf_tiles["left"].values[i]  # -39.85121,
    max_y = gdf_tiles["top"].values[i]  # -14.36413
    max_x = gdf_tiles["right"].values[i]  # -39.19078,
    min_y = gdf_tiles["bottom"].values[i]  # -15.03517
    grid_extent = "{},{},{},{} [EPSG:4326]".format(min_x, max_x, min_y, max_y)

    # -------------------------------------------------------------------------
    # GET VECTORS
    print(">>> tile {} :: processing vectors...".format(tile_id))
    # set lists
    lst_latlong_layers = list()

    s_file_vectors_db = "{}/vectors.gpkg".format(s_folder_tile)

    # ---------------------------------------------------------------------
    # OSM vectors
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
                "INPUT": "{}|layername=gis_osm_roads_free_1_{}".format(
                    s_file_osm, region
                ),
                "EXTENT": grid_extent,
                "CLIP": True,
                "OUTPUT": "ogr:dbname='{}' table=\"{}\" (geom)".format(
                    s_file_vectors_db, s_layer
                ),
            },
        )

        # railways
        s_layer = "osm_rails_{}_latlong".format(region)
        lst_latlong_layers.append(s_layer)
        # clip by extent
        processing.run(
            "native:extractbyextent",
            {
                "INPUT": "{}|layername=gis_osm_railways_free_1_{}".format(
                    s_file_osm, region
                ),
                "EXTENT": grid_extent,
                "CLIP": True,
                "OUTPUT": "ogr:dbname='{}' table=\"{}\" (geom)".format(
                    s_file_vectors_db, s_layer
                ),
            },
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
                "INPUT": "{}|layername={}".format(s_file_vectors_db, lyr),
                "TARGET_CRS": QgsCoordinateReferenceSystem(tile_proj.split(",")[0]),
                "OPERATION": "+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad +step +proj=utm +zone={} +{} +ellps=GRS80".format(
                    tile_zone, tile_hem
                ),
                "OUTPUT": "ogr:dbname='{}' table=\"{}\" (geom)".format(
                    s_file_vectors_db, new_lyr
                ),
            },
        )

    # ---------------------------------------------------------------------
    # Rasters
    print(">>> tile {} :: processing rasters...".format(tile_id))

    # ---------------------------------------------------------------------
    # biomes
    '''
    print(">>> tile {} :: biomas_we...".format(tile_id))
    # clip and warp biomes
    s_file_biomas = "{}/biomas_w.tif".format(s_folder_mapbiomas)
    s_file_biomas_output_name = "{}/biomas_w".format(s_folder_group)

    # copy style file
    shutil.copy(s_file_qml_biomes, s_file_biomas_output_name + ".qml")

    # run warp
    s_file_biomas_output = s_file_biomas_output_name + ".tif"
    processing.run(
        "gdal:warpreproject",
        {
            "INPUT": s_file_biomas,
            "SOURCE_CRS": QgsCoordinateReferenceSystem("EPSG:4326"),
            "TARGET_CRS": QgsCoordinateReferenceSystem(tile_proj.split(",")[0]),
            "RESAMPLING": 0,
            "NODATA": 255,
            "TARGET_RESOLUTION": 30,
            "OPTIONS": "",
            "DATA_TYPE": 0,
            "TARGET_EXTENT": grid_extent,
            "TARGET_EXTENT_CRS": QgsCoordinateReferenceSystem("EPSG:4326"),
            "MULTITHREADING": False,
            "EXTRA": "",
            "OUTPUT": s_file_biomas_output,
        },
    )
    '''
    # ---------------------------------------------------------------------
    # OSM
    print(">>> tile {} :: osm...".format(tile_id))
    # OSM
    s_file_osm_output = "{}/osm.tif".format(s_folder_tile)
    get_blank_raster(
        file_input=s_file_biomas_output,
        file_output=s_file_osm_output,
        blank_value=0,
    )
    # copy qml file
    shutil.copy(src=s_file_qml_osm, dst="{}/osm.qml".format(s_folder_tile))

    # ---------------------------------------------------------------------
    # rasterize vectors
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
                "INPUT": "{}|layername={}".format(s_file_vectors_db, lyr),
                "INPUT_RASTER": s_file_osm_output,
                "FIELD": "Id_OSM",
                "ADD": False,
                "EXTRA": "",
            },
        )

    # -------------------------------------------------------------------------
    # RUN YEARS
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
                "INPUT": s_file_mapbiomas,
                "SOURCE_CRS": QgsCoordinateReferenceSystem("EPSG:4326"),
                "TARGET_CRS": QgsCoordinateReferenceSystem(tile_proj.split(",")[0]),
                "RESAMPLING": 0,
                "NODATA": 255,
                "TARGET_RESOLUTION": 30,
                "OPTIONS": "",
                "DATA_TYPE": 0,
                "TARGET_EXTENT": grid_extent,
                "TARGET_EXTENT_CRS": QgsCoordinateReferenceSystem("EPSG:4326"),
                "MULTITHREADING": False,
                "EXTRA": "",
                "OUTPUT": s_file_mapbiomas_output,
            },
        )

        # ---------------------------------------------------------------------
        # compute lulc for habitat quality model

        print(">>> tile {} :: raster lulc --year {}".format(tile_id, year))
        get_lulc_model(
            file_mapbiomas=s_file_mapbiomas_output,
            file_osm=s_file_osm_output,
            file_table=s_file_lulc_table,
            output_folder=s_folder_year,
            output_name="lulc",
            file_style_hq=s_file_qml_lulchq,
            habitat_quality=True,
            plans3=True,
            file_style_plans3=s_file_qml_plans3
        )

        # create threats folder
        s_folder_threats = "{}/threats".format(s_folder_year)
        if os.path.exists(s_folder_threats):
            pass
        else:
            os.mkdir(s_folder_threats)

        # -------------------------------------------------------------------------
        # copy threat tables
        shutil.copy(src="{}/threat_mean.csv".format(s_src_folder), dst="{}/threat_mean.csv".format(s_folder_threats))
        shutil.copy(src="{}/threat_p05.csv".format(s_src_folder), dst="{}/threat_p05.csv".format(s_folder_threats))
        shutil.copy(src="{}/threat_p95.csv".format(s_src_folder), dst="{}/threat_p95.csv".format(s_folder_threats))

        # -------------------------------------------------------------------------
        # split threats
        print(">>> tile {} :: raster computing threats".format(tile_id, year))
        get_threats(
            file_lulchq="{}/lulc_hq.tif".format(s_folder_year),
            file_table=s_file_lulc_table,
            output_folder=s_folder_threats
        )

