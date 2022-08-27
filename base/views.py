from django.shortcuts import render
import pickle
from numpy import array
import numpy as np


def home (request):
    return render(request,'base/home.html')

def result(request):

    #loading the model
    with open('model_pkl', 'rb') as f:
        model = pickle.load(f)
    values=[]

    values.append(np.int(request.GET.get('Gender')))
    values.append(np.int(request.GET.get('Age')))
    values.append(np.int(request.GET.get('smoke')))
    values.append(np.int(request.GET.get('fingers')))
    values.append(np.int(request.GET.get('ANXIETY')))
    values.append(np.int(request.GET.get('Peer pressure')))
    values.append(np.int(request.GET.get('chronic disease')))
    values.append(np.int(request.GET.get('fatigue')))
    values.append(np.int(request.GET.get('Allergy')))
    values.append(np.int(request.GET.get('wheezing')))
    values.append(np.int(request.GET.get('alcohol')))
    values.append(np.int(request.GET.get('COUGHING')))
    values.append(np.int(request.GET.get('SHORTNESS OF BREATH')))
    values.append(np.int(request.GET.get('SWALLOWING DIFFICULTY')))
    values.append(np.int(request.GET.get('CHEST PAIN')))
    values[1]=(values[1]-62.20942028985507)/8.964160843770156

    print(values)
    values = array(values).reshape(1, -1)
    res= model.predict(values)
    print(res)

    f_res=""
    if(res == 1): f_res = " you have high probability of having lunge cancer"
    else: f_res = " you are fine and disqualified of having lunge cancer "
    print(f_res)
    context = {'f_res': f_res}
    return render(request,'base/result.html',context)
