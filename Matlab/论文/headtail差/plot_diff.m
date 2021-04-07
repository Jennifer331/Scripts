load('D:\Atom\Matlab\����\headtail��\heatail_diff.mat')

%% ��λ
plot(e_p, 'x')
hold on
plot(o_p, 'x')
plot(v_p, 'x')
plot(w_p, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('��λ��/��rad��')
xticklabels({})
legend('��ƿ', '��', '��', 'ˮ')

%% RSSI
plot(e_r, 'x')
hold on
plot(o_r, 'x')
plot(v_r, 'x')
plot(w_r, 'x')
hold off

set(gca, 'YGrid', 'off', 'XGrid', 'on')
ylabel('�����ź�ǿ�Ȳ�/��dB��')
xticklabels({})
legend('��ƿ', '��', '��', 'ˮ')

%%
figure(1)
plot(e_p, e_r, 'x')
hold on
plot(o_p, o_r, 'x')
plot(v_p,v_r, 'x')
plot(w_p, w_r, 'x')
hold off
legend('��ƿ', '��', '��', 'ˮ')
xlabel('��λ��/��rad��')
ylabel('�����ź�ǿ�Ȳ�/��dB��')

figure(2)
c = repmat([902.75:0.5:927.25], 1, 8);
plot3(e_p, e_r, c, 'x')
hold on
plot3(o_p, o_r, c, 'x')
plot3(v_p,v_r, c, 'x')
plot3(w_p, w_r, c, 'x')
hold off
legend('��ƿ', '��', '��', 'ˮ')
xlabel('��λ��/��rad��')
ylabel('�����ź�ǿ�Ȳ�/��dB��')