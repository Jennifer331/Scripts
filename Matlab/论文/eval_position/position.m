% load('oil_d678.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% PHASE
figure(1)
plot(freqs, unwrap(d6_oil_phase_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(d6_oil_phase_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(d7_oil_phase_f), '.-',  'color', colors(color_f,:))
plot(freqs, unwrap(d7_oil_phase_t), '.-', 'color', colors(color_t,:))

plot(freqs, unwrap(d8_oil_phase_f), 'x-', 'color', colors(color_f,:))
plot(freqs, unwrap(d8_oil_phase_t), 'x-', 'color', colors(color_t,:))
hold off

legend('位置1-正', '位置1-反','位置2-正', '位置2-反', '位置3-正', '位置3-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'dist_phase.pdf')
%% RSSI
figure(2)
plot(freqs, unwrap(d6_oil_rssi_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(d6_oil_rssi_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(d7_oil_rssi_f), '.-',  'color', colors(color_f,:))
plot(freqs, unwrap(d7_oil_rssi_t), '.-', 'color', colors(color_t,:))

plot(freqs, unwrap(d8_oil_rssi_f), 'x-', 'color', colors(color_f,:))
plot(freqs, unwrap(d8_oil_rssi_t), 'x-', 'color', colors(color_t,:))
hold off

legend('位置1-正', '位置1-反','位置2-正', '位置2-反', '位置3-正', '位置3-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'dist_rssi.pdf')
%% diff
figure(3)
plot(unwrap(d6_oil_phase_f) - unwrap(d6_oil_phase_t), d6_oil_rssi_f - d6_oil_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(d7_oil_phase_f) - unwrap(d7_oil_phase_t), d7_oil_rssi_f - d7_oil_rssi_t, 'o', 'color', colors(2,:))
plot(unwrap(d8_oil_phase_f) - unwrap(d8_oil_phase_t), d8_oil_rssi_f - d8_oil_rssi_t, 'o', 'color', colors(3,:))

hold off

legend('位置1', '位置2', '位置3')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'dist_feature.pdf')
%% bar
c = categorical({'位置1', '位置2', '位置3'});
c = reordercats(c, {'位置1', '位置2', '位置3'})
y = [1, 1, 0.62];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'position_accuracy.pdf')