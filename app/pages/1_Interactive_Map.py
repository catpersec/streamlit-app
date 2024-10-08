import streamlit as st
import leafmap.foliumap as leafmap

# markdown = """
# Web App URL: <https://geotemplate.streamlit.app>
# GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
# """

# st.sidebar.title("About")
# st.sidebar.info(markdown)
# logo = "https://i.imgur.com/UbOXYAU.png"
# st.sidebar.image(logo)


st.title("Interactive Map")

# col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

basemap = st.selectbox("Select a basemap:", options, index)
m = leafmap.Map(locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m.add_basemap(basemap)
m.to_streamlit(height=700)

# with col2:

    

# with col1:

