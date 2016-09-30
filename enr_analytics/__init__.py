# Define functions removing right and top border chartarea border
def removeLines() :
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

# Define function saving a plot
def savePlot(path) :
    plt.savefig(path + '.png', bbox_inches = 'tight', dpi = 300)
    plt.savefig(path + '.pdf', bbox_inches = 'tight')

# Set matplotlib template
def initialChartConfig() :
    plt.style.use('https://raw.githubusercontent.com/mikolajolszewski/end_analytics/master/enr_analytics/enr_analytics.mplstyle')
    matplotlib.rcParams['font.family'] = 'Open Sans'