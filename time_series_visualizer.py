import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("/workspace/boilerplate-page-view-time-series-visualizer/fcc-forum-pageviews.csv", parse_dates=[0])

# Clean data
df = df.loc[(df["value"]>=df["value"].quantile(0.025)) & (df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    fig=df.plot(figsize=(16, 6),x="date",y="value",title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019",xlabel="Date",ylabel="Page Views",legend=False, color="red")
    fig=fig.figure
# Draw line plot




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Months"]=df_bar["date"].dt.strftime("%Y %B")
    df_bar=df_bar.groupby("Months").mean()
    df_bar=df_bar.reset_index()
    df_bar["Months"]=pd.to_datetime(df_bar["Months"])
    df_bar["Years"]=pd.to_datetime(df_bar["Months"])
    df_bar["Months"]=df_bar["Months"].dt.strftime("%B")
    df_bar["Years"]=df_bar["Years"].dt.strftime("%Y")
    s=pd.Series(["January","February","March","April","May","June","July","August","September","October","November","December"])
    df_bar["Months"] = pd.Categorical(df_bar["Months"],categories=s,ordered=True)
    df_bar=df_bar.pivot(index = 'Years', columns = 'Months', values = 'value')

    # Draw bar plot
    fig=df_bar.plot(kind="bar",ylabel="Average Page Views")
    fig=fig.figure
    


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = [d.year for d in df_box.date]
    df_box['Month'] = [d.strftime('%b') for d in df_box.date]
    df_box=df_box.rename(columns={"value":"Page Views"})

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    sns.boxplot(data=df_box,x="Year",y="Page Views",hue="Year",fliersize=1,ax=axs[0], legend==False,palette="tab10").set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box,x="Month",y="Page Views",hue="Month",fliersize=1,ax=axs[1],order=("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"),palette="husl").set_title("Month-wise Box Plot (Seasonality)")
    fig=fig.figure



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
