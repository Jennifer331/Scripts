load('power.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
%%
f = 6.0;
t = 6.0;
oil_f = '.-';
oil_t = '.--';
color_f = 1;
color_t = 2;
figure(1)
plot(freqs, unwrap(oil_p27_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(oil_p27_phase_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(oil_p30_phase_f), '.-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(oil_p30_phase_t), '.--', 'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(oil_phase_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(oil_phase_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)

% water = 's-';
% plot(freqs, unwrap(water_p27_phase_f), water,  'color', colors(1,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_p27_phase_t), water,  'color', colors(1,:))
% 
% plot(freqs, unwrap(water_p30_phase_f), water,  'color', colors(2,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_p30_phase_t), water, 'color', colors(2,:))
% 
% plot(freqs, unwrap(water_phase_f), water, 'color', colors(3,:), 'MarkerSize', f)
% plot(freqs, unwrap(water_phase_t), water, 'color', colors(3,:))
hold off
set(gca, 'FontSize', 20)
legend('��-27.5dBm-��', '��-27.5dBm-��', '��-30.0dBm-��', '��-30.0dBm-��',...
    '��-32.5dBm-��', '��-32.5dBm-��')
% ,'ˮ-27.5dBm-��','ˮ-27.5dBm-��', ...
%     'ˮ-30.0dBm-��', 'ˮ-30.0dBm-��','ˮ-32.5dBm-��', 'ˮ-32.5dBm-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\power_oil_phase.pdf')
%% RSSI
figure(2)
f = 6.0;
t = 6.0;
oil_f = '.-';
oil_t = '.--';
color_f = 1;
color_t = 2;
plot(freqs, unwrap(oil_p27_rssi_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', 10)
hold on
plot(freqs, unwrap(oil_p27_rssi_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(oil_p30_rssi_f), '.-',  'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(oil_p30_rssi_t), '.--', 'color', colors(color_t,:), 'MarkerSize', 10)

plot(freqs, unwrap(oil_rssi_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', 10)
plot(freqs, unwrap(oil_rssi_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', 10)

hold off
set(gca, 'FontSize', 20)
legend({'��-27.5dBm-��', '��-27.5dBm-��', '��-30.0dBm-��', '��-30.0dBm-��',...
    '��-32.5dBm-��', '��-32.5dBm-��'},'Location','northwest','NumColumns',2)
% ,'ˮ-27.5dBm-��','ˮ-27.5dBm-��', ...
%     'ˮ-30.0dBm-��', 'ˮ-30.0dBm-��','ˮ-32.5dBm-��', 'ˮ-32.5dBm-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)
% 
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\power_oil_rssi.pdf')
%% diff
figure(3)
markersize = 3;
plot(unwrap(oil_p27_phase_f) - unwrap(oil_p27_phase_t), oil_p27_rssi_f - oil_p27_rssi_t, 'o', 'color', colors(1,:), 'MarkerSize', 10)
hold on
plot(unwrap(oil_p30_phase_f) - unwrap(oil_p30_phase_t), oil_p30_rssi_f - oil_p30_rssi_t, '*', 'color', colors(2,:), 'MarkerSize', 10)
plot(unwrap(oil_phase_f) - unwrap(oil_phase_t), oil_rssi_f - oil_rssi_t, 's', 'color', colors(3, :), 'MarkerSize', 10)

plot(unwrap(water_p27_phase_f) - unwrap(water_p27_phase_t), water_p27_rssi_f - water_p27_rssi_t, '^', 'color', colors(1,:), 'MarkerSize', 10)
plot(unwrap(water_p30_phase_f) - unwrap(water_p30_phase_t), water_p30_rssi_f - water_p30_rssi_t, 'p', 'color', colors(2,:), 'MarkerSize', 10)
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, '<', 'color', colors(3,:), 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
legend('��-27.5dBm', '��-30.0dBm', '��-32.5dBm', 'ˮ-27.5dBm', 'ˮ-30.0dBm', 'ˮ-32.5dBm')
xlabel('��λ��/��rad��', 'FontSize', 30)
ylabel('�����ź�ǿ�Ȳ�/��dB��', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])


% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\power_feature.pdf')
%% bar
c = categorical({'��-32.5dBm', '��-30.0dBm', '��-27.5dBm', 'ˮ-32.5dBm', 'ˮ-30.0dBm', 'ˮ-27.5dBm'});
c = reordercats(c, {'��-32.5dBm', '��-30.0dBm', '��-27.5dBm', 'ˮ-32.5dBm', 'ˮ-30.0dBm', 'ˮ-27.5dBm'})
y = [1, 1, 1, 0.9, 0.92, 0.96];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('׼ȷ��', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\power_accuracy.pdf')