%%
load('d:\\atom\\python\\data\\cleaned\\mr\\mr_water_2d_cus_unwrap.mat')
empty_dis=DISTANCE; empty_freq=CHANNEL; empty_phase=PHASE; empty_rssi=RSSI;
load('d:\\atom\\python\\data\\cleaned\\nongfu_water_2d_unwrap.mat')
water_dis=DISTANCE'; water_freq=CHANNEL'; water_phase=PHASE'; water_rssi=RSSI';
load('d:\\atom\\python\\data\\cleaned\\nongfu_oil_2d_unwrap.mat')
oil_dis=DISTANCE'; oil_freq=CHANNEL'; oil_phase=PHASE'; oil_rssi=RSSI';
load('d:\\atom\\python\\data\\cleaned\\nongfu_vinegar_2d_unwrap.mat')
vinegar_dis=DISTANCE'; vinegar_freq=CHANNEL'; vinegar_phase=PHASE'; vinegar_rssi=RSSI';
%%
load('d:\\atom\\python\\data\\cleaned\\white_empty.mat')
wempty_dis=DISTANCE'; wempty_freq=CHANNEL'; wempty_phase=PHASE'; wempty_rssi=RSSI';
load('d:\\atom\\python\\test_data\\empty\\test.mat')
test_dis=DISTANCE'; test_freq=CHANNEL'; test_phase=PHASE'; test_rssi=RSSI';

%%
figure(4)
plot3(empty_dis, empty_freq, empty_rssi, 'kx')
hold on
plot3(water_dis,water_freq,water_rssi,'k.')
plot3(oil_dis,oil_freq,oil_rssi,'co')
plot3(vinegar_dis,vinegar_freq,vinegar_rssi,'r*')
% plot3(wempty_dis, wempty_freq, wempty_rssi, 'gs')
% plot3(test_dis, test_freq, test_rssi, 'b+')
legend('empty','water','oil','vinegar')
% ,'white_bottle','fake')
xlabel('distance');ylabel('channel')
title('rssi')
hold off
%%
load('d:\\atom\\python\\data\\cleaned\\mr\\mr_water_2d_cus_unwrap.mat')
empty_dis=DISTANCE'; empty_freq=CHANNEL'; empty_phase=PHASE'; empty_rssi=RSSI';
figure(5)
title('phase')
plot3(empty_dis, empty_freq, empty_phase, 'kx')
hold on
plot3(water_dis/33,water_freq,water_phase/(2*pi),'k.')
plot3(oil_dis/33,oil_freq,oil_phase/(2*pi),'co')
plot3(vinegar_dis/33,vinegar_freq,vinegar_phase/(2*pi),'r*')
% plot3(wempty_dis, wempty_freq, wempty_phase, 'gs')
% plot3(test_dis, test_freq, test_phase, 'b+')
legend('empty','water','oil','vinegar')
% ,'white_bottle','fake')
xlabel('distance');ylabel('channel')
hold off