<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" minScale="1e+08" version="3.28.8-Firenze" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation zscale="1" zoffset="0" enabled="0" band="1" symbology="Line">
    <data-defined-properties>
      <Option type="Map">
        <Option value="" type="QString" name="name"/>
        <Option name="properties"/>
        <Option value="collection" type="QString" name="type"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol is_animated="0" clip_to_extent="1" alpha="1" force_rhr="0" type="line" name="" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleLine" locked="0" pass="0" enabled="1">
          <Option type="Map">
            <Option value="0" type="QString" name="align_dash_pattern"/>
            <Option value="square" type="QString" name="capstyle"/>
            <Option value="5;2" type="QString" name="customdash"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="customdash_map_unit_scale"/>
            <Option value="MM" type="QString" name="customdash_unit"/>
            <Option value="0" type="QString" name="dash_pattern_offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="dash_pattern_offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="dash_pattern_offset_unit"/>
            <Option value="0" type="QString" name="draw_inside_polygon"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="232,113,141,255" type="QString" name="line_color"/>
            <Option value="solid" type="QString" name="line_style"/>
            <Option value="0.6" type="QString" name="line_width"/>
            <Option value="MM" type="QString" name="line_width_unit"/>
            <Option value="0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="0" type="QString" name="ring_filter"/>
            <Option value="0" type="QString" name="trim_distance_end"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_end_map_unit_scale"/>
            <Option value="MM" type="QString" name="trim_distance_end_unit"/>
            <Option value="0" type="QString" name="trim_distance_start"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="trim_distance_start_map_unit_scale"/>
            <Option value="MM" type="QString" name="trim_distance_start_unit"/>
            <Option value="0" type="QString" name="tweak_dash_pattern_on_corners"/>
            <Option value="0" type="QString" name="use_custom_dash"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="width_map_unit_scale"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol is_animated="0" clip_to_extent="1" alpha="1" force_rhr="0" type="fill" name="" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" type="QString" name="name"/>
            <Option name="properties"/>
            <Option value="collection" type="QString" name="type"/>
          </Option>
        </data_defined_properties>
        <layer class="SimpleFill" locked="0" pass="0" enabled="1">
          <Option type="Map">
            <Option value="3x:0,0,0,0,0,0" type="QString" name="border_width_map_unit_scale"/>
            <Option value="232,113,141,255" type="QString" name="color"/>
            <Option value="bevel" type="QString" name="joinstyle"/>
            <Option value="0,0" type="QString" name="offset"/>
            <Option value="3x:0,0,0,0,0,0" type="QString" name="offset_map_unit_scale"/>
            <Option value="MM" type="QString" name="offset_unit"/>
            <Option value="35,35,35,255" type="QString" name="outline_color"/>
            <Option value="no" type="QString" name="outline_style"/>
            <Option value="0.26" type="QString" name="outline_width"/>
            <Option value="MM" type="QString" name="outline_width_unit"/>
            <Option value="solid" type="QString" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" type="QString" name="name"/>
              <Option name="properties"/>
              <Option value="collection" type="QString" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option value="false" type="bool" name="WMSBackgroundLayer"/>
      <Option value="false" type="bool" name="WMSPublishDataSourceUrl"/>
      <Option value="0" type="int" name="embeddedWidgets/count"/>
      <Option value="Value" type="QString" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option value="" type="QString" name="name"/>
      <Option name="properties"/>
      <Option value="collection" type="QString" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" enabled="false" maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer nodataColor="" alphaBand="-1" opacity="1" type="paletted" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry alpha="0" value="0" color="#ffffff" label="No data"/>
        <paletteEntry alpha="255" value="1" color="#1f8d49" label="Pampa Forest Formation"/>
        <paletteEntry alpha="255" value="2" color="#7dc975" label="Pampa Savanna Formation"/>
        <paletteEntry alpha="255" value="3" color="#04381d" label="Pampa Mangrove"/>
        <paletteEntry alpha="255" value="4" color="#026975" label="Pampa Floodable Forest"/>
        <paletteEntry alpha="255" value="5" color="#02d659" label="Pampa Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="6" color="#519799" label="Pampa Wetland"/>
        <paletteEntry alpha="255" value="7" color="#d6bc74" label="Pampa Grassland"/>
        <paletteEntry alpha="255" value="8" color="#fc8114" label="Pampa Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="9" color="#ffaa5f" label="Pampa Rocky Outcrop"/>
        <paletteEntry alpha="255" value="10" color="#ad5100" label="Pampa Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="11" color="#d89f5c" label="Pampa Other non Forest Formations"/>
        <paletteEntry alpha="255" value="12" color="#ffa07a" label="Pampa Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="13" color="#2532e4" label="Pampa River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="14" color="#1f8d49" label="Mata Atlantica Forest Formation"/>
        <paletteEntry alpha="255" value="15" color="#7dc975" label="Mata Atlantica Savanna Formation"/>
        <paletteEntry alpha="255" value="16" color="#04381d" label="Mata Atlantica Mangrove"/>
        <paletteEntry alpha="255" value="17" color="#026975" label="Mata Atlantica Floodable Forest"/>
        <paletteEntry alpha="255" value="18" color="#02d659" label="Mata Atlantica Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="19" color="#519799" label="Mata Atlantica Wetland"/>
        <paletteEntry alpha="255" value="20" color="#d6bc74" label="Mata Atlantica Grassland"/>
        <paletteEntry alpha="255" value="21" color="#fc8114" label="Mata Atlantica Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="22" color="#ffaa5f" label="Mata Atlantica Rocky Outcrop"/>
        <paletteEntry alpha="255" value="23" color="#ad5100" label="Mata Atlantica Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="24" color="#d89f5c" label="Mata Atlantica Other non Forest Formations"/>
        <paletteEntry alpha="255" value="25" color="#ffa07a" label="Mata Atlantica Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="26" color="#2532e4" label="Mata Atlantica River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="27" color="#1f8d49" label="Cerrado Forest Formation"/>
        <paletteEntry alpha="255" value="28" color="#7dc975" label="Cerrado Savanna Formation"/>
        <paletteEntry alpha="255" value="29" color="#04381d" label="Cerrado Mangrove"/>
        <paletteEntry alpha="255" value="30" color="#026975" label="Cerrado Floodable Forest"/>
        <paletteEntry alpha="255" value="31" color="#02d659" label="Cerrado Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="32" color="#519799" label="Cerrado Wetland"/>
        <paletteEntry alpha="255" value="33" color="#d6bc74" label="Cerrado Grassland"/>
        <paletteEntry alpha="255" value="34" color="#fc8114" label="Cerrado Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="35" color="#ffaa5f" label="Cerrado Rocky Outcrop"/>
        <paletteEntry alpha="255" value="36" color="#ad5100" label="Cerrado Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="37" color="#d89f5c" label="Cerrado Other non Forest Formations"/>
        <paletteEntry alpha="255" value="38" color="#ffa07a" label="Cerrado Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="39" color="#2532e4" label="Cerrado River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="40" color="#1f8d49" label="Caatinga Forest Formation"/>
        <paletteEntry alpha="255" value="41" color="#7dc975" label="Caatinga Savanna Formation"/>
        <paletteEntry alpha="255" value="42" color="#04381d" label="Caatinga Mangrove"/>
        <paletteEntry alpha="255" value="43" color="#026975" label="Caatinga Floodable Forest"/>
        <paletteEntry alpha="255" value="44" color="#02d659" label="Caatinga Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="45" color="#519799" label="Caatinga Wetland"/>
        <paletteEntry alpha="255" value="46" color="#d6bc74" label="Caatinga Grassland"/>
        <paletteEntry alpha="255" value="47" color="#fc8114" label="Caatinga Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="48" color="#ffaa5f" label="Caatinga Rocky Outcrop"/>
        <paletteEntry alpha="255" value="49" color="#ad5100" label="Caatinga Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="50" color="#d89f5c" label="Caatinga Other non Forest Formations"/>
        <paletteEntry alpha="255" value="51" color="#ffa07a" label="Caatinga Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="52" color="#2532e4" label="Caatinga River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="53" color="#1f8d49" label="Amazonia Forest Formation"/>
        <paletteEntry alpha="255" value="54" color="#7dc975" label="Amazonia Savanna Formation"/>
        <paletteEntry alpha="255" value="55" color="#04381d" label="Amazonia Mangrove"/>
        <paletteEntry alpha="255" value="56" color="#026975" label="Amazonia Floodable Forest"/>
        <paletteEntry alpha="255" value="57" color="#02d659" label="Amazonia Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="58" color="#519799" label="Amazonia Wetland"/>
        <paletteEntry alpha="255" value="59" color="#d6bc74" label="Amazonia Grassland"/>
        <paletteEntry alpha="255" value="60" color="#fc8114" label="Amazonia Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="61" color="#ffaa5f" label="Amazonia Rocky Outcrop"/>
        <paletteEntry alpha="255" value="62" color="#ad5100" label="Amazonia Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="63" color="#d89f5c" label="Amazonia Other non Forest Formations"/>
        <paletteEntry alpha="255" value="64" color="#ffa07a" label="Amazonia Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="65" color="#2532e4" label="Amazonia River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="66" color="#1f8d49" label="Pantanal Forest Formation"/>
        <paletteEntry alpha="255" value="67" color="#7dc975" label="Pantanal Savanna Formation"/>
        <paletteEntry alpha="255" value="68" color="#04381d" label="Pantanal Mangrove"/>
        <paletteEntry alpha="255" value="69" color="#026975" label="Pantanal Floodable Forest"/>
        <paletteEntry alpha="255" value="70" color="#02d659" label="Pantanal Wooded Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="71" color="#519799" label="Pantanal Wetland"/>
        <paletteEntry alpha="255" value="72" color="#d6bc74" label="Pantanal Grassland"/>
        <paletteEntry alpha="255" value="73" color="#fc8114" label="Pantanal Hypersaline Tidal Flat"/>
        <paletteEntry alpha="255" value="74" color="#ffaa5f" label="Pantanal Rocky Outcrop"/>
        <paletteEntry alpha="255" value="75" color="#ad5100" label="Pantanal Herbaceous Sandbank Vegetation"/>
        <paletteEntry alpha="255" value="76" color="#d89f5c" label="Pantanal Other non Forest Formations"/>
        <paletteEntry alpha="255" value="77" color="#ffa07a" label="Pantanal Beach, Dune and Sand Spot"/>
        <paletteEntry alpha="255" value="78" color="#2532e4" label="Pantanal River, Lake and Ocean"/>
        <paletteEntry alpha="255" value="79" color="#edde8e" label="Pasture"/>
        <paletteEntry alpha="255" value="80" color="#f5b3c8" label="Soybean"/>
        <paletteEntry alpha="255" value="81" color="#db7093" label="Sugar cane"/>
        <paletteEntry alpha="255" value="82" color="#c71585" label="Rice"/>
        <paletteEntry alpha="255" value="83" color="#ff69b4" label="Cotton (beta)"/>
        <paletteEntry alpha="255" value="84" color="#f54ca9" label="Other Temporary Crops"/>
        <paletteEntry alpha="255" value="85" color="#d68fe2" label="Coffee"/>
        <paletteEntry alpha="255" value="86" color="#9932cc" label="Citrus"/>
        <paletteEntry alpha="255" value="87" color="#9065d0" label="Palm Oil"/>
        <paletteEntry alpha="255" value="88" color="#e6ccff" label="Other Perennial Crops"/>
        <paletteEntry alpha="255" value="89" color="#7a5900" label="Forest Plantation"/>
        <paletteEntry alpha="255" value="90" color="#ffefc3" label="Mosaic of Uses"/>
        <paletteEntry alpha="255" value="91" color="#d4271e" label="Urban Area"/>
        <paletteEntry alpha="255" value="92" color="#9c0027" label="Mining"/>
        <paletteEntry alpha="255" value="93" color="#db4d4f" label="Other non Vegetated Areas"/>
        <paletteEntry alpha="255" value="94" color="#091077" label="Aquaculture"/>
        <paletteEntry alpha="255" value="100" color="#D2CFC0" label="Roads Very Low Traffic"/>
        <paletteEntry alpha="255" value="101" color="#D4AD9B" label="Roads Low Traffic"/>
        <paletteEntry alpha="255" value="102" color="#D47F58" label="Roads Moderate Traffic"/>
        <paletteEntry alpha="255" value="103" color="#D44A0A" label="Roads Heavy Traffic"/>
        <paletteEntry alpha="255" value="104" color="#B5A295" label="Railways"/>
        <paletteEntry alpha="255" value="105" color="#D4B40A" label="Eolic infrastructure"/>
        <paletteEntry alpha="255" value="255" color="#ffffff" label="Not Observed"/>
      </colorPalette>
      <colorramp type="randomcolors" name="[source]">
        <Option/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation saturation="0" invertColors="0" grayscaleMode="0" colorizeBlue="128" colorizeOn="0" colorizeGreen="128" colorizeStrength="100" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
