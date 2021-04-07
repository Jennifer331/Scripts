load('D:\Atom\Matlab\论文\headtail差\heatail_diff.mat')

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

%%
figure(1)
plot(e_p, e_r, 'x')
hold on
plot(o_p, o_r, 'x')
plot(v_p,v_r, 'x')
plot(w_p, w_r, 'x')
hold off
legend('空瓶', '油', '醋', '水')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')

figure(2)
c = repmat([902.75:0.5:927.25], 1, 8);
plot3(e_p, e_r, c, 'x')
hold on
plot3(o_p, o_r, c, 'x')
plot3(v_p,v_r, c, 'x')
plot3(w_p, w_r, c, 'x')
hold off
legend('空瓶', '油', '醋', '水')
xlabel('相位差/（rad）')
ylabel('接收信号强度差/（dB）')