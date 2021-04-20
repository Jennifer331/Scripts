% load('water.mat')
plot(water_d, water_r, 'x', 'MarkerSize', 10)
hold on
plot(waterp_d, waterp_r, 'o', 'MarkerSize', 10)
plot(waterant_d, waterant_r, '^', 'MarkerSize', 10)
plot(water2_d, water2_r, 's', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
xlabel('����/��cm��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)

legend('ˮ', 'ˮ-�ظ�', 'ˮ-����2', 'ˮ2')

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\�о���\��ҵ���\����\ͼ\�ػ�\water_replicate.pdf')