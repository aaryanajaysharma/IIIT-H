x = 0.1;
y = 0.2;
z = '.png';
%filename = '13.wav'

dirname = strcat(string(x),  , string(y))

chrom = mirchromagram(filename, 'Frame', x, y)
figurename = strcat('Chromagram ', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
mkdir(dirname)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
cd('..')

spect = mirspectrum(filename, 'Frame', x, y)
figurename = strcat('Spectrum ', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
cd('..')

mfcc = mirmfcc(filename, 'Frame', x, y)
figurename = strcat('MFCC ', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
cd('..')

mirsimatrix(chrom)
figurename = strcat('Simatrix Chromagram ', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
cd('..')

mirsimatrix(spect)
figurename = strcat('Simatrix Spectrum ', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
cd('..')
mirsimatrix(mfcc)
figurename = strcat('Simatrix  MFCC', ' Frame Length ', string(x), ' Hop Length ', string(y), z)
cd(dirname)
exportgraphics(gca, figurename, 'Resolution', 150)
