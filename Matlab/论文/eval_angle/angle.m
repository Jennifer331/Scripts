% load('angle.mat')
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
plot(freqs, unwrap(d101_oil_phase_t), 'o--',  'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d102_oil_phase_f), '.-',  'color', colors(color_f,:))
% plot(freqs, unwrap(d102_oil_phase_t), '.-', 'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d103_oil_phase_f), '>-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d103_oil_phase_t), '>-', 'color', colors(color_t,:))

plot(freqs, unwrap(d104_oil_phase_f), 's-', 'color', colors(color_f,:))
plot(freqs, unwrap(d104_oil_phase_t), 's--', 'color', colors(color_t,:))

% plot(freqs, unwrap(d105_oil_phase_f), 'd-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d105_oil_phase_t), 'd-', 'color', colors(color_t,:))
hold off

% legend('0��-��', '0��-��', '8��-��', '8��-��', '16��-��', '16��-��', ...
%     '24��-��', '24��-��', '32��-��', '32��-��', '40��-��', '40��-��')

% legend('0��-��', '0��-��', '8��-��', '8��-��', '32��-��', '32��-��')
set(gca, 'FontSize', 20)
legend('0��-��', '0��-��', '32��-��', '32��-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\angle_phase.pdf')

%% RSSI
figure(2)
% plot(freqs, unwrap(d11_oil_rssi_f), 'x-', 'color', colors(color_f,:))
% hold on
% plot(freqs, unwrap(d11_oil_rssi_t), 'x-', 'color', colors(color_t,:))

plot(freqs, unwrap(d101_oil_rssi_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(d101_oil_rssi_t), 'o--',  'color', colors(color_t,:))

% plot(freqs, unwrap(d102_oil_rssi_f), '.-',  'color', colors(color_f,:))
% plot(freqs, unwrap(d102_oil_rssi_t), '.-', 'color', colors(color_t,:))
% 
% plot(freqs, unwrap(d103_oil_rssi_f), '>-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d103_oil_rssi_t), '>-', 'color', colors(color_t,:))

plot(freqs, unwrap(d104_oil_rssi_f), 's-', 'color', colors(color_f,:))
plot(freqs, unwrap(d104_oil_rssi_t), 's--', 'color', colors(color_t,:))

% plot(freqs, unwrap(d105_oil_rssi_f), 'd-', 'color', colors(color_f,:))
% plot(freqs, unwrap(d105_oil_rssi_t), 'd-', 'color', colors(color_t,:))
hold off

% legend('0��-��', '0��-��', '8��-��', '8��-��', '16��-��', '16��-��', ...
%     '24��-��', '24��-��', '32��-��', '32��-��', '40��-��', '40��-��')

% legend('0��-��', '0��-��', '8��-��', '8��-��', '32��-��', '32��-��')
set(gca, 'FontSize', 20)
legend('0��-��', '0��-��', '32��-��', '32��-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\angle_rssi.pdf')
%% diff
figure(3)
dists = [101, 102, 103, 104, 105];
markers = ['.' 'o' 's' '*' '+' 'x'];
for i = 1:5
    eval(sprintf("plot(unwrap(d%d_oil_phase_f) - unwrap(d%d_oil_phase_t), d%d_oil_rssi_f - d%d_oil_rssi_t, markers(%d), 'color', colors(%d,:))", dists(i),dists(i), dists(i), dists(i), i, i))
    hold on
end

markers = ['<' '>' '^' 'v' 'd' 'p'];
for i = 1:5
    eval(sprintf("plot(unwrap(d%d_water_phase_f) - unwrap(d%d_water_phase_t), d%d_water_rssi_f - d%d_water_rssi_t, markers(%d), 'color', colors(%d,:))", dists(i),dists(i), dists(i), dists(i), i, i))
end
% plot(unwrap(oil_p30_phase_f) - unwrap(oil_p30_phase_t), oil_p30_rssi_f - oil_p30_rssi_t, 'o', 'color', colors(2,:))
% plot(unwrap(oil_phase_f) - unwrap(oil_phase_t), oil_rssi_f - oil_rssi_t, 'o', 'color', colors(3, :))
% 
% plot(unwrap(water_p27_phase_f) - unwrap(water_p27_phase_t), water_p27_rssi_f - water_p27_rssi_t, '^', 'color', colors(1,:))
% plot(unwrap(water_p30_phase_f) - unwrap(water_p30_phase_t), water_p30_rssi_f - water_p30_rssi_t, '^', 'color', colors(2,:))
% plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, '^', 'color', colors(3,:))
hold off

% legend('0��', '8��', '16��',  '24��',  '32��')

% legend('0��', '8��', '16��',  '24��',  '32��')
set(gca, 'FontSize', 20)
legend('0��-��', '8��-��', '16��-��',  '24��-��',  '32��-��', '0��-ˮ', '8��-ˮ', '16��-ˮ',  '24��-ˮ',  '32��-ˮ')
xlabel('��λ��/��rad��', 'FontSize', 30)
ylabel('�����ź�ǿ�Ȳ�/��dB��', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\angle_feature.pdf')

%% bar
c = categorical({'0��-��', '8��-��', '16��-��',  '24��-��',  '32��-��', '0��-ˮ', '8��-ˮ', '16��-ˮ',  '24��-ˮ',  '32��-ˮ'});
c = reordercats(c, {'0��-��', '8��-��', '16��-��',  '24��-��',  '32��-��', '0��-ˮ', '8��-ˮ', '16��-ˮ',  '24��-ˮ',  '32��-ˮ'});
y = [1, 1, 1, 1, 1, 1, 1, 0.98, 1, 1];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('׼ȷ��', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\angle_accuracy.pdf')