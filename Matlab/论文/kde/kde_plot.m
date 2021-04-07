load('kde.mat')

figure(1)
plot(dirty_c, dirty_r, 'x')
hold on
plot(kde_c, kde_r, 'o', 'MarkerSize', 10)
plot(truth_c, truth_r, 's')
hold off
xlabel('Ƶ��/��MHz��')
ylabel('�����ź�ǿ��/��dBm��')
legend('��·�˸��ŵ�����', 'kde�����������', '�ɼ��ĸɾ�����')

figure(2)
plot(dirty_c, dirty_p, 'x')
hold on
plot(kde_c, kde_p, 'o', 'MarkerSize', 10)
plot(truth_c, truth_p, 's')
hold off
xlabel('Ƶ��/��MHz��')
ylabel('��λ/��rad��')
legend('��·�˸��ŵ�����', 'kde�����������', '�ɼ��ĸɾ�����')