function [] = plot_diff_folder(folder, labels, file_pattern, liquids, markers)
    legends = strings(length(folder)*length(markers), 1);
    for i = 1 : length(liquids)
        f = fullfile(folder(1), sprintf(file_pattern(1), liquids(i)));
        load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI');

        figure(1); plot3(DISTANCE, CHANNEL, PHASE, "m"+markers(i)); hold on;
        figure(2); plot3(DISTANCE, CHANNEL, RSSI, "m"+markers(i)); hold on;
        legends(2*i-1) = labels(1) + "-"+liquids(i);
        
        f = fullfile(folder(2), sprintf(file_pattern(2), liquids(i)));
        load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI');

        figure(1); plot3(DISTANCE, CHANNEL, PHASE, "k"+markers(i));hold on;
        figure(2); plot3(DISTANCE, CHANNEL, RSSI, "k"+markers(i));hold on;
        legends(2*i) = labels(2) + "-"+liquids(i);
    end

    figure(1); title("PHASE"); xlabel("distance"); ylabel("channel"); legend(legends); hold off
    figure(2); title("RSSI"); xlabel("distance"); ylabel("channel"); legend(legends); hold off
    
end

