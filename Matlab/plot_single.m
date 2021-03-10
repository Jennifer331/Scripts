f = "D:\\Atom\\python\\test_data\\empty\\test.mat";
load(f, 'DISTANCE', 'CHANNEL', 'PHASE', 'RSSI')
figure(1); plot3(DISTANCE, CHANNEL, PHASE, '>'); hold on
figure(2); plot3(DISTANCE, CHANNEL, RSSI, '>'); hold on
