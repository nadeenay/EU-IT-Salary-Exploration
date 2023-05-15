import pandas as pd
from matplotlib import pyplot as plt

company_type_mapping = {
    'insurance': 'Financial/Insurance',
    'finance': 'Financial/Insurance',
    'fintech': 'Financial/Insurance',
    'ipo': 'Financial/Insurance',
    'bank': 'Financial/Insurance',
    'fin tech': 'Financial/Insurance',
    'stock market': 'Financial/Insurance',
    'financial': 'Financial/Insurance',
    'university': 'University/Research',
    'hochschule/university': 'University/Research',
    'research': 'University/Research',
    'pharma':  'University/Research',
    'industry': 'Manufacturing/Industry',
    'manufacturing': 'Manufacturing/Industry',
    'nonit, manufacturing': 'Manufacturing/Industry',
    'automotive': 'Manufacturing/Industry',
    'oem': 'Manufacturing/Industry',
    'construction': 'Manufacturing/Industry',
    'energy': 'Manufacturing/Industry',
    'semiconductor': 'Manufacturing/Industry',
    'utilities': 'Manufacturing/Industry',
    'old industry': 'Manufacturing/Industry',
    'telecom operator': 'Telecom/Communication',
    'isp': 'Telecom/Communication',
    'telecommunications': 'Telecom/Communication',
    'media': 'Media/Publishing',
    'publishing and technology': 'Media/Publishing',
    'publisher': 'Media/Publishing',
    'ecom retailer': 'ecommerce',
    'big tech': 'corporate',
    'faang': 'corporate',
    'multinational': 'corporate',
    'enterprise': 'corporate'
}

def segment_age(df,
                segment_col_name='age_segment',
                age_segments=['20-24', '25-29', '30-34', '35-39', '40s', '50+'],
                age_ranges=[20, 25, 30, 35, 40, 50, 120]):
    """
    Segments the age values in a DataFrame into predefined age groups.
    Args:
        df (pandas.DataFrame): The DataFrame containing the age column to be segmented.
        segment_col_name (str, optional): The name of the column to store the age segments. 
                                            Defaults to 'age_segment'.
        age_segments (list[str], optional): The labels for the age segments. 
                                            Defaults to ['20s', '30s', '40s', '50+'].
        age_ranges (list[int], optional): The age ranges to define the segments. 
                                            The values should be in ascending order.

    Returns:
        pandas.DataFrame: The DataFrame with an additional column storing the age segments.
    """
    df[segment_col_name] = pd.cut(df['Age'], bins=age_ranges, labels=age_segments)
    return df

def plot_pie_chart(df, column_name):
    
    plt.figure(figsize=(15, 8))
    value_counts = df[column_name].value_counts()
    labels = value_counts.index.tolist()
    sizes = value_counts.values.tolist()

    # Plotting the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') 
    plt.title(f'Frequency of {column_name}')
    plt.legend()
    plt.show()

def plot_pie_charts(df, analysis_column, division_column):
    
    plt.figure(figsize=(15, 8))
    analysis_categories = df[analysis_column].unique()
    for indx, category in enumerate(analysis_categories):
        plt.subplot(2, len(analysis_categories)//2, indx)
        category_mask = df[analysis_column == category]
        value_counts = df[category_mask][division_column].value_counts()
        labels = value_counts.index.tolist()
        sizes = value_counts.values.tolist()

        # Plotting the pie chart
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal') 
        plt.title(f'Frequency of {division_column} for {category}')
        plt.legend()
    plt.show()
