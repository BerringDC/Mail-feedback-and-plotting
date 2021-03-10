import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import (YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
import seaborn as sns
sns.set()


# from sftp_aws imp

pd.options.display.max_rows = 10


def plot_profile(df_tow, filename):
    df_down = df_tow[df_tow['type'] == 2].reset_index(drop=True)
    df_up = df_tow[df_tow['type'] == 1][::-1].reset_index(drop=True)

    coltem = plt.cm.get_cmap('autumn_r')
    coldep = plt.cm.get_cmap('Blues_r')

    # plot discrepancy temperatures over time
    fig, ax = plt.subplots(figsize=(10, 16))

    mintem_row = df_down.loc[df_down['temperature'].idxmin()]
    mintem = mintem_row['temperature']
    dep_mintem = mintem_row['pressure']

    # get the row of max value
    maxtem_row = df_down.loc[df_down['temperature'].idxmax()]
    maxtem = maxtem_row['temperature']
    dep_maxtem = maxtem_row['pressure']

    plt.plot(df_down['temperature'], -df_down['pressure'], 'green', label='down profile')

    tem = plt.scatter(df_down['temperature'], -df_down['pressure'], c=df_down['temperature'],
                      cmap='rainbow', label='temperature')
    min_tem = plt.scatter(mintem, -dep_mintem, c='blue')
    plt.annotate(round(mintem, 3), (mintem, -dep_mintem))
    max_tem = plt.scatter(maxtem, -dep_maxtem, c='green')
    plt.annotate(round(maxtem, 3), (maxtem, -dep_maxtem))

    mintem_row1 = df_up.loc[df_up['temperature'].idxmin()]
    mintem1 = mintem_row1['temperature']
    dep_mintem1 = mintem_row1['pressure']

    # get the row of max value
    maxtem_row1 = df_up.loc[df_up['temperature'].idxmax()]
    maxtem1 = maxtem_row1['temperature']
    dep_maxtem1 = maxtem_row1['pressure']

    plt.plot(df_up['temperature'], -df_up['pressure'], 'purple', label='up profile')
    tem1 = plt.scatter(df_up['temperature'], -df_up['pressure'], c=df_up['temperature'], cmap='rainbow')
    print(mintem1, dep_mintem1)
    min_tem = plt.scatter(mintem1, -dep_mintem1, c='blue')
    plt.annotate(round(mintem1, 3), (mintem1, -dep_mintem1))
    max_tem = plt.scatter(maxtem1, -dep_maxtem1, c='green')
    plt.annotate(round(maxtem1, 3), (maxtem1, -dep_maxtem1))

    ax.set_xlabel("Temperature (ºC)")
    ax.set_ylabel("Depth (meters)")

    plt.suptitle("Profile down temperature vs pressure comparison")
    plt.legend()
    # plt.gca().invert_yaxis()

    plt.savefig('/home/ec2-user/mail_reports/overview/Images/' + filename.split('.')[0] + '.png')

    plt.show()

    #
    #
    #
    #
    #
    # if len(df_down) > 0:
    #     fig, ax = plt.subplots(figsize=(5, 8))
    #
    #     # plot up and downs temperatures over pressure
    #
    #     mintem_row = df_down.loc[df_down['temperature'].idxmin()]
    #     mintem = mintem_row['temperature']
    #     dep_mintem = mintem_row['pressure']
    #
    #     # get the row of max value
    #     maxtem_row = df_down.loc[df_down['temperature'].idxmax()]
    #     maxtem = maxtem_row['temperature']
    #     dep_maxtem = maxtem_row['pressure']
    #
    #     tem = plt.scatter(df_down['temperature'], -df_down['pressure'], c=df_down['temperature'], cmap='rainbow',
    #                       label='temperature')
    #     min_tem = plt.scatter(mintem, -dep_mintem, c='blue')
    #     plt.annotate(round(mintem, 3), (mintem, -dep_mintem))
    #     max_tem = plt.scatter(maxtem, -dep_maxtem, c='green')
    #     plt.annotate(round(maxtem, 3), (maxtem, -dep_maxtem))
    #     #             clb = plt.colorbar(tem)
    #     #             clb.ax.set_title('Temp (°C)')
    #
    #     ax.set_xlim(df_down['temperature'].min() - 1.5, df_down['temperature'].max() + 1.5)
    #     ax.set_ylim(0, -df_down['pressure'].max() - 2)
    #
    #     ax.set_xlabel("Temperature (ºC)")
    #     ax.set_ylabel("Depth (meters)")
    #
    #     plt.suptitle("Profile down temperature vs pressure comparison")
    #
    #     plt.gca().invert_yaxis()
    #
    #     plt.savefig('/home/ec2-user/mail_reports/overview/Images/' + self.filename.split('.')[0] + '_down.png')
    #     plt.show()
    #     plt.close()
    #
    #
    #
    # if len(df_up) > 0:
    #     fig, ax = plt.subplots(figsize=(5, 8))
    #
    #     # plot up and downs temperatures over pressure
    #
    #     mintem_row = df_up.loc[df_up['temperature'].idxmin()]
    #     mintem = mintem_row['temperature']
    #     dep_mintem = mintem_row['pressure']
    #
    #     # get the row of max value
    #     maxtem_row = df_up.loc[df_up['temperature'].idxmax()]
    #     maxtem = maxtem_row['temperature']
    #     dep_maxtem = maxtem_row['pressure']
    #
    #     tem = plt.scatter(df_up['temperature'], -df_up['pressure'], c=df_up['temperature'], cmap='rainbow',
    #                       label='temperature')
    #     min_tem = plt.scatter(mintem, -dep_mintem, c='blue')
    #     plt.annotate(round(mintem, 3), (mintem, -dep_mintem))
    #     max_tem = plt.scatter(maxtem, -dep_maxtem, c='green')
    #     plt.annotate(round(maxtem, 3), (maxtem, -dep_maxtem))
    #     #             clb = plt.colorbar(tem)
    #     #             clb.ax.set_title('Temp (°C)')
    #
    #     ax.set_xlabel("Temperature (ºC)")
    #     ax.set_ylabel("Depth (meters)")
    #
    #     ax.set_xlim(df_up['temperature'].min() - 1.5, df_up['temperature'].max() + 1.5)
    #     ax.set_ylim(0, -df_up['pressure'].max() - 2)
    #
    #     plt.suptitle("Profile up temperature vs pressure comparison")
    #
    #     plt.gca().invert_yaxis()
    #
    #     #             plt.legend()
    #     plt.savefig('/home/ec2-user/mail_reports/overview/Images/' + self.filename.split('.')[0] + '_up.png')
    #     plt.show()
    #     plt.close()
