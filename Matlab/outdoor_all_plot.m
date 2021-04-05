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
%%
logica = (CHANNEL==902.75 & DISTANCE<120);
oil_unwrap_d = oil_unwrap_d(logica);
oil_unwrap_p = oil_unwrap_p(logica);
oil_wrap_d = oil_wrap_d(logica);
oil_wrap_p = oil_wrap_p(logica);

logica2 = DISTANCE==30
unwrap_c_150 = oil_unwrap_c(logica2);
unwrap_p_150 = oil_unwrap_p(logica2);
wrap_c_150 = oil_wrap_c(logica2);
wrap_p_150 = oil_wrap_p(logica2);
plot(unwrap_c_150, unwrap_p_150, 's-','LineWidth',1.5)
hold on
plot(wrap_c_150, wrap_p_150, 'x-','LineWidth',1.5)
hold off

xlabel('频道/（MHz）')
ylabel('相位/（rad）')
legend('反折叠相位', '实际相位')
