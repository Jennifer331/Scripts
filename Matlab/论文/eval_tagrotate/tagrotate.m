load('tagrotate.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% phase
markersize = 4;
figure(1)
plot(freqs, unwrap(r0_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', markersize)
hold on
plot(freqs, unwrap(r0_phase_t), 'o-',  'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r5_phase_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r5_phase_t), 'x-', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r10_phase_f), 's-',  'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r10_phase_t), 's-', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r15_phase_f), '>-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r15_phase_t), '>-', 'color', colors(color_t,:), 'MarkerSize', markersize)
hold off

legend('旋转0°-正', '旋转0°-反', '旋转5°-正', '旋转5°-反', '旋转10°-正', '旋转10°-反', '旋转15°-正', '旋转15°-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_phase.pdf')
%% rssi
figure(2)
plot(freqs, unwrap(r0_rssi_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', markersize)
hold on
plot(freqs, unwrap(r0_rssi_t), 'o-',  'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r5_rssi_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r5_rssi_t), 'x-', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r10_rssi_f), '>-',  'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r10_rssi_t), '>-', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r15_rssi_f), 's-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r15_rssi_t), 's-', 'color', colors(color_t,:), 'MarkerSize', markersize)
hold off
legend('旋转0°-正', '旋转0°-反', '旋转5°-正', '旋转5°-反', '旋转10°-正', '旋转10°-反', '旋转15°-正', '旋转15°-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_rssi.pdf')
%% diff
figure(3)
plot(unwrap(r0_phase_f) - unwrap(r0_phase_t), r0_rssi_f - r0_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(r5_phase_f) - unwrap(r5_phase_t), r5_rssi_f - r5_rssi_t, 'o', 'color', colors(2,:))
plot(unwrap(r10_phase_f) - unwrap(r10_phase_t), r10_rssi_f - r10_rssi_t, 'o', 'color', colors(3,:))
plot(unwrap(r15_phase_f) - unwrap(r15_phase_t), r15_rssi_f - r15_rssi_t, 'o', 'color', colors(4,:))


plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '^', 'color', colors(1,:))
hold off

legend('水-旋转0°', '水-旋转5°', '水-旋转10°', '水-旋转15°', '醋-旋转0°')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])


set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_feature.pdf')
%% bar
c = categorical({'旋转0°', '旋转5°', '旋转10°', '旋转15°'});
c = reordercats(c, {'旋转0°', '旋转5°', '旋转10°', '旋转15°'})
y = [1, 0.18, 0.44, 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_accuracy.pdf')