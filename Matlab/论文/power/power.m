% load('power.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');

f = 6.0;
t = 6.0;
oil_f = '.-';
oil_t = '.--';
color_f = 1;
color_t = 2;
figure(1)
plot(freqs, unwrap(oil_p27_phase_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(oil_p27_phase_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(oil_p30_phase_f), '.-',  'color', colors(color_f,:))
plot(freqs, unwrap(oil_p30_phase_t), '.-', 'color', colors(color_t,:))

plot(freqs, unwrap(oil_phase_f), 'x-', 'color', colors(color_f,:))
plot(freqs, unwrap(oil_phase_t), 'x-', 'color', colors(color_t,:))

% water = 's-';
% plot(freqs, unwrap(water_p27_phase_f), water,  'color', colors(1,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_p27_phase_t), water,  'color', colors(1,:))
% 
% plot(freqs, unwrap(water_p30_phase_f), water,  'color', colors(2,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_p30_phase_t), water, 'color', colors(2,:))
% 
% plot(freqs, unwrap(water_phase_f), water, 'color', colors(3,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_phase_t), water, 'color', colors(3,:))
hold off

legend('油-27.5dBm-正', '油-27.5dBm-反', '油-30.0dBm-正', '油-30.0dBm-反',...
    '油-32.5dBm-正', '油-32.5dBm-反')
% ,'水-27.5dBm-正','水-27.5dBm-反', ...
%     '水-30.0dBm-正', '水-30.0dBm-反','水-32.5dBm-正', '水-32.5dBm-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

%% RSSI
figure(2)
f = 6.0;
t = 6.0;
oil_f = '.-';
oil_t = '.--';
color_f = 1;
color_t = 2;
plot(freqs, unwrap(oil_p27_rssi_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(oil_p27_rssi_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(oil_p30_rssi_f), '.-',  'color', colors(color_f,:))
plot(freqs, unwrap(oil_p30_rssi_t), '.-', 'color', colors(color_t,:))

plot(freqs, unwrap(oil_rssi_f), 'x-', 'color', colors(color_f,:))
plot(freqs, unwrap(oil_rssi_t), 'x-', 'color', colors(color_t,:))

hold off

legend('油-27.5dBm-正', '油-27.5dBm-反', '油-30.0dBm-正', '油-30.0dBm-反',...
    '油-32.5dBm-正', '油-32.5dBm-反')
% ,'水-27.5dBm-正','水-27.5dBm-反', ...
%     '水-30.0dBm-正', '水-30.0dBm-反','水-32.5dBm-正', '水-32.5dBm-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')
%% diff
figure(3)
markersize = 3;
plot(unwrap(oil_p27_phase_f) - unwrap(oil_p27_phase_t), oil_p27_rssi_f - oil_p27_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(oil_p30_phase_f) - unwrap(oil_p30_phase_t), oil_p30_rssi_f - oil_p30_rssi_t, 'o', 'color', colors(2,:))
plot(unwrap(oil_phase_f) - unwrap(oil_phase_t), oil_rssi_f - oil_rssi_t, 'o', 'color', colors(3, :))

plot(unwrap(water_p27_phase_f) - unwrap(water_p27_phase_t), water_p27_rssi_f - water_p27_rssi_t, '^', 'color', colors(1,:))
plot(unwrap(water_p30_phase_f) - unwrap(water_p30_phase_t), water_p30_rssi_f - water_p30_rssi_t, '^', 'color', colors(2,:))
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, '^', 'color', colors(3,:))
hold off

legend('油-27.5dBm', '油-30.0dBm', '油-32.5dBm', '水-27.5dBm', '水-30.0dBm', '水-32.5dBm')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])
%% bar
c = categorical({'油-32.5dBm', '油-30.0dBm', '油-27.5dBm', '水-32.5dBm', '水-30.0dBm', '水-27.5dBm'});
c = reordercats(c, {'油-32.5dBm', '油-30.0dBm', '油-27.5dBm', '水-32.5dBm', '水-30.0dBm', '水-27.5dBm'})
y = [1, 1, 1, 0.9, 0.92, 0.96];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'power_accuracy.pdf')