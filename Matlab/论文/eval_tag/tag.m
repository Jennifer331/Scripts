load('tag.mat')
load('vinegar.mat')
freqs = [902.75:0.5:927.25];

colors = get(gca, 'ColorOrder');
color_f = 1;
color_t = 2;
%% ��λ
figure(1)
plot(freqs, unwrap(water_phase_f), 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, unwrap(water_phase_t), 'o-',  'color', colors(color_t,:))

plot(freqs, unwrap(watertag_phase_f), 'x-',  'color', colors(color_f,:))
plot(freqs, unwrap(watertag_phase_t), 'x-', 'color', colors(color_t,:))
hold off

legend('��ǩ1-��', '��ǩ1-��', '��ǩ2-��', '��ǩ2-��')
xlabel('Ƶ��/��MHz��')
ylabel('��λ/��rad��')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'tag_phase.pdf')
%% RSSI
figure(2)
plot(freqs, water_rssi_f, 'o-', 'color', colors(color_f,:))
hold on
plot(freqs, water_rssi_t, 'o-',  'color', colors(color_t,:))

plot(freqs, watertag_rssi_f, 'x-',  'color', colors(color_f,:))
plot(freqs, watertag_rssi_t, 'x-', 'color', colors(color_t,:))
hold off

legend('��ǩ1-��', '��ǩ1-��', '��ǩ2-��', '��ǩ2-��')
xlabel('Ƶ��/��MHz��')
ylabel('�����ź�ǿ��/��rad��')

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_rssi.pdf')
%% diff
figure(3)
markersize = 3;
plot(unwrap(water_phase_f) - unwrap(water_phase_t), water_rssi_f - water_rssi_t, 'o', 'color', colors(1,:))
hold on
plot(unwrap(watertag_phase_f) - unwrap(watertag_phase_t), watertag_rssi_f - watertag_rssi_t, 'o', 'color', colors(2,:))

plot(unwrap(v_phase_f) - unwrap(v_phase_t), v_rssi_f - v_rssi_t, '^', 'color', colors(1,:))
hold off

legend('��ǩ1-ˮ', '��ǩ2-ˮ', '��ǩ1-��')
xlabel('��λ��/��rad��')
ylabel('�����ź�ǿ�Ȳ�/��dB��')
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_feature.pdf')
%% bar
c = categorical({'ˮ-��ǩ1', 'ˮ-��ǩ2'});
y = [0.98, 0.82];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('׼ȷ��')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tag_accuracy.pdf')