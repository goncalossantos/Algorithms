#!pip install netcdf4
#!pip install matplotlib
#%matplotlib inline

import requests
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4
from dateutil.relativedelta import relativedelta
import datetime
import os


DATASET_URL = 'https://crudata.uea.ac.uk/cru/data/temperature/HadCRUT.4.5.0.0.median.nc'
VARIABLE_NAME = 'temperature_anomaly'
ALPHA = 0.3


class DatasetFile():
    """ Handles the context for the dataset file because we need to delete in the end"""

    def __init__(self, url, mode):
        self.url = url
        self.local_filename = b''
        self.mode = mode

    def __enter__(self):

        self.local_filename = self._download_dataset_file()
        self.dataset_file = self._open_dataset()
        return self.dataset_file

    def __exit__(self, *args):
        self.dataset_file.close()
        try:
            os.remove(self.local_filename)
        except OSError:
            pass

    def _open_dataset(self):
        return nc4.Dataset(self.local_filename, self.mode, format='NETCDF4')

    def _download_dataset_file(self):

        # We only store the file in the file system because there is no python library to read this
        # type other than netCDF4 and that one needs a file name... Remember to
        # destroy the file
        local_filename = self.url.split('/')[-1]
        r = requests.get(self.url, stream=True)
        if not r.ok:
            r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename


def get_time_axis(dataset):
    # We will do year by year
    # We need the number of measurements, the base date and the end date to be
    # thorough
    number_measurements = f.dimensions['time'].size
    base = datetime.date(f.variables['time'].start_year, f.variables[
                         'time'].start_month, 1)
    end = datetime.date(f.variables['time'].end_year, f.variables[
                        'time'].end_month, 1)
    axis = [base + relativedelta(months=+x)
            for x in range(0, number_measurements)]
    # Check correctness of axis
    assert len(axis) == number_measurements
    assert axis[-1] == end
    return axis


def remove_masked_values(variable_raw_values):

    return np.ma.MaskedArray(variable_raw_values, mask=variable_raw_values.mask)


def get_global_monthly_mean(dataset):

    # We need to remove all the masked values
    values = remove_masked_values(dataset.variables[VARIABLE_NAME][:])
    # Mean alongside one axis

    mean_axis1_per_month = values.mean(axis=1)
    # do the mean of the mean
    global_mean_per_month = mean_axis1_per_month.mean(axis=1)
    return global_mean_per_month


def get_global_yearly_mean(monthly_mean):

    aux_list = []
    while monthly_mean.any():
        v = monthly_mean[:12]
        aux_list.append(v.mean())
        monthly_mean = monthly_mean[12:]

    return np.array(aux_list)


def exponential_moving_average(values):
    # I'm assuming a static database. If it was dinamic and
    # real time an iterator would be a better solution
    # than calculating in batch

    exp = np.empty([len(values) + 1, ])

    for i, v in enumerate(values):
        s = ALPHA * v + (1 - ALPHA) * exp[i]
        exp[i + 1] = s
    exp = exp[1:]
    return exp


def plot_values(figure, datetime_list, values, exp_avg, title):

    dates = matplotlib.dates.date2num(datetime_list)

    # Monthly graphic
    fig = plt.figure(figure)
    plt.plot_date(dates, values, 'b.')
    plt.plot_date(dates, exp_avg, 'g-', label="EWMA")
    plt.plt.xlabel('Time')
    plt.ylabel('Temperature Anomalies (delta of Celcius)')
    plt.title(title)
    fig.autofmt_xdate()


with DatasetFile(DATASET_URL, 'r') as f:
    time = get_time_axis(f)
    monthly_mean = get_global_monthly_mean(f)
    exp_avg = exponential_moving_average(monthly_mean)
    yearly_mean = get_global_yearly_mean(monthly_mean)
    y_exp_avg = exponential_moving_average(yearly_mean)
    plot_values(0, time, monthly_mean, exp_avg, "Monthly Global Mean")

    plot_values(1, time[::12], yearly_mean, y_exp_avg, "Yearly Global Mean")
    plt.show()
