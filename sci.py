import scipy
#read file
from scipy.io import  wavfile
sr,ob=wavfile.read("audio_file.wav")
print(scipy.__version__)
print("sample rate:",sr)
print("data type:",ob.dtype)
print("data shape:",ob.shape)

if len(ob.shape)>1:
    left=ob[:,0]
    right=ob[:,1]
    print("sterio audio detected")
else:
    print("mono audio detected")