load('cola.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 'r';
color_t = 'k';
dists =[1 6 7];
markers = ["o-", "*-", ".-"];
%% Phase
figure(1)
for i=1:2
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_f), markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
hold on
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_t), markers(%d)+'-', 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_f), markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_t), markers(%d)+'-', 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
end
hold off
set(gca, 'FontSize', 20)
legend('有糖-位置1-正', '有糖-位置1-反', '无糖-位置1-正', '无糖-位置1-反', '有糖-位置2-正', '有糖-位置2-反', '无糖-位置2-正', '无糖-位置2-反')
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\cola_phase.pdf')
%% RSSI
figure(2)
for i=1:2
    eval(sprintf("plot(freqs, d%d_cola_rssi_f, markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    hold on
    eval(sprintf("plot(freqs, d%d_cola_rssi_t, markers(%d)+'-', 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_f, markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_t, markers(%d)+'-', 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
end
hold off
set(gca, 'FontSize', 20)
legend({'有糖-位置1-正', '有糖-位置1-反', '无糖-位置1-正', '无糖-位置1-反',...
    '有糖-位置2-正', '有糖-位置2-反', '无糖-位置2-正', '无糖-位置2-反'}, 'Location','northwest','NumColumns',2)
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('接收信号强度/（dBm）', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\cola_rssi.pdf')
%% diff
figure(3)

markers = ["o", "^",  "*", "p", ".", "<"];
for i=1:3
    eval(sprintf("plot(unwrap(d%d_cola_phase_f) - unwrap(d%d_cola_phase_t), d%d_cola_rssi_f - d%d_cola_rssi_t, markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i),dists(i), dists(i), dists(i), 2*i-1))
    hold on
    eval(sprintf("plot(unwrap(d%d_colanosugar_phase_f) - unwrap(d%d_colanosugar_phase_t), d%d_colanosugar_rssi_f - d%d_colanosugar_rssi_t, markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i),dists(i), dists(i), dists(i), 2*i))
end
hold off
set(gca, 'FontSize', 20)
legend('位置1-有糖', '位置1-无糖', '位置2-有糖', '位置2-无糖', '位置3-有糖', '位置3-无糖')
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\cola_feature.pdf')

%% bar
c = categorical({'位置1-可乐', '位置1-无糖可乐','位置2-可乐', '位置2-无糖可乐','位置3-可乐', '位置3-无糖可乐'});
c = reordercats(c, {'位置1-可乐', '位置1-无糖可乐','位置2-可乐', '位置2-无糖可乐','位置3-可乐', '位置3-无糖可乐'});
y = [1 1 1 1 0.98 1];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('准确率', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\cola_accuracy.pdf')