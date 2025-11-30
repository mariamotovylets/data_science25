import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = '/Users/mariamotovylets/Downloads/studying/python/data_science/gun_violence_data_2013_2018.xlsx'

# Population data
pop_data = {
    'Alabama': 4863300, 'Alaska': 741894, 'Arizona': 6931071, 'Arkansas': 2988248,
    'California': 39250017, 'Colorado': 5540545, 'Connecticut': 3576452, 'Delaware': 952065,
    'District of Columbia': 681170, 'Florida': 20612439, 'Georgia': 10310371, 'Hawaii': 1428557,
    'Idaho': 1683140, 'Illinois': 12801539, 'Indiana': 6633053, 'Iowa': 3134693,
    'Kansas': 2907289, 'Kentucky': 4436974, 'Louisiana': 4681666, 'Maine': 1331479,
    'Maryland': 6016447, 'Massachusetts': 6811779, 'Michigan': 9928300, 'Minnesota': 5519952,
    'Mississippi': 2988726, 'Missouri': 6093000, 'Montana': 1042520, 'Nebraska': 1907116,
    'Nevada': 2940058, 'New Hampshire': 1334795, 'New Jersey': 8944469, 'New Mexico': 2081015,
    'New York': 19745289, 'North Carolina': 10146788, 'North Dakota': 757952, 'Ohio': 11614373,
    'Oklahoma': 3923561, 'Oregon': 4093465, 'Pennsylvania': 12784227, 'Rhode Island': 1056426,
    'South Carolina': 4961119, 'South Dakota': 865454, 'Tennessee': 6651194, 'Texas': 27862596,
    'Utah': 3051217, 'Vermont': 624594, 'Virginia': 8411808, 'Washington': 7288000,
    'West Virginia': 1831102, 'Wisconsin': 5778708, 'Wyoming': 585501
}

# Regions mapping
regions = {
    'Connecticut': 'Northeast', 'Maine': 'Northeast', 'Massachusetts': 'Northeast', 'New Hampshire': 'Northeast', 
    'Rhode Island': 'Northeast', 'Vermont': 'Northeast', 'New Jersey': 'Northeast', 'New York': 'Northeast', 
    'Pennsylvania': 'Northeast', 'Illinois': 'Midwest', 'Indiana': 'Midwest', 'Michigan': 'Midwest', 
    'Ohio': 'Midwest', 'Wisconsin': 'Midwest', 'Iowa': 'Midwest', 'Kansas': 'Midwest', 
    'Minnesota': 'Midwest', 'Missouri': 'Midwest', 'Nebraska': 'Midwest', 'North Dakota': 'Midwest', 
    'South Dakota': 'Midwest', 'Delaware': 'South', 'Florida': 'South', 'Georgia': 'South', 
    'Maryland': 'South', 'North Carolina': 'South', 'South Carolina': 'South', 'Virginia': 'South', 
    'District of Columbia': 'South', 'West Virginia': 'South', 'Alabama': 'South', 'Kentucky': 'South', 
    'Mississippi': 'South', 'Tennessee': 'South', 'Arkansas': 'South', 'Louisiana': 'South', 
    'Oklahoma': 'South', 'Texas': 'South', 'Arizona': 'West', 'Colorado': 'West', 
    'Idaho': 'West', 'Montana': 'West', 'Nevada': 'West', 'New Mexico': 'West', 
    'Utah': 'West', 'Wyoming': 'West', 'Alaska': 'West', 'California': 'West', 
    'Hawaii': 'West', 'Oregon': 'West', 'Washington': 'West'
}

try:
    print("Loading Excel file...")
    raw = pd.read_excel(file)
except Exception as e:
    print(f"Error: {e}")
    exit()

# Group data
df = raw.groupby('state')['n_killed'].sum().reset_index()
df = df.rename(columns={'n_killed': 'murders'})

# Merge population
pop = pd.DataFrame(list(pop_data.items()), columns=['state', 'population'])
data = pd.merge(df, pop, on='state')

# Add region and rate
data['region'] = data['state'].map(regions)
data['rate'] = (data['murders'] / data['population']) * 100000
data['rate'] = data['rate'].round(2)

#Save CSV
data.to_csv('clean_data.csv', index=False)
print("CSV file saved.")

#Population vs murders
print("Generating Plot 1...")
plt.figure(figsize=(10, 6))

#Create scatter plot
sns.scatterplot(data=data, x='population', y='murders', size='rate', hue='rate', sizes=(50, 400), palette='coolwarm')

#Labels
plt.title('Population vs Total Murders (Color = Danger Rate)')
plt.xlabel('Population')
plt.ylabel('Total Murders')
plt.grid(True, alpha=0.3)

#Save plot1
plt.savefig('plot1_population.png')
print("Plot 1 saved as 'plot1_population.png'")
plt.show() # Show window (close it to continue)

# Regions
print("Generating Plot 2...")
plt.figure(figsize=(10, 6)) # Create a new empty figure

#Create box plot
sns.boxplot(data=data, x='region', y='rate', palette="Set3")
plt.title('Murder Rate Distribution by Region')
plt.ylabel('Murder Rate (per 100k)')

#Save plot2
plt.savefig('plot2_regions.png')
print("Plot 2 saved as 'plot2_regions.png'")
plt.show()
