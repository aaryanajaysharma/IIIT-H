s = mirrms('folder')
x1 = mirgetdata(s)

p = mirpulseclarity('folder')
y1 = mirgetdata(p)

%%
m = mirrms('folder')
x2 = mirgetdata(m)

n = mirpulseclarity('folder')
y2 = mirgetdata(n)

%%
color1 = 'red';
color2 = 'green';

scatter(x1,y1, color1, "filled")
hold on
scatter(x2, y2, color2, "filled")
xlabel('rms')
ylabel('pulse_clarity')
title('rms v/s pulse_clarity')

%%
scatter(x1, y1, color1, "filled")
xlabel('tempo')
ylabel('low_energy')
title('tempo v/s low_energy')
