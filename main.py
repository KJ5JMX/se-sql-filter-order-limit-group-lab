import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####


conn1 = sqlite3.connect('planets.db')


pd.read_sql("""SELECT * FROM planets; """, conn1)


df_no_moons = pd.read_sql("""SELECT * FROM planets WHERE num_of_moons = 0; """, conn1)

df_name_seven = pd.read_sql("""SELECT name, mass FROM planets WHERE LENGTH(name) = 7; """, conn1)

##### Part 2: Advanced Filtering #####


df_mass = pd.read_sql("""SELECT name, mass FROM planets WHERE mass <= 1.00;""", conn1)


df_mass_moon = pd.read_sql("""SELECT * FROM planets WHERE num_of_moons >= 1 AND mass < 1.00; """, conn1)

df_blue = pd.read_sql("""SELECT name, color FROM planets WHERE color LIKE '%blue%'""", conn1)



# STEP 0


conn2 = sqlite3.connect('dogs.db')

pd.read_sql("SELECT * FROM dogs;", conn2)


df_hungry = pd.read_sql("""SELECT name, age, breed FROM dogs WHERE hungry = 1 ORDER BY age ASC; """, conn2)


df_hungry_ages = pd.read_sql("""SELECT name, age, hungry FROM dogs WHERE age BETWEEN 2 AND 7 ORDER BY name ASC; """, conn2)


df_4_oldest = pd.read_sql("""SELECT name, age, breed FROM (SELECT name, age, breed FROM dogs ORDER BY age DESC LIMIT 4) ORDER BY breed ASC; """, conn2)

##### Part 4: Aggregation #####

# STEP 0


conn3 = sqlite3.connect('babe_ruth.db')

pd.read_sql("""SELECT * FROM babe_ruth_stats; """, conn3)

# STEP 9
# Replace None with your code
df_ruth_years = pd.read_sql("""SELECT COUNT(DISTINCT year) AS total_years FROM babe_ruth_stats; """, conn3)

# STEP 10
# Replace None with your code
df_hr_total = pd.read_sql("""SELECT SUM(HR) AS total_home_runs FROM babe_ruth_stats; """, conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11
# Replace None with your code
df_teams_years = pd.read_sql("""SELECT team_name, COUNT(DISTINCT year) AS number_years FROM babe_ruth_stats GROUP BY team;""", conn3).sum()

# STEP 12
# Replace None with your code
df_at_bats = pd.read_sql("""SELECT team AS team_name, AVG(at_bats) AS total_at_bats FROM babe_ruth_stats GROUP BY team HAVING AVG(at_bats) >200 """, conn3).sum()


conn1.close()
conn2.close()
conn3.close()