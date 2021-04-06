% load('heatail_diff.mat')

%% 相位
plot(e_p, 'x')
hold on
plot(o_p, 'x')
plot(v_p, 'x')
plot(w_p, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('相位差/（rad）')
xticklabels({})
legend('空瓶', '油', '醋', '水')

%% RSSI
plot(e_r, 'x')
hold on
plot(o_r, 'x')
plot(v_r, 'x')
plot(w_r, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('接收信号强度差/（dB）')
xticklabels({})
legend('空瓶', '油', '醋', '水')