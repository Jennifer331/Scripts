load('phase.mat')

dists = (30:3:120);
channels = (902.75:0.5:927.25);

figure(1)
plot(dists, e_d, '-s', 'MarkerSize', 10)
hold on
plot(dists, o_d, '-x', 'MarkerSize', 10)
plot(dists, v_d, '-o', 'MarkerSize', 10)
plot(dists, w_d, '-^', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
xlabel('距离/（cm）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)
legend('空瓶', '油', '醋', '水')
%%
figure(2)
plot(channels, e_f, '-s', 'MarkerSize', 10)
hold on
plot(channels, o_f, '-x', 'MarkerSize', 10)
plot(channels, v_f, '-o', 'MarkerSize', 10)
plot(channels, w_f, '-^', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
xlabel('频道/（MHz）', 'FontSize', 30)
ylabel('相位/（rad）', 'FontSize', 30)
legend('空瓶', '油', '醋', '水')
