load('phase.mat')

dists = (30:3:120);
channels = (902.75:0.5:927.25);

figure(1)
plot(dists, e_d, '-s')
hold on
plot(dists, o_d, '-s')
plot(dists, v_d, '-s')
plot(dists, w_d, '-s')
hold off
xlabel('距离/（cm）')
ylabel('相位/（rad）')
legend('空瓶', '油', '醋', '水')

figure(2)
plot(channels, e_f, '-s')
hold on
plot(channels, o_f, '-s')
plot(channels, v_f, '-s')
plot(channels, w_f, '-s')
hold off
xlabel('频道/（MHz）')
ylabel('相位/（rad）')
legend('空瓶', '油', '醋', '水')
