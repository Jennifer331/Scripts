load('diff_test.mat')

%%
color = get(gca, 'ColorOrder');
m_open = 's';
m_out = 'x';
plot(open_empty_p, open_empty_r, 's', 'color', color(1,:), 'MarkerSize', 10)
hold on
plot(open_oil_p, open_oil_r, 'x', 'color', color(2,:), 'MarkerSize', 10)
plot(open_vinegar_p, open_vinegar_r, 'o', 'color', color(3,:), 'MarkerSize', 10)
plot(open_water_p, open_water_r, 'p', 'color', color(4,:), 'MarkerSize', 10)

plot(outdoor_empty_p, outdoor_empty_r, '*', 'color', color(1,:), 'MarkerSize', 10)
plot(outdoor_oil_p, outdoor_oil_r, '.', 'color', color(2,:), 'MarkerSize', 10)
plot(outdoor_vinegar_p, outdoor_vinegar_r, 'd', 'color', color(3,:), 'MarkerSize', 10)
plot(outdoor_water_p, outdoor_water_r, '^', 'color', color(4,:), 'MarkerSize', 10)

hold off
set(gca, 'FontSize', 20)
xlabel('相位差/（rad）', 'FontSize', 30)
ylabel('接收信号强度差/（dB）', 'FontSize', 30)
legend('室内-空瓶', '室内-油', '室内-醋', '室内-水', '室外-空瓶', '室外-油', '室外-醋', '室外-水')