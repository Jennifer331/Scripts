load('cola.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
%% phase
figure(1)
plot(freqs, unwrap(cola_phase_f), 'r-')
hold on
plot(freqs, unwrap(cola_phase_t), 'r--')
plot(freqs, unwrap(colanosugar_phase_f), 'k-')
plot(freqs, unwrap(colanosugar_phase_t), 'k--')
hold off

legend('可乐-正', '可乐-反', '无糖可乐-正', '无糖可乐-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_phase.pdf')
%% rssi
plot(freqs, cola_rssi_f, 'r-')
hold on
plot(freqs, cola_rssi_t, 'r--')
plot(freqs, colanosugar_rssi_f, 'k-')
plot(freqs, colanosugar_rssi_t, 'k--')
hold off

legend('可乐-正', '可乐-反', '无糖可乐-正', '无糖可乐-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_rssi.pdf')
%% diff
figure(3)
plot(unwrap(cola_phase_f) - unwrap(cola_phase_t), cola_rssi_f - cola_rssi_t, 'ro')
hold on
plot(unwrap(d1_cola_phase_f) - unwrap(d1_cola_phase_t), d1_cola_rssi_f - d1_cola_rssi_t, 'r^')
plot(unwrap(d6_cola_phase_f) - unwrap(d6_cola_phase_t), d6_cola_rssi_f - d6_cola_rssi_t, 'r*')

plot(unwrap(colanosugar_phase_f) - unwrap(colanosugar_phase_t), colanosugar_rssi_f - colanosugar_rssi_t, 'ko')
plot(unwrap(d1_colanosugar_phase_f) - unwrap(d1_colanosugar_phase_t), d1_colanosugar_rssi_f - d1_colanosugar_rssi_t, 'k^')
plot(unwrap(d6_colanosugar_phase_f) - unwrap(d6_colanosugar_phase_t), d6_colanosugar_rssi_f - d6_colanosugar_rssi_t, 'k*')
hold off

legend('可乐-位置1', '可乐-位置2', '可乐-位置3', '无糖可乐-位置1', '无糖可乐-位置2', '无糖可乐-位置3')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_feature.pdf')
%% bar
c = categorical({'位置1-可乐', '位置1-无糖可乐','位置2-可乐', '位置2-无糖可乐','位置3-可乐', '位置3-无糖可乐'});
c = reordercats(c, {'位置1-可乐', '位置1-无糖可乐','位置2-可乐', '位置2-无糖可乐','位置3-可乐', '位置3-无糖可乐'});
y = [1 1 1 1 0.98 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'cola_accuracy.pdf')