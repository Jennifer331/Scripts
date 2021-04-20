load('kde.mat')

figure(1)
plot(dirty_c, dirty_r, 'x', 'MarkerSize', 10)
hold on
% plot(kde_c, kde_r, 'o', 'MarkerSize', 7, 'filled')
scatter(kde_c, kde_r, 'filled')
plot(truth_c, truth_r, 'o', 'MarkerSize', 12)
hold off
set(gca, 'FontSize', 20)
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('�����ź�ǿ��/��dBm��', 'FontSize', 30)
legend('��·�˸��ŵ�����', 'KDE�����������', '�ɼ��ĸɾ�����');
%%
figure(2)
plot(dirty_c, dirty_p, 'x', 'MarkerSize', 10)
hold on
% plot(kde_c, kde_p, 'o', 'MarkerSize', 10)
scatter(kde_c, kde_p, 'filled')
plot(truth_c, truth_p, 'o', 'MarkerSize', 12)
hold off
set(gca, 'FontSize', 20)
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)
legend('��·�˸��ŵ�����', 'KDE�����������', '�ɼ��ĸɾ�����')