import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def part_1(filename):
    data_df = pd.read_excel(filename)
    
    countries = data_df["Country Name"]
    
    years = data_df[['1990 [YR1990]', '2000 [YR2000]', '2013 [YR2013]',
                     '2014 [YR2014]', '2015 [YR2015]', '2016 [YR2016]', '2017 [YR2017]',
                     '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]',
                     '2022 [YR2022]']]

    return countries, years

def read_worldbank_data(filename):

    data_df = pd.read_excel(filename, sheet_name='Data')

    transposed_data_df = data_df.melt(id_vars=['Series Name', 'Series Code', 'Country Name', 'Country Code'],
                                      var_name='Year', value_name='Value')

    
    transposed_data_df['Year'] = transposed_data_df['Year'].str.extract('(\d+)', expand=False).astype(str)

    # Replace '..' with NaN in the 'Value' column
    transposed_data_df['Value'] = pd.to_numeric(transposed_data_df['Value'], errors='coerce')

    return transposed_data_df

def plot_electricity_access(data_df, countries):
    
    indicator_code = 'EG.ELC.ACCS.ZS'
    selected_data = data_df[data_df['Series Code'] == indicator_code]

    
    selected_data = selected_data[selected_data['Country Name'].isin(countries)]

    
    plt.figure(figsize=(15, 15))
    sns.lineplot(x='Year', y='Value', hue='Country Name', data=selected_data)
    plt.title('Access to Electricity Comparison')
    plt.xlabel('Year')
    plt.ylabel('Access to Electricity (%)')
    plt.legend(title='Country', bbox_to_anchor=(1, 1), loc='upper left')
    plt.show()


def main():

    filename = str(input("Enter your filePath : "))

    data_frame_1, data_frame_2 = part_1(filename)

    print(data_frame_1.head(10))
    print("\n\n")
    print(data_frame_2.head(10))

    transposed_data = read_worldbank_data(filename)

    # Example: Plot access to electricity for multiple countries
    countries_to_compare = ['Afghanistan', 'Russian Federation', 'Pakistan']
    plot_electricity_access(transposed_data, countries_to_compare)

if __name__ == "__main__":
    main()