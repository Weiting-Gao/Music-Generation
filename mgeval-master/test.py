import midi
import glob
import numpy as np
import pretty_midi
import seaborn as sns
import matplotlib.pyplot as plt
from mgeval import core, utils
from sklearn.model_selection import LeaveOneOut

set1 = glob.glob('/Users/gwt/Documents/njit/course/dl/project/Music-Generation-master/train/*.mid')

num_samples = 5

set1_eval = {'total_used_pitch':np.zeros((num_samples,1)),'bar_used_pitch':np.zeros((num_samples,1)),
			'total_used_note':np.zeros((num_samples,1)),'bar_used_note':np.zeros((num_samples,1)),
			'total_pitch_class_histogram':np.zeros((num_samples,1)),'bar_pitch_class_histogram':np.zeros((num_samples,1)),
			'pitch_class_transition_matrix':np.zeros((num_samples,1)),'pitch_range':np.zeros((num_samples,1)),
			'avg_pitch_shift':np.zeros((num_samples,1)),'avg_IOI':np.zeros((num_samples,1)),
			'note_length_hist':np.zeros((num_samples,1)),'note_length_transition_matrix':np.zeros((num_samples,1))}

metrics_list = list(set1_eval.keys())



for i in range(0, num_samples):
    #print(i)
    feature = core.extract_feature(set1[i])
    #print(type(feature['midi_pattern'].resolution))
    print(getattr(core.metrics(), metrics_list[1])(feature))

    #set1_eval[metrics_list[0]][i] = getattr(core.metrics(), metrics_list[0])(feature)
    #print(i)
    #set1_eval[metrics_list[1]][i] = getattr(core.metrics(), metrics_list[1])(feature)
    #set1_eval[metrics_list[2]][i] = getattr(core.metrics(), metrics_list[2])(feature)
    #set1_eval[metrics_list[3]][i] = getattr(core.metrics(), metrics_list[3])(feature)
    #set1_eval[metrics_list[4]][i] = getattr(core.metrics(), metrics_list[4])(feature)
    #set1_eval[metrics_list[5]][i] = getattr(core.metrics(), metrics_list[5])(feature)
    #set1_eval[metrics_list[6]][i] = getattr(core.metrics(), metrics_list[6])(feature)
    #set1_eval[metrics_list[7]][i] = getattr(core.metrics(), metrics_list[7])(feature)
    #set1_eval[metrics_list[8]][i] = getattr(core.metrics(), metrics_list[8])(feature)
    #set1_eval[metrics_list[9]][i] = getattr(core.metrics(), metrics_list[9])(feature)
    #set1_eval[metrics_list[10]][i] = getattr(core.metrics(), metrics_list[10])(feature)
    #set1_eval[metrics_list[11]][i] = getattr(core.metrics(), metrics_list[11])(feature)