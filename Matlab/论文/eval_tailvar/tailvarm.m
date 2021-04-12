load('tailvar.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
%% phase
figure(1)
plot(freqs, unwrap(water_phase_f), 'o-', 'color', colors(1,:))
hold on
plot(freqs, unwrap(water_phase_t), '.-',  'color', colors(2,:))
plot(freqs, unwrap(water_phase_t1), '.-',  'color', colors(3,:))
plot(freqs, unwrap(water_phase_t2), '.-',  'color', colors(4,:))
hold off

legend('水-正', '水-反', '水-反1', '水-反2')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'tailvar_phase.pdf')
%% rssi
figure(2)
plot(freqs, unwrap(water_rssi_f), 'o-', 'color', colors(1,:))
hold on
plot(freqs, unwrap(water_rssi_t), '.-',  'color', colors(2,:))
plot(freqs, unwrap(water_rssi_t1), '.-',  'color', colors(3,:))
plot(freqs, unwrap(water_rssi_t2), '.-',  'color', colors(4,:))
hold off

legend('水-正', '水-反', '水-反1', '水-反2')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tailvar_rssi.pdf')
%% diff
figure(3)
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(water_phase_f) - unwrap(water_phase_t1), water_rssi_f - water_rssi_t1, 'o', 'color', colors(2,:))
plot(unwrap(water_phase_f) - unwrap(water_phase_t2), water_rssi_f - water_rssi_t2, 'o', 'color', colors(3,:))

hold off

legend( '水-反', '水-反1', '水-反2')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])


set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tailvar_feature.pdf')
%% bar
c = categorical({'反', '反1', '反2'});
c = reordercats(c, {'反', '反1', '反2'})
y = [0.98 1 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tailvar_accuracy.pdf')