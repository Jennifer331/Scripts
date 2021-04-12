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

legend('��ת0��-��', '��ת0��-��', '��ת5��-��', '��ת5��-��', '��ת10��-��', '��ת10��-��', '��ת15��-��', '��ת15��-��')
xlabel('Ƶ��/��MHz��')
ylabel('��λ/��rad��')

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
legend('��ת0��-��', '��ת0��-��', '��ת5��-��', '��ת5��-��', '��ת10��-��', '��ת10��-��', '��ת15��-��', '��ת15��-��')
xlabel('Ƶ��/��MHz��')
ylabel('�����ź�ǿ��/��dBm��')

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

legend('ˮ-��ת0��', 'ˮ-��ת5��', 'ˮ-��ת10��', 'ˮ-��ת15��', '��-��ת0��')
xlabel('��λ��/��rad��')
ylabel('�����ź�ǿ�Ȳ�/��dB��')
xlim([-6.28, 6.28])
ylim([-6, 3])


set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_feature.pdf')
%% bar
c = categorical({'��ת0��', '��ת5��', '��ת10��', '��ת15��'});
c = reordercats(c, {'��ת0��', '��ת5��', '��ת10��', '��ת15��'})
y = [1, 0.18, 0.44, 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('׼ȷ��')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'tagrotate_accuracy.pdf')