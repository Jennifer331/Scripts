load('train.mat')

freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
matls = ["water", "vinegar", "milk", "yogurt", "oil", "liquor"];
markers = [".", "x", "s", "o", "^", "d"];
%% PHASE
figure(1)
hold on
for i=1:6
    eval(sprintf("plot(freqs, unwrap(%s_phase_f), markers(%d), 'color', colors(%d,:))", matls(i), i, i))
end
hold off
%% diff
figure(3)
for i=1:6
    eval(sprintf("plot(unwrap(%s_phase_f) - unwrap(%s_phase_t), %s_rssi_f - %s_rssi_t, markers(%d), 'color', colors(%d,:), 'MarkerSize', 10)", matls(i),matls(i), matls(i), matls(i), i, i))
    hold on
end
hold off
set(gca, 'FontSize', 20)
legend('水', '醋', '牛奶', '酸奶', '油', '白酒')
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\train_data.pdf')