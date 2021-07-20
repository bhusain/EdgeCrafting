import itertools

import numpy as np
from scipy import linalg
import pandas as pd
import matplotlib.pyplot as plt
import math
from random import randint

from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
import numpy as np
import json
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.metrics.cluster import normalized_mutual_info_score
import pandas as pd
from random import randint
from sklearn.metrics.cluster import adjusted_mutual_info_score
from sklearn.metrics.cluster import normalized_mutual_info_score

from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy.stats import gaussian_kde
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from scipy.stats import kde
from mpl_toolkits.mplot3d import Axes3D


from sklearn import mixture

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
from sklearn import metrics

d = dict()

data = pd.read_csv("kidney_GEM.txt", sep='\t')
data = data.iloc[:, 1:]
data = data.transpose()
data = data.fillna(0)
data = data.fillna(0)
data[data < 0] = 0
global_max = data.max().max()
global_min = data.min().min()

print(data.shape, global_max, global_min)

data_annot = pd.read_csv("kidney-labels.txt", sep='\t')


print(data_annot.shape)

labels = data_annot.iloc[:,1]

c = []

for i in labels:
    if i == 'kich-tumor-tcga':
        c.append('g')
    if i == 'kich-normal-tcga':
        c.append('b')
    if i == 'kidney-gtex':
        c.append('b')
    if i == 'kirc-normal-tcga':
        c.append('b')
    if i == 'kirc-tumor-tcga':
        c.append('r')
    if i == 'kirp-normal-tcga':
        c.append('b')
    if i == 'kirp-tumor-tcga':
        c.append('y')
bins = 2 * int(math.ceil(global_max))
print(bins)

count = 0

threshold = int(.7 * 927)


f = open('kidney_blob.csv', 'w')

print(len(data))


g1 = open('kidney_blob_25.txt', 'r')


for x in g1:
    a_list = x.split(',')
    i = int(a_list[0])
    j = int(a_list[1])
    #for j in range(i+1, 19215):
    if 1>0:
        count_i = sum(m > 0 for m in data.ix[:,i])
        if count_i > threshold:
            count_j = sum(n > 0 for n in data.ix[:,j])
            if count_j > threshold:
                N = np.c_[data.ix[:,i], data.ix[:,j]]
                k = np.zeros(bins * bins)
                for l,m in zip(N[:,0], N[:,1]):
                    if l > 0 and m > 0:
                        sum_l = l - math.floor(l)
                        sum_m = m - math.floor(m)
                        if sum_l < 0.5:
                            ind_l = math.floor(l) * 2
                        else:
                            ind_l = (math.floor(l) * 2) + 1
                        if sum_m < 0.5:
                            ind_m = math.floor(m) * 2
                        else:
                            ind_m = (math.floor(m) * 2) + 1
                        ind = int((ind_l * bins) + ind_m)
                        k[ind] = k[ind] + 1
                k = np.interp(k, (k.min(), k.max()), (0, +1))
                test = np.reshape(k, (bins,bins))
                #blobs_log = blob_log(test, min_sigma=1, max_sigma=10, num_sigma=10, threshold=.01)
                #blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
                blobs_dog = blob_dog(test, max_sigma=5, threshold=.25)
                blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)
                value = normalized_mutual_info_score(N[:, 0], N[:, 1])
                #blobs_doh = blob_doh(test, max_sigma=10, threshold=.01)
                #if len(blobs_log) > 1 or len(blobs_dog) > 1 or len(blobs_doh) > 1:
                if len(blobs_dog) > 1 and value > 0.95:
                    print(i,j)
                    blobs_list = [blobs_dog]
                    colors = ['yellow', 'lime', 'red']
                    titles = ['Difference of Gaussian']
                    sequence = zip(blobs_list, colors, titles)
                    fig, axes = plt.subplots(2, 1, figsize=(9, 8))
                    ax = axes.ravel()
                    for idx, (blobs, color, title) in enumerate(sequence):
                        ax[idx].set_title(title)
                        ax[idx].imshow(test)
                        for blob in blobs:
                            y, x, r = blob
                            cam = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
                            ax[idx].add_patch(cam)
                        ax[idx].set_axis_off()
                    plt.tight_layout()
                    plt.subplot(212)
                    plt.scatter(N[:,1], N[:,0], 5, alpha = .5, color = c)
                    plt.xlim(0, global_max)
                    plt.ylim(0, global_max)
                    plt.title(str(value))
                    plt.show()
                    #fig.savefig('./results2/'+str(data.columns.values[i]) + '_' + str(data.columns.values[j]) + '.png')
                    #string_val = '%s,%s,%s,%s,%0.3f\n' % (str(i), str(j), str(data.columns.values[i]), str(data.columns.values[j]), value)
                    #f.write(string_val)
                    #f.flush()
