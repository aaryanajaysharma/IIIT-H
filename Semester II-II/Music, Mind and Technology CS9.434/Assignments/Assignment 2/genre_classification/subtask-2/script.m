for k = 55:99
    name = sprintf('rock.000%d.wav', k)
    a = mirgetdata(mirspectrum(miraudio(name),'Frame',0.5)); %Get the spectrogram assuming you are using a frame length of 500ms (which you must change by the way) and default overlap
    time_frames=size(a,2); %this tells you the number of frames
    for m=1:time_frames,
    for n=1:time_frames,
    Vi=a(:,m);
    Vj=a(:,n);
    D(m,n)=sum(Vi.*Vj)./(sqrt(sum(Vi.^2))*sqrt(sum(Vj.^2)));
    end
    end
    imagesc(D) %this will allow you to view your similarity matrix
    title('')
    xlabel('')
    ylabel('')
    xticks('')
    yticks('')
    save_song = sprintf('rock%d.png', k)
    exportgraphics(gca,save_song)

end