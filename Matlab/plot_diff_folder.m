function [] = plot_diff_folder(folder, file_pattern, liquids, markers)
    i=1;
    for i = 1 : length(liquids)
        f = fullfile(folder(1), sprintf(file_pattern(1), liquids(i)));
        load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI');

        figure(1); plot3(DISTANCE, CHANNEL, PHASE, markers(i:i+1)); hold on;
        figure(2); plot3(DISTANCE, CHANNEL, RSSI, markers(i:i+1)); hold on;
        
        i=i+1;
        f = fullfile(folder(2), sprintf(file_pattern(2), liquids(i)));
        load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI');

        figure(1); plot3(DISTANCE, CHANNEL, PHASE, markers(i:i+1));hold on;
        figure(2); plot3(DISTANCE, CHANNEL, RSSI, markers(i:i+1));hold on;
        
        i=i+1;
    end

    figure(1); title("PHASE"); xlabel("distance"); ylabel("channel");  hold off
    figure(2); title("RSSI"); xlabel("distance"); ylabel("channel"); hold off
end

