load('angle.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% PHASE
figure(1)
% plot(freqs, unwrap(d11_oil_phase_f), 'x-', 'color', colors(color_f,:))
% hold on
% plot(freqs, unwrap(d11_oil_phase_t), 'x-', 'color', colors(color_t,:))

plot(freqs, unwrap(d101_oil_phase_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(d101_oil_phase_t), 'o-',  'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d102_oil_phase_f), '.-',  'color', colors(color_f,:))
% plot(freqs, unwrap(d102_oil_phase_t), '.-', 'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d103_oil_phase_f), '>-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d103_oil_phase_t), '>-', 'color', colors(color_t,:))

plot(freqs, unwrap(d104_oil_phase_f), 's-', 'color', colors(color_f,:))
plot(freqs, unwrap(d104_oil_phase_t), 's-', 'color', colors(color_t,:))

% plot(freqs, unwrap(d105_oil_phase_f), 'd-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d105_oil_phase_t), 'd-', 'color', colors(color_t,:))
hold off

% legend('0°-正', '0°-反', '8°-正', '8°-反', '16°-正', '16°-反', ...
%     '24°-正', '24°-反', '32°-正', '32°-反', '40°-正', '40°-反')

% legend('0°-正', '0°-反', '8°-正', '8°-反', '32°-正', '32°-反')
legend('0°-正', '0°-反', '32°-正', '32°-反')
xlabel('频道/（MHz）')
ylabel('相位/（rad）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'angle_phase.pdf')

%% RSSI
figure(2)
% plot(freqs, unwrap(d11_oil_rssi_f), 'x-', 'color', colors(color_f,:))
% hold on
% plot(freqs, unwrap(d11_oil_rssi_t), 'x-', 'color', colors(color_t,:))

plot(freqs, unwrap(d101_oil_rssi_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(d101_oil_rssi_t), 'o-',  'color', colors(color_t,:))

% plot(freqs, unwrap(d102_oil_rssi_f), '.-',  'color', colors(color_f,:))
% plot(freqs, unwrap(d102_oil_rssi_t), '.-', 'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d103_oil_rssi_f), '>-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d103_oil_rssi_t), '>-', 'color', colors(color_t,:))

plot(freqs, unwrap(d104_oil_rssi_f), 's-', 'color', colors(color_f,:))
plot(freqs, unwrap(d104_oil_rssi_t), 's-', 'color', colors(color_t,:))

% plot(freqs, unwrap(d105_oil_rssi_f), 'd-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d105_oil_rssi_t), 'd-', 'color', colors(color_t,:))
hold off

% legend('0°-正', '0°-反', '8°-正', '8°-反', '16°-正', '16°-反', ...
%     '24°-正', '24°-反', '32°-正', '32°-反', '40°-正', '40°-反')

% legend('0°-正', '0°-反', '8°-正', '8°-反', '32°-正', '32°-反')
legend('0°-正', '0°-反', '32°-正', '32°-反')
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'angle_rssi.pdf')
%% diff
figure(3)
dists = [101, 102, 103, 104, 105];
for i = 1:5
    eval(sprintf("plot(unwrap(d%d_oil_phase_f) - unwrap(d%d_oil_phase_t), d%d_oil_rssi_f - d%d_oil_rssi_t, 'o', 'color', colors(%d,:))", dists(i),dists(i), dists(i), dists(i), i))
    hold on
end

for i = 1:5
    eval(sprintf("plot(unwrap(d%d_water_phase_f) - unwrap(d%d_water_phase_t), d%d_water_rssi_f - d%d_water_rssi_t, '^', 'color', colors(%d,:))", dists(i),dists(i), dists(i), dists(i), i))
end
% plot(unwrap(oil_p30_phase_f) - unwrap(oil_p30_phase_t), oil_p30_rssi_f - oil_p30_rssi_t, 'o', 'color', colors(2,:))
% plot(unwrap(oil_phase_f) - unwrap(oil_phase_t), oil_rssi_f - oil_rssi_t, 'o', 'color', colors(3, :))
% 
% plot(unwrap(water_p27_phase_f) - unwrap(water_p27_phase_t), water_p27_rssi_f - water_p27_rssi_t, '^', 'color', colors(1,:))
% plot(unwrap(water_p30_phase_f) - unwrap(water_p30_phase_t), water_p30_rssi_f - water_p30_rssi_t, '^', 'color', colors(2,:))
% plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, '^', 'color', colors(3,:))
hold off

% legend('0°', '8°', '16°',  '24°',  '32°')

% legend('0°', '8°', '16°',  '24°',  '32°')
legend('0°-油', '8°-油', '16°-油',  '24°-油',  '32°-油', '0°-水', '8°-水', '16°-水',  '24°-水',  '32°-水')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'angle_feature.pdf')

%% bar
c = categorical({'0°-油', '8°-油', '16°-油',  '24°-油',  '32°-油', '0°-水', '8°-水', '16°-水',  '24°-水',  '32°-水'});
c = reordercats(c, {'0°-油', '8°-油', '16°-油',  '24°-油',  '32°-油', '0°-水', '8°-水', '16°-水',  '24°-水',  '32°-水'});
y = [1, 1, 1, 1, 1, 1, 1, 0.98, 1, 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('准确率')
ylim([0 1.05])

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'angle_accuracy.pdf')