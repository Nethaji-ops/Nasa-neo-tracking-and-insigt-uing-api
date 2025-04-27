import streamlit as st
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('asteroids.db')
cursor = conn.cursor()

st.title("🚀 Asteroid Close Approach Dashboard")

# Sidebar for query selection
query_options = [
    "Number of approaches per asteroid",
    "Top 10 fastest asteroids",
    "Hazardous asteroids approached >3 times",
    "Closest asteroid approaches",
    "Asteroids >50,000 km/h",
    "Asteroids >5 km diameter",
    "Average velocity of all approaches",
    "Asteroids approaching Earth (orbiting body = Earth)",
    "Asteroids with multiple approaches in same year",
    "Top 5 hazardous asteroids by size",
    "Number of hazardous asteroids",
    "Maximum miss distance (farthest asteroid)",
    "Asteroids with missing orbit_id",
    "Asteroids within 1 Lunar Distance",
    "Earliest close approach date"
]

selected_query = st.sidebar.selectbox("Choose an Insight to View:", query_options, key="insight_selector_sidebar")


# Filters Example (for future expansion)
min_velocity = st.sidebar.slider("Minimum Relative Velocity (km/h)", 0, 100000, 0, key="min_velocity_slider")

# Query mapping
query_map = {
    "Number of approaches per asteroid": '''
        SELECT neo_reference_id, COUNT(*) AS approach_count
        FROM close_approach
        GROUP BY neo_reference_id
        ORDER BY approach_count DESC;
    ''',

    "Top 10 fastest asteroids": f'''
        SELECT a.name, c.relative_velocity_kmph
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.relative_velocity_kmph >= {min_velocity}
        ORDER BY c.relative_velocity_kmph DESC
        LIMIT 10;
    ''',

    "Hazardous asteroids approached >3 times": '''
        SELECT a.name, COUNT(*) AS approach_count
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE a.is_potentially_hazardous_asteroid = 1
        GROUP BY a.id
        HAVING approach_count > 3
        ORDER BY approach_count DESC;
    ''',

    "Closest asteroid approaches": '''
        SELECT a.name, c.close_approach_date, c.miss_distance_km
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        ORDER BY c.miss_distance_km ASC
        LIMIT 10;
    ''',

    "Asteroids >50,000 km/h": '''
        SELECT a.name, c.relative_velocity_kmph
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.relative_velocity_kmph > 50000
        ORDER BY c.relative_velocity_kmph DESC;
    ''',

    "Asteroids >5 km diameter": '''
        SELECT name, estimated_diameter_max_km
        FROM asteroids
        WHERE estimated_diameter_max_km > 5
        ORDER BY estimated_diameter_max_km DESC;
    ''',

    "Average velocity of all approaches": '''
        SELECT AVG(relative_velocity_kmph) AS avg_velocity
        FROM close_approach;
    ''',

    "Asteroids approaching Earth (orbiting body = Earth)": '''
        SELECT a.name, c.close_approach_date
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.orbiting_body = 'Earth';
    ''',

    "Asteroids with multiple approaches in same year": '''
        SELECT a.name, STRFTIME('%Y', c.close_approach_date) AS year, COUNT(*)
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        GROUP BY a.id, year
        HAVING COUNT(*) > 1
        ORDER BY year;
    ''',

    "Top 5 hazardous asteroids by size": '''
        SELECT name, estimated_diameter_max_km
        FROM asteroids
        WHERE is_potentially_hazardous_asteroid = 1
        ORDER BY estimated_diameter_max_km DESC
        LIMIT 5;
    ''',

    "Number of hazardous asteroids": '''
        SELECT COUNT(*)
        FROM asteroids
        WHERE is_potentially_hazardous_asteroid = 1;
    ''',

    "Maximum miss distance (farthest asteroid)": '''
        SELECT MAX(miss_distance_km) AS farthest_distance
        FROM close_approach;
    ''',

    "Asteroids with missing orbit_id": '''
        SELECT name
        FROM asteroids
        WHERE orbit_id IS NULL OR orbit_id = '';
    ''',

    "Asteroids within 1 Lunar Distance": '''
        SELECT a.name, c.close_approach_date, c.miss_distance_lunar
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.miss_distance_lunar <= 1
        ORDER BY c.miss_distance_lunar ASC;
    ''',

    "Earliest close approach date": '''
        SELECT MIN(close_approach_date) AS earliest_approach
        FROM close_approach;
    '''
}

# Execute the selected query
query_to_run = query_map[selected_query]
df = pd.read_sql_query(query_to_run, conn)

# Show result
st.subheader(f"Result: {selected_query}")
st.dataframe(df)

# Close DB
conn.close()
import streamlit as st
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('asteroids.db')
cursor = conn.cursor()

st.title("🚀 Asteroid Close Approach Dashboard")

# Sidebar for query selection
query_options = [
    "Number of approaches per asteroid",
    "Top 10 fastest asteroids",
    "Hazardous asteroids approached >3 times",
    "Closest asteroid approaches",
    "Asteroids >50,000 km/h",
    "Asteroids >5 km diameter",
    "Average velocity of all approaches",
    "Asteroids approaching Earth (orbiting body = Earth)",
    "Asteroids with multiple approaches in same year",
    "Top 5 hazardous asteroids by size",
    "Number of hazardous asteroids",
    "Maximum miss distance (farthest asteroid)",
    "Asteroids with missing orbit_id",
    "Asteroids within 1 Lunar Distance",
    "Earliest close approach date"
]

selected_query = st.sidebar.selectbox("Choose an Insight to View:", query_options)

# Filters Example (for future expansion)
min_velocity = st.sidebar.slider("Minimum Relative Velocity (km/h)", 0, 100000, 0)

# Query mapping
query_map = {
    "Number of approaches per asteroid": '''
        SELECT neo_reference_id, COUNT(*) AS approach_count
        FROM close_approach
        GROUP BY neo_reference_id
        ORDER BY approach_count DESC;
    ''',

    "Top 10 fastest asteroids": f'''
        SELECT a.name, c.relative_velocity_kmph
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.relative_velocity_kmph >= {min_velocity}
        ORDER BY c.relative_velocity_kmph DESC
        LIMIT 10;
    ''',

    "Hazardous asteroids approached >3 times": '''
        SELECT a.name, COUNT(*) AS approach_count
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE a.is_potentially_hazardous_asteroid = 1
        GROUP BY a.id
        HAVING approach_count > 3
        ORDER BY approach_count DESC;
    ''',

    "Closest asteroid approaches": '''
        SELECT a.name, c.close_approach_date, c.miss_distance_km
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        ORDER BY c.miss_distance_km ASC
        LIMIT 10;
    ''',

    "Asteroids >50,000 km/h": '''
        SELECT a.name, c.relative_velocity_kmph
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.relative_velocity_kmph > 50000
        ORDER BY c.relative_velocity_kmph DESC;
    ''',

    "Asteroids >5 km diameter": '''
        SELECT name, estimated_diameter_max_km
        FROM asteroids
        WHERE estimated_diameter_max_km > 5
        ORDER BY estimated_diameter_max_km DESC;
    ''',

    "Average velocity of all approaches": '''
        SELECT AVG(relative_velocity_kmph) AS avg_velocity
        FROM close_approach;
    ''',

    "Asteroids approaching Earth (orbiting body = Earth)": '''
        SELECT a.name, c.close_approach_date
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.orbiting_body = 'Earth';
    ''',

    "Asteroids with multiple approaches in same year": '''
        SELECT a.name, STRFTIME('%Y', c.close_approach_date) AS year, COUNT(*)
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        GROUP BY a.id, year
        HAVING COUNT(*) > 1
        ORDER BY year;
    ''',

    "Top 5 hazardous asteroids by size": '''
        SELECT name, estimated_diameter_max_km
        FROM asteroids
        WHERE is_potentially_hazardous_asteroid = 1
        ORDER BY estimated_diameter_max_km DESC
        LIMIT 5;
    ''',

    "Number of hazardous asteroids": '''
        SELECT COUNT(*)
        FROM asteroids
        WHERE is_potentially_hazardous_asteroid = 1;
    ''',

    "Maximum miss distance (farthest asteroid)": '''
        SELECT MAX(miss_distance_km) AS farthest_distance
        FROM close_approach;
    ''',

    "Asteroids with missing orbit_id": '''
        SELECT name
        FROM asteroids
        WHERE orbit_id IS NULL OR orbit_id = '';
    ''',

    "Asteroids within 1 Lunar Distance": '''
        SELECT a.name, c.close_approach_date, c.miss_distance_lunar
        FROM asteroids a
        JOIN close_approach c ON a.id = c.neo_reference_id
        WHERE c.miss_distance_lunar <= 1
        ORDER BY c.miss_distance_lunar ASC;
    ''',

    "Earliest close approach date": '''
        SELECT MIN(close_approach_date) AS earliest_approach
        FROM close_approach;
    '''
}

# Execute the selected query
query_to_run = query_map[selected_query]
df = pd.read_sql_query(query_to_run, conn)

# Show result
st.subheader(f"Result: {selected_query}")
st.dataframe(df)

# Close DB
conn.close()