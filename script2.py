import openrouteservice as ors
import requests
import streamlit as st
import folium
from streamlit_folium import folium_static

# Set up the ORS client with API key
ors_client = ors.Client(key='5b3ce3597851110001cf6248d40580fab7774f5db05efdc9f51eda5c')

# Get user inputs
from_location = st.text_input("From")
to_location = st.text_input("To")

# Define the vehicle options
vehicle_options = ["Ola", "Uber"]

# Add a navigation bar to select the vehicle option
selected_vehicle = st.selectbox("Select a vehicle", vehicle_options)

# Add a "Submit" button
if st.button("Submit"):
    try:
        # Initialize the map
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Geocode the source and destination addresses
        from_url = f"https://nominatim.openstreetmap.org/search.php?q={from_location}&format=json"
        from_resp = requests.get(from_url).json()
        from_coords = {'lat': float(from_resp[0]['lat']), 'lon': float(from_resp[0]['lon'])}

        to_url = f"https://nominatim.openstreetmap.org/search.php?q={to_location}&format=json"
        to_resp = requests.get(to_url).json()
        to_coords = {'lat': float(to_resp[0]['lat']), 'lon': float(to_resp[0]['lon'])}

        # Get the route using ORS client
        route = ors_client.directions(
            coordinates=[[from_coords['lon'], from_coords['lat']],
                         [to_coords['lon'], to_coords['lat']]],
            profile='driving-car',
            format='geojson'
        )

        # Display the selected vehicle option
        st.write("Selected Vehicle:", selected_vehicle)

        # Parse the route data
        distance = round(route['features'][0]['properties']['segments'][0]['distance'] / 1000, 2)
        duration = round(route['features'][0]['properties']['segments'][0]['duration'] / 60, 2)
        steps = [step['instruction'] for step in route['features'][0]['properties']['segments'][0]['steps']]

        # Display the route data
        st.write("Path:", from_location, "to", to_location)
        st.write("Distance:", distance, "km")
        st.write("Duration:", duration, "minutes")
        #st.write("Steps:")
        #for i, step in enumerate(steps):
         #   st.write(f"{i+1}. {step}")

        # Add the route to the map
        folium.PolyLine(locations=[list(reversed(coord)) for coord in route['features'][0]['geometry']['coordinates']],
                        color='blue').add_to(m)

        # Set the map center and display the map
        map_center = [(from_coords['lat'] + to_coords['lat']) / 2, (from_coords['lon'] + to_coords['lon']) / 2]
        m.location = map_center
        m.fit_bounds(m.get_bounds())
        st.write("Route Map:")
        folium_static(m)

        # Open the selected vehicle service in a new browser tab
        if selected_vehicle == "Ola":
            ola_url = "https://www.olacabs.com/"
            st.write("[Open Ola](%s){:target='_blank'}" % ola_url)

        elif selected_vehicle == "Uber":
            uber_url = "https://www.uber.com/"
            st.write("[Open Uber](%s){:target='_blank'}" % uber_url)

    except:
        st.write("Error fetching route data")

