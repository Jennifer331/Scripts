load('cola.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 'r';
color_t = 'k';
dists =[1 6 7];
markers = ["o-", "*", ".-"];
%% Phase
figure(1)
hold on
for i=1:2
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_f), markers(%d), 'color', colors(1,:))", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_t), markers(%d), 'color', colors(1,:), 'MarkerSize', 3)", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_f), markers(%d), 'color', colors(2,:))", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_t), markers(%d), 'color', colors(2,:), 'MarkerSize', 3)", dists(i), i))
end
hold off
legend('有糖-位置1-正', '有糖-位置1-反', '无糖-位置1-正', '无糖-位置1-反', '有糖-位置2-正', '有糖-位置2-反', '无糖-位置2-正', '无糖-位置2-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'cola_phase2.pdf')
%% RSSI
figure(2)
for i=1:2
    eval(sprintf("plot(freqs, d%d_cola_rssi_f, markers(%d), 'color', colors(1,:))", dists(i), i))
    hold on
    eval(sprintf("plot(freqs, d%d_cola_rssi_t, markers(%d), 'color', colors(1,:), 'MarkerSize', 3)", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_f, markers(%d), 'color', colors(2,:))", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_t, markers(%d), 'color', colors(2,:), 'MarkerSize', 3)", dists(i), i))
end
hold off
legend('有糖-位置1-正', '有糖-位置1-反', '无糖-位置1-正', '无糖-位置1-反', '有糖-位置2-正', '有糖-位置2-反', '无糖-位置2-正', '无糖-位置2-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_rssi2.pdf')
%% diff
figure(3)

markers = ["o", "*", "^"];
hold on
for i=1:3
    eval(sprintf("plot(unwrap(d%d_cola_phase_f) - unwrap(d%d_cola_phase_t), d%d_cola_rssi_f - d%d_cola_rssi_t, markers(%d), 'color', colors(1,:))", dists(i),dists(i), dists(i), dists(i), i))
    eval(sprintf("plot(unwrap(d%d_colanosugar_phase_f) - unwrap(d%d_colanosugar_phase_t), d%d_colanosugar_rssi_f - d%d_colanosugar_rssi_t, markers(%d), 'color', colors(2,:))", dists(i),dists(i), dists(i), dists(i), i))
end
hold off
legend('位置1-有糖', '位置1-无糖', '位置2-有糖', '位置2-无糖', '位置3-有糖', '位置3-无糖')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'cola_feature2.pdf')