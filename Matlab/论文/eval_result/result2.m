load('train.mat')

freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
matls = ["water", "vinegar", "milk", "yogurt", "oil", "liquor"];
%% PHASE
figure(1)
hold on
for i=1:6
    eval(sprintf("plot(freqs, unwrap(%s_phase_f), 'o-', 'color', colors(%d,:))", matls(i), i))
end
hold off
%% diff
figure(3)
hold on
for i=1:6
    eval(sprintf("plot(unwrap(%s_phase_f) - unwrap(%s_phase_t), %s_rssi_f - %s_rssi_t, 'o', 'color', colors(%d,:))", matls(i),matls(i), matls(i), matls(i), i))
end
hold off
legend('水', '醋', '牛奶', '酸奶', '油', '白酒')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'train_data.pdf')