load('kde.mat')

figure(1)
plot(dirty_c, dirty_r, 'x', 'MarkerSize', 10)
hold on
% plot(kde_c, kde_r, 'o', 'MarkerSize', 7, 'filled')
scatter(kde_c, kde_r, 'filled')
plot(truth_c, truth_r, 'o', 'MarkerSize', 12)
hold off
set(gca, 'FontSize', 20)
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('接收信号强度/（dBm）', 'FontSize', 30)
legend('有路人干扰的数据', 'KDE处理过的数据', '采集的干净数据');
%%
figure(2)
plot(dirty_c, dirty_p, 'x', 'MarkerSize', 10)
hold on
% plot(kde_c, kde_p, 'o', 'MarkerSize', 10)
scatter(kde_c, kde_p, 'filled')
plot(truth_c, truth_p, 'o', 'MarkerSize', 12)
hold off
set(gca, 'FontSize', 20)
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)
legend('有路人干扰的数据', 'KDE处理过的数据', '采集的干净数据')