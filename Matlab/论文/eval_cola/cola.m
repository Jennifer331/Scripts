load('cola.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
%% phase
figure(1)
plot(freqs, unwrap(cola_phase_f), 'r-')
hold on
plot(freqs, unwrap(cola_phase_t), 'r--')
plot(freqs, unwrap(colanosugar_phase_f), 'k-')
plot(freqs, unwrap(colanosugar_phase_t), 'k--')
hold off

legend('����-��', '����-��', '���ǿ���-��', '���ǿ���-��')
xlabel('Ƶ��/��MHz��')
ylabel('��λ/��rad��')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_phase.pdf')
%% rssi
plot(freqs, cola_rssi_f, 'r-')
hold on
plot(freqs, cola_rssi_t, 'r--')
plot(freqs, colanosugar_rssi_f, 'k-')
plot(freqs, colanosugar_rssi_t, 'k--')
hold off

legend('����-��', '����-��', '���ǿ���-��', '���ǿ���-��')
xlabel('Ƶ��/��MHz��')
ylabel('�����ź�ǿ��/��dBm��')

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_rssi.pdf')
%% diff
figure(3)
plot(unwrap(cola_phase_f) - unwrap(cola_phase_t), cola_rssi_f - cola_rssi_t, 'ro')
hold on
plot(unwrap(d1_cola_phase_f) - unwrap(d1_cola_phase_t), d1_cola_rssi_f - d1_cola_rssi_t, 'r^')
plot(unwrap(d6_cola_phase_f) - unwrap(d6_cola_phase_t), d6_cola_rssi_f - d6_cola_rssi_t, 'r*')

plot(unwrap(colanosugar_phase_f) - unwrap(colanosugar_phase_t), colanosugar_rssi_f - colanosugar_rssi_t, 'ko')
plot(unwrap(d1_colanosugar_phase_f) - unwrap(d1_colanosugar_phase_t), d1_colanosugar_rssi_f - d1_colanosugar_rssi_t, 'k^')
plot(unwrap(d6_colanosugar_phase_f) - unwrap(d6_colanosugar_phase_t), d6_colanosugar_rssi_f - d6_colanosugar_rssi_t, 'k*')
hold off

legend('����-λ��1', '����-λ��2', '����-λ��3', '���ǿ���-λ��1', '���ǿ���-λ��2', '���ǿ���-λ��3')
xlabel('��λ��/��rad��')
ylabel('�����ź�ǿ�Ȳ�/��dB��')
xlim([-6.28, 6.28])
ylim([-6, 3])

% set(gcf, 'PaperPosition', [0 0 16 12])
% set(gcf, 'PaperSize', [16 12])
% saveas(gcf, 'cola_feature.pdf')
%% bar
c = categorical({'λ��1-����', 'λ��1-���ǿ���','λ��2-����', 'λ��2-���ǿ���','λ��3-����', 'λ��3-���ǿ���'});
c = reordercats(c, {'λ��1-����', 'λ��1-���ǿ���','λ��2-����', 'λ��2-���ǿ���','λ��3-����', 'λ��3-���ǿ���'});
y = [1 1 1 1 0.98 1];
bar(c, y)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center'); 
ylabel('׼ȷ��')
ylim([0 1.05])

set(gcf, 'PaperPosition', [0 0 16 12])
set(gcf, 'PaperSize', [16 12])
saveas(gcf, 'cola_accuracy.pdf')