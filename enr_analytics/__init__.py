import matplotlib

# Define functions removing right and top border chartarea border
def removeLines(ax) :
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

# Define function saving a plot
def savePlot(path) :
    matplotlib.pyplot.savefig(path + '.png', bbox_inches = 'tight', dpi = 300)
    matplotlib.pyplot.savefig(path + '.pdf', bbox_inches = 'tight')

# Set matplotlib template
def initialChartConfig() :
    matplotlib.pyplot.style.use('https://raw.githubusercontent.com/mikolajolszewski/enr_analytics/master/enr_analytics/enr_analytics.mplstyle')
    matplotlib.rcParams['font.family'] = 'Open Sans'