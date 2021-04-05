matls = ["empty", "water", "oil", "vinegar"];
side = ['f', 't'];
%% 导入数据
for i = 1:4
    for j = 1:2
        file = sprintf('D:\\Atom\\python\\data\\cleaned\\outdoor\\front-tail\\outdoor_all_%s_%s_aligned.mat', side(j), matls(i));
        load(file);
        eval(sprintf('%s_%s_d = DISTANCE;', matls(i), side(j)));
        eval(sprintf('%s_%s_f = CHANNEL;', matls(i), side(j)));
        eval(sprintf('%s_%s_r = RSSI;', matls(i), side(j)));
        eval(sprintf('%s_%s_p = PHASE;', matls(i), side(j)));
    end
end
disp("data imported!")
%% 绘制
figure(1)
marker = ["x", "o", ".", ">"];
l = [];
for i = 1:4
    for j = 1:2
        label = sprintf("%s_%s",  matls(i), side(j));
        l = [l, label];
        eval(sprintf('plot3(%s_d, %s_f, %s_p, "%s")', label, label, label, marker(i)));
        hold on
    end
end
legend(l)
hold off
disp('figured drawn!')
%% 绘制front-tail
figure(2)

marker = ["x", "o", ".", ">"];
l = [];
for i = 1:4
    label = matls(i);
    l = [l, label];
    eval(sprintf('plot3(%s_t_d, %s_t_f, %s_f_p - %s_t_p, "%s")', label, label, label, label, marker(i)));
    hold on
end
legend(l)
title('front-tail')
hold off
