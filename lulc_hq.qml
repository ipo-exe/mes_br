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
		<paletteEntry label="Forest Formation" color="#1f8d49" alpha="255" value="3"/>
		<paletteEntry label="Savanna Formation" color="#7dc975" alpha="255" value="4"/>
		<paletteEntry label="Mangrove" color="#04381d" alpha="255" value="5"/>
		<paletteEntry label="Floodable Forest" color="#026975" alpha="255" value="6"/>
		<paletteEntry label="Wooded Sandbank Vegetation" color="#02d659" alpha="255" value="49"/>
		<paletteEntry label="Non Forest Natural Formation" color="#ad975a" alpha="255" value="10"/>
		<paletteEntry label="Wetland" color="#519799" alpha="255" value="11"/>
		<paletteEntry label="Grassland" color="#d6bc74" alpha="255" value="12"/>
		<paletteEntry label="Hypersaline Tidal Flat" color="#fc8114" alpha="255" value="32"/>
		<paletteEntry label="Rocky Outcrop" color="#ffaa5f" alpha="255" value="29"/>
		<paletteEntry label="Herbaceous Sandbank Vegetation" color="#ad5100" alpha="255" value="50"/>
		<paletteEntry label="Other non Forest Formations" color="#d89f5c" alpha="255" value="13"/>
		<paletteEntry label="Pasture" color="#edde8e" alpha="255" value="15"/>
		<paletteEntry label="Soybean" color="#f5b3c8" alpha="255" value="39"/>
		<paletteEntry label="Sugar cane" color="#db7093" alpha="255" value="20"/>
		<paletteEntry label="Rice" color="#c71585" alpha="255" value="40"/>
		<paletteEntry label="Cotton (beta)" color="#ff69b4" alpha="255" value="62"/>
		<paletteEntry label="Other Temporary Crops" color="#f54ca9" alpha="255" value="41"/>
		<paletteEntry label="Perennial Crop" color="#d082de" alpha="255" value="36"/>
		<paletteEntry label="Coffee" color="#d68fe2" alpha="255" value="46"/>
		<paletteEntry label="Citrus" color="#9932cc" alpha="255" value="47"/>
		<paletteEntry label="Palm Oil" color="#9065d0" alpha="255" value="35"/>
		<paletteEntry label="Other Perennial Crops" color="#e6ccff" alpha="255" value="48"/>
		<paletteEntry label="Forest Plantation" color="#7a5900" alpha="255" value="9"/>
		<paletteEntry label="Mosaic of Uses" color="#ffefc3" alpha="255" value="21"/>
		<paletteEntry label="Non vegetated area" color="#d4271e" alpha="255" value="22"/>
		<paletteEntry label="Beach, Dune and Sand Spot" color="#ffa07a" alpha="255" value="23"/>
		<paletteEntry label="Urban Area" color="#d4271e" alpha="255" value="24"/>
		<paletteEntry label="Mining" color="#9c0027" alpha="255" value="30"/>
		<paletteEntry label="Other non Vegetated Areas" color="#db4d4f" alpha="255" value="25"/>
		<paletteEntry label="Water" color="#0000FF" alpha="255" value="26"/>
		<paletteEntry label="River, Lake and Ocean" color="#2532e4" alpha="255" value="33"/>
		<paletteEntry label="Aquaculture" color="#091077" alpha="255" value="31"/>
		<paletteEntry label="Not Observed" color="#ffff" alpha="255" value="27"/>        
        <paletteEntry alpha="255" value="100" color="#D2CFC0" label="Roads Very Low Traffic"/>
        <paletteEntry alpha="255" value="101" color="#D4AD9B" label="Roads Low Traffic"/>
        <paletteEntry alpha="255" value="102" color="#D47F58" label="Roads Moderate Traffic"/>
        <paletteEntry alpha="255" value="103" color="#D44A0A" label="Roads Heavy Traffic"/>
        <paletteEntry alpha="255" value="104" color="#B5A295" label="Railways"/>
        <paletteEntry alpha="255" value="105" color="#D4B40A" label="Eolic infrastructure"/>
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
