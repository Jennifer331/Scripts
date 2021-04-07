load('kde.mat')

figure(1)
plot(dirty_c, dirty_r, 'x')
hold on
plot(kde_c, kde_r, 'o', 'MarkerSize', 10)
plot(truth_c, truth_r, 's')
hold off
xlabel('频道/（MHz）')
ylabel('接收信号强度/（dBm）')
legend('有路人干扰的数据', 'kde处理过的数据', '采集的干净数据')

figure(2)
plot(dirty_c, dirty_p, 'x')
hold on
plot(kde_c, kde_p, 'o', 'MarkerSize', 10)
plot(truth_c, truth_p, 's')
hold off
xlabel('频道/（MHz）')
ylabel('相位/（rad）')
legend('有路人干扰的数据', 'kde处理过的数据', '采集的干净数据')