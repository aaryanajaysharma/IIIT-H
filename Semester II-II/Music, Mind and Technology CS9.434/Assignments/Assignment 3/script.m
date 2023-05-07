%% Question 1
fs = 44100
input = mirgetdata(miraudio('guitar.wav','sampling',44100),'frame',0.15)
%%
% soundsc(input,fs)

% filter function takes arguments as coefficients of x, y and the audio
% file respectively
% Num - fstop : 450 fpass: 600
Y = filter(Num,1,input);
% soundsc(Y,fs)
% pause
%%
fdatool
%%
soundsc(input,fs)
%%
soundsc(Y,fs)
%% Question 2:
input1 = mirgetdata(miraudio('guitar.wav','sampling',44100));
array = [1 zeros(1,11024) 0.5];
feedforward_filter = filter(array, 1, input1);
%%
fvtool(array, 1);
%% 
soundsc(feedforward_filter, fs);
%% Question 3: 
guitar = mirgetdata(miraudio('guitar.wav','sampling',22050));
x_array = [1];
y_array1 = [1 zeros(1,4410) 0.7];
y_array2 = [1 zeros(1,6615) 0.7];
feedback_filter_100 = filter(x_array, y_array1, input);
feedback_filter_150 = filter(x_array, y_array2, input);
%% 
soundsc(feedback_filter_100, fs);
%%
soundsc(feedback_filter_150, fs);
%% Question 4

R = 1 - (((2*3.14*50)/44100)/2);

theta = (2 * 3.14 * 440) /44100;
cos_theta = (2*R)/(1+(R^2)) * cos(theta);
A0 = (1 +(R^2)) * sin(theta);
a1 = 2 * R * cos(theta);
a2 = R ^ 2;

B = [1];
A = [1 -a1 a2];

resonant_filter = filter(B,A,input);
%%
fvtool(B,A);

%% Question 5
%Part 1
sampling_rate = 44100;
time = 0:1/sampling_rate:2;
freq1 = 400;
freq2 = 1000;
%general formula : Amplitude*sin(2*pi*freq*time)
figure(1),clf
signal1 =  sin(2*pi*time*freq1);
signal2 =  sin(2*pi*time*freq2);
signalf = signal1+signal2;
plot(time,signalf)
xlabel('time')
title('Wave Before Attenuation')
%Part2
R = 1 - (((2*3.14*50)/44100)/2);
theta = (2 * 3.14 * 1000) /44100;
cos_theta = (2*R)/(1+(R^2)) * cos(theta);
A0 = (1 +(R^2)) * sin(theta);
a1 = 2 * R * cos(theta);
a2 = R ^ 2;

B = [1];
A = [1 -a1 a2];

notch_filter = filter(A,B,signalf);
%%
plot(time, notch_filter)
xlabel('time')
title('Wave After Attenuation')
%%
fvtool(A, B)
%%
plot(abs(fft(signalf)))