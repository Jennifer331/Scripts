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
xlabel('����/��cm��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)
legend('��ƿ', '��', '��', 'ˮ')
%%
figure(2)
plot(channels, e_f, '-s', 'MarkerSize', 10)
hold on
plot(channels, o_f, '-x', 'MarkerSize', 10)
plot(channels, v_f, '-o', 'MarkerSize', 10)
plot(channels, w_f, '-^', 'MarkerSize', 10)
hold off
set(gca, 'FontSize', 20)
xlabel('Ƶ��/��MHz��', 'FontSize', 30)
ylabel('��λ/��rad��', 'FontSize', 30)
legend('��ƿ', '��', '��', 'ˮ')
