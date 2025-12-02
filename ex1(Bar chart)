import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#SETUP
file = '/Users/mariamotovylets/Downloads/studying/python/data_science/gun_violence_data_2013_2018.xlsx'

#Population data
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

#PROCESS DATA
try:
    print("Reading Excel ")
    raw = pd.read_excel(file)
    
    #Sum murders by state
    df = raw.groupby('state')['n_killed'].sum().reset_index()
    df = df.rename(columns={'n_killed': 'murders'})
    
    #Merge with population
    pop = pd.DataFrame(list(pop_data.items()), columns=['state', 'population'])
    data = pd.merge(df, pop, on='state')
    
    #Calc rate per 100k
    data['rate'] = (data['murders'] / data['population']) * 100000
    
except Exception as e:
    print(f"Error: {e}")
    exit()

#PLOT
print("Plotting ")

#High to Low
data = data.sort_values('rate', ascending=False)

#Wide figure for 50 states
plt.figure(figsize=(20, 8))

#Vertical bars
sns.barplot(data=data, x='state', y='rate', palette='Reds_r')

#Labels and style
plt.title('US States Ranked by Murder Rate', fontsize=16)
plt.ylabel('Rate (per 100k)', fontsize=12)
plt.xlabel('State', fontsize=12)
plt.grid(axis='y', alpha=0.5)

#Rotate text 90 degrees
plt.xticks(rotation=90, fontsize=10)

#Save and show
plt.tight_layout()
plt.savefig('vertical_ranking.png')
print("Saved as 'vertical_ranking.png'")
plt.show()
