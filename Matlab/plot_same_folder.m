function [] = plot_same_folder(folder, file_pattern, liquids, markers)
    for i = 1 : length(liquids)
        f = fullfile(folder, sprintf(file_pattern, liquids(i)));
        load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI');

        figure(1); plot3(DISTANCE, CHANNEL, PHASE, markers(2*i-1 : 2*i));hold on;
        figure(2); plot3(DISTANCE, CHANNEL, RSSI, markers(2*i-1 : 2*i));hold on;
    end

    figure(1); title("PHASE"); xlabel("distance"); ylabel("channel"); legend(liquids); hold off
    figure(2); title("RSSI"); xlabel("distance"); ylabel("channel"); legend(liquids); hold off
end

