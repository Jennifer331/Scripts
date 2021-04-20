load('tag.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];

colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% ��λ
figure(1)
plot(freqs, unwrap(water_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(water_phase_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(watertag_phase_f), 'x-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(watertag_phase_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('��ǩ1-��', '��ǩ1-��', '��ǩ2-��', '��ǩ2-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tag_phase.pdf')
%% RSSI
figure(2)
plot(freqs, water_rssi_f, 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, water_rssi_t, 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, watertag_rssi_f, 'x-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, watertag_rssi_t, 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('��ǩ1-��', '��ǩ1-��', '��ǩ2-��', '��ǩ2-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)
% 
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tag_rssi.pdf')
%% diff
figure(3)
markersize = 3;
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, 'o', 'color', colors(1,:), 'MarkerSize', 10)
hold on
plot(unwrap(watertag_phase_f) - unwrap(watertag_phase_t), watertag_rssi_f - watertag_rssi_t, '^', 'color', colors(2,:), 'MarkerSize', 10)

plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '*', 'color', colors(1,:), 'MarkerSize', 10)
hold off

set(gca, 'FontSize', 20)
legend('��ǩ1-ˮ', '��ǩ2-ˮ', '��ǩ1-��')
xlabel('��λ��/��rad��', 'FontSize', 30)
ylabel('�����ź�ǿ�Ȳ�/��dB��', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tag_feature.pdf')
%% bar
c = categorical({'ˮ-��ǩ1', 'ˮ-��ǩ2'});
y = [0.98, 0.82];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('׼ȷ��', 'FontSize', 30)
ylim([0 1.1])
set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tag_accuracy.pdf')