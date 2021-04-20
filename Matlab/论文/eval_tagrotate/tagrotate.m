load('tagrotate.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% phase
markersize = 10;
figure(1)
plot(freqs, unwrap(r0_phase_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', markersize)
hold on
plot(freqs, unwrap(r0_phase_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r5_phase_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r5_phase_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r10_phase_f), 's-',  'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r10_phase_t), 's--', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r15_phase_f), '>-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r15_phase_t), '>--', 'color', colors(color_t,:), 'MarkerSize', markersize)
hold off
set(gca, 'FontSize', 20)
legend('��ת0��-��', '��ת0��-��', '��ת5��-��', '��ת5��-��', '��ת10��-��', '��ת10��-��', '��ת15��-��', '��ת15��-��')
xlabel('Ƶ��/��MHz��')
ylabel('��λ/��rad��')

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tagrotate_phase.pdf')
%% rssi
figure(2)
plot(freqs, unwrap(r0_rssi_f), 'o-', 'color', colors(color_f,:), 'MarkerSize', markersize)
hold on
plot(freqs, unwrap(r0_rssi_t), 'o--',  'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r5_rssi_f), 'x-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r5_rssi_t), 'x--', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r10_rssi_f), '>-',  'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r10_rssi_t), '>--', 'color', colors(color_t,:), 'MarkerSize', markersize)

plot(freqs, unwrap(r15_rssi_f), 's-', 'color', colors(color_f,:), 'MarkerSize', markersize)
plot(freqs, unwrap(r15_rssi_t), 's--', 'color', colors(color_t,:), 'MarkerSize', markersize)
hold off

set(gca, 'FontSize', 20)
legend({'��ת0��-��', '��ת0��-��', '��ת5��-��', '��ת5��-��', '��ת10��-��', '��ת10��-��', '��ת15��-��', '��ת15��-��'}, 'Location', 'northwest', 'NumColumns', 4)
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)
% 
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tagrotate_rssi.pdf')
%% diff
figure(3)
plot(unwrap(r0_phase_f) - unwrap(r0_phase_t), r0_rssi_f - r0_rssi_t, 's', 'color', colors(1,:))
hold on
plot(unwrap(r5_phase_f) - unwrap(r5_phase_t), r5_rssi_f - r5_rssi_t, 'o', 'color', colors(2,:))
plot(unwrap(r10_phase_f) - unwrap(r10_phase_t), r10_rssi_f - r10_rssi_t, 'x', 'color', colors(3,:))
plot(unwrap(r15_phase_f) - unwrap(r15_phase_t), r15_rssi_f - r15_rssi_t, '^', 'color', colors(4,:))


plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '^', 'color', colors(1,:))
hold off

set(gca, 'FontSize', 20)
legend('ˮ-��ת0��', 'ˮ-��ת5��', 'ˮ-��ת10��', 'ˮ-��ת15��', '��-��ת0��')
xlabel('��λ��/��rad��', 'FontSize', 30)
ylabel('�����ź�ǿ�Ȳ�/��dB��', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

% 
% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tagrotate_feature.pdf')
%% bar
c = categorical({'��ת0��', '��ת5��', '��ת10��', '��ת15��'});
c = reordercats(c, {'��ת0��', '��ת5��', '��ת10��', '��ת15��'})
y = [1, 0.18, 0.44, 1];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('׼ȷ��', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\tagrotate_accuracy.pdf')