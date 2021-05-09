load('cola.mat')
freqs = [902.75:0.5:927.25];
colors = get(gca, 'ColorOrder');
color_f = 'r';
color_t = 'k';
dists =[1 6 7];
markers = ["o-", "*-", ".-"];
%% Phase
figure(1)
for i=1:2
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_f), markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
hold on
    eval(sprintf("plot(freqs, unwrap(d%d_cola_phase_t), markers(%d)+'-', 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_f), markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, unwrap(d%d_colanosugar_phase_t), markers(%d)+'-', 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
end
hold off
set(gca, 'FontSize', 20)
legend('����-λ��1-��', '����-λ��1-��', '����-λ��1-��', '����-λ��1-��', '����-λ��2-��', '����-λ��2-��', '����-λ��2-��', '����-λ��2-��')
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\cola_phase.pdf')
%% RSSI
figure(2)
for i=1:2
    eval(sprintf("plot(freqs, d%d_cola_rssi_f, markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    hold on
    eval(sprintf("plot(freqs, d%d_cola_rssi_t, markers(%d)+'-', 'color', colors(1,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_f, markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
    eval(sprintf("plot(freqs, d%d_colanosugar_rssi_t, markers(%d)+'-', 'color', colors(2,:), 'MarkerSize', 10)", dists(i), i))
end
hold off
set(gca, 'FontSize', 20)
legend({'����-λ��1-��', '����-λ��1-��', '����-λ��1-��', '����-λ��1-��',...
    '����-λ��2-��', '����-λ��2-��', '����-λ��2-��', '����-λ��2-��'}, 'Location','northwest','NumColumns',2)
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\cola_rssi.pdf')
%% diff
figure(3)

markers = ["o", "^",  "*", "p", ".", "<"];
for i=1:3
    eval(sprintf("plot(unwrap(d%d_cola_phase_f) - unwrap(d%d_cola_phase_t), d%d_cola_rssi_f - d%d_cola_rssi_t, markers(%d), 'color', colors(1,:), 'MarkerSize', 10)", dists(i),dists(i), dists(i), dists(i), 2*i-1))
    hold on
    eval(sprintf("plot(unwrap(d%d_colanosugar_phase_f) - unwrap(d%d_colanosugar_phase_t), d%d_colanosugar_rssi_f - d%d_colanosugar_rssi_t, markers(%d), 'color', colors(2,:), 'MarkerSize', 10)", dists(i),dists(i), dists(i), dists(i), 2*i))
end
hold off
set(gca, 'FontSize', 20)
legend('λ��1-����', 'λ��1-����', 'λ��2-����', 'λ��2-����', 'λ��3-����', 'λ��3-����')
xlabel('��λ��/��rad��', 'FontSize', 30)
ylabel('�����ź�ǿ�Ȳ�/��dB��', 'FontSize', 30)
xlim([-6.28, 6.28])
ylim([-6, 3])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\cola_feature.pdf')

%% bar
c = categorical({'λ��1-����', 'λ��1-���ǿ���','λ��2-����', 'λ��2-���ǿ���','λ��3-����', 'λ��3-���ǿ���'});
c = reordercats(c, {'λ��1-����', 'λ��1-���ǿ���','λ��2-����', 'λ��2-���ǿ���','λ��3-����', 'λ��3-���ǿ���'});
y = [1 1 1 1 0.98 1];
set(gca, 'FontSize', 20)
bar(c, y)
set(gca, 'FontSize', 20)
text(1:length(y), y, num2str(y'),'vert','bottom','horiz','center', 'FontSize', 20); 
ylabel('׼ȷ��', 'FontSize', 30)
ylim([0 1.1])

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\cola_accuracy.pdf')