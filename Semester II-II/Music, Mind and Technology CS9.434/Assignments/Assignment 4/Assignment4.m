%% Quesiton 1
down_factor = 2
pulse_clarity = mirgetdata(mirpulseclarity('fmri_music_stimulus.mp3','Frame',3,0.33))
%pulse_clarity = mirgetdata(mirpulseclarity('fmri_music_stimulus.mp3','Frame',3,0.33))
%%

%%
g = fmri_doublegamma(0:1:25)
plot(g)
%%
conv_pulse = conv(pulse_clarity,g)
down_conv_pulse = downsample(conv_pulse, down_factor)
down_pulse_clarity = downsample(pulse_clarity, down_factor)
%figure, plot(pulse_clarity),hold on, plot(conv_pulse)
%%
detrend_pulse = fmri_detrend(conv_pulse)
down_detrend_pulse = downsample(detrend_pulse, down_factor)
figure, plot(down_pulse_clarity),hold on, plot(down_conv_pulse), plot(down_detrend_pulse)
%%
% RMS PART
rms = mirgetdata(mirrms('fmri_music_stimulus.mp3','Frame',0.25,0.5))
%%
conv_rms = conv(rms,g)
figure, plot(rms),hold on, plot(conv_rms)
%%
detrend_rms= fmri_detrend(conv_rms)
figure, plot(rms),hold on, plot(conv_rms), plot(detrend_rms)
%%
down_factor = 2
down_rms = downsample(rms, down_factor)
down_conv_rms = downsample(conv_rms, down_factor)
down_detrend_rms = downsample(detrend_rms, down_factor)
%%
figure, plot(down_rms),hold on, plot(down_conv_rms), plot(down_detrend_rms)
%% Question 2. a 
% Load 2 participants at a time
%%
load('mus16.mat');
%%
load('mus17.mat');
%%
load('mus18.mat');
%%
load('mus19.mat');
%%
load('mus20.mat');
%%
matrix = zeros(vox_no, 1);
for n=1:vox_no
    matrix(n) = corr(m16(n,:)', m17(n, :)');
end
%%

%% Question 2. b

load('musicalfeatures.mat')
% Storing all the features in variable features
features = feat{1,1}
%%
% Storing the required features in the separate variables
brightness = features(:,2)
brightness = transpose(brightness)

pul_clarity = features(:,5)
pul_clarity = transpose(pul_clarity)
%%
% Loading the participants from musicians group
% The data is stored in variables named as m<file_number>
load('nonmus01.mat')
%%
load('nonmus02.mat')
%%
load('nonmus03.mat')
%%
load('nonmus04.mat')
%%
load('nonmus05.mat')
%% 
% Finding corrgressors for each of the feature
c1_1 = fmri_corregressor(brightness',m1)
c1_2 = fmri_corregressor(pul_clarity',m1)
%%
% Plot them for the participant
fmri_show3d(c1_1 > 0.32) % highest correlation for brightness for P1
%%
fmri_show3d(c1_1 < -0.32) % lowest correlation for brigthness for P1
%%
fmri_show3d(c1_2 > 0.28) % highest correlation for pulse clarity for P1
%%
fmri_show3d(c1_2 < -0.30) % lowest correlation for pulse clarity for P1