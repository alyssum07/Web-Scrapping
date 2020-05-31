import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fig,ax = plt.subplots()

fig.patch.set_visible(False)
ax.axis("off")
def animate(i): 
    # fig,ax = plt.subplots()

    fig.patch.set_visible(False)
    ax.axis("off")
    #================Calls table==========================
    df = pd.read_csv("Call_Max_OI.csv")
    df1= pd.read_csv("Call_Max_negchnginOI.csv")
    df2= pd.read_csv("Call_Max_poschnginOI.csv")
    df3= pd.read_csv("Call_Max_volume.csv")

    df.update(df.select_dtypes(include=np.number).applymap('{:,}'.format))
    df1.update(df1.select_dtypes(include=np.number).applymap('{:,}'.format))
    df2.update(df2.select_dtypes(include=np.number).applymap('{:,}'.format))
    df3.update(df3.select_dtypes(include=np.number).applymap('{:,}'.format))
    # df['OI'] = df['OI'].map('{:,.2f}'.format)

    fig.tight_layout()
    
    colors = plt.cm.PuBuGn(np.linspace(0.1, 0.9, len(df)))
    ax.text(0.00690061, 0.860942, "Calls:-",size=35)
    ax.text(0.00690061, 0.386018, "Puts:-",size=35)
    tab1 = ax.table(cellText=df.values, colLabels=df.columns,
                            cellLoc='center',colColours=colors,bbox=[0.00690061, 0.568072, 0.2, 0.2])
    tab2 = ax.table(cellText=df1.values, colLabels=df1.columns,
                            cellLoc='center',colColours=colors,bbox=[0.248842, 0.568072, 0.2, 0.2])
    tab3 = ax.table(cellText=df2.values, colLabels=df2.columns,
                            cellLoc='center',colColours=colors,bbox=[0.493855, 0.568072, 0.2, 0.2])
    # tab2.scale(3,1.5)
    tab4 = ax.table(cellText=df3.values, colLabels=df3.columns,
                            cellLoc='center',colColours=colors,bbox=[0.742709, 0.568072, 0.2, 0.2])
    tab1.auto_set_font_size(False)
    tab1.set_fontsize(11)
    tab2.auto_set_font_size(False)
    tab2.set_fontsize(11)
    tab3.auto_set_font_size(False)
    tab3.set_fontsize(11)
    tab4.auto_set_font_size(False)
    tab4.set_fontsize(11)

    #===================Puts table============================
    f = pd.read_csv("Put_Max_OI.csv")
    f1= pd.read_csv("Put_Max_negchnginOI.csv")
    f2= pd.read_csv("Put_Max_poschnginOI.csv")
    f3 = pd.read_csv("Put_Max_Vol.csv")

    f.update(f.select_dtypes(include=np.number).applymap('{:,}'.format))
    f1.update(f1.select_dtypes(include=np.number).applymap('{:,}'.format))
    f2.update(f2.select_dtypes(include=np.number).applymap('{:,}'.format))
    f3.update(f3.select_dtypes(include=np.number).applymap('{:,}'.format))
    tab5 = ax.table(cellText=f.values, colLabels=f.columns,
                            cellLoc='center',colColours=colors,bbox=[0.00690061, 0.0714286, 0.2, 0.2])
    tab6 = ax.table(cellText=f1.values, colLabels=f1.columns,
                            cellLoc='center',colColours=colors,bbox=[0.248842, 0.0714286, 0.2, 0.2])
    # tab2.scale(3,1.5)
    tab7 = ax.table(cellText=f2.values, colLabels=f2.columns,
                            cellLoc='center',colColours=colors,bbox=[0.493855, 0.0714286, 0.2, 0.2])
    tab8 = ax.table(cellText=f3.values, colLabels=f3.columns,
                            cellLoc='center',colColours=colors,bbox=[0.742709, 0.0714286, 0.2, 0.2])
    tab5.auto_set_font_size(False)
    tab5.set_fontsize(11)
    tab6.auto_set_font_size(False)
    tab6.set_fontsize(11)
    tab7.auto_set_font_size(False)
    tab7.set_fontsize(11)
    tab8.auto_set_font_size(False)
    tab8.set_fontsize(11)
    # ax.annotate(f"Calls:-",
                # xy=(0.00690061, 0.939683), xytext=(0, 10))
                # xycoords=('axes fraction', 'figure fraction'),
                # textcoords='offset points',
                # size=20, ha='center', va='bottom',color = 'g')
    # plt.subplots_adjust(left=0.2, bottom=0.2)

    # tab2.auto_set_column_width(col=list(range(len(df.columns))))
    # props=tab2.properties()
    # print(props)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
