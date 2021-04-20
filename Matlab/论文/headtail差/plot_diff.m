load('D:\Atom\Matlab\论文\headtail差\heatail_diff.mat')

%% 相位
figure(1)
% p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12, 13, 14, 15,16, 17, 18,19,20,...
%     21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,...
%     41,42,42,44,45,46,47,48,49,50];
% p = [2, 3, 4, 5, 7, 8, 9, 10,12, 13, 14, 15, 17, 18,19,20,...
%     22,23,24,25,27,28,29,30,32,33,34,35,37,38,39,40,...
%     42,42,44,45,47,48,49,50];
% repmat([902.75 : 0.5 : 927.25], 1, 8);
% p = union(union([1:3:400], [1:5:400]), [1: 7:400]);
p = setdiff([1:400], [1:7:400]);
e_p(p)=NaN;
o_p(p)=NaN;
v_p(p)=NaN;
w_p(p)=NaN;

plot(e_p, 'x', 'MarkerSize', 10)
hold on
plot(o_p, 's', 'MarkerSize', 10)
plot(v_p, 'o', 'MarkerSize', 10)
plot(w_p, '^', 'MarkerSize', 10)
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on', 'GridLineStyle', '--', 'GridAlpha', 0.7, 'FontSize', 20)
ylabel('相位差/（rad）', 'FontSize', 30)
xlabel('距离/（cm）', 'FontSize', 30)
xticklabels([50:10:120])
set(gca, 'xtick', [0:50:400])
legend('空瓶', '油', '醋', '水')

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\headtail_phase_diff.pdf')
%% RSSI
p = setdiff([1:400], [1:7:400]);
e_r(p)=NaN;
o_r(p)=NaN;
v_r(p)=NaN;
w_r(p)=NaN;

figure(2)
plot(e_r, 'x', 'MarkerSize', 10)
hold on
plot(o_r, 's', 'MarkerSize', 10)
plot(v_r, 'o', 'MarkerSize', 10)
plot(w_r, '^', 'MarkerSize', 10)
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on', 'GridLineStyle', '--', 'GridAlpha', 0.7, 'FontSize', 20)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
xlabel('距离/（cm）', 'FontSize', 30)
xticklabels([50:10:120])
set(gca, 'xtick', [0:50:400])
legend('空瓶', '油', '醋', '水')

% set(gcf, 'PaperPosition', [0 0 24 18])
% set(gcf, 'PaperSize', [24 18])
% saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\headtail_rssi_diff.pdf')
%%
figure(3)
plot(e_p, e_r, 'x', 'MarkerSize', 10)
hold on
plot(o_p, o_r, 's', 'MarkerSize', 10)
plot(v_p,v_r, 'o', 'MarkerSize', 10)
plot(w_p, w_r, '^', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
legend('空瓶', '油', '醋', '水')
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\diff_cluster.pdf')
%%
figure(4)
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
%% 3d PHASE
dists = repelem([50:10:120], 50);
f = repmat([902.75 : 0.5 : 927.25], 1, 8);

figure(1)
plot3(dists, f, e_p, 's', 'MarkerSize', 10)
hold on
plot3(dists, f, o_p, 'o', 'MarkerSize', 10)
plot3(dists, f, v_p, '^', 'MarkerSize', 10)
plot3(dists, f, w_p, 'x', 'MarkerSize', 10)
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on', 'FontSize', 20)
xlabel('距离/（cm）', 'FontSize', 30)
ylabel('频道/（MHz）', 'FontSize', 30)
zlabel('相位差/（rad）', 'FontSize', 30)

legend('空瓶', '油', '醋', '水')

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\headtail_phase_diff3d.pdf')
%% 3d RSSI
dists = repelem([50:10:120], 50);
f = repmat([902.75 : 0.5 : 927.25], 1, 8);

figure(2)
plot3(dists, f, e_r, 's', 'MarkerSize', 10)
hold on
plot3(dists, f, o_r, 'o', 'MarkerSize', 10)
plot3(dists, f, v_r, '^', 'MarkerSize', 10)
plot3(dists, f, w_r, 'x', 'MarkerSize', 10)
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on', 'FontSize', 20)
xlabel('距离/（cm）', 'FontSize', 30)
ylabel('频道/（MHz）', 'FontSize', 30)
zlabel('接收信号强度差/（dB）', 'FontSize', 30)

legend('空瓶', '油', '醋', '水')

set(gcf, 'PaperPosition', [0 0 24 18])
set(gcf, 'PaperSize', [24 18])
saveas(gcf, 'D:\研究生\毕业设计\论文\图\重绘\headtail_rssi_diff3d.pdf')